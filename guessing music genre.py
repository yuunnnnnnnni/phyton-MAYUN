
def main():
    """"Guess a song genre kpop,rnb,pop"""
    print("Guess a music genre. Clue sugar rush ride by txt")

    secret_word = "kpop"
    guess=""
    guess_count=0
    while guess!= secret_word:
        if guess_count <=2:
           guess=input("Enter guess")
           guess_count +=2 
        if guess == secret_word:
            print("mantop 2 point")
        else:
             print("you lose")
        break

#question 2

    """Guess a song genre pop,rnb or kpop"""
    print("clue heaven and back by chase atlantic")

    secret_word="pop"
    guess=""
    guess_count=1
    while guess!= secret_word:
        if guess_count <=2:
           guess=input("Enter guess")
           guess_count +=2
        if guess == secret_word:
            print("mantop 2 point")
        else:
            print("you lose")
        break
    
#question 3

    """Guess a spng genre pop,rnb or kpop"""
    print(" clue limbo by keshi")

    secret_word="rnb"
    guess=""
    guess_count=1
    while guess!= secret_word:
        if guess_count <=2:
           guess=input("Enter guess")
           guess_count +=2
        if guess == secret_word:
            print("mantop 2 point")
        else:
            print ("you lose")
        break

    print("total your own marks")
    
main()

