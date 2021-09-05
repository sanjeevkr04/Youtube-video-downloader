import os
from flask import Flask, send_from_directory
from page import page

app = Flask(__name__)
app.register_blueprint(page)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True) 