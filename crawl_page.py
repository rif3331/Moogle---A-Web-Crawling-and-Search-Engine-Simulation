#################################################################
# FILE : ex6.py
# WRITER : reef menaged , rifmenaged , 211396528
# EXERCISE : intro2cs2 ex6 2023
# DESCRIPTION: ex6 intro
#################################################################

import pickle
import sys
import urllib.parse
import requests
import bs4


"""Downloading and managing words from websites"""
def bs4_url(url, file):
    dic = create_main_dict(file)
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target in dic:
                dic[target] = dic[target] + 1
    lst = []
    for i in dic.items():
        keys = i[0]
        value = i[1]
        if value == 0:
            lst.append(keys)
    for i in range(len(lst)):
        del dic[lst[i]]
    return dic


"""Creating the main dictionary"""
def create_main_dict(temp_file):
    file = open(temp_file, "r")
    temp_dic = dict()
    for row in file:
        temp_dic.update({row.replace("\n", ""): 0})
    file.close()
    return temp_dic


"""Creating pointers for each page"""
def crawl():
    base_url = sys.argv[2]
    index_file = sys.argv[3]
    out_file = sys.argv[4]

    traffic_dic = create_main_dict(index_file)
    all_keys = list(traffic_dic.keys())
    for key in all_keys:
        url = urllib.parse.urljoin(base_url, key)
        traffic_dic[key] = bs4_url(url, index_file)

    with open(out_file, 'wb') as f:
        pickle.dump(traffic_dic, f)

