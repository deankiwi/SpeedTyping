import json
import matplotlib.pyplot as plt
import numpy as np

def time_from_seconds(time):
    "will return a string such as '0:00:02.411543' as a float in sectons"
    hour, minute, second = time.split(':')
    seconds = 60*60*int(hour) + 60*int(minute) + float(second)
    return seconds


def letter_and_time(location):
    "will read the spelling quiz JSON file and return a list with time took to type and letter"
    with open(location) as f:
        d = json.load(f)
    data = []
    typeData = d["typeData"]
    numberOfWords = len(typeData)
    for indexWords, word in enumerate(typeData):
        numberOfLetter = len(word)
        for indexLetter, letter in enumerate(word):
            if indexWords == 0 and indexLetter == 0:
                data.append((time_from_seconds(letter[0]), letter[-1]))

            elif indexLetter == 0:
                beforetime = time_from_seconds(typeData[indexWords-1][-1][0])
                letterpresstime = time_from_seconds(letter[0])
                data.append((letterpresstime-beforetime, letter[-1]))
            else:
                beforetime = time_from_seconds(typeData[indexWords][indexLetter-1][0])
                letterpresstime = time_from_seconds(letter[0])
                data.append((letterpresstime-beforetime, letter[-1]))

    return data



data = letter_and_time(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data\typingtest0\dataSet.json')



x = np.arange(len(data))
y = [time[0] for time in data]
letters = [letter[1] for letter in data]




fig, ax = plt.subplots()

plt.bar(x, y)
plt.xticks(x, letters)
plt.show()