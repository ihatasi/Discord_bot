import requests
#短縮URLサービス
def get_shortenURL(longUrl):
    url = 'https://api-ssl.bitly.com/v3/shorten'
    access_token = '00000000000000000000000000' #bitlyのトークン
    query = {
            'access_token': access_token,
            'longurl':longUrl
            }
    r = requests.get(url,params=query).json()['data']['url']
    return r
