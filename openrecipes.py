import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


@app.route('/')
def index():
    return page('index')


@app.route('/stats/')
def stats():
    """
    special stats page that renders a template directly
    """
    return render_template('stats.html')


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@freezer.register_generator
def page_gen():
    for page in pages:
        if page.path != "index":
            yield "page", {'path': page.path}


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
