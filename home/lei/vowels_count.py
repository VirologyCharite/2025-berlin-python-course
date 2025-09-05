import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.function
def count_vowels(s):
    s = s.lower()  
    vowels = "aeiou"
    count = 0
    
    for str in s:
        if str in vowels:
            count += 1
    
    if count == 0:
        print("No Vowels In It!")
    else:
        print(f"Number of vowels: {count}")
    
    return count


@app.cell
def _():
    count_vowels("N")  
    return


if __name__ == "__main__":
    app.run()
