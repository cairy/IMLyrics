"""Written By cairy """
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
sys.path.append(r'D:\python_code\lib')
import glob
import eyed3
import urllib2
import os
from bs4 import BeautifulSoup
from searchlrcfrombaidu import searchLrcFromBaidu

def main(d):
    song_names= glob.glob(d.decode('gb18030'))
    for name in song_names:
        print ((name)).encode('gb18030')
        basename=os.path.basename(name)
        basename=basename.encode('gb18030')
        basename= basename.replace('.mp3','')
        
        audiofile = eyed3.load((name))
        lyrics=searchLrcFromBaidu(basename +' ¸è´Ê')
        if lyrics:
            audiofile.tag.lyrics.set(lyrics )
            audiofile.tag.save()
            print('³É¹¦')
            with open (name.replace('+',' ')+'.txt','w') as f:
                f.write(lyrics.encode('gb18030'))
        else:
            with open ('errorfile.txt','a') as f:
                f.write('\n'+name.encode('gb18030'))
                
if __name__=='__main__':
    d=r"F:\Ipad_OK\*.mp3"
    main(d)