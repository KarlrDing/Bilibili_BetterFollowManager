import requests
# from bs4 import BeautifulSoup
from datetime import datetime

#api
api_url	= 'https://api.bilibili.com/x/space/arc/search'

#up ids
up_id	= ['1629347259']

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Referer":"https://space.bilibili.com/"
}

params	= {
	'mid'		:up_id[0],
	'ps'		:30,
	'tid'		:0,
	'pn'		:1,
	#'keyward'	:,
	'order'		:'pubdate',
	'jsonp'		:'jsonp'
}

try:
	response = requests.get(api_url,headers = headers,params = params)
	print('sucess.')
except:
	print('failed.')

video_flow = response.json()
video_list = video_flow['data']['list']['vlist']# all the video in one scratch
item = 0

print('《' + video_list[item]['title'] + '》')

ts = int(video_list[item]['created'])
print('发布时间：' + datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')+
	' 时长：' + video_list[item]['length'] + ' BV号：' + video_list[item]['bvid'])







