#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:52:39 2020

@author: joe
"""
FileIn = "test.gro"
FileOut = "Test_Py.gro"
with open (FileIn, "r") as f:
    
    count = 0
    for line in f.readlines(  ):
        count += 1

PastLines = []
LineKeep = []
    
with open (FileIn, "r") as f:    
    
    ln = 1 
    for line in f:
        
        #print(ln)
        if ln < 3:
            ln+=1
        elif ln > (count - 1 ):       
            print ("DONE")
        else:
            AtomNam = str(line[12:15])

###OW          
            if " OW" in AtomNam and len(PastLines) == 0 :
                PastLines.append(AtomNam)
                ln+=1


            elif "HW1" in AtomNam and ' OW' in PastLines and\
            len(PastLines) == 1:
                PastLines.append(AtomNam)
                ln+=1                


            elif "HW2" in AtomNam and "HW1" in PastLines and " OW" in PastLines\
            and len(PastLines) == 2:
                PastLines.append(AtomNam)
                PastLines.clear()
                LineKeep.append(ln)
                LineKeep.append(ln-1) 
                LineKeep.append(ln-2)
                ln+=1                        
            
            elif "HW2" in AtomNam or "HW1" in AtomNam or " OW" in AtomNam:
                PastLines.clear()
                ln+=1
            
            else:
                LineKeep.append(ln)
                ln+=1


ListLen = len(LineKeep)
FileLen = ListLen
with open (FileIn, "r") as f:
    with open (FileOut, "w") as fo:
        fo.write("TestPy \n")
        fo.write("%5s \n" %(FileLen))
        ln = 1 
        for line in f:
            print(ln)
            if ln < 3:
                ln+=1
            elif ln > (count - 1 ):
                print ("DONE")
            elif ln in LineKeep:
                fo.write(line)

                ln+=1
            else:
                ln+=1
        fo.write("%10.5f%10.5f%10.5f \n" % (40,40,40))   
