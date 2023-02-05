from pathlib import Path

from flask import (
    Blueprint,
    current_app,
    flash,
    make_response,
    redirect,
    render_template,
    send_file,
    url_for,
)

from .forms import UploadTxtForm
from .main import main
from .models.recreate_dir import recreate_dir

_FILE_NAME = "output.txt"
_TEXT_PLAIN = "text/plain"

data_merge_app = Blueprint("", __name__, template_folder="templates")


@data_merge_app.route("/", methods=["GET", "POST"])
def index():
    upload_path = current_app.config["UPLOAD_FOLDER"]
    output_path = current_app.config["OUTPUT_FOLDER"]

    form = UploadTxtForm()

    if form.validate_on_submit():
        # アップロードされた画像ファイルの取得
        sc_file = form.sc_file.data
        main_file = form.main_file.data

        # ファイルを保存しないため、sc_path、main_path、output_pathにディレクトリがある場合は削除
        # その後、空のディレクトリを作成しておく
        recreate_dir(upload_path)
        recreate_dir(output_path)

        sc_path = Path(upload_path, sc_file.filename)
        main_path = Path(upload_path, main_file.filename)

        # ファイルを保存
        sc_file.save(sc_path)
        main_file.save(main_path)

        output_file_path = Path(output_path, _FILE_NAME)
        # データをマージする
        main(sc_path, main_path, output_file_path)

        # 中にあるファイルを全て削除しておく
        recreate_dir(upload_path)

        flash("マージが正常に完了しました。")
        return redirect(url_for("complete_merge"))

    return render_template("data_merge_app/index.html", form=form)


@data_merge_app.route("/download", methods=["GET", "POST"])
def download_file():
    output_path = current_app.config["OUTPUT_FOLDER"]
    output_file_path = Path(output_path, _FILE_NAME)

    response = make_response()
    with open(output_file_path, "rb") as f:
        response.data = f.read()

    # 読み取り後にファイル削除
    recreate_dir(output_path)

    response.headers["Content-Disposition"] = "attachment; filename=" + _FILE_NAME
    response.mimetype = _TEXT_PLAIN

    return response


@data_merge_app.route(
    "/complete",
    methods=[
        "GET",
    ],
)
def complete_merge():
    return render_template("data_merge_app/download.html")
