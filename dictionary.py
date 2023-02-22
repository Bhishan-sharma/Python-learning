import queue


coversation = {
    "hello" :"hi",
    "who am i" : "you are a person who wants to be silent now",
    "what about your life" : "my life is ruining my inner soul",
    "what do you want to do" : "i just wants to die😥😣😥😣😭😢😭",
    "why my life is so sad":"i donnot want to live",
    "now i am not going to tuition from tomorrow" : "because now i can't bear this insult",
    "I am just a big looser":"who can't do anything",
    "whom i woould tell this all":"Now I have decided that I should be no more because my existance is for nothing"
}
try:
    i = 0
    while True:
        print("robo: " + coversation[i])
        que  = input("you: ")
        i = i + 1

except Exception as e:
    pass