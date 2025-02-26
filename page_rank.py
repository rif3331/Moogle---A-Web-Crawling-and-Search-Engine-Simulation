#################################################################
# FILE : ex6.py
# WRITER : reef menaged , rifmenaged , 211396528
# EXERCISE : intro2cs2 ex6 2023
# DESCRIPTION: ex6 intro
#################################################################

import pickle
import sys

"""Quick dictionary creation"""
def create_new_dict(keys, value):
    dic = dict()
    for key in keys:
        dic.update({key: value})
    return dic


"""Checks how many pointers to the page"""
def sum_links(key, link, file, dic):
    try:
        return sum(list(link[key].values()))
    except:
        return 0


"""Checks how many votes for a particular page"""
def sum_link_page_to_other_page(key, link, page2):
    try:
        return link[key][page2]
    except:
        return 0


"""Pickle file saver"""
def save(file, dic):
    with open(file, 'wb') as f:
        pickle.dump(dic, f)


"""Creating a ranked dictionary"""
def page_rank():
    iterations = int(sys.argv[2])
    dict_file = sys.argv[3]
    out_file = sys.argv[4]
    with open(dict_file, 'rb') as fp:
        words = fp.read()
        if len(words) < 5:
            save(out_file, dict())
            return
    with open(dict_file, 'rb') as fp:
        link_dict = pickle.load(fp)
    all_keys = list(link_dict.keys())
    try:
        sum(list(link_dict[all_keys[0]].values()))
    except:
        save(out_file, dict())
        return
    rating_dic = create_new_dict(all_keys, 1.0)
    for t in range(iterations):
        new_r = create_new_dict(all_keys, 0)
        for j in all_keys:
            count = 0
            for i in all_keys:
                denominator_formula = sum_links(i, link_dict, out_file, rating_dic)
                first_member_formula = rating_dic[i]
                counter_formula = sum_link_page_to_other_page(i, link_dict, j)
                formula = first_member_formula * counter_formula / denominator_formula
                count += formula
            new_r[j] = count
        rating_dic = new_r
    save(out_file, rating_dic)
