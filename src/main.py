import TextAnalyser
print("Text Analyser Program")
sample = input("กรุณาใส่ข้อความที่ต้องการวิเคราะห์:\n")

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
        print("ตัวอักษร (รวมช่องว่าง):", count_characters(sample, True))
        print("ตัวอักษร (ไม่รวมช่องว่าง):", count_characters(sample, False))
    elif choice == "2":
        print("จำนวนคำ:", count_words(sample))
    elif choice == "3":
        print("จำนวนประโยค:", count_sentences(sample))
    elif choice == "4":
        vowels_cnt = count_vowels(sample)
        print(f"จำนวนสระทั้งหมด: {vowels_cnt}")
    elif choice == "5":
        reversed_txt = reverse_text(sample)
        print(f"ข้อความที่กลับแล้ว:\n{reversed_txt}")
    elif choice == "6":
        word, cnt = top_word(sample)
        print(f"คำที่พบบ่อยที่สุดคือ '{word}' จำนวน {cnt} ครั้ง")
    elif choice == "7":
        print("จบการทำงาน")
        break
    else:
        print("กรุณาเลือกใหม่ (1-7)")
