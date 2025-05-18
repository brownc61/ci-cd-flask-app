from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def home():
    return "🚀 CI/CD Flask App is Running!"

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
