import math
import speech_recognition as sr
import pyttsx3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def square_root(a):
    if a < 0:
        raise ValueError("Square root of a negative number is not allowed.")
    return math.sqrt(a)

def exponent(a, b):
    return a ** b

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_voice_input(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak(prompt)
        print(prompt)
        try:
            audio = recognizer.listen(source)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return get_voice_input(prompt)
        except sr.RequestError as e:
            speak("Error with the speech recognition service. Please try again later.")
            raise e

def main():
    speak("Welcome to the Voice Command Calculator!")
    print("Available operations:")
    print("1. Addition (say 'add')")
    print("2. Subtraction (say 'subtract')")
    print("3. Multiplication (say 'multiply')")
    print("4. Division (say 'divide')")
    print("5. Square Root (say 'square root')")
    print("6. Exponentiation (say 'exponent')")
    print("7. Exit (say 'exit')")

    while True:
        try:
            operation = get_voice_input("Please say the operation you want to perform.")

            if operation.lower() in ['exit', 'quit']:
                speak("Thank you for using the calculator. Goodbye!")
                break

            if operation.lower() == 'square root':
                num = float(get_voice_input("Please say the number you want the square root of."))
                result = square_root(num)
                speak(f"The square root of {num} is {result}")
                print(f"The square root of {num} is {result}")
            else:
                num1 = float(get_voice_input("Please say the first number."))
                # num2 = float(get_voice_input("Please say the second number."))
                num2=2

                if operation.lower() == 'add':
                    result = add(num1, num2)
                elif operation.lower() == 'subtract':
                    result = subtract(num1, num2)
                elif operation.lower() == 'multiply':
                    result = multiply(num1, num2)
                elif operation.lower() == 'divide':
                    result = divide(num1, num2)
                elif operation.lower() == 'exponent':
                    result = exponent(num1, num2)
                else:
                    speak("Invalid operation. Please try again.")
                    continue

                speak(f"The result is {result}")
                print(f"The result is {result}")
        except ValueError as e:
            speak(f"Error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            speak(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
