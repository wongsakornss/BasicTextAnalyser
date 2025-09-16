from Functions.API_text import API_text
from Functions.Self_input import main_menu


while True:

  print("===== Basic Text Menu =====")
  print("1. API Text")
  print("2. Manual Input")
  print("3. Exit")

  user_menu = input("กรุณาเลือกรายการ: ")

  if user_menu == "1":
    num_range = int(input("กรุณาใส่จำนวนประโยค: "))
    API_text(num_range)
  elif user_menu == "2":
    input_text = input("กรุณาใส่ข้อความ: ")
    main_menu(input_text)
  elif user_menu == "3":
    print("จบการทำงาน")
    break
  else:
    print("ไม่พบรายการที่เลือก\n")
