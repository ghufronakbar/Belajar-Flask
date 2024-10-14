from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'my-flask-app'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        data = cur.fetchall()
        cur.close()    
        return render_template('index.html', users=data)
    except Exception as e:
        return str(e)
    
@app.route('/users/<user_id>')
def get_user(user_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", [user_id])
        data = cur.fetchone()
        cur.close()
        return render_template('user.html', user=data)
    except Exception as e:
        return str(e)    
    
@app.route('/about')    
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug=True)
