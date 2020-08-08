#This is a simple trivial game about me (Safina Nganga)


print("Hello Player, welcome to the game")
x=input("Are you ready to play (yes/no): ")

score=0
total=4



if x.lower()=="yes":

    x=input(" What is my first name? ")
    
    if x=="Safina":
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")

    x=input("How old is am I? ")
    if x=="24":
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")   

    x=input("What is my favorite color? ")
    if x.lower()=="pink":
        score+=1
        print("Correct!")
    else:
            print("Incorrect!")  

    x=input("What year was I born? ")
    if x.lower()=="1996":
        score+=1
        print("Correct!")
    else:
        print("Incorrect!") 

print("You got", score, "questions right")
per=(score/total)*100
print("You got", per,"%!")