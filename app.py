from flask import Flask, render_template, session, redirect, url_for, request
from flask_mysqldb import MySQL

# Initialize the Flask App
app = Flask(__name__)

# Configure MySQL Database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'database-saya'
app.secret_key = 's3cr3t'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST' and 'inpEmail' in request.form and 'inpPassword' in request.form:
            email = request.form['inpEmail']
            password = request.form['inpPassword']
            if email == '' or password == '':
                return render_template('login.html', error='Email and password are required')
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
            result = cur.fetchone()
            cur.close()
            if result:
                session['is_logged_in'] = True                
                session['username'] = result[1]                
                return redirect(url_for('get_all_users'))
            else:
                return render_template('login.html', error='Invalid email or password')
        return render_template('login.html')
    except Exception as e:        
        return str(e)

# User Page
@app.route('/users')
def get_all_users():
    try:
        if 'is_logged_in' in session:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users")
            data = cur.fetchall()
            cur.close()    
            return render_template('index.html', users=data)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return str(e)

# Detail User Page    
@app.route('/users/<user_id>')
def get_user(user_id):
    try:
        if 'is_logged_in' in session:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE id = %s", [user_id])
            data = cur.fetchone()
            cur.close()
            return render_template('user.html', user=data)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return str(e)    
    
    
# About Page    
@app.route('/about')    
def about():
    try:
        if 'is_logged_in' in session:
            return render_template('about.html')
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return str(e)

@app.route('/logout')
def logout():
    session.pop('is_logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


# Run the App    
if __name__ == '__main__':
    app.run(debug=True)
