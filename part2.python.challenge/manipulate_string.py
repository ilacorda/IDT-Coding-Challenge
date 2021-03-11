#!/usr/bin/python

import string

sentences = ['Hello world! How (sp?) are you today (;',
             'Hello world! How (sp?) are you today :(',
             'Hello world! How (sp?) are you today :)']

list_emoticons = {
    '(;': '000crying',
    ':(': '000sad',
    ':)': '000smile'
}


def main():
    clean_up_sentence = []

    for sentence in sentences:
        # Temporarily substitute the emoticons with its corresponding value from the map
        for emoticon, rpl in list_emoticons.items():
            sentence = sentence.replace(emoticon, rpl)

        # Remove punctuation from the string
        for char in sentence:
            if char in string.punctuation:
                sentence = sentence.replace(char, '')

        # Invert key/value in the initial map
        inv_map = {v: k for k, v in list_emoticons.items()}

        # Re-instate the initial key in the emoticons map
        for emoticon, rpl in inv_map.items():
            sentence = sentence.replace(emoticon, rpl)
        # Populate the clean up list of sentences
        clean_up_sentence.append(sentence.split())

    print(clean_up_sentence)


if __name__ == "__main__":
    main()
