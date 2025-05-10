import os
import logging
import re
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_flatpages import FlatPages, Page
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
import pygments
from markdown_katex.extension import KatexExtension
from mdx_math import MathExtension

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key_for_development")

# Bootstrap setup
bootstrap = Bootstrap(app)

# Configure FlatPages
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'tables', 'toc', 'mdx_math', KatexExtension()]

app.config.from_object(__name__)
pages = FlatPages(app)

# Pagination settings
PER_PAGE = 5

def get_all_tags():
    """Extract all unique tags from all pages"""
    all_tags = set()
    for page in pages:
        tags = page.meta.get('tags', [])
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]
        all_tags.update(tags)
    return sorted(all_tags)

@app.route('/')
def index():
    """Render the homepage with paginated code entries"""
    # Get page parameter
    page = int(request.args.get('page', 1))
    
    # Get search query
    query = request.args.get('query', '').lower()
    
    # Get tag filter
    tag_filter = request.args.get('tag', None)
    
    # Filter pages based on search query and tag
    filtered_pages = []
    for page_item in pages:
        # Handle tag search
        if tag_filter:
            page_tags = page_item.meta.get('tags', '')
            if isinstance(page_tags, str):
                page_tags = [tag.strip() for tag in page_tags.split(',')]
            if tag_filter not in page_tags:
                continue
                
        # Handle text search
        if query:
            name = str(page_item.meta.get('name', '')).lower()
            description = str(page_item.meta.get('description', '')).lower()
            title = str(page_item.path).lower()
            
            # Handle different types of metadata
            code_example = ''
            if example := page_item.meta.get('example'):
                code_example = str(example).lower()
                
            usage = ''
            if usage_item := page_item.meta.get('usage'):
                usage = str(usage_item).lower()
                
            # Handle tags
            tags = ''
            if tag_items := page_item.meta.get('tags'):
                if isinstance(tag_items, str):
                    tags = tag_items.lower()
                elif isinstance(tag_items, list):
                    tags = ' '.join(tag_items).lower()
            
            if not (query in name or query in description or query in title or 
                   query in code_example or query in usage or query in tags):
                continue
                
        filtered_pages.append(page_item)
    
    # Sort pages by name
    filtered_pages.sort(key=lambda p: p.meta.get('name', ''))
    
    # Calculate pagination
    total_pages = (len(filtered_pages) + PER_PAGE - 1) // PER_PAGE
    page = min(max(page, 1), total_pages) if total_pages > 0 else 1
    
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginated_pages = filtered_pages[start:end]
    
    # Get all tags for TOC
    all_tags = get_all_tags()
    
    return render_template('index.html', 
                          pages=paginated_pages, 
                          current_page=page, 
                          total_pages=total_pages,
                          query=query,
                          all_tags=all_tags,
                          current_tag=tag_filter)

@app.route('/<path:path>/')
def code_detail(path):
    """Display a single code entry"""
    page = pages.get_or_404(path)
    
    # Get all tags for TOC
    all_tags = get_all_tags()
    
    return render_template('code_detail.html', 
                          page=page, 
                          all_tags=all_tags)

@app.route('/tag/<tag>/')
def tag(tag):
    """Display code entries for a specific tag"""
    tagged_pages = []
    
    for page in pages:
        page_tags = page.meta.get('tags', [])
        if isinstance(page_tags, str):
            page_tags = [t.strip() for t in page_tags.split(',')]
        
        if tag in page_tags:
            tagged_pages.append(page)
    
    # Sort tagged pages by name
    tagged_pages.sort(key=lambda p: p.meta.get('name', ''))
    
    # Get all tags for TOC
    all_tags = get_all_tags()
    
    return render_template('tag.html', 
                          pages=tagged_pages, 
                          tag=tag, 
                          all_tags=all_tags)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
