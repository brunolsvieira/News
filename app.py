import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	template = 'index.html'
	return render_template(template)

@app.route('/maester')
def maester():
	data = pd.read_csv('./static/Maester Vieira - Data.csv').tail()
	data = data.to_html(classes=['table', 'table-hover'])
	return data

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

