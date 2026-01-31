import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

students = [
    ('John', 'Doe', '123 Main St', 123456, 'Mumbai', 'Maharashtra', 'Robert Doe', 'Mary Doe', 9876543210, 'john.doe@example.com', 123456789012),
    ('Jane', 'Smith', '456 Park Ave', 654321, 'Delhi', 'Delhi', 'James Smith', 'Lisa Smith', 9123456789, 'jane.smith@example.com', 987654321098),
    ('Raj', 'Kumar', '789 Lake Road', 400001, 'Bangalore', 'Karnataka', 'Suresh Kumar', 'Priya Kumar', 9988776655, 'raj.kumar@example.com', 456789123456)
]

for s in students:
    c.execute("INSERT INTO student (first_name, last_name, address, pincode, city, state, father_name, mother_name, phno, emailid, adhaar_no) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", s)

conn.commit()
print(f'Added {len(students)} test students')

c.execute('SELECT COUNT(*) FROM student')
print(f'Total students in database: {c.fetchone()[0]}')

conn.close()

