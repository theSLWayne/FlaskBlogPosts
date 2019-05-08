from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Tony Stark',
        'title': 'Blog Post 1',
        'content': 'I am Iron Man!',
        'date_posted': 'May 8, 2019'
    },
    {
        'author': 'Hiran Hasanka',
        'title': 'Blog Post 2',
        'content': 'I am inevitable',
        'date_posted': 'May 8, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
