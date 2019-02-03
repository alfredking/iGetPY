import os
from selenium import webdriver
import requests
'''
for root, dirs, files in os.walk('./'):
    for name in files:
        print(name)
        if name.endswith(".jpg"):
            print(name)
            os.remove(os.path.join(root, name))
'''
driver = webdriver.chrome
driver.get(request_url)

srcs = html.xpath

def getMovieImages():
    url = 'https://movie.douban.com/subject_search?search_text='+ query +'&cat=1002'
    driver = webdriver.Chrome('/Users/yong/Desktop/Python/xpath/libs/chromedriver')
    driver.get(url)
    html = etree.HTML(driver.page_source)
    # 使用xpath helper, ctrl+shit+x 选中元素，如果要匹配全部，则需要修改query 表达式
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"

    srcs = html.xpath(src_xpath)
    titles = html.xpath(title_xpath)
    for src, title in zip(srcs, titles):
        print('\t'.join([str(src),str(title.text)]))
        download(src, title.text)

    driver.close()

getMovieImages()