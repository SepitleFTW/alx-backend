#!/usr/bin/env python3
'''first task
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''default rosadaute'''
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
