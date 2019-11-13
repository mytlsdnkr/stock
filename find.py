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

fd=open("stock.txt","r",encoding="euc-kr")
print(fd.readlines())
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


def politics(stop,font_path):
    m=Mecab()
    tags=""
    df=pd.read_csv("Article_정치.csv",header=None,names=['1','2','3','4','desc','6']);
    desc=df['desc'][0]
    nouns=m.nouns(desc)
    count=Counter(nouns)

    for n,c in count.most_common(100):
        if len(n)>=2 and len(n)<=49:
            if n in stop:
                continue
            tags=tags+n+" "
    makeWordCloud(font_path,tags,"politics.png")




#politics(stop,font_path)
    
