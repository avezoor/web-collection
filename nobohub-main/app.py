import os
from flask import Flask, render_template, abort
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown
import logging

logging.basicConfig(level=logging.DEBUG)

def markdown_with_mathjax(text):
    return pygmented_markdown(text)

app = Flask(__name__)
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'content'
app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['fenced_code', 'tables']

pages = FlatPages(app)

@app.route('/')
def index():
    posts = [p for p in pages]
    posts.sort(key=lambda p: p.meta.get('date', ''), reverse=True)
    return render_template('index.html', posts=posts)

@app.route('/<path:path>/')
def post(path):
    page = pages.get_or_404(path)
    return render_template('post.html', page=page)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('base.html', error="Page not found"), 404