from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<name>')
def home(name):
    return render_template('index.html', name=name.capitalize())


if __name__ == "__main__":
    app.run()
