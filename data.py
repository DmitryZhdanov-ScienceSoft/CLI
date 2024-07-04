from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    # Выполнение команды в терминале и получение вывода
    result = subprocess.run(['termgraph', 'data.csv'], stdout=subprocess.PIPE, text=True)
    output = result.stdout

    # HTML шаблон для отображения вывода
    html_template = r"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CLI Output</title>
        <style>
            pre {
                background-color: #f4f4f4;
                padding: 10px;
                border: 1px solid #ddd;
            }
        </style>
    </head>
    <body>
        <h1>CLI Output</h1>
        <pre>{{ output }}</pre>
    </body>
    </html>
    """
    return render_template_string(html_template, output=output)


if __name__ == '__main__':
    app.run(debug=True)
