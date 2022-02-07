import pyttsx3

main = pyttsx3.init()

print("##### welcome to the Text converter #####")

rate = input("enter the Speed of speech: ")
volume = input("enter the volume: ")
text = input("enter the text: ")

main.setProperty("rate", int(rate))
main.setProperty("volume", int(volume))
main.say(text)
main.runAndWait()