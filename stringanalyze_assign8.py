def main():
# The function must receive as a parameter a string.
    ms = str(input("Enter a string to be analyzed: "))
    stringAnalyze(ms)

def stringAnalyze(ms):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for x in ms:
        if x == "a" or x == "A":
# Write a function that finds the number (or total count) of each vowel in a string. Vowels are counted using an abreviation operator.
            a += 1
        elif x == "e" or x == "E":
            e += 1
        elif x == "i" or x == "I":
            i += 1
        elif x == "o" or x == "O":
            e += 1
        elif x == "u" or x == "U":
            u += 1
# Iterate over the string looking for any vowel. If you find a vowel, count it appropriately.
# At the end of function, print the total number of a's, e's, i's, o's and u's separately
    print("a: ",a, "\ne: ",e, "\ni: ",i, "\no: ",o, "\nu: ",u)

# Demonstrate your function works by calling your function with a valid string. Main is called below.
main()