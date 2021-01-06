from random import randint
def saveToFileBefore(list, name):
    with open(name, 'w') as file:

        for item in list:
            file.write("%s\n" % item)

def saveToFileAfter(list, name):
    with open(name, 'w') as file:
        file.write("Numer procesu   Czas trwania  Czas przyjscia  Czas oczekiwania \n")
        for item in list:
            for i in item:
                file.write("%s              " % i)
            file.write("\n")

def generateDataRandom(listTimes, listDuration, numberOfProcesses):
    for i in range(numberOfProcesses):
        listTimes.append(randint(0, numberOfProcesses+5))
        listDuration.append(randint(1, 8))
    listTimes.sort()
    saveToFileBefore(listTimes, "time")
    saveToFileBefore(listDuration, "duration")

def generateDataZero(listTimes, listDuration, numberOfProcesses):
    for i in range(numberOfProcesses):
        listTimes.append(0)
        listDuration.append(randint(1, 7))
    saveToFileBefore(listTimes, "time")
    saveToFileBefore(listDuration, "duration")