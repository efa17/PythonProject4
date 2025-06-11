from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'secret123'


@app.route('/', methods=['GET', 'POST'])
def add_role():
    if request.method == 'POST':
        role = request.form['role']
        name = request.form['name']
        age = request.form['age']
        contact = request.form['contact']

        # You can save this info to a database or file here

        flash(f"Role for {name} added successfully!")
        return redirect(url_for('add_role'))

    return render_template('role.html')


if __name__ == '__main__':
    app.run(debug=True)
