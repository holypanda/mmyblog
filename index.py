from flask import Flask
from flask import render_template
from flask import request
from flask import flash
import sqlite3

import os



def save_post_to_db(create_date, title, content, img):
    conn = sqlite3.connect("static/post/blog.db")
    c = conn.cursor()
    c.execute("INSERT INTO blog (title, create_date, content, img_path) VALUES (?,?,?,?)", (title, create_date, content, img))
    conn.commit()
    conn.close()

def read_post():
    conn = sqlite3.connect("static/post/blog.db")
    c = conn.cursor()
    c.execute("SELECT * FROM blog")
    posts = c.fetchall()
    conn.close()
    return posts

def read_more_post(id):
    conn = sqlite3.connect("static/post/blog.db")
    c = conn.cursor()
    c.execute("SELECT * FROM blog WHERE id=?",id)
    read_more_data = c.fetchall()
    conn.close()
    return read_more_data[0]
app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome_page():
    return render_template("welcome.html", title="口羊咩")


@app.route("/home", methods=["GET"])
def home_page():
    posts = read_post()
    # id, title, date, content, img_path
    print(posts)

    return render_template("home_page.html", title="小窝", posts=posts)

@app.route("/post/<id>", methods=["GET"])
def read_more(id):

    # with open("static/post/%s.txt" % filename) as f:
    #     img_name = filename + ".jpg"
    #     title = filename
    #     path = filename
    #     content = f.read()
    #     detail_article = (title, content, img_name, path)
    #     print(detail_article)
    detail_article = read_more_post(id)
    print(detail_article)
    return render_template("read_more.html", title="小窝", detail_article=detail_article)

@app.route("/upload_post", methods=["GET", "POST"])
def upload_post():
    if request.method == "GET":
        return render_template("upload_post.html")
    elif request.method == "POST":
        date = request.form['upload_date']
        title = request.form['upload_title']
        content = request.form['upload_content']
        file = request.files["upload_image"]
        path = "static/post_img/%s" % file.filename
        file.save(path)
        save_post_to_db(date, title, content, path)
        return render_template("upload_post.html", messages="上传成功")

@app.route("/archive", methods=["GET"])
def archive():
    posts = read_post()
    # id, title, date, content, img_path
    print(posts)
    return render_template("archive.html", posts=posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80) # port 80