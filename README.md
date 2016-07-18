
1.Run the Map-Reduce task with proper files(mapper.py,reducer.py,input(log file),output) with command

"$ hadoop  jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.num.map.output.key.fields=4 -D mapred.text.key.comparator.options='-k1 -k2,2n' -input /user/hduser/gg/* -output /user/hduser/sample-output -mapper /home/hduser/ggmapper.py -reducer /home/hduser/ggreducer.py
"

2.Take the output file and run the final_mapper.py on it. The necessary libraries should be installed on the system beforehand. This can also be done using Map-Reduce phase. 
