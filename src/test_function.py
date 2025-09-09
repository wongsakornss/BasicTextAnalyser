import unittest
from TextAnalyser import (
    count_characters,
    count_words,
    count_sentences,
    count_vowels,
    reverse_text,
    top_word
)

class TestTextAnalyzer(unittest.TestCase):

    def test_count_characters(self):
        self.assertEqual(count_characters("Hello World"), 11)
        self.assertEqual(count_characters("Hello World"), 10)

    def test_count_words(self):
        self.assertEqual(count_words("Hello world!"), 2)
        self.assertEqual(count_words("This is a test."), 4)
        self.assertEqual(count_words("That is my cat."), 5)

    def test_count_sentences(self):
        self.assertEqual(count_sentences("Hello world! How are you?"), 2)
        self.assertEqual(count_sentences("No punctuation"), 0)
        self.assertEqual(count_sentences("I like apples, bananas, and oranges."), 3)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("Spring"), 2)

    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")
        self.assertEqual(reverse_text("12345"), "54321")
        self.assertEqual(reverse_text("12345"), "12345")

    def test_top_word(self):
        text = "Hello hello world! Hello again."
        self.assertEqual(top_word(text), ("hello", 3))
        text2 = "This is programing test. That is my project."
        self.assertEqual(top_word(text2), ("is", 1))