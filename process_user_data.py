from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/get_user/<name>')
def get_user(name):
    return f'<h1>Good morning {name} </h1>'


@app.route('/user', methods=['POST', 'GET'])
def user_info():
    username = ''
    if request.method == 'POST':
        username = request.form.get('fullname')
        return redirect(url_for('get_user', name=username))
    else:
        username = request.args.get('name')
        return redirect(url_for('get_user', name=username))


if __name__ == '__main__':
    app.run(debug=True)
