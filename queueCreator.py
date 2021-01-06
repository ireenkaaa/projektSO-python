from dataGenerator import generateDataRandom, generateDataZero, saveToFileAfter

timeList = []
durationList = []
generateDataRandom(timeList, durationList, 20)


def createQueue(queue, timer, processCounter):

    waitingTime = 0
    while timer in timeList:
        if durationList:
            queue.append(["P" + str(processCounter), durationList[0], timer, waitingTime]) #timer oznacza tu czas stworzenia procesu
            durationList.pop(0)
            timeList.remove(timer)
            processCounter += 1

    return processCounter