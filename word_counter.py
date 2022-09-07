import matplotlib.pyplot as plt

def word_counter(text):
    post_text = text.lower().translate(text.maketrans({char: None for char in ";'.,$:*!♪"})).split()
    word_count = {}
    for word in post_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
    
def main():
    dict_word = word_counter(open('apple_transcription.txt').read().strip())
    dict_word = dict(sorted(dict_word.items(), key=lambda item: item[1])[-50:-8])
    
    plt.barh(range(len(dict_word)), list(dict_word.values()),align='center')
    plt.yticks(range(len(dict_word)), list(dict_word.keys()))
    plt.xlabel('Count')
    plt.ylabel('Words')
    plt.title('Word Histogram Apple Event 2022')
    plt.show()

if __name__ == "__main__":
    main()
