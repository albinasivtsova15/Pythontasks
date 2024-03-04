#10 В порядке увеличения среднего количества «зеркальных» троек
(например, «ada») символов в строке.

def count_mirror_triplets(text):
    def is_mirror_triplet(substring):
        return substring == substring[::-1]

    triplets = [text[i:i + 3] for i in range(len(text) - 2)] #список троек

    # Фильтр троек, оставляя зеркал
    mirror_triplets = [triplet for triplet in triplets if is_mirror_triplet(triplet)]


    count = len(mirror_triplets)

    return count

text = "abacaba"
mirror_triplets_count = count_mirror_triplets(text)
print(mirror_triplets_count)
