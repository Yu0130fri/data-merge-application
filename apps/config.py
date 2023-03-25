from pathlib import Path

basedir = Path(__file__).absolute().parent.parent


class BaseConfig:
    SECRET_KEY = "ad421f0c228b4b7911490e0eaa581aaed6dee7a673500f8a188291f44dc3678f"
    UPLOAD_SC_FOLDER = Path.joinpath(basedir, "apps", "txt_files", "data", "sc")
    UPLOAD_MAIN_FOLDER = Path.joinpath(basedir, "apps", "txt_files", "data", "main")
    UPLOAD_SC_LAYOUT_FOLDER = Path.joinpath(
        basedir, "apps", "txt_files", "layout", "sc"
    )
    UPLOAD_MAIN_LAYOUT_FOLDER = Path.joinpath(
        basedir, "apps", "txt_files", "layout", "main"
    )
    CHART_RAWDATA_FOLDER = Path.joinpath(
        basedir, "apps", "txt_files", "chart", "rawdata"
    )
    CHART_LAYOUT_FOLDER = Path.joinpath(basedir, "apps", "txt_files", "chart", "layout")
    OUTPUT_FOLDER = Path.joinpath(basedir, "output_files")


class LocalConfig(BaseConfig):
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    WTF_CSRF_ENABLED = False


# config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
