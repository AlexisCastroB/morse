MORSE = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "ñ": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--.."
}

def convert():
  text = input('Write a word or text to be converted into Morse Code:\n')
  code = []

  for letter in text.lower():
    app = MORSE[letter] if letter in MORSE else letter
    code.append(app)
  code = ''.join(code)

  print(f"'{text}' in Morse Code is: '{code}'")
  askAgain()

def askAgain():
  wrong_answer = True
  repeat_conversion = False
  while wrong_answer:
    again = input('Do you want to convert another word? (Y/N)\n').lower()
    if again in ['y','n']:
      wrong_answer = False
      repeat_conversion = again == 'y'
    else:
      print('Please respond in Y or N format.')
  if repeat_conversion:
    convert()
  else:
    print('Ok, have a good day.')

convert()