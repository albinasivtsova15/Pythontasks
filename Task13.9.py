#9 В порядке увеличения квадратичного отклонения между наибольшим
ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально
расположенных символов строки (относительно ее середины).

def calculate_ascii_deviations(text):
    max_ascii = max(ord(char) for char in text)

    mid = len(text) // 2


    mirror_pairs_ascii_diff = [abs(ord(text[i]) - ord(text[-i - 1])) for i in range(mid)]

    sorted_ascii_diff = sorted(mirror_pairs_ascii_diff)

    return sorted_ascii_diff, max_ascii



text = "parallel"
result, max_ascii = calculate_ascii_deviations(text)
print(result)
print(max_ascii)
