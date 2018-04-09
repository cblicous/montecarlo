import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

def setupMediocre(amount,showPlot):
    numsMediocre = setupRng(-5, 5,amount)
    numsMediocre = [x+5 for x in numsMediocre]
    if(showPlot):
        plt.hist(numsMediocre, bins = len(numsMediocre))
        plt.show()
        #print(numsMediocre)
    return numsMediocre

def setupGood(amount,showPlot):
    numsGood = setupRng(-10, 0,amount)
    #print(numsGood)
    numsGood = [(11-x*-1 )for x in numsGood]
    if(showPlot):
        plt.hist(numsGood, bins = len(numsGood))
        plt.show()
    return numsGood

def setupBad(amount,showPlot):
    numsBad =setupRng(1,11,amount)
    if(showPlot):
        plt.hist(numsBad, bins = len(numsBad))
        plt.show()
    return numsBad

def calculateSprint():
    sprintTotal = 0
    currentSprint = 0
    while (sprintTotal < 600):
        numsMediocre = setupMediocre(2,False)
        currentSprintTotal = sum (numsMediocre)
        numsGood =setupGood(7,False)
        currentSprintTotal = currentSprintTotal + sum(numsGood)
        numsBad = setupBad(1,False)
        currentSprintTotal = currentSprintTotal + sum(numsBad)

        sprintTotal = sprintTotal + currentSprintTotal
        #print ('Current Sprint gave SP:{}'.format(currentSprintTotal))
        #print ('Current Sprint Number:{}'.format(currentSprint))
        #print ('Total done SP:{}'.format( spintTotal))
        currentSprint +=1
    print ('----')
    print ('Finished SP:{}'.format( sprintTotal))
    print ('Needed Sprints:{}'.format( currentSprint))
    return currentSprint

def setupRng(lowOffset,topOffset,groupSize):
    x = np.arange(lowOffset, topOffset)
    xU = x + 0.5
    xL = x - 0.5
    prob = ss.norm.cdf(xU, scale = 2) - ss.norm.cdf(xL, scale = 2)
    prob = prob / prob.sum() #normalize the probabilities so their sum is 1
    # map(lambda x: x+170, list1)
    result = np.random.choice(x, size = groupSize, p = prob)
    #plt.hist(result, bins = len(x))
    #plt.show()
    return result


testRuns = 0;

neededSprints = []

print("Showing distribution")
setupBad(1000,True)
setupMediocre(1000,True)
setupGood(1000,True)

while (testRuns < 100):
    currentSprintSP = calculateSprint()
    neededSprints.append(currentSprintSP)
    testRuns += 1

print ('On {} Testruns, average of {} Sprints was needed'.format(testRuns,np.mean(neededSprints)))
#plt.hist(numsMediocre, bins = len(x))
#plt.show()
print("done")
