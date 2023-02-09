from pathlib import Path
from zipfile import ZipFile

from flask import (
    Blueprint,
    current_app,
    flash,
    make_response,
    redirect,
    render_template,
    url_for,
)

from .forms import UploadTxtForm
from .models.recreate_dir import recreate_dir
from .output_data import output_data
from .output_layout import output_layout

_FILE_NAME = "output.txt"
_LAYOUT_FILE_NAME = "output_layout.txt"
_OUTPUT_ZIP_NAME = "output.zip"
_TEXT_PLAIN = "text/plain"
_ZIP_APPLICATION = "application/zip"

_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

data_merge_app = Blueprint(
    "data_merge_app", __name__, template_folder="templates", static_folder="static"
)


@data_merge_app.route("/", methods=["GET", "POST"])
def index():
    upload_path = current_app.config["UPLOAD_FOLDER"]
    output_path = current_app.config["OUTPUT_FOLDER"]

    form = UploadTxtForm()

    if form.validate_on_submit():
        # アップロードされたtxtファイルの取得
        sc_file = form.sc_file.data
        main_file = form.main_file.data
        sc_layout_file = form.sc_layout_file.data
        main_layout_file = form.main_layout_file.data

        # ファイルを保存しないため、sc_path、main_path、output_pathにディレクトリがある場合は削除
        # その後、空のディレクトリを作成しておく
        recreate_dir(upload_path)
        recreate_dir(output_path)

        sc_path = Path(upload_path, sc_file.filename)
        main_path = Path(upload_path, main_file.filename)
        sc_layout_path = Path(upload_path, sc_layout_file.filename)
        main_layout_path = Path(upload_path, main_layout_file.filename)

        # ファイルを保存
        sc_file.save(sc_path)
        main_file.save(main_path)
        sc_layout_file.save(sc_layout_path)
        main_layout_file.save(main_layout_path)

        output_file_path = Path(output_path, _FILE_NAME)
        output_layout_file_path = Path(output_path, _LAYOUT_FILE_NAME)

        # データをマージする
        output_data(sc_path, main_path, output_file_path)
        output_layout(sc_layout_path, main_layout_path, output_layout_file_path)

        # 中にあるファイルを全て削除しておく
        recreate_dir(upload_path)

        flash("マージが正常に完了しました。")
        return redirect(url_for("data_merge_app.complete_merge"))

    return render_template("data_merge_app/index.html", form=form)


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
    # with open(output_file_path, "rb") as f:
    #     response.data = f.read()

    response.data = open(output_zip_path, "rb").read()

    # 読み取り後にファイル削除
    recreate_dir(output_path)

    response.headers["Content-Disposition"] = "attachment; filename=" + _OUTPUT_ZIP_NAME
    # response.mimetype = _TEXT_PLAIN
    response.mimetype = _ZIP_APPLICATION

    return response


@data_merge_app.route(
    "/complete",
    methods=[
        "GET",
    ],
)
def complete_merge():
    return render_template("data_merge_app/download.html")


def _make_zip(data_path: Path, layout_path: Path, zip_file_path: Path) -> ZipFile:
    print(zip_file_path)
    with ZipFile(zip_file_path, "w") as zip:
        zip.write(data_path)
        zip.write(layout_path)
