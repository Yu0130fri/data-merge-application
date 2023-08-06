https://mapps-data-merge-application.onrender.com/

# 始め方
1. レポジトリをcloneする（対象のブランチに必ず切り替える）
2. data-merge-applicationの中に移動する
3. 仮想環境を構築する
```
python -m venv .venv
```
4. 仮想環境を起動する
```
source .venv/bin/activate
```
5. requirements.txtを読み込む
```
pip install -r requirements.txt
```
6. data-merge-applicationに.envファイルを作成
7. .envファイルに以下を記載
```
FLASK_APP=apps.app:create_app("local")
FLASK_DEBUG=True
```
8. flaskを起動してみる
```
flask run
```

## スクリーニング調査と本調査のテキストファイルをマージするサイト構築

### memo 
modelsの関数などはpytestで実装済み
エラーハンドリングやエラー画面の作成はしていない
レイアウトのマージ
