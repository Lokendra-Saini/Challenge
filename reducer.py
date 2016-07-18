#!/usr/bin/env python
#Works on the mapped values to calculate the session times per user per game
import sys
import re
flag = 0
flag1 = 0
#P refers to previous
p_ai5 = ''
p_game_id = ''
p_ts = 0
p_sdkv = ''
p_event = ''
session = 0     #Stores the session time(period of time)
ai5 = ''
ts = 0
game_id = ''
event = ''
sdkv = ''
for line in sys.stdin:
    line = line.strip()
    
    if(flag == 0):
        temp_list = re.split(r'\t+', line.rstrip('\t'))
        if(temp_list[3] == 'ggstart'):              #To avoid printing a session if the first record is 'ggstop' event
            flag =  1      
            p_ai5 = temp_list[0]
            p_ts = long(temp_list[1])
            p_game_id = temp_list[2]
            p_event = temp_list[3]
            p_sdkv = temp_list[4]
        
        
    else:
        temp_list = re.split(r'\t+', line.rstrip('\t'))
        ai5 = temp_list[0]
        ts = long(temp_list[1])
        game_id = temp_list[2]
        event = temp_list[3]
        sdkv = temp_list[4]
        if(flag1 == 0):
		if((p_event == 'ggstart') and (event == 'ggstop') and (p_ai5 == ai5) and (p_game_id == game_id)):     #To wait for a valid session in start of the log file
			flag1 = 1
			session = ts-p_ts
        elif(p_ai5 == ai5):
            if(p_game_id == game_id):
                if((p_event == 'ggstart') and (event == 'ggstart')):        #Session time will be considered from the last ggstart event
                    session = 0
                elif((p_event == 'ggstart') and (event == 'ggstop')):       
                    session = session+(ts-p_ts)
                elif((p_event == 'ggstop') and (event == 'ggstart')):
                    if((ts-p_ts)>30000):
                        print p_ai5+'\t'+p_game_id+'\t',(session/1000.0),'\t'+p_sdkv
                        session = 0
                else:
                    print p_ai5+'\t'+p_game_id+'\t',(session/1000.0),'\t'+p_sdkv
                    session = 0
            else:
                print p_ai5+'\t'+p_game_id+'\t',(session/1000.0),'\t'+p_sdkv
                session = 0
        else:
            print p_ai5+'\t'+p_game_id+'\t',(session/1000.0),'\t'+p_sdkv
            session = 0

    p_ai5 = ai5
    p_ts = ts
    p_game_id = game_id
    p_sdkv =    sdkv
    p_event = event
print p_ai5+'\t'+p_game_id+'\t',(session/1000.0),'\t'+p_sdkv
                
                        
                    
                    
        
        
