import os
from pathlib import Path
from typing import Any

from flask import Blueprint, current_app, flash, render_template, request
from werkzeug.utils import secure_filename

from ..models.recreate_dir import recreate_dir
from .src.chart import Chart

data_visualization_app = Blueprint(
    "data_visualization",
    __name__,
    template_folder="templates",
    static_folder="static",
)

_LAYOUT_CLASS_NAME = "layout"
_RAWDATA_CLASS_NAME = "rawdata"

ALLOWED_EXTENSIONS = {"txt"}


@data_visualization_app.route("/", methods=["GET", "POST"])
def index():
    rawdata_path = current_app.config["CHART_RAWDATA_FOLDER"]
    layout_path = current_app.config["CHART_LAYOUT_FOLDER"]

    # ファイルを保存しないため、各pathにファイルがある場合は削除
    # その後、空のディレクトリを作成しておく
    recreate_dir(rawdata_path)
    recreate_dir(layout_path)

    if request.method == "POST":
        try:
            rawdata = request.files[_RAWDATA_CLASS_NAME]
        except ValueError:
            flash("Rawdataが選択されていません")
            raise ValueError()

        rawdata_filename = rawdata.filename

        # クロスサイトインジェクション対策
        if rawdata and _allowed_file(rawdata_filename):
            rawdata_filename = secure_filename(rawdata_filename)
            rawdata_path = Path(rawdata_path, rawdata_filename)

            rawdata.save(rawdata_path)

        layout = request.files[_LAYOUT_CLASS_NAME]
        layout_filename = layout.filename
        if layout_filename == "":
            flash("Layoutが選択されていません")

        # クロスサイトインジェクション対策
        if layout and _allowed_file(layout_filename):
            layout_filename = secure_filename(layout_filename)
            layout_path = Path(layout_path, rawdata_filename)

            layout.save(layout_path)

        chart = Chart.from_input_file(
            rawdata_path=rawdata_path, layout_path=layout_path
        )

        # try:
        #     query_data = chart.query(request.form["show-question"])
        # except Exception:
        #     query_data = chart.query("Q4")

        chart_list: list[dict[str, Any]] = []  # type: ignore
        html_id_list: list[str] = []  # type: ignore
        for idx, q_name in enumerate(chart.extract_answer_list()):
            idx += 1
            html_id_list.append(str(idx))
            query_data = chart.query(q_name)

            chart_data = {
                "chart_title": query_data.dimension.question_description,  # 設問文
                "chart_labels": query_data.dimension.option_data,  # 回答内容 # 自動で決まる
                "chart_data": list(
                    query_data.measurement.chart_data.values()
                ),  # データのカウント
                "question_num": query_data.dimension.question_number,
            }

            chart_list.append(chart_data)

        if os.path.exists(rawdata_path):
            os.remove(rawdata_path)
        if os.path.exists(layout_path):
            os.remove(layout_path)

        return render_template(
            "show_graph.html", chart_data_list=zip(chart_list, html_id_list)
        )

    return render_template("index.html")


def _allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
