#5
В порядке увеличения квадратичного отклонения частоты встречаемости самого часто встречаемого в строке символа от частоты его
встречаемости в текстах на этом алфавите.

from collections import Counter
import math
def calculate_deviation(text):
    freq_counter = Counter(text)

    most_common_symbol, most_common_freq = freq_counter.most_common(1)[0]

    alphabet_freq = 1 / len(set(text))
    deviation = math.sqrt((most_common_freq - alphabet_freq) ** 2)

    return deviation


text = "abracadabra"
result = calculate_deviation(text)
print(result)
