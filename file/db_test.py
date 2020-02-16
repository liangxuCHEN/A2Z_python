from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 数据库连接字符串
DB_CONNECT_STRING = 'sqlite:///db_test.sqlite'


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    # 另外写法
    age = Column("age", Integer, default=0)

    books = relationship('Book')

# 创建一个书的类
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

# 初始化数据库连接:
engine = create_engine(DB_CONNECT_STRING)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 删除所有表
# Base.metadata.drop_all(engine)
# 创建数据表，如果数据表存在则忽视！！！
Base.metadata.create_all(engine)


def add_user(name, age=0):
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(name=name, age=age)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    print("user id", new_user.id)
    # 关闭session:
    session.close()
    return new_user

def add_book(book_name, user_id):
    # 创建session对象:
    session = DBSession()
    # 添加到session:
    # TODO: 写你们的代码
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    print("book id", new_book.id)
    session.close()
    return new_book

def get_book(book_id):
    """
    输入书本ｉｄ，输出书名和人名
    :param book_id: 
    :return: 
    """
    pass

if __name__ == '__main__':
    user1 = add_user(name="小灵", age=10)
    user2 = add_user(name="大鸿", age=18)
    #book = add_book(book_name='鼠标', user_id=user.id)
    #print(book.id)
    #get_book(5)
