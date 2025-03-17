# Frivolous Ferrets - Nia Lam and Amanda Tan
# SoftDev
# K35 - mxrobbotto
# 2025-03-14
# time spent: 2.5

from flask import render_template, request, redirect, url_for, session, g, flash, current_app
from .models import get_db, query_db

def init_app(app):
    app.teardown_appcontext(close_db)

def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@current_app.route('/')
def index():
    blogs = query_db('SELECT * FROM blog')
    return render_template('index.html', blogs=blogs)

@current_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        db.execute('INSERT INTO user (username, password) VALUES (?, ?)', (username, password))
        db.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html')

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = query_db('SELECT * FROM user WHERE username = ? AND password = ?', (username, password), one=True)
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('profile'))
        flash('Invalid username or password')
    return render_template('login.html')

@current_app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    blogs = query_db('SELECT * FROM blog WHERE user_id = ?', (user_id,))
    return render_template('profile.html', blogs=blogs)

@current_app.route('/create_blog', methods=['GET', 'POST'])
def create_blog():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session['user_id']
        db = get_db()
        db.execute('INSERT INTO blog (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
        db.commit()
        return redirect(url_for('profile'))
    return render_template('create_blog.html')

@current_app.route('/edit_blog/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    blog = query_db('SELECT * FROM blog WHERE id = ?', (blog_id,), one=True)
    if not blog or blog[3] != session['user_id']:
        return redirect(url_for('index'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db = get_db()
        db.execute('UPDATE blog SET title = ?, content = ? WHERE id = ?', (title, content, blog_id))
        db.commit()
        return redirect(url_for('profile'))
    return render_template('edit_blog.html', blog=blog)

@current_app.route('/view_blog/<int:blog_id>')
def view_blog(blog_id):
    blog = query_db('SELECT * FROM blog WHERE id = ?', (blog_id,), one=True)
    return render_template('view_blog.html', blog=blog)

@current_app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))