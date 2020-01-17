from flask import Flask, render_template, url_for
app = Flask(__name__)

posts=[
	{
		'author': 'Cooper Wallace',
		'title': 'Tweet 1',
		'content': 'content',
		'date_posted': 'January 1, 2020'
	},
	{
		'author': 'Sam Wallace',
		'title': 'Tweet 2',
		'content': 'content',
		'date_posted': 'January 1, 2020'

	}

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')



if __name__ == '__main__':
    app.run(debug=True)