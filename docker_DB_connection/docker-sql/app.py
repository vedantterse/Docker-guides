from flask import Flask, request, render_template
import pymysql
import logging

app = Flask(__name__)

# MySQL configuration
mysql_host = 'mysql'
mysql_user = 'root'
mysql_password = 'example'
mysql_db = 'userdb'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    phone = request.form['phone']
    email = request.form['email']

    try:
        # Connect to MySQL and insert data
        connection = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password, db=mysql_db)
        cursor = connection.cursor()
        sql = "INSERT INTO users (name, age, phone, email) VALUES (%s, %s, %s, %s)"
        val = (name, age, phone, email)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        logging.error(f"Error: {e}")
        return "Internal Server Error", 500

    return 'User registered successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
