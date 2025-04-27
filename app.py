from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('health.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize DB tables
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS programs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            program_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES clients (id),
            FOREIGN KEY (program_id) REFERENCES programs (id)
        )
    ''')
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_program', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        conn.execute('INSERT INTO programs (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('add_program.html')

@app.route('/register_client', methods=['GET', 'POST'])
def register_client():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        conn = get_db_connection()
        conn.execute('INSERT INTO clients (name, age, gender) VALUES (?, ?, ?)', (name, age, gender))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('register_client.html')

@app.route('/enroll_client', methods=['GET', 'POST'])
def enroll_client():
    conn = get_db_connection()
    clients = conn.execute('SELECT * FROM clients').fetchall()
    programs = conn.execute('SELECT * FROM programs').fetchall()
    conn.close()

    if request.method == 'POST':
        client_id = request.form['client_id']
        program_ids = request.form.getlist('program_ids')
        conn = get_db_connection()
        for program_id in program_ids:
            conn.execute('INSERT INTO enrollments (client_id, program_id) VALUES (?, ?)', (client_id, program_id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('enroll_client.html', clients=clients, programs=programs)

@app.route('/search_client', methods=['GET', 'POST'])
def search_client():
    results = []
    if request.method == 'POST':
        search_name = request.form['search_name']
        conn = get_db_connection()
        results = conn.execute("SELECT * FROM clients WHERE name LIKE ?", ('%' + search_name + '%',)).fetchall()
        conn.close()
    return render_template('search_client.html', results=results)

@app.route('/view_client/<int:client_id>')
def view_client(client_id):
    conn = get_db_connection()
    client = conn.execute('SELECT * FROM clients WHERE id = ?', (client_id,)).fetchone()
    programs = conn.execute('''
        SELECT programs.name FROM enrollments
        JOIN programs ON enrollments.program_id = programs.id
        WHERE enrollments.client_id = ?
    ''', (client_id,)).fetchall()
    conn.close()
    return render_template('view_client.html', client=client, programs=programs)

@app.route('/api/client/<int:client_id>')
def api_client(client_id):
    conn = get_db_connection()
    client = conn.execute('SELECT * FROM clients WHERE id = ?', (client_id,)).fetchone()
    programs = conn.execute('''
        SELECT programs.name FROM enrollments
        JOIN programs ON enrollments.program_id = programs.id
        WHERE enrollments.client_id = ?
    ''', (client_id,)).fetchall()
    conn.close()

    if client is None:
        return jsonify({'error': 'Client not found'}), 404

    return jsonify({
        'id': client['id'],
        'name': client['name'],
        'age': client['age'],
        'gender': client['gender'],
        'programs': [program['name'] for program in programs]
    })

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
