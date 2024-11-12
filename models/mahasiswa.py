import sqlite3

def create_table():
    conn = sqlite3.connect('database/db.sqlite')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            npm TEXT NOT NULL,
            jurusan TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_mahasiswa(nama, npm, jurusan):
    conn = sqlite3.connect('database/db.sqlite')
    c = conn.cursor()
    c.execute('INSERT INTO mahasiswa (nama, npm, jurusan) VALUES (?, ?, ?)', (nama, npm, jurusan))
    conn.commit()
    conn.close()

def get_all_mahasiswa():
    conn = sqlite3.connect('database/db.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM mahasiswa')
    result = c.fetchall()
    conn.close()
    return result

def get_mahasiswa_by_id(mahasiswa_id):
    conn = sqlite3.connect('database/db.sqlite')
    c = conn.cursor()
    c.execute('SELECT * FROM mahasiswa WHERE id = ?', (mahasiswa_id,))
    result = c.fetchone()
    conn.close()
    return result

def update_mahasiswa(mahasiswa_id, nama, npm, jurusan):
    conn = sqlite3.connect('database/db.sqlite')
    c = conn.cursor()
    c.execute('UPDATE mahasiswa SET nama = ?, npm = ?, jurusan = ? WHERE id = ?', (nama, npm, jurusan, mahasiswa_id))
    conn.commit()
    conn.close()

def delete_mahasiswa(mahasiswa_id):
    conn = sqlite3.connect('database/db.sqlite')
    c = conn.cursor()
    c.execute('DELETE FROM mahasiswa WHERE id = ?', (mahasiswa_id,))
    conn.commit()
    conn.close()
