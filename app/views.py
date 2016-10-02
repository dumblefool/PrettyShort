from flask import render_template
from app import app
import PrettyShort

@app.route('/')
@app.route('/index')
def index():
        url=raw_input()
        output=PrettyShort.prest(url)
        return render_template('index.html',output=output)
