import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.function
def print_vowels(s):
    s = s.lower()
    vowels = "aeiou"  
    found_vowels = []  
    
    for char in s:     
        if char in vowels:
            found_vowels.append(char)
    
    if found_vowels:   
        print("Vowels found:",)  
    else:
        print("No Vowels In It!")
    
    return found_vowels


@app.cell
def _():
    print_vowels("appear")
    return


if __name__ == "__main__":
    app.run()
