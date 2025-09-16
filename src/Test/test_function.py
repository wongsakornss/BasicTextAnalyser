from Functions.TextAnalyser import (
    count_characters,
    count_words,
    count_sentences,
    count_vowels,
    reverse_text,
    top_word
)

# ---------- count_characters ----------
@pytest.mark.parametrize("text, include_spaces, expected", [
    ("ab c", True, 4),
    ("  ", True, 2),
    ("", True, 0),
    ("ab c", False, 3),
    (" a\tb\nc ", False, 3),
    ("", False, 0),
    ("Hello World", True, 11),
    ("Hello World", False, 10),
])
def test_count_characters(text, include_spaces, expected):
    if include_spaces:
        assert count_characters(text) == expected
    else:
        assert count_characters(text, include_spaces=False) == expected


# ---------- count_words ----------
@pytest.mark.parametrize("text, expected", [
    ("hello world", 2),
    ("hello, world!", 2),
    ("item 123 codeX7", 3),
    ("... ,,, !!!", 0),
    ("Hello world!", 2),
    ("This is a test.", 4),
    ("That is my cat.", 4),
])
def test_count_words(text, expected):
    assert count_words(text) == expected


# ---------- count_sentences ----------
@pytest.mark.parametrize("text, expected", [
    ("Hi. How are you? Fine!", 3),
    ("Wait... Really?!", 5),
    ("Hello world! How are you?", 2),
    ("No punctuation", 0),
    ("I like apples, bananas, and oranges.", 1),
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


# ---------- count_vowels ----------
@pytest.mark.parametrize("text, expected", [
    ("AEiou", 5),
    ("Hello", 2),
    ("Python", 1),
    ("Spring", 1),
])
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


# ---------- reverse_text ----------
@pytest.mark.parametrize("text, expected", [
    ("abcd", "dcba"),
    ("", ""),
    ("abc", "cba"),
    ("12345", "54321"),
    ("1221", "1221"),
])
def test_reverse_text(text, expected):
    assert reverse_text(text) == expected


# ---------- top_word ----------
@pytest.mark.parametrize("text, expected_word, expected_count", [
    ("a a a b b c", "a", 3),
    ("Hello hello world! Hello again.", "hello", 3),
    ("This is programing test. That is my project.", "is", 2),
    ("... ,,, !!!", None, 0),
])
def test_top_word(text, expected_word, expected_count):
    word, count = top_word(text)
    assert word == expected_word
    assert count == expected_count