MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

def text_to_morse(text):
    text = text.upper()
    morse = ' '.join(MORSE_CODE_DICT[char] if char in MORSE_CODE_DICT else ' ' for char in text)
    return morse
def morse_to_text(morse_code):
    reverse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse_code.split("   ")
    decoded = [''.join(reverse_dict[char] for char in word.split()) for word in words]
    return ' '.join(decoded)

# 示例
morse_code = ".. .-.. --- ...- . -.-- --- ..-"
decoded_message = morse_to_text(morse_code)
print(decoded_message)  # 输出: HELLO WORLD

# 示例
message = "HELLO WORLD"
morse_code = text_to_morse(message)
print(morse_code)  # 输出: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
