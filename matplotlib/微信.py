import itchat
import pandas as pd
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

class WeChat(object):
    def __init__(self):
        itchat.login ()
        self.friends = itchat.get_friends ( update=True )[0:]
        print ( self.friends )
        print ( self.friends[0] )

    def save_info(self,NickName,Sex,Province,City,Signature):
        list=[]
        for i in self.friends:
            dict={}
            dict["NickName"]=i[NickName]
            if i[Sex]==1:
                dict["Sex"]="男"
            elif i[Sex]==2:
                dict["Sex"]="女"
            else:
                dict["Sex"]="不明性别"
            dict["Province"]=i[Province]
            dict["City"]=i[City]
            dict["Signature"]=i[Signature]
            list.append(dict)
        return list
    def save_csv(self):
        list=self.save_info("NickName","Sex","Province","City","Signature")
        print(list)
        pf=pd.DataFrame(list)
        print(pf)
        try:
            pf.to_csv("wechat.csv",index=True,encoding="gb18030")
        except Exception as ret:
            print(ret)

    def cloud(self):
        taglist=[]
        for i in self.friends:
            signature = i["Signature"].strip ().replace ( "span","" ).replace ( "class","" ).replace ( "emoji","" )
            rep = re.compile ( "1f\d+\w*|[<>/=]" )
            signature = rep.sub ( "",signature )
            taglist.append ( signature )
        text = "".join ( taglist )
        wordlist = jieba.cut ( text,cut_all=True )
        word_space_split = " ".join ( wordlist )
        coloring = np.array ( Image.open ( "3.png" ) )
        my_wordcloud = WordCloud ( background_color="white",max_words=2000,mask=coloring,max_font_size=60,
                                   random_state=42,scale=2,font_path="/usr/share/fonts/opentype/stix-word/STIX-Regular.otf" ).generate(word_space_split )

        image_colors = ImageColorGenerator ( coloring )
        plt.imshow ( my_wordcloud.recolor ( color_func=image_colors ) )
        plt.imshow ( my_wordcloud )
        plt.axis ( "off" )
        plt.show ()
        print("结束")




if __name__ == '__main__':
    wechat=WeChat()
    # wechat.save_csv()
    wechat.cloud()


