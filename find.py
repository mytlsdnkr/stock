import pandas as pd
import csv
from konlpy.tag import Mecab
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
    #plt.show()
    fig.savefig(filename)


def keyword(category,stop,font_path,stock):
    global tags
    global addedStop

    m=Mecab()
    df=pd.read_csv("Article_"+category+".csv",header=None,names=['1','2','3','4','desc','6']);
    desc=df['desc'][0]
    nouns=m.nouns(desc)
    count=Counter(nouns)

    for n,c in count.most_common(100):
        if len(n)>=2 and len(n)<=49:
            if n in stop:
                continue
            if n in stock:
                tags=tags+' '.join(stock[n])
            else:
                print(n+"에 대한 데이터가 없습니다.")
                temp=input("추가하시겠습니까?(Y or N 그 외 입력 시 불용어에 추가) ")
                if temp=='Y':
                    print("END 입력시 끝")
                    li=[]
                    li.append(n)
                    while True:
                        a=input()
                        if a=="END":
                            break
                        if a in li:
                            print("이미 존재합니다.")
                            continue
                        li.append(a)
                    fd=open("/root/workspace/stock/stock/stock.txt","a",encoding="euc-kr")
                    wr=csv.writer(fd)
                    wr.writerow(li)
                    del li[0]
                    fd.close()
                    tags=tags+' '.join(li)
                    stock[n]=li
                elif temp=='N':
                    tags=tags+' '+n
                    continue
                else:
                    addedStop=addedStop+n+"\n"
					stop.append(n)
					



if __name__ == "__main__":


    #font 경로 설정
    font_path="/usr/share/fonts/nanum/nanum.ttf"

    #불용어 stop 리스트에 저장
    stop=[]
    fd=open("stopwords.txt","r")
    lines=csv.reader(fd)
    for line in lines:
        stop.append(str(line[0]))
    fd.close()
    stop=list(set(stop))

    addedStop=""

    #현재 있는 관련주 stock 딕셔너리에 추가
    fd=open("/root/workspace/stock/stock/stock.txt","r",encoding="euc-kr")
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
    #wordCloud를 만들기위한 tags 추가
    tags=""
    
    keyword("정치",stop,font_path,stock)
    keyword("IT과학",stop,font_path,stock)
    keyword("경제",stop,font_path,stock)
    keyword("사회",stop,font_path,stock)
    keyword("생활문화",stop,font_path,stock)
    keyword("오피니언",stop,font_path,stock)
    keyword("세계",stop,font_path,stock)
    fd=open("stopwords.txt","at")
    fd.write(addedStop)
    fd.close()
    makeWordCloud(font_path,tags,"/root/workspace/stock/keyword.png")
