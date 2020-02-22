import requests
from lxml import etree
import time
import random
#user_agent 集合
user_agent_list = [#模拟登入
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
  'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]
#随机选择一个
user_agent = random.choice(user_agent_list)
#传递给header
headers = { 'User-Agent': user_agent }
def gethref(href):
    global Html
    try:
        Html=requests.get(href, 'utf-8',headers=headers)#获取目录的链接
        print("爬取目录成功")
    except:
        print("爬取目录失败")
    html=etree.HTML(Html.text)
    for i in range(1,1061):#取得各章节的链接
        x='//*[@id="novel49948"]/dl/dd['+str(i)+']/a/@href'
        results = html.xpath(x)
        y=results
        getcontent(i,str(y))#获取各章节的内容
        time.sleep(1)
        #print(results)
def getcontent(num,results):
    #print(len(results))
    url = 'https://www.qktsw.com/' + results[2:25]#章节的链接
    #33print(url)
    global html1
    try:
       html1= requests.get(url,'utf-8',headers=headers)
       print("爬取第%d章成功,爬取%.2f"%(num,num/1061*100))
    except:
        print("爬取第%d章失败"%num)
    Html1=etree.HTML(html1.text)
    con=Html1.xpath('//*[@id="content28763646"]/div[1]/p/text()')#获取章节内容
    title=Html1.xpath('//*[@id="main"]/div[1]/div[1]/h1/text()')
    for i in title:
        print(i)
        save(0,i)
   # savet(title)
    for i in con:
        save(1,i)
def save(flag,content):#保存内容
    f=open('novel.text','a',encoding='utf-8')
    if flag==1:
        f.write(content)
        f.write('\n')
    else:
        f.write(content)
        f.write('\n')
    f.close()
    #f.write('\n')
if __name__ == '__main__':
    href="https://www.qktsw.com/book/49948/"
    gethref(href)#得到链接
    print("爬取完成")