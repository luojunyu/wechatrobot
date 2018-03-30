# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
import random

j=0
#获取url地址
def get_url(content):
    keywd = urllib2.quote(content.encode('utf8'))
    keywords = keywd[27:]
    url = "https://s.taobao.com/search?q=" + keywords + "&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171113&ie=utf8"
    return url

#打开网页，获取网页内容
def url_open(url):
    headers=("user-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener=urllib2.build_opener()
    opener.addheaders=[headers]
    urllib2.install_opener(opener)
    data=urllib2.urlopen(url).read().decode("utf-8","ignore")
    return data




def img_spyder(content):
    url=get_url(content)
    data=url_open(url)
    img_pat='"pic_url":"(//.*?)"'
    imgL=re.compile(img_pat).findall(data)
    img="http:"+imgL[j]#商品图片链接
    return img

def name_spyder(content):
    url=get_url(content)
    data=url_open(url)
    name_pat = '"raw_title":"(.*?)"'
    nameL = re.compile(name_pat).findall(data)
    name = nameL[j]  # 商品名称
    return name

def nick_spyder(content):
    url=get_url(content)
    data=url_open(url)
    nick_pat = '"nick":"(.*?)"'
    nickL = re.compile(nick_pat).findall(data)
    nick = nickL[j]  # 淘宝店铺名称
    return nick

def price_spyder(content):
    url=get_url(content)
    data=url_open(url)
    price_pat = '"view_price":"(.*?)"'
    priceL = re.compile(price_pat).findall(data)
    price = priceL[j]  # 商品价格
    return price

def fee_spyder(content):
    url=get_url(content)
    data=url_open(url)
    fee_pat = '"view_fee":"(.*?)"'
    feeL = re.compile(fee_pat).findall(data)
    fee = feeL[j]  # 运费
    return fee

def comment_spyder(content):
    url=get_url(content)
    data=url_open(url)
    comment_pat = '"comment_count":"(.*?)"'
    commentL = re.compile(comment_pat).findall(data)
    comment = commentL[j]  # 商品评论数，会存在为空值的情况
    global j
    j=j+1
    if (comment == ""):
        comment = 0
    return comment

def city_spyder(content):
    url=get_url(content)
    data=url_open(url)
    city_pat = '"item_loc":"(.*?)"'
    cityL = re.compile(city_pat).findall(data)
    city = cityL[j]  # 店铺所在城市
    return city



