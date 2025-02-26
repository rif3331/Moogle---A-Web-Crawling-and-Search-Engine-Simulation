#################################################################
# FILE : ex6.py
# WRITER : reef menaged , rifmenaged , 211396528
# EXERCISE : intro2cs2 ex6 2023
# DESCRIPTION: ex6 intro
#################################################################

import sys
from crawl_page import *
from page_rank import *
from words import *
from search import *

"""The function redirects to the correct operating line"""
if __name__ == '__main__':
    if sys.argv[1] == "crawl":
        crawl()
    elif sys.argv[1] == "page_rank":
        page_rank()
    elif sys.argv[1] == "words_dict":
        words_dic()
    elif sys.argv[1] == "search":
        search()
