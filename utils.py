import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, URITemplateAction, PostbackTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text, imgurl):
    line_bot_api = LineBotApi(channel_access_token)
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text=text,
            thumbnail_image_url=imgurl,
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='玫瑰瞳鈴眼第51集',
                    uri='https://www.youtube.com/watch?v=alD7ixZQKso'
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
