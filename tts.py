import pyttsx3

if __name__ == '__main__':
    print("Welcome to my first Python project which will convert your text to speech!!")
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what do you want me to speak (or 'q' to quit): ")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()

        
   