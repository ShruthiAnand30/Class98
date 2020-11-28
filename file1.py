def wordCount():
    fileName = input("Enter the file name ")
    file = open(fileName)
    noWords = 0
    for line in file:
        words = line.split()
        noWords = noWords + len(words)
    print("number of words ")
    print(noWords)


wordCount() 