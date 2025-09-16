from Functions.TextAnalyser import (
    count_characters,
    count_words,
    count_sentences,
    count_vowels,
    reverse_text,
    top_word
)

def main_menu(input_text):
  while True:
      print("\n===== Basic Text Analyzer =====")
      print("1. นับจำนวนตัวอักษร")
      print("2. นับจำนวนคำ")
      print("3. นับจำนวนประโยค")
      print("4. นับสระ")
      print("5. กลับข้อความ")
      print("6. หาคำที่เจอบ่อยที่สุด")
      print("7. ออกจากโปรแกรม")

      choice = input("เลือกเมนู (1-7): ")

      if choice == "1":
          print("ตัวอักษร (รวมช่องว่าง):", count_characters(input_text, True))
          print("ตัวอักษร (ไม่รวมช่องว่าง):", count_characters(input_text, False))
      elif choice == "2":
          print("จำนวนคำ:", count_words(input_text))
      elif choice == "3":
          print("จำนวนประโยค:", count_sentences(input_text))
      elif choice == "4":
          vowels_cnt = count_vowels(input_text)
          print(f"จำนวนสระทั้งหมด: {vowels_cnt}")
      elif choice == "5":
          reversed_txt = reverse_text(input_text)
          print(f"ข้อความที่กลับแล้ว:\n{reversed_txt}")
      elif choice == "6":
          word, cnt = top_word(input_text)
          print(f"คำที่พบบ่อยที่สุดคือ '{word}' จำนวน {cnt} ครั้ง")
      elif choice == "7":
          print("จบการทำงาน")
          break
      else:
          print("กรุณาเลือกใหม่ (1-7)")