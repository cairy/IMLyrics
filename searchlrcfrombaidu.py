#!/usr/bin/env python
#-*- coding:utf-8 -*-
import urllib2
import urllib
from bs4 import BeautifulSoup
import re

useragent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36 OPR/29.0.1795.47'
tag_dict={'www.kuwo.cn/yinyue':{'name':'div','id':'lrcContent'},
          'www.kuwo.cn/geci':{'name':'div','id':'lrc_yes'},
          'www.xiami.com/lrc':{'name':'li','class':'clearfix'},
          'www.xiami.com/song':{'name':'div','class':'lrc_main'},
          'www.yy8844.cn/geci':{'name':'div','id':'geci'},
          'www.1ting.com/geci':{'name':'div','id':'container'}
          }

def getLrcFromLrclink(link,taginfo):
    '''从网站解析歌词'''
    request = urllib2.Request(link)
    request.add_header('User-Agent',useragent)
    lyrics_html = urllib2.urlopen(request).read()    
    soup = BeautifulSoup(lyrics_html,"html.parser")
    #lrc_tag= (soup.findAll('div', attrs={'id' : 'lrcContent'}))
    lrc_tag=soup.find(**taginfo)
    if lrc_tag:
        #return lrc_tag.get_text().strip()
        lrc=re.sub('^.+歌词[:：]?'.decode('utf8'),'',lrc_tag.get_text().lstrip()).strip()
        return u'\n'.join(lrc.splitlines())
    else:
        return ''
    
def searchLrcFromBaidu(name):
    '''从百度搜索歌词'''
    urltemplate = 'http://www.baidu.com/s?wd='+urllib.quote(name)+'&pn='
    for pn in ('0','10','20'):
        req = urllib2.Request(urltemplate+pn, headers={'User-Agent' : useragent})
        response = urllib2.urlopen(req)
        result = response.read()
        link_start=-1
        lrc=''
        for i in tag_dict:
            link_start=result.find('>'+i)
            if link_start>=0:
                m=re.search('"url":"([^"]+)"', result[link_start:], flags=0)
                if m:
                    link=m.group(1)
                    if link:
                        try:
                            lrc=getLrcFromLrclink(link, tag_dict[i])
                        except urllib2.HTTPError:
                            continue
                        if lrc:
                            return lrc
    return lrc
if __name__=='__main__':
    test1=searchLrcFromBaidu('G.E.M.邓紫棋 - 单行的轨道 歌词')
    print test1
    #link='http://music.baidu.com/song/239779239?fm=altg5'
    #if link:
        #getLrcFromBaidu(link)
