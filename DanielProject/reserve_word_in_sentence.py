def split_conect(sentence):
    sentence_2 = sentence.split()
    print(sentence_2)

    sentence_3 = []
    for a in reversed(sentence_2):
        sentence_3.append(a)
    print(sentence_3)

    sentence_3 = ' '.join(str(b) for b in sentence_3)
    print(sentence_3)


sentence = str(input("Enter a sentence with spacing: \n"))
split_conect(sentence)
