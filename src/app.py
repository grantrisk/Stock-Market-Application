from flask import Flask

from blueprints.index import index_page

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

app.register_blueprint(index_page, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
