import string
import random
import matplotlib.pyplot as plt

def main():
    #findMean()
    #return 0

    while True:
        input1 = input("Please enter a short word: ")
        if input1 == "":
            break
        trials = generateWord(input1)
        print("Word generated! Monkey " + str(int(random.uniform(1, 100))) + " took " + str(trials) + " attempts to get the word!")

def findMean():
    sum = 0
    for i in range(10000):
        val = generateWord("hi")
        sum += val
    print(sum / 10000)

def plotDistribution():
    map1 = {}
    for i in range(10000):
        val = generateWord("hi")
        if val not in map1.keys():
            map1[val] = 1
        else:
            map1[val] += 1
    keys = map1.keys()
    values = map1.values()
    plt.bar(keys, values)
    plt.show()

def generateLetter():
    alphabet = string.ascii_lowercase
    randLetter = random.choice(alphabet)
    return randLetter

def generateWord(input):
    numTrials = 0
    str = ""
    while str != input:
        str = ""
        numTrials += 1
        for k in range(len(input)):
            letter = generateLetter()
            str += letter
        if str == input:
            return numTrials


if __name__ == "__main__":
    main()