import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #define print vowels from a word
    def print_vowels(word):
        vowels = "aeiouAEIOU"

        for letter in word:
            if letter in vowels:
                print(letter)

    print_vowels("Ilia")

    
  
   
    
    
    
    
    
    
    
    
    
    
    return


if __name__ == "__main__":
    app.run()
