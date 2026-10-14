import json
import os

file_path = os.path.join("data", "vocabulary.json")

def verify_vocabulary():
    if not os.path.exists(file_path):
        print("خطأ: الملف غير موجود في المسار data/vocabulary.json")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    letter_b = data["letters"]["ب"]
    print("--- نتيجة فحص بنك المفردات ---")
    print("الحرف الأساسي:", letter_b["name"])
    print("الصوت الساكن:", letter_b["sound"])
    print("الكلمة الأولى (جماد):", letter_b["words"][0]["word"])
    print("التقطيع المقطعي:", " + ".join(letter_b["words"][0]["syllables"]))

if __name__ == "__main__":
    verify_vocabulary()
