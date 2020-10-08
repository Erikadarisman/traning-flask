from app import app
from markupsafe import escape


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return "Hello, world!"


# @app.route('/user/<username>')
# def show_user(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def post_id(post_id):
    return 'Post id %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
