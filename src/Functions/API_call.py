# ไฟล์สำหรับเรียกใช้งาน API
import requests

def fetch_text_from_api():
    """
    ดึงข้อความแบบสุ่มจาก API
    """
    try:
        response = requests.get("https://api.quotable.io/random", timeout=10, verify=False)
        response.raise_for_status() # ตรวจสอบว่าเกิดข้อผิดพลาด HTTP หรือไม่
        data = response.json()
        return data.get("content", "")
    except requests.exceptions.RequestException as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
        return None
