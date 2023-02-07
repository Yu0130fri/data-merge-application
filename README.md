# 始め方
1. レポジトリをcloneする
2. data-merge-applicationの中に移動する
3. 仮想環境を構築する
```
python -m venv .venv
```
4. requirements.txtを読み込む
```
pip install -r requirements.txt
```
5. data-merge-applicationに.envファイルを作成
6. .envファイルに以下を記載
```
FLASK_APP=flaskr.apps.app:create_app("local")
FLASK_DEBUG=True
```
5. flaskを起動してみる
```
flask run
```

## スクリーニング調査と本調査のテキストファイルをマージするサイト構築

### memo 
modelsの関数などはpytestで実装済み
エラーハンドリングやエラー画面の作成はしていない
レイアウトのマージ
