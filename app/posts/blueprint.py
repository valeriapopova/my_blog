from flask import Blueprint, render_template, redirect, url_for
from models import Post, Tag
from app import db
from flask import request
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder="templates")


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if title:
            try:
                post = Post(title=title, body=body)
                db.session.add(post)
                db.session.commit()
            except:
                print('сломався')
            return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        p = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    # else:order_by(Post.created.desc())
    else:
        p = Post.query.all()
    return render_template('posts/index.html', posts=p)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
