from flask import render_template
from app import app
import PrettyShort

@app.route('/')
@app.route('/index')
def index():
        output=PrettyShort.prest()
        return render_template('index.html',output=output)
