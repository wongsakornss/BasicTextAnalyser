# ไฟล์ที่เก็บฟังก์ชันสำหรับการวิเคราะห์ข้อความ
import re

def analyze_text(text):
    """
    ฟังก์ชันหลักที่รวบรวมการวิเคราะห์ข้อความทั้งหมด
    และส่งผลลัพธ์กลับในรูปแบบ dictionary
    """
    return {
        "text": text,
        "char_count_with_spaces": count_characters(text, True),
        "char_count_without_spaces": count_characters(text, False),
        "word_count": count_words(text),
        "sentence_count": count_sentences(text),
        "vowel_count": count_vowels(text),
        "reversed_text": reverse_text(text),
        "top_word_data": top_word(text)
    }

def count_characters(text, include_spaces=True):
    """นับจำนวนตัวอักษรในข้อความ"""
    if include_spaces:
        return len(text)
    else:
        # ใช้ regular expression เพื่อลบช่องว่างทั้งหมด
        return len(re.sub(r'\s', '', text))

def count_words(text):
    """นับจำนวนคำในข้อความ"""
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)

def count_sentences(text):
    """นับจำนวนประโยคจากเครื่องหมายวรรคตอน"""
    return len(re.split(r'[.!?]\s*', text.strip()))

def count_vowels(text):
    """นับจำนวนสระ (a, e, i, o, u)"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def reverse_text(text):
    """ส่งคืนข้อความที่กลับด้าน"""
    return text[::-1]

def top_word(text):
    """หาคำที่พบบ่อยที่สุดและจำนวนครั้ง"""
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return "ไม่มีคำ", 0
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    top_word = max(word_counts, key=word_counts.get)
    max_count = word_counts[top_word]
    return top_word, max_count
