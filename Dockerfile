# ใช้ Python base image
FROM python:3.12-slim

# ตั้ง working directory
WORKDIR /app

# คัดลอก requirements.txt และติดตั้ง
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมด
COPY . .

# รัน pytest เพื่อทดสอบ (optional)
CMD ["python", "src/main.py"]
