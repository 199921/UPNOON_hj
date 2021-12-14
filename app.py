from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('admin.html')

@app.route('/index')
def index_admin():
	return render_template('index.html')

@app.route('/mypage')
def index_admin_lists():
	return render_template('mypage.html')

if __name__ == '__main__':
    app.run()
