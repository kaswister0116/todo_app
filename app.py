from flask import Flask, request, render_template, redirect, url_for
from  datetime import datetime, date
import db

app = Flask(__name__)
db.init_db()

# ToDoの表示
@app.route('/')
def show_todos():
    todos = db.get_todos()
    return render_template('index.html', todos=todos, current_date=date.today())

# 新規ToDoの作成
@app.route('/create_todo', methods=['POST'])
def create_todo():
    description = request.form['description']
    deadline = request.form.get('deadline')
    
    if deadline:
        deadline = datetime.strptime(deadline, '%Y-%m-%d').date()
    
    db.add_todo(description)
    return redirect(url_for('show_todos'))

# ToDoの完了
@app.route('/update_todo', methods=['POST'])
def update_todo():
    # 関数の処理をここに書く
    return redirect(url_for('show_todos'))

# ToDoの削除
@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    # 関数の処理をここに書く
    return redirect(url_for('show_todos'))

if __name__ == '__main__':
    app.run(debug=True)
