from flask import Blueprint, render_template, request

data_visualization_app = Blueprint(
    "data_visualization", __name__, template_folder="templates", static_folder="static"
)


@data_visualization_app.route("/", methods=["GET"])
def index():
    c = {
        "chart_title": "グラフサンプル",  # 設問文
        "chart_labels": "項目1, 項目２, 項目３, 項目４,項目５",  # 回答内容 # 自動で決まる
        "chart_data": "4, 7, 8, 5, 6",  # データのカウント
        "question_num": "設問番号",
    }
    return render_template("index.html", c=c)


@data_visualization_app.route("/visualization", methods=["GET", "POST"])
def show_graph():
    if request.method != "POST":
        raise ValueError()

    graph_title = request.form["sample-title"]
    chart_title = request.form["chart_title"]
    chart_labels = request.form["chart_labels"]
    chart_data = request.form["chart_data"]
    question_num = request.form["question_num"]

    c = {
        "graph_title": graph_title,
        "chart_title": chart_title,
        "chart_labels": chart_labels,
        "chart_data": chart_data,
        "question_num": question_num,
    }
    return render_template("show_graph.html", c=c)
