'''
1.  填空题  数据采集-简单爬虫示例-具体实例
用 list 充当 URL 管理模块，新建一个列表queue，列表内有一元素seed；
使用re模块构造正则表达式对象r，匹配网页中的 URL。
将结果保存到 dict 中，其中 key 是 URL，value 是从网页中解析出来的链接的数目，新建的字典名为storage；
设置一个计数器 count，爬取这么多网页就结束程序，防止死循环。
使用while循环，停止条件为队列queue中没有元素及计数器count为0时：
    使用异常处理方法try:
        选取队列中第一个元素，保存到变量url中；
        使用urllib.request.urlopen(url).read()方法读取此url数据，并存储到变量html中;
        使用正则表达式的findall()方法，对网站进行匹配，并将返回的网站添加到队列queque中；
        将此网站内容及网站地址存放在字典storage；
    当发生错误时:
        打印发成错误的网站地址 url
        打印错误信息
'''
import urllib, re
count = 10
r = re.compile(r'href=[\'"]?(http[^\'" >]+)')
seed = "http://webcrawler.cookdata.cn/httpbin/" # 这是一个神奇的网站，专门为爬虫练习而生
queue = [seed]
storage = {}
while len(queue) > 0 and count > 0:
    try:
        url = queue.pop(0)
        html = urllib.request.urlopen(url).read(text)
        news_urls = r.findall(html)
        queue.extend(news_urls)
        storage[url] = len(news_urls)
        count -= 1
    except Exception as e:
        print(url)
        print(e)
