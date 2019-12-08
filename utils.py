import os
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, URITemplateAction, PostbackTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, title, text, imgurl, option1, option2):
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    line_bot_api = LineBotApi(channel_access_token)
    
    buttons_template = TemplateSendMessage(
        alt_text="請到聊天視窗中確認訊息！",
        template=ButtonsTemplate(
            title = title,
            text = text,
            thumbnail_image_url = imgurl,

            actions=[
                MessageTemplateAction(
                    label=option1,
                    text=option1
                ),
                MessageTemplateAction(
                    label=option2,
                    text=option2
                ),
                URITemplateAction(
                    label='立即觀看「玫瑰瞳鈴眼第51集」',
                    uri='https://www.youtube.com/watch?v=alD7ixZQKso'
                ),
            ]
        )
    )

    movie();
    line_bot_api.reply_message(reply_token, [buttons_template,content])

    return "OK"



def movie():
    target_url = 'https://www.ttv.com.tw/videocity/videolist.asp?sid=364/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('thumbnail a')):
        if index == 20:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)

    line_bot_api.reply_message(reply_token, content)
    return"OK"
    #return content

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
