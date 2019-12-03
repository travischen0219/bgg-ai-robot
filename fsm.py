from transitions.extensions import GraphMachine

from utils import send_text_message


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
        send_text_message(reply_token, "謝謝媽媽 媽媽真好")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "嬤嬤我想吃烤山藥")
        ///////////////////////////////////////////////////
        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
        title = "國立臺灣科技大學"
        address = "106台北市大安區基隆路四段43號"
        latitude = 25.0136906
        longitude = 121.5406792
        try:
            line_bot_api.push_message(to, LocationSendMessage(title=title,address=address,latitude=latitude,longitude=longitude))
        except LineBotApiError as e:
            # error handle
            raise e
        ///////////////////////////////////////////////////
        self.go_back()


    def on_exit_state2(self):
        print("Leaving state2")
