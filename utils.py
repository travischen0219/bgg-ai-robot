import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, Tem plateSendMessage, ButtonsTemplate, MessageTemplateAction, URITemplateAction, PostbackTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, title, text, imgurl,option1,option2):
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    line_bot_api = LineBotApi(channel_access_token)
    
    buttons_template = TemplateSendMessage(
        alt_text='請到聊天視窗中確認訊息',
        template=ButtonsTemplate(
            title = title,
            text = text,
            thumbnail_image_url = imgurl,

            actions=[
                if expression:option1
                    MessageTemplateAction(
                        label=option1,
                        text=option1
                    ),
                if expression:option2
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

    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
