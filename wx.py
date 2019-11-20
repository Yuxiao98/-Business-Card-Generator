from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()

def send_news():
    try:
        my_friend = bot.friends().search(u'5P5')[0]
        my_friend.send(u"Hi")
        # 每86400秒（1天），发送1次
        t = Timer(86400, send_news)
        t.start()
    except:

        # 你的微信名称，不是微信帐号。

        my_friend = bot.friends().search('箫洒哥')[0]
        my_friend.send(u"今天消息发送失败了")

if __name__ == "__main__":
    send_news()
