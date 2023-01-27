from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Pass in a cat name
    # We insert it to the html with jinja2 templates!
    return '<h1> Go to /cat/name </h1>'


@app.route('/cat/<name>')
def cat_name(name):
    # Pass in a cat name
    # We insert it to the html with jinja2 templates!
    return render_template('Template-Filters.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
