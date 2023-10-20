from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="db",
        user="test_user",
        password="password",
        database="test_database",
    )
    cursor = conn.cursor()
    cursor.execute("select * from article")
    data = cursor.fetchall()
    return str(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
