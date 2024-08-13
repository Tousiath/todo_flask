# **ToDo Application using Flask**

## **1. Introduction**

The ToDo Application is a simple web application built using Flask and SQLAlchemy. It allows users to create, read, update, and delete tasks. The application uses an SQLite database to store task information and provides a user-friendly interface for managing daily tasks.

## **2. Directory Structure**

For easier navigation, the project is organized as follows:

```plaintext
ToDo_Application
│
├── app.py           # Main Flask application
├── static/          # Static files (CSS, JS, Images)
├── templates/       # HTML templates for the application
├── Todo.db          # SQLite database file
└── Procfile         # For deploying to Heroku or similar platforms
```


**app.py**  
This file contains the main code for the Flask application. It defines routes for adding, viewing, updating, and deleting tasks. The application interacts with an SQLite database using SQLAlchemy.

**static/**  
This directory holds the static files like CSS for styling, JavaScript for interactivity, and any images required by the web application.

**templates/**  
This directory contains HTML files used by Flask to render web pages. The main pages are `index.html`, `about.html`, and `update.html`.

**Todo.db**  
This is the SQLite database file where all the tasks are stored. It contains the `Todo` table with fields like `sno`, `title`, `desc`, and `date_created`.

**Procfile**  
This file is used for deploying the application on platforms like Heroku. It specifies the commands that are run by the application server.


## **3. Features**
Add Task: Users can add a new task with a title and description.

View Tasks: The home page displays all the tasks stored in the database.

Update Task: Users can update the details of a task.

Delete Task: Users can delete a task from the list.

## **4. Usage**
Home Page: Add, view, update, or delete tasks.

About Page: Information about the application.

### **Output Screens**
![result3](https://github.com/user-attachments/assets/0dba6fe8-6533-4f73-8b96-a73073a9bf93)

![result1](https://github.com/user-attachments/assets/289f92eb-4982-41b4-ba0b-bc76651afc89)

**update page**
![Screenshot (627)](https://github.com/user-attachments/assets/f8d2b613-6bc2-49f3-9019-1085f3e8c1ea)


## **5. Conclusion**
This ToDo application is a basic example of using Flask to create a CRUD (Create, Read, Update, Delete) application. It's a great starting point for learning about web development with Flask and SQLAlchemy.

---

**Happy coding and keep exploring! 😊😊**
