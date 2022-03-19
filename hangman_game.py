import random

hangman_stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def generate_word():
  wordList = ["unruly" , "subscribe" , "resell" , "nonstop" , "letter" , "engine" ,
  "steady" , "idolize" , "fall" , "intelligent" , "participate" , "beds" ,
  "chess" , "dare" , "skillful" , "grieving" , "draw" , "numberless" , "integrate" ,
  "mountainous" , "stop" , "stage" , "inhabit" , "deny" , "song" , "savvy" , "caption" ,
  "sincere" , "ground" , "output" , "shop" , "overjoyed" , "wary" , "cool" , "view" ,
  "frantic" , "annoyed" , "approve" , "adorable" , "painful" , "fetch" , "thunder" ,
  "infamous" , "frog" , "bizarre" , "outgoing" , "ambitious" , "surprise" , "van" ,
  "mistake" , "mean" , "potato", "computer", "google", "computer engineering", "calculator"]
  random_word = random.choice(wordList).upper()
  return random_word

def send_formatted_word(guessed_letters, generated_word):
  word = ""
  for letter in generated_word:
    if letter.upper() in guessed_letters:
      word += letter.upper()
    else:
      word += "_"
  return word

def check_user_input(user_input, word):
  if isinstance(user_input, str):
    if user_input.upper() == word.upper():
      return True
    else:
      return False
  elif isinstance(user_input, list):
    if user_input[-1].upper() in word.upper():
      return True
    else:
      return False
  else:
    return None

selected_word = generate_word()
mistake_count = 0
guessed_letters = []

while(send_formatted_word(guessed_letters, selected_word) != selected_word and mistake_count <= 6):
  if mistake_count < 6:
    print(hangman_stages[mistake_count])
    print(f"\n{send_formatted_word(guessed_letters, selected_word)}")
    print("Guessed letters: {}".format(", ".join(guessed_letters)))
    
    user_input = input("\nSelected letter or word: ")
    
    if len(user_input) == 1:
      guessed_letters.append(user_input.upper())
      if check_user_input(guessed_letters, selected_word) == False:
        mistake_count += 1
        print(f"Sorry the word does not contain \"{user_input}\". You are now at {mistake_count} mistakes. Try again :/")
      else:
        print(f"Great guess! The word does in fact contain \"{user_input}\"")
    else:
      if check_user_input(user_input, selected_word) == False:
        mistake_count += 1
        guessed_letters.append(user_input.upper())
        print(f"Sorry the word is not \"{user_input.upper()}\". Unfortunatly that means you are at {mistake_count} mistakes :/")
      else:
        print("That is epic! You just guessed the right word, congrats!")
        for letter in user_input.upper():
          guessed_letters.append(letter)
  
  else:
    print(hangman_stages[mistake_count])
    print(f"The word was: {selected_word}")
    mistake_count += 1

if send_formatted_word(guessed_letters, selected_word) == selected_word:
  print(hangman_stages[mistake_count])
  print(f"You got it right! The word was {selected_word}")