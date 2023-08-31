from flask import Flask

app = Flask('meu app')

@app.route('/')
def hello():
    return "Hello Word"

@app.route('/novo')
def nova():
    return "<h1> Nova Página</h1>"