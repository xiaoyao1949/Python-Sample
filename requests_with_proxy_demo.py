import requests

if __name__ == '__main__':
    url = 'http://www.xbiquge.la/10/10489/15999944.html'
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit '
                      '/ 537.36(KHTML, likeGecko) Chrome / 63.0.3239.132Safari / 537.36'
    }
    proxies = {'http': '47.94.217.37:80'}
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        print(response.text[:1000])
    except Exception as e:
        print('网络错误')
