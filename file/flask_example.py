# 再来一个Hello
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '这里是主页'


@app.route('/about')
def about():
    return '这是关于我们的信息'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 获取参数
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.run()