#################################################################
# FILE : ex6.py
# WRITER : reef menaged , rifmenaged , 211396528
# EXERCISE : intro2cs2 ex6 2023
# DESCRIPTION: ex6 intro
#################################################################

import pickle
import sys

"""Opening a Pickle file"""
def open_pickle(file):
    with open(file, 'rb') as fp:
        return pickle.load(fp)


"""A function of analyzing the words entered into the search"""
def search_word(page_dic, word_list, dic, limit):
    match_pages = []
    words_set = set()
    all_pages = list({k: page_dic[k] for k in sorted(page_dic, key=page_dic.get, reverse=True)}.keys())
    counter = 0
    for page in all_pages:
        if counter >= limit:
            continue
        bool_var = True
        for word in word_list:
            if word not in dic:
                continue
            elif page not in dic[word]:
                bool_var = False
                break
            words_set.add(word)
        if bool_var:
            match_pages.append(page)
            counter += 1
    return match_pages, words_set


"""Sorting the results of the pages for presentation"""
def sort_pages(max, rank, words, pages, words_search):
    end_list_values = []
    end_list_pages = []
    if max > len(pages):
        max = len(pages)
    for i in range(len(pages)):
        min_word = False
        for word in words_search:
            if min_word == False:
                min_word = words[word][pages[i]]
            elif words[word][pages[i]] < min_word:
                min_word = words[word][pages[i]]
        end_list_pages.append(pages[i])
        end_list_values.append(rank[pages[i]]*min_word)
    try:
        end_list_values, end_list_pages = zip(*sorted(zip(end_list_values, end_list_pages)))
    except:
        pass

    for row in range(len(end_list_values)-1, len(end_list_values)-max-1, -1):
        print(end_list_pages[row], end_list_values[row])


"""The central search function"""
def search():
    query = sys.argv[2]
    ranking_dict_file = sys.argv[3]
    words_dict_file = sys.argv[4]
    max_results = sys.argv[5]
    search_words = query.split(" ")
    rank_dict = open_pickle(ranking_dict_file)
    words_dict = open_pickle(words_dict_file)

    words_dict = {}
    match_pages, words_set = search_word(rank_dict, search_words, words_dict, int(max_results))
    sort_pages(int(max_results), rank_dict, words_dict, match_pages, words_set)
