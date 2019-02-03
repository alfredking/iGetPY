# coding :utf-8
import requests
import json
query = '王祖贤'
''' 下载图片 '''

def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout = 10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


''' for循环 请求全部的url '''
for i in range(0, 22471, 20):
    url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
    html = requests.get(url).text
    response = json.loads(html, encoding='utf-8',)#将json数据转换成python对象
    for image in response['images']:
        print(image['src'])
        download(image['src'],image['id'])#下载一张图片



