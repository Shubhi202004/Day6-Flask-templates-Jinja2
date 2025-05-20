from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    users = ['Alice', 'Bob', 'Charlie', 'Diana']
    user_info = {
        'name': 'Alice',
        'age': 25,
        'location': 'New York'
    }
    is_logged_in = True
    return render_template("home.html", users=users, info=user_info, logged_in=is_logged_in)

if _name_ == '_main_':
    app.run(debug=True)