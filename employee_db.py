import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("employee_data.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        salary REAL
    )
''')
conn.commit()

# Add new employee
def add_employee(name, age, department, salary):
    cursor.execute('''
        INSERT INTO employees (name, age, department, salary)
        VALUES (?, ?, ?, ?)
    ''', (name, age, department, salary))
    conn.commit()
    print("✅ Employee added successfully!")

# View all employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update employee
def update_employee(emp_id, name, age, department, salary):
    cursor.execute('''
        UPDATE employees
        SET name = ?, age = ?, department = ?, salary = ?
        WHERE id = ?
    ''', (name, age, department, salary, emp_id))
    conn.commit()
    print("✅ Employee updated successfully!")

# Delete employee
def delete_employee(emp_id):
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    print("❌ Employee deleted successfully!")

# Menu system
def menu():
    while True:
        print("\n--- Employee Database Menu ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            dept = input("Department: ")
            salary = float(input("Salary: "))
            add_employee(name, age, dept, salary)

        elif choice == '2':
            view_employees()

        elif choice == '3':
            emp_id = int(input("Enter Employee ID to update: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            dept = input("New Department: ")
            salary = float(input("New Salary: "))
            update_employee(emp_id, name, age, dept, salary)

        elif choice == '4':
            emp_id = int(input("Enter Employee ID to delete: "))
            delete_employee(emp_id)

        elif choice == '5':
            print("👋 Exiting program.")
            break

        else:
            print("❗ Invalid choice. Try again.")

# Run the menu
menu()

# Close the connection
conn.close()
