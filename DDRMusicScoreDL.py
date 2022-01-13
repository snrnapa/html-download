import os
import re
import sys
import csv
from bs4 import BeautifulSoup
from bs4.builder import HTMLTreeBuilder
import requests
import numpy as np
import urllib.request
from urllib.parse import urljoin
# ローカルURLから各楽曲のページのURLを落とすコード
source_data = input("please write playstayle and difficult:")

soup = BeautifulSoup(open((source_data + '.html'), encoding='utf-8'), "html.parser")
atag = soup.select('#contents table a')
# print(atag)
link_list = []
MusicName_list = []
for link in atag:
    href_url = link.get("href")
    link_list.append(href_url)
    music_name = link.get("title")
    MusicName_list.append(music_name)

music_link = [temp for temp in link_list if "w.atwiki.jp/ddr_dp/pages/" in temp if "login" not in temp if "hatena" not in temp]
print(music_link)
print(MusicName_list)

Score_list = [element for element in link_list if element.endswith("html")]

# ここまでローカルhtmlを用いて、各楽曲のURLを取得　music_linkに代入

# ここから、取得したURLで必要な部分”wikibody"のID部分のみ落としていく（必要部分だけであればCSSファイルは不要）
# ここまでの変数の種類
# Score_list : 各楽曲のリンク ◎◎.HTML
# MusicName_list : 各楽曲の名前　リスト型

os.makedirs(source_data,exist_ok=True)

for score_number in range(len(Score_list)):
    url3 = "https:" + Score_list[score_number]
    sitedata = requests.get(url3)
    soup3 = BeautifulSoup(sitedata.text,"html.parser")
    score_maincotent = soup3.select('div#wikibody')
    with open(source_data + "/" + MusicName_list[score_number] + ".html","w",encoding="utf-8") as f:
        f.write(str(score_maincotent))

        # with open(MusicName_list[score_number] + ".html", "w", encoding="utf-8") as f:
        #     f.write(sitedata.text)


sys.exit()



# これは上記の単独型　保存として残しておく

# url3 = "https:" + Score_list[0]
# print(url3)



# sitedata = requests.get(url3)
# soup3 = BeautifulSoup(sitedata.text,"html.parser")
# score_maincotent = soup3.select('div#wikibody')
# print(score_maincotent)

# with open("output.txt","w") as f:
#     f.write(str(score_maincotent))

#     # with open(MusicName_list[score_number] + ".html", "w", encoding="utf-8") as f:
#     #     f.write(sitedata.text)







# atag = soup.select('#contents table a')
# print(atag)
# link_list = []
# MusicName_list = []
# for link in atag:
#     href_url = link.get("href")
#     link_list.append(href_url)
#     music_name = link.get("title")
#     MusicName_list.append(music_name)

# music_link = [temp for temp in link_list if "w.atwiki.jp/ddr_dp/pages/" in temp if "login" not in temp if "hatena" not in temp]
# print(music_link)
# print(MusicName_list)

# Score_list = [element for element in link_list if element.endswith("html")]




sys.exit()

