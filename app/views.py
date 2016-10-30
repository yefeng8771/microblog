from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('你登入的OpenID 是 = %s, remember_me = %s' %(
            form.openid.data, str(form.remember_me)))
        return redirect('/index')
    return render_template('login.html',
        title = '登入',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])