from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="companyDB"
)
cursor = db.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  name VARCHAR(50),
                  age INT,
                  salary DECIMAL(10,2))''')
db.commit()


@app.route('/')
def index():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    salary = request.form['salary']
    cursor.execute("INSERT INTO employees (name, age, salary) VALUES (%s, %s, %s)", (name, age, salary))
    db.commit()
    return redirect('/')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']
        cursor.execute("UPDATE employees SET name=%s, age=%s, salary=%s WHERE id=%s", (name, age, salary, id))
        db.commit()
        return redirect('/')
    
    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()
    return render_template('edit.html', employee=employee)


@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    db.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
