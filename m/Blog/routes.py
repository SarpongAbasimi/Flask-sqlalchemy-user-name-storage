from flask import Flask,render_template,session,redirect,url_for,flash
from Blog import app,db
from datetime import datetime
from Blog.form import NameForm
from Blog.models import User,Role

@app.route('/',methods=['GET','POST'])
def index():
    usernam=NameForm()
    if usernam.validate_on_submit():
        user=User.query.filter_by(username=usernam.username.data).first()
        if user is None:
            user=User(username=usernam.username.data)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known']=True
        session['anon']=usernam.username.data
        usernam.username.data=''
        return redirect(url_for('index'))
    return render_template('index.html',usernam=usernam,anon=session.get('anon'), known=session.get('known',False))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
