from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


items = []

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html', items=items)

@app.route("/add", methods=["POST"])
def add_item():
    item_text = request.form.get("item")
    if item_text:
        items.append({"text": item_text, "checked": False})
    return redirect(url_for("home"))

@app.route("/clear", methods=["POST"])
def clear_item():
    items.clear()
    return redirect(url_for("home"))


@app.route("/toggle", methods=["POST"])
def toggle_item():
    index_str = request.form.get("index")
    if index_str is not None:
        index = int(index_str)
        items[index]["checked"] = not items[index]["checked"]
    return redirect(url_for("home"))

@app.route("/delete", methods=["POST"])
def delete_item():
    index_str = request.form.get("index")
    if index_str is not None:
        index = int(index_str)
        if 0 <= index < len(items):
            items.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
