from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/main")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)
