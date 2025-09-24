# ไฟล์หลักของ Flask
from flask import Flask, request, jsonify, render_template

# นำเข้าฟังก์ชันจากไฟล์แยก
from functions.textanalyser import analyze_text
from functions.api_call import fetch_text_from_api

# กำหนดให้ Flask รู้จักโฟลเดอร์ templates และ static
app = Flask(__name__, template_folder='templates', static_folder='static')

# Route สำหรับหน้าแรก
@app.route("/")
def home():
    """แสดงหน้าเว็บหลัก"""
    # Flask จะประมวลผล url_for ในไฟล์ HTML ก่อนส่งให้เบราว์เซอร์
    return render_template("home.html")

# Route สำหรับการวิเคราะห์ข้อความที่ผู้ใช้กรอกเอง
@app.route("/analyze_manual", methods=["POST"])
def analyze_manual():
    """วิเคราะห์ข้อความที่ส่งมาผ่านฟอร์ม"""
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "กรุณาใส่ข้อความเพื่อวิเคราะห์"}), 400

    results = analyze_text(text)
    return jsonify(results)

# Route สำหรับการดึงข้อความจาก API และวิเคราะห์
@app.route("/analyze_api", methods=["POST"])
def analyze_api():
    """ดึงข้อความจาก API และวิเคราะห์"""
    text = fetch_text_from_api()
    if not text:
        return jsonify({"error": "ไม่สามารถดึงข้อความจาก API ได้"}), 500

    results = analyze_text(text)
    return jsonify(results)

if __name__ == "__main__":
    # รันเซิร์ฟเวอร์ Flask ในโหมด debug
    app.run(debug=True)
