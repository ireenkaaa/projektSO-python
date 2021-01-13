from SJF import SJFsort
from queueCreator import createQueue, numberOfProcesses, doProcess
from dataGenerator import saveToFileAfter

queueFCFS = []
queueSJF = []

finalFCFS = []
finalSJF = []
timer = 0
processTimerFCFS = 0
processTimerSJF = 0
processCounterFCFS = 0
processCounterSJF = 0


while queueSJF or processCounterSJF < numberOfProcesses:
    processCounterFCFS = createQueue(queueFCFS, timer, processCounterFCFS)
    processCounterSJF = createQueue(queueSJF, timer, processCounterSJF)
    SJFsort(queueSJF)
    print("SJF", queueSJF)

    processTimerFCFS = doProcess(queueFCFS, processTimerFCFS, timer, finalFCFS)
    processTimerSJF = doProcess(queueSJF, processTimerSJF, timer, finalSJF)
    timer = timer + 1

saveToFileAfter(finalFCFS, "afterFCFS")
saveToFileAfter(finalSJF, "afterSJF")