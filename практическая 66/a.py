words = []
print("Введите строчку:\n")
while True:
    s = input()
    if s != "":
        words.append(s)
    else:
        break
words.sort()
print(",".join(words))
