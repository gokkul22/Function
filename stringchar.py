def most_frequent(string):
    x = {}
    for n in string:
        y = x.keys()
        if n in y:
            x[n] += 1
        else:
            x[n] = 1
    return x
print(char_frequency(input("Enter string \n")))


Output:

Enter string 
Mississippi
{'M': 1, 'i': 4, 's': 4, 'p': 2}
