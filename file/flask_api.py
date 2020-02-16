from file.db_test import engine, Base, DBSession, User
from flask import Flask, g, redirect, url_for, escape, request, render_template, jsonify

# Flask相关变量声明
app = Flask(__name__)

# 构建数据模型的json格式
def get_json(user):
    return {"id": user.id, "name": user.name, "age": user.age}

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
session = DBSession()

@app.route('/')
def index():
    return '<p><a href="/list">用户列表</a></p><p><a href="/create">添加用户</a></p>'

@app.route('/list', methods=['GET', 'POST'])
def users_list():
    users = session.query(User).all()
    content =  [get_json(user) for user in users]
    return jsonify(summary=content)


@app.route('/create', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user = User(name=request.form["name"], age=request.form["age"])
        session.add(user)
        session.commit()
        return redirect(url_for('users_list'))
    return '''
        <form method="post">
            <p>添加用户：</p>
            <p>名字：<input type=text name=name></p>
            <p>年龄：<input type=number name=age></p>
            <p><input type=submit value=add_user></p>
        </form>
    '''

# TODO:根据id - 删除用户
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # 获取参数
    # # session.query(User).filter(User.id == user_id).delete()
    return 'user_id %d' % user_id


# TODO:根据id - 修改用户信息
@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    user_ids_set = set([user.id for user in session.query(User.id)])
    print(user_ids_set)

    # 用户不存在，返回404
    if user_id not in user_ids_set:
        return "不存在用户"

    # 更新用户数据
    # user = session.query(User).filter(User.id == user_id)
    # user.name = ???
    # user.age = ???
    # session.merge(user)
    # session.commit()

    # 更新成功
    # return jsonify(get_json(user))
    return 'user_id %d' % user_id

# TODO: book 的增，　删，　更新，显示所有

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9088)
