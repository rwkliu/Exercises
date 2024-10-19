from flask import Flask, render_template, render_template_string
from flask_htmx import HTMX

app = Flask(__name__)
htmx = HTMX(app)


@app.route("/")
def home():
    if htmx:
        return render_template("thing.html")
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>HTMX Button Example</title>
            <script src="https://unpkg.com/htmx.org@1.8.4"></script>
        </head>
        <body>
            <h1>HTMX + Flask Example</h1>

            <!-- Button that triggers hx-get on click -->
            <button hx-get="/example" hx-target="#response" hx-swap="outerHTML">
                <div id="response">
                    Click me to get a message
                </div>
            </button>

        </body>
        </html>
        """
    )


@app.route("/example")
def example():
    return "<p>replaced button HTMX</p>"


if __name__ == "__main__":
    app.run(debug=True)
