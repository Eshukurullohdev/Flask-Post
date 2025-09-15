from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Postlarni xotirada saqlaymiz (dastur yopilsa o'chadi)
posts = []

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        posts.append({"title": title, "content": content})
        return redirect("/")
    return render_template("add_post.html")

if __name__ == "__main__":
    app.run(debug=True)
