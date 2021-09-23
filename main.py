from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def index():
    time_now = datetime.datetime.now()
    this_year = time_now.year
    return render_template("index.html", year=this_year)


@app.route("/guess/<name>")
def page2(name):
    # agify
    agify_url = "https://api.agify.io?name="
    response = requests.get(agify_url + name)
    r = response.json()
    age = r['age']
    # genderize
    genderize_url = 'https://api.genderize.io?name='
    gen_resp = requests.get(genderize_url + name)
    resp = gen_resp.json()
    gender = resp['gender']
    # Copyright
    date = datetime.datetime.now()
    year = date.year
    name = name.capitalize()
    return render_template("page2.html", year=year, age=age, name=name, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/d234a5e820c263d16604"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)