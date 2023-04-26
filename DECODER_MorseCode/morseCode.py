

"""
An edit by me on the CodeWars Kata made by jolaf.
https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

"""


# Define the dictionary
MORSE_CODE_DECODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', 
              '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', 
              '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
              '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', 
              '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', 
              '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', 
              '...---...': 'SOS'}

MORSE_CODE_ENCODE = {value:key for key, value in MORSE_CODE_DECODE.items()}

print("Morse Code Decoder Dictionary is ", MORSE_CODE_DECODE)
print("Morse Code Encoder Dictionary is ", MORSE_CODE_ENCODE)

def decode_morse(morse_code):
    morse_code = morse_code.split(" ")              # Transform input into a list.
    answerList = []

    for letter in morse_code:
        
        if letter == "":
            answerList.append(" ")
        else:
            answerList.append(MORSE_CODE_DECODE[letter])

    answerString = ''.join(answerList).strip()          # Turn list into string and remove leading and trailling whitespaces.
    answerString = answerString.replace("  ", " ")      # Check for extra spaces.

    print(answerString)

def encode_morse(text_to_encode):
    text_to_encode = list(text_to_encode)               # Transform input into a list.
    answerList = []

    for letter in text_to_encode:
        
        if letter == " ":
            answerList.append(" ")
        else:
            answerList.append(MORSE_CODE_ENCODE[letter])

    answerString = ' '.join(answerList).strip()         # Turn list into string and remove leading and trailling whitespaces.
    answerString = answerString.replace("  ", " ")      # Check for extra spaces.

    print(answerString)

decode_morse('.... . -.--  .--- ..- -.. .')             # Says HEY JUDE

encode_morse('HEY JUDE')