import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, URITemplateAction, PostbackTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    #line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text=text,
            thumbnail_image_url='顯示在開頭的大圖片網址',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='影片網址'
                ),
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='postback1'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
