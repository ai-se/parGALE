import re
import string
import numpy
import os

if __name__ == '__main__':
    # for each case
    path=os.getcwd()
    print path
    chpath=str(path)+"\\..\\results\\fsGIA\hound.opteron\ERS"
#replace    chpath=str(path)+"\\..\\results\\fsGIA\hound.opteron\WPT"

    os.chdir(chpath)
    #print os.getcwd()
    prefix="fsGIA_ERS_betterconfig_P"
#replace    prefix="fsGIA_WPT_betterconfig_P"

    # for each #cores
    totalfilename =  str('Total_'+prefix[0:22]+'.csv')
    outputFile = open(totalfilename, 'w')
    try:
        #remove FrontSize, already verified in pnpGIA.py
#         outputFile.writelines('Cores'+','+'FrontSize'+','+'FoundPoints'+','+'SatCalls'+','+'Time'+'\n')
#        outputFile.writelines('Cores'+','+'FoundPoints'+','+'SatCalls'+','+'Time'+'\n')
        outputFile.writelines('Cores'+','+'Time'+'\n')
    
    finally:
        outputFile.close()
    
    # change for xeon/opteron
#    for i in range(2, 13):
    for i in [2, 4, 8, 16]:
        # initiate a set of lists for collecting all data from ParentFile and ChildFiles
        summary = []
        
        inputParentFile = open(str(prefix+str(i)+'.csv'))
        inputParentList = inputParentFile.readlines()
        for m in range(len(inputParentList)):
            summary.append([])
        m = 0
        for inputParentLine in inputParentList:
            #print inputParentLine
            #print re.split(',| ', str(inputParentLine))
            summary[m] = re.split(',| ', str(inputParentLine))
            summary[m].remove('\n')
            # #cores, #foundPoints/#unsatCalls, #SizeFront, TotalTime, #satcalls
            # set #SizeFront = 0
            summary[m][0]=string.atoi(summary[m][0])
            summary[m][1]=string.atoi(summary[m][1])
            summary[m][2]=string.atoi(summary[m][2])
            # this time is the record in parent subprocess, which should be the largest one in its subprocesses
            # update it below
            summary[m][3]=0.0
            # for WPT seconds -> minutes
            #summary[m][3]=string.atof(summary[m][3])/60
            summary[m].append(0)
            #print summary[m]
            m += 1
        
        for j in range(0, i):
            inputChildFile = open(str(prefix+str(i)+'C'+str(j)+'.csv'))
            inputChildList = inputChildFile.readlines()
            m = 0
            for inputChildLine in inputChildList:
                # fix a running problem on Sharcnet
                if m == len(inputParentList):
                    break
                tmpChildLineList = re.split(',| ', str(inputChildLine))
                tmpChildLineList.remove('\n')
                # get #sat calls
                num_satcalls = string.atoi(tmpChildLineList[2])
                summary[m][-1] += num_satcalls                
                #print summary[m]
                # get the time record in each subprocess, and choose the largest one
                # for WPT seconds -> minutes
                time_subprocess = string.atof(tmpChildLineList[4])
                #time_subprocess = string.atof(tmpChildLineList[4])/60
                if time_subprocess > summary[m][3]:
                    summary[m][3] = time_subprocess
                m += 1

        
        #print summary
        arr = numpy.array(summary)
        meanList = numpy.mean(arr, axis=0)
        print meanList[3]
        stdList = numpy.std(arr, axis=0)
        print stdList[3]
        
        outputFile = open(totalfilename, 'a')
        try:
#             outputFile.writelines('Cores'+','+'FrontSize'+','+'FoundPoints(UnSatCalls-1)'+','+'SatCalls'+','+'Time'+'\n')
            for m in range(10):
                outputFile.writelines(str(summary[m][0])+','+str(summary[m][3])+'\n')
#                outputFile.writelines(str(summary[m][0])+','+str(summary[m][1])+','+str(summary[m][4])+','+str(summary[m][3])+'\n')
#             outputFile.writelines(str(meanList[0])+','+str(meanList[2])+','+str(meanList[1])+','+str(meanList[4])+','+str(meanList[3])+'\n')
#             outputFile.writelines(str(stdList[0])+','+str(stdList[2])+','+str(stdList[1])+','+str(stdList[4])+','+str(stdList[3])+'\n')                          
        finally:
            outputFile.close()
            
    print "Done"