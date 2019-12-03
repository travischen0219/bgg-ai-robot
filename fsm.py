from transitions.extensions import GraphMachine

from utils import send_text_messagefrom linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = "YOUR CHANNEL TOKEN"
to = "YOUR USER ID"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

#文字訊息

try:
    line_bot_api.push_message(to, TextSendMessage(text='台科大電腦研習社'))
except LineBotApiError as e:
    # error handle
    raise e

#圖片訊息
# ImageSendMessage物件中的輸入
# original_content_url 以及 preview_image_url都要寫才不會報錯。
#輸入的網址要是一個圖片，應該說只能是一個圖片，不然不會報錯但是傳過去是灰色不能用的圖
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
image_url = "https://i.imgur.com/eTldj2E.png?1"
try:
    line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
except LineBotApiError as e:
    # error handle
    raise e


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
