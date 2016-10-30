from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Keqing'}
    posts = [
        {
            'author':{'nickname': 'John'},
            'body': 'Beautiful day in Wuxue!'
        },
        {
            'author':{'nickname': 'Susan'},
            'body': 'Beautiful day in Daye!'
        }
    ]
    return render_template('index.html',
            title = '首页',
            user =user,
            posts = posts
    )