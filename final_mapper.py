from __future__ import division
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    avg_session = 0;
    valid_session = 0
    invalid_session = 0
    v_devices = 0       #Number of valid devices
    try:
        file_pointer = open('C:\\greedygames\\final.txt','rU')
    except IOError:
        print "File not found"
        sys.exit()
    
    datalist = [[]]
    dType= [str, str, float, str]   #Datatype format in which we will store the data
    for line in file_pointer:
        line=line.strip();
        raw_list = re.split(r'\t+', line.rstrip('\t'))  #Getting a list of strings(tab separated)
        temp_list = [t(x) for t,x in zip(dType,raw_list)]  #To convert the datatype of 3rd column to float
        if(temp_list[2] >= 1.0):            #Discarding the sessions which are less than 1 second
            datalist.append(temp_list)
            if(temp_list[2] >60.0):         #Working on Valid Sessions
                avg_session = (((avg_session*v_devices)+temp_list[2])/(v_devices+1))
                valid_session = valid_session+1
                v_devices = v_devices+1
            else:
                invalid_session = invalid_session+1
            #print temp_list
    datalist.pop(0)     # remove the entry first empty list from list of lists
    #print datalist
    print "Total Sessions are      :",valid_session+invalid_session
    print "Valid Sessions are      :",valid_session
    print "Average Session time is :",avg_session," Seconds"    
    df = pd.DataFrame(datalist, columns=['ai5','game_id','Session','sdkv'])
    del(datalist)       #freeing the memory(Dont need the datalist anymore,data is in Dataframe)
    
    
    ##Making the Plots
    max_game =pd.DataFrame(df.groupby('game_id').count())
    game_list = max_game.index.values
    device_count = max_game['ai5'].tolist()
    fig = plt.figure()
    width = .35
    plt.figure(figsize=(20,10))
    plt.xlabel('Game_ID')
    plt.ylabel('#Devices')
    plt.title('Game v/s No. of Devices')
    ind = np.arange(len(device_count))
    plt.bar(ind, device_count, width=width)
    plt.xticks(ind + width / 2, game_list)    
    fig.autofmt_xdate()    
    
    
    
if __name__ == "__main__":
    main()
