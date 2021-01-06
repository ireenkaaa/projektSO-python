# from operator import itemgetter
from SJF import SJFsort
from queueCreator import createQueue
from dataGenerator import saveToFileAfter

queue = []
final = []
timer = 0
processTimer = 0
processCounter = 0


while queue or not final:

    processCounter = createQueue(queue, timer, processCounter)
    SJFsort(queue)
    print(queue)

    if queue:
        if processTimer == 0:
            processTimer = queue[0][1]
            queue[0][3] = (timer-queue[0][2])
        print("aktualny proces: " + queue[0][0] + " czas do końca:" + str(processTimer))
        processTimer -= 1
        if processTimer == 0:
            final.append(queue[0])
            queue.pop(0)
            # sorted(queue, key=lambda x: x[1])  # czy tak może być

    timer = timer + 1
saveToFileAfter(final, "after")
