"""
Primary driver code for the truecar classification pipeline.
"""

import sys
from collapse_tools import collapser

def print_help():
    print("""truecar_collab | version 0.0.1 | Agrawal, Roy, Singhal

python main.py [help] [member_clicks]

help                -- print this help message
member_clicks       -- get all clicks associated with member IDs

Submodules can be combined together to execute multiple
functions in a single call.""")

def main():
    argv = [a.lower() for a in sys.argv]

    if 'help' in argv:
        print_help()
        exit()
    if 'member_clicks' in argv:
        clickstreamfile = 'clickstream/click_20150730.tsv'
        temp_members_clicks = 'output/member_clicks.txt'
        outputfile = 'output/members.txt'
        CLICK_COUNT = 0
        print "Finding members..."
        collapser.get_member_clicks(clickstreamfile,temp_members_clicks,CLICK_COUNT)
        print "Collapsing sessions..."
        collapser.collapse_member_clicks(temp_members_clicks,outputfile)

if __name__ == '__main__': main()