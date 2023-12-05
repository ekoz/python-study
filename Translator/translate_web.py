#!/usr/bin/env python
# encoding: utf-8

"""
$env:FLASK_APP="translate_web.py"
flask run
@version: 1.0
@author: eko.zhan
@contact: eko.z@hotmail.com
@file: translate_web.py
@time: 2019/4/26 17:55
@see https://docs.python.org/3/library/tempfile.html
@see http://flask.pocoo.org/docs/1.0/
@see https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.FileStorage
"""
import tempfile
try:
    import threading
except ImportError:
    import dummy_threading as threading
from translator import transfer, Translator
from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "It works."


@app.route("/<text>")
def translate(text):
    return Translator(text).fire()


@app.route('/upload', methods=['post'])
def upload():
    f = request.files['file']
    # f.filename language.js
    tmp_file_dir = tempfile.gettempdir() + '/' + f.filename
    f.save(tmp_file_dir)
    # fixme not async
    threading.Thread(target=transfer(tmp_file_dir)).start()
    return tmp_file_dir


if __name__ == '__main__':
    app.run()
