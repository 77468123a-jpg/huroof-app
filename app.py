import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

# مسار بنك المفردات المعزول لضمان قراءته بشكل قياسي
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'vocabulary.json')

def load_vocabulary():
    """تحميل بنك المفردات بترميز UTF-8 لدعم الحركات والتنوين بدقة"""
    if not os.path.exists(DATA_FILE_PATH):
        return {}
    with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/health', methods=['GET'])
def health_check():
    """فحص سلامة وجاهزية الخادم"""
    return jsonify({
        "status": "healthy",
        "service": "huroof-backend",
        "version": "1.0.0"
    }), 200

@app.route('/api/letter/<char>', methods=['GET'])
def get_letter(char):
    """جلب بيانات الحرف، ومفردات الجمادات والنباتات، ومصفوفة التقطيع الصوتي"""
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

if __name__ == '__main__':
    app.run(debug=True)
