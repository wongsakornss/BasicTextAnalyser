# ใช้ base image ที่มี Python
FROM python:3.10-slim

# เปลี่ยน working directory ไปที่ src
WORKDIR /app

# copy ไฟล์ requirements.txt ที่อยู่ใน root directory เข้าไปใน container
COPY requirements.txt .

# ติดตั้ง dependencies ที่อยู่ใน requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy ไฟล์ทั้งหมดใน project เข้าไปใน container
COPY . .

# ตั้งค่าให้ Python path มองเห็น module ใน src
ENV PYTHONPATH=/app/src

# กำหนด port ที่ app จะรัน
EXPOSE 5000

# คำสั่งสำหรับรัน app
# app:app หมายถึงรัน app ที่ชื่อ app ในไฟล์ main.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
