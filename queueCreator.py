from dataGenerator import generateDataRandom, generateDataZero, saveToFileAfter

timeList = []
durationList = []
numberOfProcesses = 4

generateDataRandom(timeList, durationList, numberOfProcesses)


def createQueue(queue, timer, processCounter):
    waitingTime = 0
    numberOfTimes= timeList.count(timer)


    while numberOfTimes!=0:
        if durationList:
            queue.append(["P" + str(processCounter), durationList[processCounter], timer, waitingTime])  # timer oznacza tu czas stworzenia procesu
            processCounter += 1
            numberOfTimes -=1

    return processCounter


def doProcess(queue, processTimer, timer, finalQueue):
    if queue:
        if processTimer == 0:
            processTimer = queue[0][1]
            queue[0][3] = (timer - queue[0][2])
        #print("aktualny proces: " + queue[0][0] + " czas do końca:" + str(processTimer))
        processTimer -= 1
        if processTimer == 0:
            finalQueue.append(queue[0])
            queue.pop(0)

    return processTimer
