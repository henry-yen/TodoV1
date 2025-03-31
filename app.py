from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

items = []
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html', items=items)

@app.route("/", methods=["POST"])
def add_item():
    item = request.form.get("item")
    if item:
        items.append(item)
    return redirect(url_for("home"))

if __name__ == ('__main__'):
    app.run()