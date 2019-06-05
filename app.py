from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__) # definig the Flash object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #4 / absolute path, 3/ relative path
db = SQLAlchemy(app)

class Todo(db.Model): # metadata
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    data_created = db.Column(db.DateTime, default = datetime.now)

    def __repr__(self):
        return '<Task %r>' %self.id

@app.route("/") # 
def index():
    """index function """
    #return ("Hello World!")
    return render_template('index.html') #  load html template, no need to define the folder module takes care of it
if __name__ == "__main__":
    app.run(debug=True) # calling the run function to start the local host
