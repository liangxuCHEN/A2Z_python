from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

"""
SECRET_KEY 配置变量是通用密钥, 可在 Flask 和多个第三方扩展中使用. 
如其名所示, 加密的强度取决于变量值的机密度. 不同的程序要使用不同的密钥, 
而且要保证其他人不知道你所用的字符串.
"""
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('hello.html', name=session['username'])
        # return '<p>欢迎 %s 回来 <a href="/logout">退出</a></p>' % escape(session['username'])
    return '<p><a href="/login">请登录</a></p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # 删除用户信息
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()