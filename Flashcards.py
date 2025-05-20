class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+self.meaning
flash=[]
print("Welcome to python FlashCard")

running=True
while(True):
    word=input("enter the name you want to add to the flashcard: ")
    meaning=input("enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option=int(input('enter 99, if u wish to add another flashcard else type 2342353: '))
    if(option):
        break
print("ur flashcards")
for k in flash:
    print(">", k)