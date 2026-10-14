import sqlite3

def init_database():
    """تهيئة قاعدة بيانات SQLite لتتبع درجات الإتقان الصوتي للطفل"""
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # إنشاء جدول تتبع الوعي الفونولوجي والتقطيع المقطعي
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
    print("Database and progress table initialized successfully.")

if __name__ == '__main__':
    init_database()
