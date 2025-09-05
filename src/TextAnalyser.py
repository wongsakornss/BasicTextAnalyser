def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    else:
        count = 0
        for ch in text:
            if not ch.isspace():
                count += 1
        return count

def count_words(text):
    words = []
    word = ""
    for ch in text:
        if ch.isalnum():
            word += ch
        else:
            if word != "":
                words.append(word.lower())
                word = ""
    if word != "":
        words.append(word.lower())
    return len(words)

def count_sentences(text):
    count = 0
    for ch in text:
        if ch in ".!?":
            count += 1
    return count

def count_vowels(text):
    """Returns the number of vowels (a, e, i, o, u)"""
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

def reverse_text(text):
    """Returns the text reversed"""
    return text[::-1]

def top_word(text):
    words = []
    word = ""
    for ch in text:
        if ch.isalnum():
            word += ch
        else:
            if word != "":
                words.append(word.lower())
                word = ""
    if word != "":
        words.append(word.lower())

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    max_word = None
    max_count = 0
    for w in freq:
        if freq[w] > max_count:
            max_count = freq[w]
            max_word = w
    return max_word, max_count
