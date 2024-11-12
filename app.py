# app.py
from flask import Flask, request
from controllers.mahasiswa_controller import show_all_mahasiswa, show_create_form, create_mahasiswa, show_update_form, update_mahasiswa_data, delete_mahasiswa_data

app = Flask(__name__)

# Route for showing all mahasiswa
@app.route('/')
def semua_mahasiswa():
    return show_all_mahasiswa()

# Route for creating mahasiswa (GET for form, POST for submission)
@app.route('/create', methods=['GET', 'POST'])
def buat_mahasiswa():
    if request.method == 'POST':
        return create_mahasiswa()
    return show_create_form()

# Route for updating mahasiswa (GET for form, POST for submission)
@app.route('/update/<int:mahasiswa_id>', methods=['GET', 'POST'])
def update_mahasiswa(mahasiswa_id):  # Ensure this matches the name you're using in the controller
    if request.method == 'POST':
        return update_mahasiswa_data(mahasiswa_id)
    return show_update_form(mahasiswa_id)

# Route for deleting mahasiswa
@app.route('/delete/<int:mahasiswa_id>')
def hapus_mahasiswa(mahasiswa_id):  # Ensure this matches the name you're using in the controller
    return delete_mahasiswa_data(mahasiswa_id)

if __name__ == '__main__':
    app.run(debug=True)
