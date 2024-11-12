from flask import render_template, request, redirect, url_for
from models.mahasiswa import create_table, insert_mahasiswa, get_all_mahasiswa, get_mahasiswa_by_id, update_mahasiswa, delete_mahasiswa

create_table()

def show_all_mahasiswa():
    mahasiswa_list = get_all_mahasiswa()
    return render_template('index.html', mahasiswa_list=mahasiswa_list)

def show_create_form():
    return render_template('create.html')

def create_mahasiswa():
    if request.method == 'POST':
        nama = request.form['nama']
        npm = request.form['npm']
        jurusan = request.form['jurusan']
        insert_mahasiswa(nama, npm, jurusan)
        return redirect(url_for('semua_mahasiswa'))  
    
def show_update_form(mahasiswa_id):
    mahasiswa = get_mahasiswa_by_id(mahasiswa_id)
    return render_template('update.html', mahasiswa=mahasiswa)

def update_mahasiswa_data(mahasiswa_id):
    if request.method == 'POST':
        nama = request.form['nama']
        npm = request.form['npm']
        jurusan = request.form['jurusan']
        update_mahasiswa(mahasiswa_id, nama, npm, jurusan)
        return redirect(url_for('semua_mahasiswa'))  
    
def delete_mahasiswa_data(mahasiswa_id):
    delete_mahasiswa(mahasiswa_id)
    return redirect(url_for('semua_mahasiswa'))  
