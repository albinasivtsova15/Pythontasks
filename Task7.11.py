11 Дана строка. Необходимо найти все незадействованные символы
латиницы в этой строке.

def find_latin_chars(string):
    latin = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") 
    use = set(string) 
    raznitsa = latin - use 

    return raznitsa

string = "ABcd"
print(find_latin_chars(string), len(find_latin_chars(string)))
