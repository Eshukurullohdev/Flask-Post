from flask import Flask, request, render_template, redirect

app = Flask(__name__);

posts = []; 

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

if __name__ =="__main__":
    app.run(debug=True)
    
     
# Post ---- yangi malumotni qoyish
# Get ---- Olish Bor malumotni oldi
# Update ---- Bor malumotni yangilash
# Delete ---- Bor malumotni ochirish
# Put ---- Rest Api


# List
# Method
# append
# remove

# Authentication