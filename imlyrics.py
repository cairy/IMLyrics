"""Written By cairy """
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import glob
import eyed3
import urllib2
import os
from bs4 import BeautifulSoup
from searchlrcfrombaidu import searchLrcFromBaidu

def main(d):
    song_names= glob.glob(d)
    for name in song_names:
        print(name)
        basename=os.path.basename(name)
        basename=basename.decode('gb18030').encode('utf8')
        basename= basename.replace('.mp3','')
        
        audiofile = eyed3.load(name)
        lyrics=searchLrcFromBaidu(basename +' 歌词')
        if lyrics:
            audiofile.tag.lyrics.set(lyrics )
            audiofile.tag.save()
            print('成功'.decode('utf8').encode('gb18030'))
            with open (name.replace('+',' ')+'.txt','w') as f:
                f.write(lyrics.encode('gb18030'))
        else:
            with open ('errorfile.txt','a') as f:
                f.write('\n'+name)
                
if __name__=='__main__':
    #d=r"F:\Ipad_OK\*.mp3"
    d=''
    if len(sys.argv)==2:
        d=sys.argv[1]
    if not d:
        d=raw_input("请输入目录名:".decode('utf8').encode('gb18030'))    
    if os.path.isdir(d):
        print d
        d=os.path.join(d,'*.mp3')
        main(d)
