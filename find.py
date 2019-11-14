import pandas as pd
import csv
from konlpy.tag import Mecab
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

font_path="/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

stop=[]
fd=open("stopwords.txt","r")
lines=csv.reader(fd)
for line in lines:
    stop.append(str(line[0]))

fd.close()

def makeWordCloud(font_path,data,filename):
    wordcloud=WordCloud(
            font_path=font_path,
            width=800,
            height=800
            )
    wordcloud=wordcloud.generate_from_text(data)
    array=wordcloud.to_array()

    fig=plt.figure(figsize=(10,10))
    plt.imshow(array,interpolation="bilinear")
    plt.show()
    fig.savefig(filename)


def keyword(category,stop,font_path):
    fd=open("/root/workspace/bigdata/stock/"+category+".txt","r",encoding="euc-kr")
    lines=fd.readlines()
    fd.close()
    stock=dict()
    for i in lines:
        if len(lines)==0:
            break
        spl=i.split(',')
        li=[]
        for k in range(1,len(spl)):
            li.append(spl[k])
        stock[spl[0]]=li


    m=Mecab()
    tags=""
    df=pd.read_csv("Article_"+category+".csv",header=None,names=['1','2','3','4','desc','6']);
    desc=df['desc'][0]
    nouns=m.nouns(desc)
    count=Counter(nouns)
    for n,c in count.most_common(1000):
        if len(n)>=2 and len(n)<=49:
            if n in stop:
                continue
            tags=tags+n+" "
    print(tags)
'''
    for n,c in count.most_common(100):
        if len(n)>=2 and len(n)<=49:
            if n in stop:
                continue
            if n in stock:
                tags=tags+' '.join(stock[n])
            else:
                print(stock[n]+"에 대한 데이터가 없습니다.")
                temp=input("추가하시겠습니까?(Y or N)")
                if temp=='Y':
                    print("END 입력시 끝")
                    li=[]
                    li.append(stock[n])
                    while True:
                        a=input()
                        if a=="END":
                            break
                        li.append(a)
                    fd=open("/root/workspace/bigdata/stock/"+category+".txt","a",encoding="euc-kr")
                    wr=csv.writer(fd)
                    wr.writerrow(li)
                    fd.close()

    makeWordCloud(font_path,tags,"politics.png")
'''

keyword("정치",stop,font_path)
keyword("IT과학",stop,font_path)
keyword("경제",stop,font_path)
keyword("사회",stop,font_path)
keyword("생활문화",stop,font_path)
keyword("오피니언",stop,font_path)
keyword("세계",stop,font_path)
    
