import json
import matplotlib.pyplot as plt
import numpy as np
import os

def time_from_seconds(time):
    "will return a string such as '0:00:02.411543' as a float in sectons"
    hour, minute, second = time.split(':')
    seconds = 60*60*int(hour) + 60*int(minute) + float(second)
    return seconds


def letter_and_time(location):
    """will read the spelling quiz JSON file and return a list with time took to type and letter
    [(1.146258, ''), (1.265285, 'N'), (0.464105, 'e'),..... (time , letter) ]"""
    with open(location) as f:
        d = json.load(f)
    data = []
    typeData = d["typeData"]

    for indexWords, word in enumerate(typeData):

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

#print(letter_and_time(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data\typingtest0\dataSet.json'))

def time_per_letter(location):
    'reads json file in "location" and makes a graph of time in took to type each letter'

    data = letter_and_time(location)

    x = np.arange(len(data))
    y = [time[0] for time in data]
    letters = [letter[1] for letter in data]

    fig, ax = plt.subplots()

    plt.bar(x, y)
    plt.xticks(x, letters)
    plt.show()

#time_per_letter(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data\typingtest0\dataSet.json')


def find_json_files(location):
    'will return an arrary containing the location of all given json files'
    locations = []
    for path, subdirs, files in os.walk(location):
        for name in files:
            if name[-5:] == '.json':
                locations.append(os.path.join(path, name))
    return locations

#print(find_json_files(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data'))

def analysis_letters(location):
    '''
    :param location: location of where you want to start looking for files
    :return:
    {'n': [1.265285, 0.12802900000000017, 0.20804700000000054],
    's': [0.2230509999999999, 0.19204199999999982, 1.0717810000000005, 0.7341809999999995],
    .....
    'letter from alphebet': array containing all the times
    '''
    jsonsfiles = find_json_files(location)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    data = {}
    for files in jsonsfiles:
        times = letter_and_time(files)
        #todo would be cool to know if uppercase and lower case makes a differnce
        for time, letter in times:
            letter = letter.lower()
            if letter in abc and not letter == '':
                if letter in data:
                    data[letter].append(time)
                else:
                    data[letter] = [time]

    return data


#print(analysis_letters(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data'))

def letter_average(location):
    '''
    find the overall average time it took to do the letter
    :param location: location of where you want to start looking for JSON files
    :return: [['a', 0.37469837931034566], ['b', 0.5375216000000004], .... [letter, float]
    '''
    data = analysis_letters(location)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    letteraverage = []

    for letter in abc:
        if letter in data:
            average = sum(data[letter])/len(data[letter])
            letteraverage.append([letter,average])

    return letteraverage


#print(letter_average(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data'))


def letter_average_graph(location):
    '''
    used matplot lib to make a graph x axis letter, y axis average time to type
    :param location:
    :return: none
    '''

    data = letter_average(location)

    x = np.arange(len(data))
    y = [time[1] for time in data]
    letters = [letter[0] for letter in data]

    fig, ax = plt.subplots()

    plt.bar(x, y)
    plt.xticks(x, letters)
    plt.show()

letter_average_graph(r'C:\Users\Log Head\Documents\Programming\spellingQuiz\data')