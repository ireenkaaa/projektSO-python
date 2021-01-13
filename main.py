# from operator import itemgetter
from SJF import SJFsort
from queueCreator import createQueue, numberOfProcesses, doProcess
from dataGenerator import saveToFileAfter

queueFCFS = []
#queueSJF = []
finalFCFS = []
#finalSJF = []
timer = 0
processTimerFCFS = 0
processCounterFCFS = 0
averageWaitingTimeFCFS = 0
"""processTimerSJF = 0
processCounterSJF = 0
averageWaitingTimeSJF = 0
"""
while queueFCFS or processCounterFCFS < numberOfProcesses:

    processCounterFCFS = createQueue(queueFCFS, timer, processCounterFCFS)
   # processCounterSJF = createQueue(queueSJF,timer,processCounterSJF)
    #SJFsort(queueFCFS)
    #print(queue)
    processTimerFCFS = doProcess(queueFCFS ,processTimerFCFS,timer,finalFCFS)
    #processTimerSJF=doProcess(queueSJF,processCounterSJF,timer,finalSJF)

    timer = timer + 1
temp = 0

"""for i in range(len(finalSJF)):
    temp=temp+finalSJF[i][3]
averageWaitingTime = temp/len(finalSJF)
saveToFileAfter(finalSJF, averageWaitingTime,  "after")"""
temp2=0

for i in range(len(finalFCFS)):
    temp2=temp2+finalFCFS[i][3]
averageWaitingTime = temp/len(finalFCFS)
saveToFileAfter(finalFCFS, averageWaitingTime,  "after")