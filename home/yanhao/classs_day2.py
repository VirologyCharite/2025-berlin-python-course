import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    # def count_vowels(word: str):
    #     vowels = "aeiouAEIOU"  
    #     found = [char for char in word if char in vowels]  
    #     return found

    # f=set()

    # while True:
    #     word = input("plz input a word ( input q to quit): ")

    #     if word == "q":
    #         print("seeU")
    #         break
    #     else:
    #         vowels_in_word = count_vowels(word)
        
    # for uiword in vowels_in_word :
    
    #     f.add(vowels_in_word)
    
    #     if vowels_in_word in set()
    #         uiword = vowels_in_word
      
            
    #     print(f"In '{word}' ,there is  {len(uiword)} vowels: {', '.join(uiword)}")
    #     else:
    #             print(f"In '{word}' ，there is no vowels")

    return


@app.cell
def _():
    def unique_vowels(word: str):
        vowels = "aeiouAEIOU"
        # 用 set 去重，然后再转 list 排序（方便展示）
        return sorted(set(ch.lower() for ch in word if ch in vowels))

    while True:
        word = input("plz input a word (input q to quit): ")

        if word == "q":
            print("seeU")
            break

        vowels_in_word = unique_vowels(word)

        if vowels_in_word:
            print(f"In '{word}', there are {len(vowels_in_word)} unique vowels: {', '.join(vowels_in_word)}")
        else:
            print(f"In '{word}', there are no vowels.")

    return


@app.cell
def _():
    def reverse_sequence(seq: str) -> str:
        # 定义允许的碱基
        valid_bases = {"A", "G", "C", "T"}
    
        # 检查是否有非法字符
        for base in seq.upper():
            if base not in valid_bases:
                raise ValueError(f"输入错误: {base} 不是有效的碱基 (只能包含 A, G, C, T)")
    
        # 返回反向序列
        return seq.upper()[::-1]


    while True:
        dna = input("请输入DNA序列 (输入 q 退出): ")
        if dna.lower() == "q":   # 输入 q 或 Q 退出
            print("程序已退出。")
            break
        try:
            print("反向序列为:", reverse_sequence(dna))
        except ValueError as e:
            print(e)

    return


if __name__ == "__main__":
    app.run()
