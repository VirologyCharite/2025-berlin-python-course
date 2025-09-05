import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    word = input ("What's the word?")

    guesses = []
    guess_count = 0
    secret = "_"*len(word)
    word_progress = ""
    word_position = 0

    print("Try to guess this:", secret)

    while True:
        letter = input (f"Guess a letter for {secret}")

        if letter == word:
            print ("Yay - you found it!")
        
        if letter in guesses:
            print ("Already guessed!")
        guesses.append(letter)
    
        if letter in word:
            print (letter, "exists in secret")
        
            if letter in word.index(word_position):
                word_progress.insert(letter, word_position)
                word_position += 1
    
            elif letter not in word.index(word_position):
                word_progress.insert("_", word_position)
                word_position += 1
                

            else:
                print("There's something wrong")
            print (word_progress)
    
        elif letter not in word:
            if guess_count == 0:
                print ("Nah, try again! 7 more lives"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        "
                    "|       "
                    "|        "
                    "|       "
                    "|"
                    "|"
                )
                guess_count +=1

            elif guess_count == 1:
                print ("Nah, try again! 6 more lives"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|       "
                    "|        "
                    "|       "
                    "|"
                    "|"
                )
                guess_count +=1


            elif guess_count == 2:
                print ("Nah, try again! 5 more lives"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|        |"
                    "|        "
                    "|       "
                    "|"
                    "|"
                )
                guess_count +=1


            elif guess_count == 3:
                print ("Nah, try again! 4 more lives"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|       /|"
                    "|       "
                    "|       "
                    "|"
                    "|"
                )
                guess_count +=1


            elif guess_count == 4:
                print ("Nah, try again! 3 more lives"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|       /|/"
                    "|       "
                    "|       "
                    "|"
                    "|"
                )
                guess_count +=1


            elif guess_count == 5:
                print ("Nah, try again! 2 more lives"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|       /|/"
                    "|        |"
                    "|       "
                    "|"
                    "|"
                )
                guess_count +=1

            elif guess_count == 6:
                print ("Nah, try again! Last chance!"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|       /|/"
                    "|        |"
                    "|       /"
                    "|"
                    "|"
                )
                guess_count +=1

            elif guess_count == 7:
                print ("Nah, YOU'RE DEAD!"
                    "__________"
                    "|        |"
                    "|        O"
                    "|        |"
                    "|       /|/"
                    "|        |"
                    "|       / /"
                    "|"
                    "|"
                )
                guess_count +=1

            else:
                print ("Problem with hanging, prlease refer to code.")

    return


if __name__ == "__main__":
    app.run()
