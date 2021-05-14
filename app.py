from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "<h1>This is me</h1><p>Hello, World!</p>"
