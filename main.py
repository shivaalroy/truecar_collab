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
        collapser.get_member_clicks('clickstream/click_20150730.tsv', 'output/some_members.txt')

if __name__ == '__main__': main()