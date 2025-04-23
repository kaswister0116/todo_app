import psycopg2, os
from psycopg2 import errors

# DBへの接続を開始する
def connect_db():
    username = "postgres"
    password = "postgres"
    try:
        connection = psycopg2.connect(
            dbname="todo_app",
            user=username,
            password=password,
            host="localhost"
        )
    except errors.OperationalError:
        create_database()
        connection = psycopg2.connect(
            dbname="todo_app",
            user=username,
            password=password,
            host="localhost"
        )
    return connection

# データベースを作成する
def create_database():
    username = "postgres"
    password = "postgres"
    con = psycopg2.connect(
        dbname="postgres",
        user=username,
        password=password,
        host="localhost"
    )
    con.autocommit = True
    try:
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE todo_app")
        cursor.close()
    finally:
        con.close()

# todoテーブルを作成する
# テーブルにカラムを追加する時は、ここのSQL文を編集する
def init_db():
    con = connect_db()
    cursor = con.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS todo (
            todo_id SERIAL PRIMARY KEY,
            description VARCHAR(255) NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            deadline DATE
        );
        """)
        con.commit()
        cursor.close()
    finally:
        con.close()

# すべてのToDoの読み込み（期限日でソート）
def get_todos():
    con = connect_db()
    try:
        cur = con.cursor()
        # 未完了のToDoは期限日の昇順（NULLは最後）
        # 完了済みのToDoは完了日時の降順
        cur.execute("""
            (
                SELECT * FROM todo
                WHERE completed = FALSE
                ORDER BY
                    CASE
                        WHEN deadline IS NULL THEN 1
                        ELSE 0
                    END,
                    deadline ASC,
                    created_at ASC
            )
            UNION ALL
            (
                SELECT * FROM todo
                WHERE completed = TRUE
                ORDER BY completed_at DESC
            );
        """)
        todos = cur.fetchall()
        return todos
    finally:
        cur.close()
        con.close()

# ToDoの追加
def add_todo(description):
    con = connect_db()
    try:
        cur = con.cursor()
        # 新規作成時に期限日を追加する場合はこのSQL文を編集する
        cur.execute("INSERT INTO todo (description) VALUES (%s)", (description,))
        con.commit()
    finally:
        cur.close()
        con.close()

# ToDoの更新（完了）
def update_todo(todo_id):
    con = connect_db()
    try:
        cur = con.cursor()
        # todo完了処理のSQL文をここに書く
        cur.execute("""
            ここにSQL文
        """, (todo_id,))
        con.commit()
    finally:
        cur.close()
        con.close()
        
# ToDoの削除
def delete_todo(todo_id):
    con = connect_db()
    try:
        cur = con.cursor()
        # 削除処理のSQL文を書く
        cur.execute("ここにSQL文", (todo_id,))
        con.commit()
    finally:
        cur.close()
        con.close()