# todolist_app

## 実行環境について  
Python 3.11.2  
Flask 2.2.3  
PostgreSQL 14.17  

## 概要

ToDoリスト管理ツールです。
ローカル環境で完結するため、各自のPC上で環境構築が必要です。

## 技術スタック

- **バックエンド**: Python 3.11.2 (Flask 2.2.3)
- **データベース**: PostgreSQL 14.17
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

#### PostgreSQL接続テスト：

```bash
# PostgreSQLのbinディレクトリにPATHが通っている場合
psql -U postgres
```
パスワードを入力して接続できれば、PostgreSQLは正常に動作しています。終了するには `\q` と入力してEnterを押します。


---以下は参考---

---
#### PostgreSQLサービスの起動/停止/状態確認：

```bash
# サービスの状態確認
# コマンドプロンプトを管理者権限で起動する必要あり
sc query postgresql-x64-17

# サービスの起動
net start pstgresql-x64-17

# サービスの停止
net stop pstgresql-x64-17
```

---

### プロジェクトディレクトリの作成とリポジトリのクローン

```bash
# todo_appディレクトリを作成
mkdir todo_app
cd todo_app

# リポジトリをクローン
git clone <リポジトリURL> .
```

### 仮想環境のセットアップ

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化（コマンドプロンプトの場合）
venv\Scripts\activate.bat

# または、Git Bashの場合
source venv/Scripts/activate

# または、PowerShellの場合
# venv\Scripts\Activate.ps1
```

### 必要なパッケージのインストール

```bash
# pipのアップグレード
# コマンドプロンプト
pip.exe install --upgrade pip

# GitBash
pip install --upgrade pip

# ライブラリインストール
pip install -r requirements.txt


# うまくいかない時(psycopg2が入らない)
pip install --upgrade pip setuptools wheel
pip install psycopg2-binary
pip install -r requirements.txt
```

### PostgreSQL接続用の環境変数設定（Windowsのみ）

Windowsでは、PostgreSQL接続用の環境変数を設定する必要があります：

---以下は参考---

---

```bash
# コマンドプロンプトの場合
set USER=postgres
set PGPASSWORD=あなたのパスワード  # PostgreSQLインストール時に設定したパスワード

# または、PowerShellの場合
# $env:USER = "postgres"
# $env:PGPASSWORD = "あなたのパスワード"
```
---

## アプリケーションの実行

### 1. サーバーの起動

```bash
python app.py
```

起動後、ブラウザで `http://127.0.0.1:8080` にアクセスしてください。

アプリケーション初回起動時に、自動的にデータベースとテーブルが作成されます。

### 2. サーバーの終了

サーバーを終了するには、コマンドプロンプト上で `Ctrl + C` キーを押します。確認を求められた場合は `Y` を入力してEnterを押してください。

### 3. 作業終了時

仮想環境を終了するには次のコマンドを実行します：

```bash
# コマンドプロンプトまたはGitBash/PowerShellで
deactivate
```
