from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "重新來過"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "是"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "是"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "否" or text.lower() == "認錯"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "相信" or text.lower() == "明日再來"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "放棄" or text.lower() == "不承認"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "是"

    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "否"

    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "不捐錢"

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "奉上紅包" or text.lower() == "加入戰局" or text.lower() == "下跪認錯" or text.lower() == "被無罪釋放"

    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "念經"

    def is_going_to_state12(self, event):
        text = event.message.text
        return text.lower() == "現行犯"

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "開壇作法"

##########################################################

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "玫瑰瞳鈴眼第51集「鞭屍女活佛」","民國八十年八月十二日宜蘭地區發生了一起拍案叫絕的神祕案件。而這一切似乎都與慈善會的「女活佛」有關……",'https://i.imgur.com/ppE2R8X.png')

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "妳是女主角麗芬，是否趁亂逃跑?","妳是女主角麗芬，因為一些陰錯陽差的緣故被慈善會的幫眾綁架，妳趁著歹徒們不注意的時候趁亂……",'https://i.imgur.com/NlA0o22.jpg')

    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "麗芬衝進警察局主張有人要追殺她，身為刑事組長的你是否要相信她?","麗芬慌慌張張的衝進最近的警察局，向刑事組長哭訴有人要殺害她。而正當組長詢問兇手究竟是誰時，麗芬卻說出是妹妹和手下聯合起來……",'https://i.imgur.com/A1MaIbC.jpg')

    def on_enter_state4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        send_text_message(reply_token, "凡夫俗子，注定六道輪迴！")
        
    def on_enter_state5(self, event):
        print("I'm entering state5")
        reply_token = event.reply_token
        send_text_message(reply_token, "刑警是否加入慈善會調查秘密?")

    def on_enter_state6(self, event):
        print("I'm entering state6")
        reply_token = event.reply_token
        send_text_message(reply_token, "果然是妖魔鬼怪附身！")
        
    def on_enter_state7(self, event):
        print("I'm entering state7")
        reply_token = event.reply_token
        send_text_message(reply_token, "慈善會今天不開門！")
        
    def on_enter_state8(self, event):
        print("I'm entering state8")
        reply_token = event.reply_token
        send_text_message(reply_token, "順利進入慈善會總壇！")
        
    def on_enter_state9(self, event):
        print("I'm entering state9")
        reply_token = event.reply_token
        send_text_message(reply_token, "面色乾黃，肝有問題！")
        
    def on_enter_state10(self, event):
        print("I'm entering state10")
        reply_token = event.reply_token
        send_text_message(reply_token, "女活佛看起來相當滿意！")

    def on_enter_state11(self, event):
        print("I'm entering state11")
        reply_token = event.reply_token
        send_text_message(reply_token, "結局實在令人費解！")
        
    def on_enter_state12(self, event):
        print("I'm entering state12")
        reply_token = event.reply_token
        send_text_message(reply_token, "隔離偵訊")
        
    def on_enter_state13(self, event):
        print("I'm entering state13")
        reply_token = event.reply_token
        send_text_message(reply_token, "當場打死人")
        
