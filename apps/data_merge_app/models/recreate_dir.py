import os
import shutil


def recreate_dir(dir_path: str) -> None:
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)

    try:
        os.makedirs(dir_path, exist_ok=True)
    except FileNotFoundError:
        raise FileNotFoundError("指定したディレクトリが見つかりませんでした。", dir_path)
