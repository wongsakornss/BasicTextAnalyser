from Functions.TextAnalyser import (
    count_characters,
    count_words,
    count_sentences,
    count_vowels,
    reverse_text,
    top_word
)

text = "Hello world! This is a simple text analyzer. Hello again!"

print("ข้อความ: " + text)
print("ตัวอักษร (รวมช่องว่าง): " + str(count_characters(text, True)))
print("ตัวอักษร (ไม่รวมช่องว่าง): " + str(count_characters(text, False)))
print("จำนวนคำ: " + str(count_words(text)))
print("จำนวนประโยค: " + str(count_sentences(text)))
print("จำนวนสระทั้งหมด: " + str(count_vowels(text)))
print("คำที่พบบ่อยที่สุดคือ: " + f"{top_word(text)[0]} ({top_word(text)[1]} times)")
print("ข้อความ Reversed: " + reverse_text(text))