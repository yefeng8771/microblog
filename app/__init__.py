from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)    #这个是app变量
app.config.from_object('config')
db = SQLAlchemy(app)


'''
为何这个导入不在首行导入，是为了避免循环引用
因为导入views模块前需要先定义app变量，*不懂*
'''
from app import views,models   #这个app是包名（app文件夹）