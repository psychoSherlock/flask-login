from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
