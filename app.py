from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_data = request.form.to_dict()
        if not os.path.exists('results'):
            os.makedirs('results')
        with open('results/users.json', 'a') as f:
            json.dump(user_data, f)
            f.write('\n')
    return render_template('add_user.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_data = request.form.to_dict()
        if not os.path.exists('results'):
            os.makedirs('results')
        with open('results/books.json', 'a') as f:
            json.dump(book_data, f)
            f.write('\n')
    return render_template('add_book.html')

@app.route('/users')
def show_users():
    if os.path.exists('results/users.json'):
        with open('results/users.json', 'r') as f:
            users = [json.loads(line) for line in f]
        return render_template('users.html', users=users)
    else:
        return "No users data available"

@app.route('/books')
def show_books():
    if os.path.exists('results/books.json'):
        with open('results/books.json', 'r') as f:
            books = [json.loads(line) for line in f]
        return render_template('books.html', books=books)
    else:
        return "No books data available"

if __name__ == '__main__':
    app.run(debug=True)