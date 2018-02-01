import sys
import random
import io

def main(src, n):
    raw_words = word_list(src)
    dict = dict_build(raw_words)
    word_builder(dict, n)

def word_list(src):

    f = open(src, 'r')
    text = f.read()
    f.close()
    text = text.split()
    strip_text= []
    for word in text:
        strip_text.append(word.strip('.!()?_:""'))

    return strip_text

def dict_build(new_words):

    dict = {'the the': ['the']}

    for i in range(0, len(new_words)):
        if i < len(new_words) - 2:

            if new_words[i] + " " + new_words[i+1] not in dict:
                dict[new_words[i] + " " + new_words[i+1]] = [new_words[i+2]]
            else: 
                dict[new_words[i] + " " + new_words[i+1]] = dict[new_words[i] + " " + new_words[i+1]] + [new_words[i+2]]
                
    return dict

def word_builder(dict, n):

    dict_keys = list(dict.keys())
    begin = random.choice(dict_keys)
    paragraph = begin.split()
    paragraph.append(random.choice(dict[begin]))
    for i in range(1,n):
        paragraph.append(random.choice(dict[paragraph[i] + " " + paragraph[i + 1]]))
    paragraph = ' '.join(paragraph)

    print(paragraph)

main('romeo.txt', 10)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))