import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    #Check for anagrams between two given arguments

    def anagram(word1, word2):
        x = len(word1) is not len(word2)
    
        if x is True:
            return print("Definitely not an anagram")
        elif x is False:
            if sorted(word1) == sorted(word2):
                return print("It's an anagram")
            else:
                return print("It's NOT an anagram")
        else:
            print("Provide two words..?")

    anagram(input("Provide word 1"), input("Provide word 2"))
        
        
    return


if __name__ == "__main__":
    app.run()
