import matplotlib.pyplot as plt
import sys
import operator
import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
    )

    args = parser.parse_args()

    try:
        open(args.filename)
    except FileNotFoundError:

        # Custom error print
        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)


def word_freq(word, filename):
    doc = {}

    for line in open(filename, encoding='utf-8'):

        split = line.split(' ')
        for entry in split:
            if doc.__contains__(entry):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    sorted_doc = (sorted(doc.items(), key=operator.itemgetter(1)))[::-1]
    just_the_occur = []
    just_the_rank = []
    word_rank = 0
    word_frequency = 0

    entry_num = 1
    for entry in sorted_doc:

        if entry[0] == word:
            word_rank = entry_num
            word_frequency = entry[1]

        just_the_rank.append(entry_num)
        entry_num += 1
        just_the_occur.append(entry[1])
    print("success")
    plt.title("Amount of times words appear in " + filename)
    plt.ylabel("Total number of appearances")
    plt.xlabel("word")
    plt.plot

    print(sorted_doc)