import os
import sqlite3
from app import app

DB_FILE = 'database.db'

def ensure_database():
    """التحقق من جاهزية قاعدة البيانات لتسجيل أداء الطفل قبل بدء الخادم"""
    if not os.path.exists(DB_FILE):
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                letter TEXT NOT NULL,
                word TEXT NOT NULL,
                skill_type TEXT NOT NULL,
                score INTEGER NOT NULL DEFAULT 0,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        connection.commit()
        connection.close()
        print("Database initialized successfully.")

if __name__ == '__main__':
    ensure_database()
    print("Starting Huroof Educational App on http://127.0.0.1:5000 ...")
    app.run(host='0.0.0.0', port=5000, debug=True)
