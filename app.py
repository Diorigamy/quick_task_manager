from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secure_secret_key'
app.config['DEBUG'] = False

# Configure the database URI. Replace 'sqlite:////tmp/test.db' with your actual database URI.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a simple model for demonstration purposes
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

@app.route('/')
def landing_page():
    return render_template('landing.html')

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)

