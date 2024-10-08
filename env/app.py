from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session management

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    tick = db.Column(db.Boolean, default=False)  # New column for checkboxes

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route('/complete/<int:sno>', methods=['POST'])
def complete_todo(sno):
    todo = Todo.query.get_or_404(sno)
    todo.tick = True  # Update the tick attribute to indicate completion
    db.session.commit()
    return redirect("/")

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if 'new_user' not in session:
        session['new_user'] = True

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        session['new_user'] = False

    allTodo = Todo.query.all()
    
    if session['new_user']:
        return render_template('index.html', allTodo=allTodo, new_user=True)
    else:
        return render_template('index.html', allTodo=allTodo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
