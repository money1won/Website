# To import flask, go to "File" "Settings" "Project" "Project Interpreter" "+ (on the right side of the window)"

from flask import Flask, render_template
app = Flask(__name__)  # This is the main object for the website

@app.route("/")
def home():
    return "<h1>This website looks as shady as Cragislist</h1>"

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

# @app.route("/profile/<name>")
# def profile(name):
#    return render_template("profile.html", name=name)

# def index():
#    return "hello: %s" % request.method

# @app.route("/info")
# def info():
#     return "<h2>This is a test</h2>"
#
# @app.route("/profile/<username>")  # Routes if a string is used in the URL
# def profile(username):
#     return "<h2>Hey there %s</h2>" % username
#
# @app.route("/profile/<int:post_id>") # Routes if a number is used in the URL
# def show_post(post_id):
#     return "<h2>Post ID is %s</h2>" % post_id

if __name__ == "__main__":
    app.run()