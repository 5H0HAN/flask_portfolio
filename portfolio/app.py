from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def contact_post():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    return render_template("contact.html", success=True)


if __name__ == "__main__":
    app.run(debug=True)
