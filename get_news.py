import requests
import urllib.request
from bs4 import BeautifulSoup

import get_shortenURL

def get_yahoo_news():
    # ヘッドラインニュースのタイトル格納用リスト
    news_data = []

    # urlの指定
    url = 'http://www.yahoo.co.jp/'

    # ユーザーエージェントを指定
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Gecko/20100101 Firefox/60.0 '

    req = urllib.request.Request(url, headers={'User-Agent': ua})

    #htmlの取得
    html = urllib.request.urlopen(req)

    # htmlパース
    soup = BeautifulSoup(html, "html.parser")
    topicsindex = soup.find('div', attrs={'class': 'topicsindex'})
    # class「topicsindex」内から記事タイトルを抽出
    for li in topicsindex.find_all('li'):
        a = li.find('a')
        # 記事タイトルとURLを保存
        re_url = '--<'+get_shortenURL.get_shortenURL(a.get('href'))+'>--'

        news_data.append([a.contents[0], re_url])
    return news_data

def get_nhk_news():
    # ニュース格納用リスト
    news_data = []
    # urlの指定
    url = 'http://k.nhk.jp/knews/index.html'

    # ユーザーエージェントを指定
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) '\
     'AppleWebKit/537.36 (KHTML, like Gecko) '\
     'Gecko/20100101 Firefox/60.0 '

    req = urllib.request.Request(url, headers={'User-Agent': ua})

    #htmlの取得
    html = urllib.request.urlopen(req)
    # htmlパース
    soup = BeautifulSoup(html, "html.parser")
    #簡易型NHKnewsへの変換
    text_data = []
    long_path = 'https://www3.nhk.or.jp/news/html/'
    news_path = 'http://k.nhk.jp/knews/'
    all_a = soup.find_all('a')
    all_a = all_a[:7]
    #対象のURLを獲得
    for index in (all_a):
        n_url = news_path+index.get('href')
        l_url = long_path+index.get('href')
        news_data.append([index.contents[0], n_url, l_url])
    for data in news_data:
        url = data[1]
        req = urllib.request.Request(url, headers={'User-Agent': ua})
        #htmlの取得
        html = urllib.request.urlopen(req)
        # htmlパース
        soup = BeautifulSoup(html, "html.parser")
        #title取得
        title_text = data[0]
        split_text = soup.text.split("\n")
        for target in range(len(split_text)):
            if(split_text[target].find("。")!=-1):
                main_text = split_text[target]
                date_text = split_text[target+2]+\
                    '--<'+get_shortenURL.get_shortenURL(data[2])+'>--'
        text_data.append([title_text, main_text, date_text, "-----"])
        #time.sleep(1)
        print("*")
    print("-----")
    return text_data, news_data


if __name__ == '__main__':
    get_yahoo_news()
