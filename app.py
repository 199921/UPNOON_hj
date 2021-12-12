from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index_user.html')

@app.route('/index_admin')
def index_admin():
	return render_template('index_admin.html')

@app.route('/index_admin_lists')
def index_admin_lists():
	return render_template('index_admin_lists.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
