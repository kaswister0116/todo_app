# todolist_app

## 実行環境について  
Python 3.11.2  
Flask 2.2.3  
PostgreSQL  

## 概要

ToDoリスト管理ツールです。
ローカル環境で完結するため、各自のPC上で環境構築が必要です。

## 技術スタック

- **バックエンド**: Python 3.11.2 (Flask 2.2.3)+ ライブラリ
- **データベース**: PostgreSQL17（インストール済み）
- **フロントエンド**: HTML, CSS, JavaScript（必要に応じて）

## ディレクトリ構造

```
.
├── README.md            # プロジェクト説明ファイル
├── __init__.py          # Pythonパッケージ化用ファイル
├── app.py               # メインのFlaskアプリケーション
├── db.py                # データベース接続と操作
├── requirements.txt     # 必要なパッケージリスト
├── static               # 静的ファイル格納ディレクトリ
│   └── styles.css       # CSSスタイルシート
└── templates            # HTMLテンプレート格納ディレクトリ
    └── index.html       # メインページのテンプレート
```

### プロジェクトディレクトリの作成とリポジトリのクローン
GitBashでコマンドを実行すること。

```bash
# tech_processディレクトリを作成して移動
mkdir tech_process
cd tech_process

# リポジトリをクローン
git clone <リポジトリURL> .
```

### 仮想環境のセットアップ

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
source venv/Scripts/activate
```

### 必要なパッケージのインストール

```bash
# pipのアップグレード
python.exe -m pip install --upgrade pip

# ライブラリインストール
pip install -r requirements.txt

# うまくいかない時(psycopg2が入らない)
pip install --upgrade pip setuptools wheel
pip install psycopg2-binary
pip install -r requirements.txt
```

## アプリケーションの実行

### 1. サーバーの起動

```bash
python app.py
```

起動後、ブラウザで `http://127.0.0.1:8080` にアクセスしてください。

アプリケーション初回起動時に、自動的にデータベースとテーブルが作成されます。

### 2. サーバーの終了

サーバーを終了するには、GitBash上で `Ctrl + C` キーを押します。確認を求められた場合は `Y` を入力してEnterを押してください。

### 3. 作業終了時

仮想環境を終了するには次のコマンドを実行します：

```bash
deactivate
```

## Git操作
各ファイルの変更を確定させるとき
```bash
git add .
git commit -m "(ここにコミットメッセージ)"
```

初回のコミット時に
```bash
git config --global user.name "Your Name"
git config --global user.email "your@example.com"
```
上記ような設定を求められるため、コミット情報に表示させたい名前をメールアドレスを入力する。

---
---以下は参考---

#### PostgreSQL接続テスト：

```bash
# PostgreSQLのbinディレクトリにPATHが通っている場合
psql -U postgres
```
パスワードを入力して接続できれば、PostgreSQLは正常に動作しています。終了するには `\q` と入力してEnterを押します。

#### PostgreSQLサービスの起動/停止/状態確認：

```bash
# サービスの状態確認
# コマンドプロンプトを管理者権限で起動する必要あり
sc query postgresql-x64-17

# サービスの起動
net start postgresql-x64-17

# サービスの停止
net stop postgresql-x64-17
```

---
