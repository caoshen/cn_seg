#-*- coding:utf-8 -*-

import codecs
import sys

dict={}

def getdict(filename='pku_training.utf8'):
    """获取字典"""
    f = codecs.open(filename,'r','utf-8')
    contents = f.read()
    contents = contents.replace(u'\r',u'')
    contents = contents.replace(u'\n',u'')
    mydict = contents.split(u' ')
    mydict.remove(u'')
    #newdict = list(set(mydict))
    #newdict.remove(u'')


    for item in mydict:
        if len(item)>0 and item in dict:
            dict[item]=dict[item]+1
        else:
            dict[item]=1


if __name__=='__main__':
    output_file = codecs.open('people.dic','w','utf-8')
    getdict()
    for word,freq in dict.items():
        output_file.write(word+'\t'+str(freq)+'\n')
