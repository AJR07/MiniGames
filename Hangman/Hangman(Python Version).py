import time
#introduction
intro = """
Hello there, this is a Hangman Game made by AJR, Dec 23 2020
More improvements will be made in the future, feel free to open an issue if u have any suggestions/There is any bugs!
Thanks and enjoy! :D

--------FUTURE IMPROVEMENTS---------
1. App
2. more words
3. multiplayer
"""
print(intro)
time.sleep(5)

#functions
def error(input, requirements):
  print("Ur input: " + input + " is Invalid. Please input acccording to the requirements of(" + requirements + ") instead.")

#gathering the list of topics for the game
myList = []
words = open("/Users/angjunray/Desktop/Coding/General/Projects/Hangman/words.txt", "r")
for topic in words:
  myList.append(topic)

#topic choice
while True:
  topic = input("What topic do you want to choose? Type ? for list of topics!")
  if topic == "?":
    print("----------LIST OF TOPICS AVALIABLE------------")
    for word in myList:
      print(word)
    
    print("------------------END OF LIST-----------------")
  elif topic in myList:
    break
  else:
    error(topic, "Input must be in the list of topics. input ? for list!")
