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

## 環境構築手順 (Windows)

### 1. Pythonのインストール

まず、Python 3.11.2がインストールされていることを確認します。

```bash
# Pythonのバージョンを確認（コマンドプロンプトまたはPowerShellで実行）
python --version
```

もしPython 3.11.2がインストールされていない場合は、以下のいずれかの方法でインストールできます：

#### Windows用インストーラーを使用する場合：
1. [Python公式サイト](https://www.python.org/downloads/)からインストーラーをダウンロード
2. インストーラーを実行し、「Add Python 3.11 to PATH」オプションにチェックを入れる
3. 「Install Now」をクリック

#### wingetを使用する場合（Windows 10/11）：
```bash
winget install --id Python.Python.3.11 --version 3.11.2
```

### 2. Gitのインストール

Gitがインストールされているか確認します：

```bash
git --version
```

インストールされていない場合は、以下のいずれかの方法でインストールできます：

#### Windows用インストーラーを使用する場合：
1. [Git公式サイト](https://git-scm.com/download/win)からインストーラーをダウンロード
2. インストーラーを実行し、デフォルト設定でインストール

#### wingetを使用する場合：
```bash
winget install Git.Git
```

### 3. PostgreSQLのインストールと設定

#### PostgreSQLのインストール：
GUI操作によりインストールする。

PostgleSQLのexeファイルからインストールを実行。

1. コントロールパネルを開く: スタートメニューから「コントロールパネル」を検索し、開きます。

2. システムとセキュリティを選択: コントロールパネル内で「システムとセキュリティ」をクリックします。

3. システムを選択: 「システム」をクリックします。

4. システムの詳細設定へ進む: 左側のメニューから「システムの詳細設定」を選びます。

5. 環境変数をクリック: 「詳細設定」タブの下部にある「環境変数」ボタンをクリックします。

6. Path環境変数を編集: 「システム環境変数」セクションで「Path」を選び、「編集」をクリックします。

7. 新しいパスを追加: 「新規」ボタンをクリックして、PostgreSQLのbinディレクトリのパスを入力します。
    通常、このパスは C:\Program Files\PostgreSQL\<バージョン>\bin のようになりますが、インストール時の設定により異なる場合があります。

8. 変更を保存: OKボタンをクリックしてすべてのウィンドウを閉じ、変更を保存します。

上記の手順で環境変数を更新した後、コマンドプロンプトを再起動して psql --version を再度実行すると、psqlのバージョン情報が表示されるはずです。これで psql コマンドが使えるようになります。

---以下は参考---
1. [PostgreSQL公式サイト](https://www.postgresql.org/download/windows/)からPostgreSQL 14のインストーラーをダウンロードします。

2. インストーラーを実行し、画面の指示に従ってインストールします。
   - インストール時にはパスワードの設定を求められますので、忘れないように記録してください。
   - デフォルトのポート(5432)を使用することをお勧めします。
--------------

---以下は参考---
#### PostgreSQLサービスの起動/停止/状態確認：

```bash
# サービスの状態確認
sc query postgresql-x64-14

# サービスの起動
net start pstgresql-x64-14

# サービスの停止
net stop pstgresql-x64-14
```
サービスの起動・停止については管理者として実行する必要があります。

--------------

#### PostgreSQL接続テスト：

```bash
# PostgreSQLのbinディレクトリにPATHが通っている場合
psql -U postgres
```
パスワードを入力して接続できれば、PostgreSQLは正常に動作しています。終了するには `\q` と入力してEnterを押します。

### 4. プロジェクトディレクトリの作成とリポジトリのクローン

```bash
# todo_appディレクトリを作成
mkdir todo_app
cd todo_app

# リポジトリをクローン
git clone <リポジトリURL> .
```

### 5. 仮想環境のセットアップ

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化（コマンドプロンプトの場合）
venv\Scripts\activate.bat

# または、PowerShellの場合
# venv\Scripts\Activate.ps1
```

### 6. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

### 7. PostgreSQL接続用の環境変数設定（Windowsのみ）

Windowsでは、PostgreSQL接続用の環境変数を設定する必要があります：

```bash
# コマンドプロンプトの場合
set USER=postgres
set PGPASSWORD=あなたのパスワード  # PostgreSQLインストール時に設定したパスワード

# または、PowerShellの場合
# $env:USER = "postgres"
# $env:PGPASSWORD = "あなたのパスワード"
```

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
# コマンドプロンプトまたはPowerShellで
deactivate
```
