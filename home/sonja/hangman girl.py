import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import random

    ASCII_GIRL = r"""
                                        
                                        
                                        
                                           .....                                    
                                     .-+*###%%%###*+-.                             
                                   -*%%%%%%%%%%%%%%%%%*=.                           
                               .:-#%%%@@@@@@@@@@@@@@%%%%%+                          
                             =#%%%%%@@@@@@@@@@@@@@@@@@@%#%#:                        
                           :#%%%@@@@@@@@@@@@@@@@@@@@@@@@@%#%=                       
                          -%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%-                      
                         .%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%.                     
                         #%%@@@@@@@@*%@@@@@@@@@@@@@@@@@@@@@@%%*                     
                        :@#@@@@@@@%=.:=#@@@@@@@@@@@@@@@@@@@@@%%:                    
                        +%%@@@@@@=.....:-=*#%@@@@@@@@@@@@@@@@%%+                    
                        #%@@@@@@-.-===:....::-=+*#%%%%##%@@@@@%#                    
                        %%@%@@@+.:+-:--..........:-:-=:.:@@@%@%%                    
                        %%*.#@%:...=%=-..........-#+-....%@%.*%%                    
                        #%*.=@#....%@%*..........+@%#....%@= +@#                    
                        *%@*=#%:...-++:..........:=+-...-@#-+@%*                    
                        -%%@@@@+..:-::....:..:.....:-:..+@@@@%%=                    
                         %#@@@@@*-........====.......:-*@@@@@%%.                    
                         +%#%%@@@@*=-:.....::.....::=*%@@%@@%@+                     
                          +#%@%@@@@@@%#*+======+*##%@@@@%@@%#=                      
                            -+#@@@@@@@%%%-====-%%%@@@@@@@#+-                        
                               .-#@#*+++#=....=#+++*#@#-.                           
                               :**+++++++#****#+++++++**:                           
                              =#++++++++++++++++++++++++#+                          
                             =%++**++++++++++++++++++++++%=                         
                     :-::::--*%%#%#*************+++++*#*##*                         
                    **++++++++=++++++++++++++++%*++++*%=:.#:                        
                    =#=========================*%++++#@=..=*                        
                    .%+========================+%+++*%-#:..#-                       
                     **==========+%%*===========%***#+ =*::=#                       
                     :%==========*@@%===========#%*#%--=#+=:#:                      
                      #+==========++=======++++++%+##-::..:-#                       
                    -=##+++++++++++++++++++++++++%=:=#+**#%%+======-                
                    %%#%*************************%@%#@@@%#########%%                
                    *%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#########%*                
                     ..............................................                 

    """

    def split_into_tiles(ascii_art, num_tiles):
        """Split ASCII art into num_tiles rectangular chunks."""
        lines = ascii_art.splitlines()
        h = len(lines)
        w = max(len(line) for line in lines)

        # normalize line lengths
        lines = [line.ljust(w) for line in lines]

        # decide tile width
        tile_width = w // num_tiles
        tiles = []

        for i in range(num_tiles):
            start_x = i * tile_width
            end_x = (i + 1) * tile_width if i < num_tiles - 1 else w
            tile = [line[start_x:end_x] for line in lines]
            tiles.append(tile)

        return tiles, h, w

    def display_with_revealed(tiles, revealed, h, w):
        """Show ASCII art with some tiles revealed, others hidden."""
        # Build blank picture first
        picture = [[" " for _ in range(w)] for _ in range(h)]

        for idx in revealed:
            tile = tiles[idx]
            # put this tile into picture
            start_x = idx * (w // len(tiles))
            for y, row in enumerate(tile):
                for x, ch in enumerate(row):
                    picture[y][start_x + x] = ch

        return "\n".join("".join(row) for row in picture)

    # Example game loop
    def hangman_with_ascii(secret_word):
        tiles, h, w = split_into_tiles(ASCII_GIRL, len(secret_word))
        revealed = set()
        wrong_guesses = 0
        guessed = set()

        print("Word to guess:", "_" * len(secret_word))

        while True:
            print(display_with_revealed(tiles, revealed, h, w))
            guess = input("Guess a letter: ").lower()

            if guess in guessed:
                print("Already guessed!")
                continue
            guessed.add(guess)

            if guess in secret_word:
                print("✅ Correct!")
            else:
                print("❌ Wrong!")
                # reveal one random hidden tile
                hidden = [i for i in range(len(tiles)) if i not in revealed]
                if hidden:
                    revealed.add(random.choice(hidden))
                wrong_guesses += 1

            # win check
            masked = "".join(ch if ch in guessed else "_" for ch in secret_word)
            print("Word:", masked)

            if "_" not in masked:
                print("🎉 You win!")
                break
            if wrong_guesses >= len(secret_word):
                print("💀 You lose! Word was:", secret_word)
                break

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
