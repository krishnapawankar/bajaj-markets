from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    cats = ['tom', 'luna', 'simba', 'milo', 'leo']
    return render_template('Template-Control-Flow.html',
                           cats=cats)


if __name__ == '__main__':
    app.run(debug=True)
