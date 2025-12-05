sentence=input("Enter a sentence:")
words=sentence.split()
words.sort()
print("Sorted Sentence:")
for word in words:
    print(word)