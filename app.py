from flask import Flask, render_template
import database


app = Flask(__name__)

database.init_db()


@app.route("/")
def home():

    logs = database.fetch_logs()

    return render_template(
        "index.html",
        logs=logs
    )


if __name__ == "__main__":

    app.run(debug=True)