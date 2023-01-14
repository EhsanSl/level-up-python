import re
import collections

def word_count(path):
    lines = ""
    with open(path, 'r', encoding='utf-8') as fptr:
        words = re.findall(r'[0-9a-zA-Z-]+', fptr.read())
        words = [word.upper() for word in words]

        word_counts = collections.Counter(words)
        #print(word_counts)
        i = 1
        for word in word_counts.most_common(20):
            print(f'{i}- word: {word[0]}, count: {word[1]}')
            i+=1


if __name__ == '__main__':
    word_count('shakespeare.txt')
