import os
import json
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# تحديد مسارات الملفات المعزولة
BASE_DIR = os.path.dirname(__file__)
DATA_FILE_PATH = os.path.join(BASE_DIR, 'data', 'vocabulary.json')
DB_FILE_PATH = os.path.join(BASE_DIR, 'database.db')

def load_vocabulary():
    """تحميل بنك المفردات بالترميز العربي UTF-8 مع الحركات التامة"""
    if not os.path.exists(DATA_FILE_PATH):
        return {}
    with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_db_connection():
    """إنشاء اتصال آمن بقاعدة بيانات SQLite"""
    connection = sqlite3.connect(DB_FILE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/health', methods=['GET'])
def health_check():
    """فحص سلامة الخادم الخلفي"""
    return jsonify({
        "status": "healthy",
        "service": "huroof-backend",
        "version": "1.0.0"
    }), 200

@app.route('/api/letter/<char>', methods=['GET'])
def get_letter(char):
    """جلب بيانات الحرف ومصفوفة التقطيع الصوتي لمفردات الجمادات والنباتات"""
    data = load_vocabulary()
    letters = data.get('letters', {})
    
    if char not in letters:
        return jsonify({
            "error": "Letter not found",
            "message": f"الحرف '{char}' غير مسجل في بنك المفردات حالياً."
        }), 404
        
    return jsonify({
        "letter": char,
        "details": letters[char]
    }), 200

@app.route('/api/score', methods=['POST'])
def save_score():
    """تسجيل تقدم وإتقان الطفل الفونولوجي في قاعدة البيانات"""
    payload = request.get_json()
    if not payload:
        return jsonify({"error": "Invalid payload"}), 400

    letter = payload.get('letter')
    word = payload.get('word')
    skill_type = payload.get('skill_type')  # مثل: syllable_segmentation
    score = payload.get('score', 0)

    if not all([letter, word, skill_type]):
        return jsonify({"error": "Missing required fields"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO progress (letter, word, skill_type, score)
        VALUES (?, ?, ?, ?)
    ''', (letter, word, skill_type, score))
    connection.commit()
    connection.close()

    return jsonify({
        "status": "success",
        "message": "تم حفظ نتيجة النشاط الفونولوجي بنجاح."
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
