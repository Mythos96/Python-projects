import speech_recognition as sr
import random

mic = sr.Microphone()
recog = sr.Recognizer()

levels = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

point = 0

def listen():
    with mic as audio_file:
        print("Ready to listen, please say something.")
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-GB")

def game(response):
    global point
    level = input("Choose a level to begin (easy, medium, hard):").lower()

    if level not in levels:
        print("Level name is undefined")
        level = input("Please choose a valid level (easy, medium, hard): ").lower()
        
    elif level == "easy":
        word = random.choice(levels["easy"])
        print(f'Pronounce the word {word}')
        response = listen()
        if response.lower() == word:
            print("Correct answer! +1 point")
            print(" ")
            point += 1
            
        else:
            print(f'Incorrect answer! you said "{response}", but the correct word was "{word}"')
            print(" ")
            

    elif level == "medium":
        word = random.choice(levels["medium"])
        print(f'Pronounce the word {word}')
        response = listen()
        if response.lower() == word:
            print("Correct answer! +3 point")
            print(" ")
            point += 3
            
        else:
            print(f'Incorrect answer! you said "{response}", but the correct word was "{word}"')
            print(" ")

    elif level == "hard":
        word = random.choice(levels["hard"])
        print(f'Pronounce the word {word}')
        response = listen()
        if response.lower() == word:
            print("Correct answer! +5 point")
            print(" ")
            point += 5
        else:
            print(f'Incorrect answer! you said "{response}", but the correct word was "{word}"')
            print(" ")

print("Welcome to the pronunciation game!")
print("You will be given a word, from the level that you choose, to pronounce, and you will earn points for correct pronunciations.")
ready = input("Are you ready to play? (yes/no): ").lower()

while True:
    if ready == "yes":
        game(response="")
        print(f"Your current point: {point}")
        ready = input("Do you want to play again? (yes/no): ").lower()
        print(" ")
        
    elif ready == "no":
        print("Thank you for playing!")
        break

    else:
        print("Please answer with 'yes' or 'no'.")
        ready = input("Are you ready to play? (yes/no): ").lower()
