from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

#app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///Todo.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D:/env/var/app-instance/Todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

#models
#table(database)
class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
    #app.app_context().push()
    
    def __repr__(self)->str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc'] 
        
        
        todo=Todo(title=title, desc=desc)
        db.session.add(todo)            #inorder to write the content into db
        db.session.commit()             #inorder to write the content into db
    
    allTodo=Todo.query.all()        #for displaying
    return render_template('index.html', allTodo=allTodo) #using jinja2 template #in index.html also {{%for in%}} {{%%end for}} is used near table and "loop.index" for the purpose of continuing the numbers
    #return 'Hello, World!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show')
def products():
    allTodo=Todo.query.all()    #for displaying
    print(allTodo)
    return 'this is products page'

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()    #for deleting
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port=8000)