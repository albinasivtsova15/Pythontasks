n = int(input())
eng_lat_dict = {}
for _ in range(n):
    line = input().split(' - ')
    english_word = line[0]
    latin_translations = line[1].split(', ')
    for latin_word in latin_translations:
        if latin_word in eng_lat_dict:
            eng_lat_dict[latin_word].add(english_word)
        else:
            eng_lat_dict[latin_word] = {english_word}


latin_eng_dict = {}
for latin_word in sorted(eng_lat_dict.keys()):
    english_words = sorted(list(eng_lat_dict[latin_word]))
    latin_eng_dict[latin_word] = english_words


print(len(latin_eng_dict))
for latin_word, english_words in latin_eng_dict.items():
    print(f"{latin_word} - {', '.join(english_words)}")

