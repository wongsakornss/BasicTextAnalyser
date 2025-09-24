# Basic Text Analyser - Sprint Final
---
### เป้าหมายสัปดาห์ที่ 4 (Goals)
*   แก้ไข Warning ของ API
*   พัฒนาโปรแกรมเป็นเว็บแอปพลิเคชัน (Web Application) ด้วย **Flask Python**
*   Deploy Web Application ด้วย Docker
### Acceptance Criteria (เสร็จสมบูรณ์)
* แอปพลิเคชันสามารถทำงานได้อย่างราบรื่นและไม่เกิดข้อผิดพลาดรันในระหว่างการใช้งาน
* User Interface เป็นระเบียบ และสามารถใช้งานได้ง่าย
---
### บทบาทและความรับผิดชอบ
**1. ฟอง (Planner)**
* วางแผนโครงสร้างเว็บแอปพลิเคชัน (การสร้างไฟล์ Flask, การเชื่อมต่อ API ใน Flask, การสร้าง Folder Templates, การออกแบบ UI)
* วางแผนแก้ไข Warning หรือ Error ของ API
* วางโครงสร้างโค้ดและการแยกไฟล์ (เช่น main.py, utils.py, api.py, tests/)
* วางแผนการสร้าง Docker Compose เพื่อให้ทีมสามารถรันโปรแกรมได้สะดวก
---
**2. นัท (Coder)**
* สร้างโครงสร้างโปรเจกต์สำหรับ Flask (เช่น ไฟล์ app.py, โฟลเดอร์ templates)
* นำฟังก์ชัน Text Analyser ที่มีอยู่มาใช้ใน Flask routes
* สร้าง Route สำหรับการวิเคราะห์ข้อความที่รับจากผู้ใช้ (Manual Input)
* สร้าง Route สำหรับการดึงข้อความจาก API และวิเคราะห์
* สร้างไฟล์ docker-compose.yml และ Dockerfile สำหรับโปรเจกต์
---
**3. คิม (Debugger)**
*   ตรวจสอบ Code Coverage ของ Test Cases และพยายามเพิ่มให้ครอบคลุมตามเป้าหมาย (≥90%)
*   รัน Test Cases ทั้งหมดและแก้ไขข้อบกพร่องที่พบ
*   ทดสอบการทำงานของ Web Application ทั้งหมด (Manual Input, API Fetch) ผ่าน Browser
*   ทดสอบกระบวนการ Build และ Run ด้วย Docker และ Docker Compose
