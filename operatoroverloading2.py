class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + ' : ' + self.meaning
flash=[]
print("Welcome to flashcard application")
while(True):
    word=input("enter the name u want to add to the flashcard: ")
    meaning=input("enter the meaning of the word: ")
    flash.append(flashcard(word,meaning))
    option=int(input("Enter 0 if u want to add another flashcard, otherwise enter 1: "))
    if(option):
        break
print("\n Your flashcards")
for i in flash:
    print(">",i)