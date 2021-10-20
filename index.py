from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")

emoji_list = [
    {
        "name": "Umbrella",
        "code": 2602,
    },
    {
        "name": "Spades",
        "code": 2660,
    },
    {
        "name": "Heart",
        "code": 2764,
    },
    {
        "name": "Snowflake",
        "code": 2744,
    },
    {
        "name": "Coffeeeee",
        "code": 2615,
    },
]

@app.route("/")
def index():
    return render_template("index.html", emoji_list=emoji_list)

@app.route("/emoji/<emoji_id>")
def emoji(emoji_id):

    # ===== Error handling ===== #

    emoji_exists = emoji_id.isdigit() and int(emoji_id) < len(emoji_list)
    if not emoji_exists:
        return render_template("404.html"), 404

    # ===== Returning emoji page ===== #

    emoji_id_int = int(emoji_id)
    emoji_obj = emoji_list[emoji_id_int]
    return render_template("emoji_view.html", emoji=emoji_obj)

@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"), 404

app.run(debug=True)