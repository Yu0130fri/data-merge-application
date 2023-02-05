from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField


class UploadTxtForm(FlaskForm):
    sc_file = FileField(
        "Screening File",
        validators=[
            FileRequired("スクリーニングファイルを選択してください"),
            FileAllowed(["txt"], ".txt形式でアップロードしてください"),
        ],
    )
    main_file = FileField(
        "Main File",
        validators=[
            FileRequired("本調査ファイルを選択してください"),
            FileAllowed(["txt"], ".txt形式でアップロードしてください"),
        ],
    )

    submit_form = SubmitField("アップロード")
