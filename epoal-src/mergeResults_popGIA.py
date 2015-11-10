import re
import string
import numpy
import os

if __name__ == '__main__':
    # for each case
    path=os.getcwd()
    #print path

#replace    chpath=str(path)+"\\..\\results\popGIA\hound.opteron\ERS"
    chpath=str(path)+"\\..\\results\popGIA\hound.opteron\WPT"

    os.chdir(chpath)
    #print os.getcwd()
#replace    prefix="popGIA_ERS_P"
    prefix="popGIA_WPT_P"

    # for each #cores
    totalfilename =  str('Total_'+prefix[0:10]+'.csv')
    outputFile = open(totalfilename, 'w')
    try:
        # remove ParetoSize, add uniqueFoundPoints to check overlapping ratio
#        outputFile.writelines('Cores'+','+'FoundPoints'+','+'UniqueFoundPoints'+','+'SatCalls'+','+'Time'+'\n')
        outputFile.writelines('Cores'+','+'Time'+'\n')

    finally:
        outputFile.close()
    
    # change for xeon/opteron
    #for i in [4, 6, 8, 10, 12]:
    for i in [4, 6, 8, 10, 12, 14, 16]:
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
            # this time is the record in parent subprocess, which should be choose min in each group and then choose max in all groups
            # update it below
            summary[m][3]=0.0
            # for WPT seconds -> minutes
            #summary[m][3]=string.atof(summary[m][3])/60
            summary[m].append(0)
            #print summary[m]
            m += 1
        
        # create group id, e.g. P4 has two groups for the two partitions
        group = []
        for k in range(i/2):
            group.append([])
        for k in range(i/2):
            for m in range(len(inputParentList)):
                group[k].append([])
        
        #print group 
        # choose min values in child files and update them to groups 
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
                # get time
                #time_subprocess = string.atof(tmpChildLineList[4])
                # for WPT seconds -> minutes
                time_subprocess = string.atof(tmpChildLineList[4])/60
                if len(group[j/2][m]) == 0 :
                    group[j/2][m].append(time_subprocess)
                else:
                    if time_subprocess < group[j/2][m][0] :
                        group[j/2][m][0] = time_subprocess
                m += 1
        
        #print group
                 
        # choose max value in each group and update to parent file        
        for m in range(len(inputParentList)):
            for k in range(i/2):
                time_subgroup = group[k][m][0]
                if time_subgroup > summary[m][3]:
                    summary[m][3] = time_subgroup                


        
#         #print summary
        arr = numpy.array(summary)
        meanList = numpy.mean(arr, axis=0)
        print meanList[3]
        stdList = numpy.std(arr, axis=0)
        print stdList[3]
        
        outputFile = open(totalfilename, 'a')
        try:
#             outputFile.writelines('Cores'+','+'FoundPoints(UnSatCalls-1)'+','+'UniqueFoundPoints'+','+'SatCalls'+','+'Time'+'\n')
            for m in range(10):
                outputFile.writelines(str(summary[m][0])+','+str(summary[m][3])+'\n')
#                outputFile.writelines(str(summary[m][0])+','+str(summary[m][1])+','+str(summary[m][2])+','+str(summary[m][4])+','+str(summary[m][3])+'\n')
#             outputFile.writelines(str(meanList[0])+','+str(meanList[2])+','+str(meanList[1])+','+str(meanList[4])+','+str(meanList[3])+'\n')
#             outputFile.writelines(str(stdList[0])+','+str(stdList[2])+','+str(stdList[1])+','+str(stdList[4])+','+str(stdList[3])+'\n')                          
        finally:
            outputFile.close()
            
    print "Done"