import matplotlib.pyplot as plt
import sys
import operator
import argparse
import csv
import numpy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word",
        help="the word to be searched for in the text file."
    )
    parser.add_argument(
        "filename",
        help="the path to the text file to be searched through"
    )

    parser.add_argument(
        "filename2",
        help="The second file to be searched through to compare the word rank to"
    )

    args = parser.parse_args()

    try:
        open(args.filename)
    except FileNotFoundError:

        # Custom error print
        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)

    word_freq(args.word, args.filename, args.filename2)


def word_freq(word, filename, filename2):
    doc = {}

#    file = open(filename, encoding='utf-8')
#    data = file.read()
#    words = data.split()
#    print(len(words))

#   file2 = open(filename2, encoding='utf-8')
#    data2 = file2.read()
#    words2 = data2.split()
#    print(len(words2))

    for line in open(filename, encoding='utf-8', errors='ignore'):

        text = line.lower()
        # Assume each word is separated by a space
        split = text.split(' ')
        for entry in split:
            if doc.__contains__(entry):
                doc[entry] = int(doc.get(entry)) + 1
            else:
                doc[entry] = 1

    if word not in doc:
        sys.stderr.write("Error: " + word + " does not appear in " + filename)
        sys.exit(1)

    doc2 = {}

    for line in open(filename2, encoding='utf-8', errors='ignore'):

        text = line.lower()
        # Assume each word is separated by a space
        split = text.split(' ')
        for entry in split:
            if doc2.__contains__(entry):
                doc2[entry] = int(doc2.get(entry)) + 1
            else:
                doc2[entry] = 1

    if word not in doc2:
        sys.stderr.write("Error: " + word + " does not appear in " + filename2)
        sys.exit(1)

    sorted_doc = (sorted(doc.items(), key=operator.itemgetter(1)))[::-1]
    sorted_doc2 = (sorted(doc2.items(), key=operator.itemgetter(1)))[::-1]
    just_the_occur = []
    just_the_rank = []
    just_the_occur2 = []
    just_the_rank2 = []
    word_rank = 0
    word_frequency = 0
    word_rank2 = 0
    word_frequency2 = 0

    entry_num = 1
    for entry in sorted_doc:

        if entry[0] == word:
            word_rank = entry_num
            word_frequency = entry[1]

        just_the_rank.append(entry_num)
        entry_num += 1
        just_the_occur.append(entry[1])

    entry_num2 = 1
    for entry in sorted_doc2:

        if entry[0] == word:
            word_rank2 = entry_num2
            word_frequency2 = entry[1]

        just_the_rank2.append(entry_num2)
        entry_num2 += 1
        just_the_occur2.append(entry[1])

#    print(word_rank2)
#    print(word_rank)
#    print(word_frequency2)
#    print(word_frequency)

#    word_frequencyP = (word_frequency/words)*100
#    word_frequency2P = (word_frequency2/words2)*100


    rank_difference = abs(word_rank - word_rank2)
    freq_difference = abs(word_frequency2 - word_frequency)

    if rank_difference == 0:
        print("They are the same rank!")
    else:
        print("The rank difference is " + str(rank_difference))
    if freq_difference == 0:
        print("They appear the same amount of times!")
    else:
        print("The frequency difference is " + str(freq_difference))

#    sorted_doc.append(just_the_rank)
#    sorted_doc2.append(just_the_rank2)

    d1 = dict(sorted_doc)
    d2 = dict(sorted_doc2)

    w = csv.writer(open("Output1RANK.csv", "w", encoding='utf-8'))
    for key, val in d1.items():
        w.writerow([key, val])

    w = csv.writer(open("Output2RANK.csv", "w", encoding='utf-8'))
    for key, val in d2.items():
        w.writerow([key, val])
    plt.xlabel("Ranks of " + word + " are " + str(word_rank) + " and " + str(word_rank2))
    plt.loglog(just_the_rank, just_the_occur, basex=10)
    plt.loglog(just_the_rank2, just_the_occur2, basex=10)


if _z_name__ == "__main__":
    main()

