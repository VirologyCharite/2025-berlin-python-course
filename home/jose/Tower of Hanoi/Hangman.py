import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    def TowerOfHanoi(n , source, destination, auxiliary):
        if n==1:
            print ("Move disk 1 from source",source,"to destination",destination)
            return
        TowerOfHanoi(n-1, source, auxiliary, destination)
        print ("Move disk",n,"from source",source,"to destination",destination)
        TowerOfHanoi(n-1, auxiliary, destination, source)

    # Driver code
    n = 10
    TowerOfHanoi(n,'A','B','C') 


    return


@app.cell
def _():


    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


    def Hangman (word): 

        Attempts = 0
        hangmancount = 0
        correct_letters_guessed = set()
        word_letters = set(word)

        while Attempts < 7:
            letter = input("What is your guess? ( 6 letter word")
            if letter == "quit":
                break
            if letter not in word: 
                print ("not there")
                Attempts += 1
                print(HANGMANPICS[hangmancount])
                hangmancount += 1
            else:
                correct_letters_guessed.add(letter)
                output = "".join([l if l in correct_letters_guessed else "_" for l in word])
                print("Correct:", output)


            if word_letters.issubset(correct_letters_guessed):
                print("You got it! The word was:", word)
                break
        else:
            print("Game over! The word was:", word)



    Hangman("python")

    return


if __name__ == "__main__":
    app.run()
