"""
Tool for preprocessing clickstream data into user sessions for classication algorithms.

Columns of sessions are:
member_id
first_click_time
zip_code
num_visits
num_clicks(number of rows)
mean_click_time(midpoint)
last_click_time
"""


import csv
import time

class collapser():
    """
    Tools to help with downloading TCGA datasets.
    """
    @staticmethod
    def get_member_clicks(input_file_name, output_filename, stopCount=0):
        inputcsv = open(input_file_name,'rb')
        csv.reader(inputcsv, delimiter='\t')
        outputtxt = open(output_filename, 'w')

        count = 0
        for row in inputcsv:
            if count == 0:
                count += 1
                continue
            if stopCount > 0 and count > stopCount: break
            row = row.replace('\n','')
            entry = row.split('\t')
            if entry[0] != '':
                count += 1
                outputtxt.write('\t'.join(entry)+'\n')

    @staticmethod
    def getAvgTime(times):
        pattern = '%Y-%m-%d %H:%M:%S'
        epoch_times = [ int(time.mktime(time.strptime(t, pattern))) for t in times ]
        avgTime = sum(epoch_times) / len(epoch_times)
        return time.strftime(pattern, time.localtime(avgTime))

    @staticmethod
    def finalizeSession(session, times, num_clicks):
        collapser.getAvgTime(times)
        session.append(str(num_clicks))
        session.append(collapser.getAvgTime(times))
        session.append(times[len(times)-1])


    @staticmethod
    def collapse_member_clicks(input_file_name, output_filename):
        inputcsv = open(input_file_name,'rb')
        csv.reader(inputcsv, delimiter='\t')
        outputtxt = open(output_filename, 'w')

        session = ['']
        times = []
        num_clicks = 0
        for row in inputcsv:
            row = row.replace('\n','')
            entry = row.split('\t')
            if entry[0] != session[0]:
                if len(session) > 1:
                    collapser.finalizeSession(session, times, num_clicks)
                    outputtxt.write('\t'.join(session)+'\n')
                session = [entry[0], entry[1], entry[2], entry[3]]
                times = []
                num_clicks = 0
            times.append(entry[1])
            num_clicks += 1
        collapser.finalizeSession(session, times, num_clicks)
        outputtxt.write('\t'.join(session)+'\n')
