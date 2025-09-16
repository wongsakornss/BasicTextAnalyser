import time
from Functions.API_call import fetch_text_from_api
from Functions.TextAnalyser import (
    count_characters,
    count_words,
    count_sentences,
    count_vowels,
    reverse_text,
    top_word
)

def API_text(num_range):
  random_texts = []
  for _ in range(num_range):
      text = fetch_text_from_api()
      if text:  
          random_texts.append(text)
          time.sleep(1)
    
  for item in range(len(random_texts)):
    print(f"{item + 1}: {random_texts[item]}")
    print("ข้อความ: " + text)
    print("ตัวอักษร (รวมช่องว่าง): " + str(count_characters(random_texts[item], True)))
    print("ตัวอักษร (ไม่รวมช่องว่าง): " + str(count_characters(random_texts[item], False)))
    print("จำนวนคำ: " + str(count_words(random_texts[item])))
    print("จำนวนประโยค: " + str(count_sentences(random_texts[item])))
    print("จำนวนสระทั้งหมด: " + str(count_vowels(random_texts[item])))
    print("คำที่พบบ่อยที่สุดคือ: " + f"{top_word(random_texts[item])[0]} ({top_word(random_texts[item])[1]} times)")
    print("ข้อความ Reversed: " + reverse_text(random_texts[item]))
    print()