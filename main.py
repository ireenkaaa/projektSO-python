from random import randint
from operator import itemgetter

def saveToFile(list, name):
    with open(name, 'w') as f:
        for item in list:
            f.write("%s\n" % item)


def generateData(listTimes, listDuration):
    for i in range(20):
        listTimes.append(randint(0, 23))
        listDuration.append(randint(1, 7))
    listTimes.sort()
    saveToFile(listTimes, "time")
    saveToFile(listDuration, "duration")


queue = []
timer = 0
processNumber = 1
timeList = []
durationList = []
generateData(timeList, durationList)

while queue or processNumber<20:

    while timer in timeList:
        if durationList:
            queue.append(["P" + str(processNumber), durationList[0], timer])
            print(queue)
            durationList.pop(0)
            timeList.remove(timer)
            processNumber +=1


    print(queue)
    if queue:
        print("aktualny proces: "+queue[0][0]+" czas do końca:"+str(queue[0][1]))
        queue[0][1] -= 1
        if queue[0][1] == 0:
            queue.pop(0)
            sorted(queue, key=lambda x: x[1]) #czy tak może być 

    timer = timer + 1
