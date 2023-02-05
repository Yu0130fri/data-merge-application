from pathlib import Path

basedir = Path(__file__).parent.parent.parent


class BaseConfig:
    SECRET_KEY = "ad421f0c228b4b7911490e0eaa581aaed6dee7a673500f8a188291f44dc3678f"
    UPLOAD_FOLDER = str(Path.joinpath(basedir, "flaskr", "apps", "txt_files"))
    OUTPUT_FOLDER = str(Path.joinpath(basedir, "output_files"))


class LocalConfig(BaseConfig):
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    WTF_CSRF_ENABLED = False


# config辞書にマッピングする
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
