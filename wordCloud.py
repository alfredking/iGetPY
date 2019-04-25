#-*- coding:utf-8 -*-
import requests
import re
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from lxml import etree
# 生成词云
def create_word_cloud(f):
     print('根据词频计算词云')
     text = " ".join(jieba.cut(f,cut_all=False, HMM=True))
     wc = WordCloud(
           font_path="./SimHei.ttf",
           max_words=100,
           width=2000,
           height=1200,
    )
     wordcloud = wc.generate(text)
     # 写词云图片
     wordcloud.to_file("wordcloud.jpg")
     # 显示词云文件
     plt.imshow(wordcloud)
     plt.axis("off")
     plt.show()


# 去掉停用词
def remove_stop_words(f):
     stop_words = ['学会', '就是', '什么']
     for stop_word in stop_words:
           f = f.replace(stop_word, '')
     return f


f = '数据分析全景图及修炼指南\
学习数据挖掘的最佳学习路径是什么？\
Python 基础语法：开始你的 Python 之旅\
Python 科学计算：NumPy\
Python 科学计算：Pandas\
学习数据分析要掌握哪些基本概念？\
用户画像：标签化就是数据的抽象能力\
数据采集：如何自动化采集数据？\
数据采集：如何用八爪鱼采集微博上的“D&G”评论？\
Python 爬虫：如何自动化下载王祖贤海报？\
数据清洗：数据科学家 80% 时间都花费在了这里？\
数据集成：这些大号一共 20 亿粉丝？\
数据变换：大学成绩要求正态分布合理么？\
数据可视化：掌握数据领域的万金油技能\
一次学会 Python 数据可视化的 10 种技能'

f = remove_stop_words(f)

create_word_cloud(f)



headers = {
    'Referer': 'http://music.163.com',
    'Host': 'music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Chrome/10'
}


# 得到某一首歌的歌词
def get_song_lyric(headers, lyric_url):
    res = requests.request('GET', lyric_url, headers=headers)
    if 'lrc' in res.json():
        lyric = res.json()['lrc']['lyric']
        new_lyric = re.sub(r'[\d:.[\]]', '', lyric)  # 去掉时间信息
        return new_lyric
    else:
        return ''
        print(res.json())


# 去掉停用词
def remove_stop_words(f):
    stop_words = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                  'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and',
                  'distributed']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    f = remove_stop_words(f)
    cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path="./wc.ttf",
        max_words=100,
        width=2000,
        height=1200,
    )
    print(cut_text)
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# 得到指定歌手页面 热门前 50 的歌曲 ID，歌曲名
def get_songs(artist_id):
    page_url = 'https://music.163.com/artist?id=' + artist_id
    # 获取网页 HTML
    res = requests.request('GET', page_url, headers=headers)
    # 用 XPath 解析 前 50 首热门歌曲
    html = etree.HTML(res.text)
    href_xpath = "//*[@id='hotsong-list']//a/@href"
    name_xpath = "//*[@id='hotsong-list']//a/text()"
    hrefs = html.xpath(href_xpath)
    names = html.xpath(name_xpath)
    # 设置热门歌曲的 ID，歌曲名称
    song_ids = []
    song_names = []
    for href, name in zip(hrefs, names):
        song_ids.append(href[9:])
        song_names.append(name)
        print(href, '  ', name)
    return song_ids, song_names


# 设置歌手 ID，毛不易为 12138269
artist_id = '12138269'
[song_ids, song_names] = get_songs(artist_id)
# 所有歌词
all_word = ''
# 获取每首歌歌词
for (song_id, song_name) in zip(song_ids, song_names):
    # 歌词 API URL
    lyric_url = 'http://music.163.com/api/song/lyric?os=pc&id=' + song_id + '&lv=-1&kv=-1&tv=-1'
    lyric = get_song_lyric(headers, lyric_url)
    all_word = all_word + ' ' + lyric
    print(song_name)
# 根据词频 生成词云
create_word_cloud(all_word)


#需要注意的有两点
#1.歌单返回的是json文件，get_songs需要参考get_songs_lyri获取
#2.list_url中间是str类型，注意类型转换

# 网易云音乐 通过歌单ID，生成该歌单的词云

def get_songs(songlist):
    list_url='https://music.163.com/api/playlist/detail?id='+songlist
    res = requests.request('GET', list_url, headers=headers)
    if 'result' in res.json():
        for item in res.json()['result']['tracks']: # 读取json数据中的每一个ID和name
            song_ids.append(item['id'])
            song_names.append(item['name'])
            print(item['id']," ",item['name'])
            time.sleep(1) # 设置停留时间，防止“bad handshake”
        return song_ids,song_names
    else:
        return ''
        print(res.json())
# 设置歌单
songlist = '753776811'
[song_ids, song_names] = get_songs(songlist)
# 所有歌词
all_word = ''
# 获取每首歌歌词
for (song_id, song_name) in zip(song_ids, song_names):
    # 歌词 API URL
    list_url = 'http://music.163.com/api/song/lyric?os=pc&id=' + str(song_id) + '&lv=-1&kv=-1&tv=-1'
    lyric = get_song_lyric(headers, list_url)
    all_word = all_word + ' ' + lyric
    print(song_name)
# 根据词频 生成词云
create_word_cloud(all_word)
