#!/usr/bin/env python
#Maps the required fields to the standard IO in Hadoop Environment
import sys
import json
for line in sys.stdin:
	line = line.strip()
	temp_JSON=json.loads(line)      #stores the JSON object of one record
	temp_str=''                     #stores the tab separated values of required fields in JSON object
	print temp_JSON['headers']['ai5']+'\t'+temp_JSON['post']['ts']+'\t'+temp_JSON['bottle']['game_id']+'\t'+temp_JSON['post']['event']+'\t'+temp_JSON['headers']['sdkv']
