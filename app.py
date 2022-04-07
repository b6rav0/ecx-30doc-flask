from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initializing the database
db = SQLAlchemy(app)

# Creating Database Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/home/<username>')
def home(username):
    return render_template('index.html', username=username)


if __name__ == "__main__":
    app.run()
