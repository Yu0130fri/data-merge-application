from pathlib import Path
from zipfile import ZipFile

from flask import (
    Blueprint,
    current_app,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.utils import secure_filename

from .models.recreate_dir import recreate_dir
from .survey_model import SurveyModel

_FILE_NAME = "output.txt"
_LAYOUT_FILE_NAME = "output_layout.txt"
_OUTPUT_ZIP_NAME = "output.zip"

_TEXT_PLAIN = "text/plain"
_ZIP_APPLICATION = "application/zip"

ALLOWED_EXTENSIONS = {"txt"}

_BASE_DIR = Path(__file__).resolve().parent.parent.parent

_DEFAULT_MAIN_FILE_NAME = "main-0"
_SC_FILE_ID = "sc-file"
_SC_LAYOUT_FILE_ID = "sc-layout-file"

_GENERATE_FLAG = "flag-name-0"


data_merge_app = Blueprint(
    "data_merge_app", __name__, template_folder="templates", static_folder="static"
)


@data_merge_app.route("/", methods=["GET", "POST"])
def index():
    upload_sc_path = current_app.config["UPLOAD_SC_FOLDER"]
    upload_main_path = current_app.config["UPLOAD_MAIN_FOLDER"]
    upload_sc_layout_path = current_app.config["UPLOAD_SC_LAYOUT_FOLDER"]
    upload_main_layout_path = current_app.config["UPLOAD_MAIN_LAYOUT_FOLDER"]
    output_path = current_app.config["OUTPUT_FOLDER"]

    # ファイルを保存しないため、各pathにファイルがある場合は削除
    # その後、空のディレクトリを作成しておく
    recreate_dir(upload_sc_path)
    recreate_dir(upload_main_path)
    recreate_dir(upload_sc_layout_path)
    recreate_dir(upload_main_layout_path)
    recreate_dir(output_path)

    if request.method == "POST":
        if _DEFAULT_MAIN_FILE_NAME in request.files:
            # scファイルがあるか確認し、あれば読み込む
            if _SC_FILE_ID in request.files and _SC_LAYOUT_FILE_ID in request.files:
                # スクリーニングデータの読み込み
                sc_file = request.files[_SC_FILE_ID]
                sc_file_filename = sc_file.filename

                # クロスサイトインジェクション対策
                if sc_file and _allowed_file(sc_file_filename):
                    sc_file_filename = secure_filename(sc_file_filename)
                    sc_file_path = Path(upload_sc_path, sc_file_filename)

                    sc_file.save(sc_file_path)
                else:
                    sc_file_path = None

                # レイアウトファイルの読み込み
                sc_layout = request.files[_SC_LAYOUT_FILE_ID]
                sc_layout_filename = sc_layout.filename
                # クロスサイトインジェクション対策
                if sc_layout and _allowed_file(sc_layout_filename):
                    sc_layout_filename = secure_filename(sc_layout_filename)
                    sc_layout_file_path = Path(
                        upload_sc_layout_path, sc_layout_filename
                    )

                    sc_layout.save(sc_layout_file_path)
                else:
                    sc_layout_file_path = None

            elif (
                _SC_FILE_ID not in request.files and _SC_LAYOUT_FILE_ID in request.files
            ) or (
                _SC_FILE_ID in request.files and _SC_LAYOUT_FILE_ID not in request.files
            ):
                flash("データとレイアウトは両方入れてください")
                raise ValueError()  # TODO エラー画面の生成
            else:
                sc_file_path = None

            # 本調査の読み込み
            i = 0
            file_name_list: list[str] = []
            while True:
                try:
                    file_id = "main-" + str(i)

                    main_file = request.files[file_id]
                    main_filename = f"{str(i).zfill(2)}-" + main_file.filename

                    # check file name is secure
                    if main_file and _allowed_file(main_filename):
                        main_filename = secure_filename(main_filename)
                        file_name_list.append(main_filename[3:])
                        if main_filename != "":
                            main_file_path = Path(upload_main_path, main_filename)
                            main_file.save(main_file_path)
                        else:
                            break
                    i += 1
                except Exception:
                    break

            # 本調査のレイアウトファイルをload
            i = 0
            while True:
                try:
                    layout_file_id = "main-layout-" + str(i)

                    main_layout_file = request.files[layout_file_id]
                    main_layout_filename = (
                        f"{str(i).zfill(2)}-" + main_layout_file.filename
                    )

                    # check file name is secure
                    if main_layout_file and _allowed_file(main_layout_filename):
                        main_layout_filename = secure_filename(main_layout_filename)
                        if main_layout_filename != "":
                            main_layout_file_path = Path(
                                upload_main_layout_path, main_layout_filename
                            )
                            main_layout_file.save(main_layout_file_path)
                        else:
                            break

                    i += 1
                except Exception:
                    break

        # アップロードされたデータを読み込んでインスタンスを生成
        survey_data = SurveyModel.load_files(
            sc_file_path, upload_main_path, sc_layout_file_path, upload_main_layout_path
        )

        # アウトプットファイルを設定
        output_file_path = Path(output_path, _FILE_NAME)
        output_layout_file_path = Path(output_path, _LAYOUT_FILE_NAME)

        # データをマージする
        flag_names: list[str] | None = []  # type:ignore
        if _GENERATE_FLAG in request.form:
            i = 0
            while True:
                flag_name = "flag-name-" + str(i)
                try:
                    flag_names.append(str(request.form[flag_name]))
                    i += 1
                except Exception:
                    break
        else:
            flag_names = None

        # マージしたデータを出力
        survey_data.output(output_file_path, flag_names)
        survey_data.output_layout(output_layout_file_path, flag_names)

        # TODO 画面表示のロジック修正する（一時的）
        if flag_names is not None:
            for file_name, flag_name in zip(file_name_list, flag_names):
                flash(f"{file_name}→ラベル:{flag_name}")

        # 中にあるファイルを全て削除しておく
        recreate_dir(upload_sc_path)
        recreate_dir(upload_main_path)
        recreate_dir(upload_sc_layout_path)
        recreate_dir(upload_main_layout_path)

        flash("マージが正常に完了しました。")
        return redirect(url_for("data_merge_app.complete_merge"))

    return render_template("data_merge_app/index.html")


@data_merge_app.route("/download", methods=["GET", "POST"])
def download_file():
    output_path = Path(current_app.config["OUTPUT_FOLDER"])
    output_file_path = Path(output_path, _FILE_NAME)
    output_layout_file_path = Path(output_path, _LAYOUT_FILE_NAME)

    output_zip_path = Path(output_path, _OUTPUT_ZIP_NAME)

    # zipを作成
    _make_zip(
        output_file_path.relative_to(_BASE_DIR),
        output_layout_file_path.relative_to(_BASE_DIR),
        output_zip_path,
    )

    response = make_response()
    response.data = open(output_zip_path, "rb").read()

    # with open(output_file_path, "rb") as f:
    #     response.data = f.read()

    # 読み取り後にファイル削除
    recreate_dir(output_path)

    response.headers["Content-Disposition"] = "attachment; filename=" + _OUTPUT_ZIP_NAME
    response.mimetype = _ZIP_APPLICATION
    # response.mimetype = _TEXT_PLAIN
    # response.headers["Content-Disposition"] = "attachment; filename=" + _FILE_NAME

    return response


@data_merge_app.route("/complete", methods=["GET"])
def complete_merge():
    return render_template("data_merge_app/download.html")


def _make_zip(  # type: ignore
    data_path: Path, layout_path: Path, zip_file_path: Path
) -> ZipFile:
    with ZipFile(zip_file_path, "w") as zip:
        zip.write(data_path)
        zip.write(layout_path)


def _allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@data_merge_app.route("/modal_sample", methods=["GET"])
def modal_sample():
    return render_template("data_merge_app/modal_sample.html")
