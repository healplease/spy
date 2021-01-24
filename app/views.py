from flask import request, render_template, abort, session, g, url_for

from app import app, api

@app.route('/')
def index():
    return render_template('index.html')