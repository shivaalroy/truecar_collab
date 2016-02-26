"""
Tool for preprocessing clickstream data into user sessions for classication algorithms.
"""

import csv
import os

class collapser():
    """
    Tools to help with downloading TCGA datasets.
    """
    @staticmethod
    def get_member_clicks(input_file_name, output_filename):
        with open(input_file_name,'rb') as input:
            csv.reader(input, delimiter='\t')
            output = open(output_filename, 'w')

            count = -1
            for row in input:
                count += 1
                if count == 0: continue
                if count > 22000: break
                entry = row.split("\t")
                entry[len(entry)-1] = entry[len(entry)-1][:-2]
                if entry[0] != "":
                    output.write("\t".join(entry) + "\n")
                    # print "\t".join(entry)

