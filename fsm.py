from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "重新來過" or text.lower() == "我要成為下個女活佛" or text.lower() =="開始"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "是" or text.lower() == "開始體驗"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "是" or text.lower() == "趁亂逃跑"

    def is_going_to_state4(self, event):
        text = event.message.text
        return text.lower() == "否" or text.lower() == "誠心的喝下符水" or text.lower() == "我不敢開始" or text.lower() == "把符水潑在麗美頭上" or text.lower() == "我還是留在原地好了" or text.lower() == "不相信" or text.lower() == "給麗美一巴掌下去"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() == "相信" or text.lower() == "明日再來"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() == "放棄吧 好麻煩喔" or text.lower() == "我不承認我有肝病"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "是" or text.lower() == "前往慈善會報名處"

    def is_going_to_state8(self, event):
        text = event.message.text
        return text.lower() == "否" or text.lower() == "直接秘密潛入"

    def is_going_to_state9(self, event):
        text = event.message.text
        return text.lower() == "不捐錢" or text.lower() == "摸摸口袋表示沒錢" or text.lower() == "感覺氣氛好詭異 還是先離開好了"

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "誠心的奉上紅包一大包" or text.lower() == "加入戰局" or text.lower() == "下跪向佛祖懺悔" or text.lower() == "被無罪釋放"

    def is_going_to_state11(self, event):
        text = event.message.text
        return text.lower() == "念大悲咒試圖改善情況" or text.lower() == "向警方承認吸食安非他命"

    def is_going_to_state12(self, event):
        text = event.message.text

        return text.lower() == "對對對這就是我要的" or text.lower() == "真好 我也想加入戰局"

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "即刻開壇做法"

##########################################################

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        #send_text_message(reply_token, "是否開始體驗玫瑰瞳鈴眼第51集「鞭屍女活佛」？","民國八十年八月十二日宜蘭發生了一起驚悚的神祕案件。而這一切又似乎與慈善會的「女活佛」有關……",'https://i.imgur.com/ppE2R8X.png',"開始體驗","我不敢開始")
        movie(reply_token)
        
    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "妳是女主角麗芬，是否趁亂逃跑？","妳是女主角麗芬，因為一些陰錯陽差的緣故被慈善會的幫眾綁架，妳趁著歹徒們不注意的時候趁亂……",'https://i.imgur.com/NlA0o22.jpg',"趁亂逃跑","我還是留在原地好了")

    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "麗芬衝進警察局主張有人要追殺她，身為刑事組長你是否要相信她？","麗芬向刑事組長哭訴有人要殺害她。而正當組長詢問兇手究竟是誰時，麗芬卻說出是妹妹和手下聯合起來……",'https://i.imgur.com/A1MaIbC.jpg',"相信","不相信")

    def on_enter_state4(self, event):
        print("I'm entering state4")
        reply_token = event.reply_token
        send_text_message(reply_token, "凡夫俗子，注定六道輪迴！，施主是否從新開始？","你已經中了張麗美的詭計，落入六道輪迴、永不超生！","https://i.imgur.com/k0bFN4n.jpg","重新來過","我要成為下個女活佛")
        
    def on_enter_state5(self, event):
        print("I'm entering state5")
        reply_token = event.reply_token
        send_text_message(reply_token, "身為刑警的你是否要加入慈善會秘密調查？","為了解開這件詭譎的謎團，賴警官眉頭一皺，似乎決心隻身前往慈善會總壇探探口風……","https://i.imgur.com/l6arcRX.jpg","前往慈善會報名處","直接秘密潛入")

    def on_enter_state6(self, event):
        print("I'm entering state6")
        reply_token = event.reply_token
        send_text_message(reply_token, "果然是妖魔鬼怪附身，趕緊向佛祖認錯！","你已經被大量的妖魔鬼怪附身！趕緊喝下這杯特調符水並向佛祖誠心懺悔……","https://i.imgur.com/h9m1gcw.jpg","誠心的喝下符水","把符水潑在麗美頭上")
        
    def on_enter_state7(self, event):
        print("I'm entering state7")
        reply_token = event.reply_token
        send_text_message(reply_token, "慈善會今天不開門，是否改日再來呢？","當賴警官抵達慈善會總壇之後，應門的信徒竟然表示今天不招收新的會員……","https://i.imgur.com/rbkVgrM.jpg","明日再來","放棄吧 好麻煩喔")
        
    def on_enter_state8(self, event):
        print("I'm entering state8")
        reply_token = event.reply_token
        send_text_message(reply_token, "順利進入慈善會總壇，是否給佛祖紅包一大包？","聽說今天佛祖要開壇作法，大批的信眾蜂擁而入、紛紛獻上紅包一大包……","https://i.imgur.com/xRxjukx.jpg","摸摸口袋表示沒錢","誠心的奉上紅包一大包")
        
    def on_enter_state9(self, event):
        print("I'm entering state9")
        reply_token = event.reply_token
        send_text_message(reply_token, "面色乾黃，肝有問題！佛祖趕緊用粗木棒逼出你體內的妖魔！","佛祖見你的臉色枯黃肌瘦，只好拿出比寶特瓶還粗的木棒給你一記當頭棒喝……","https://i.imgur.com/nm3Rc01.jpg","我不承認我有肝病","下跪向佛祖懺悔")
        
    def on_enter_state10(self, event):
        print("I'm entering state10")
        reply_token = event.reply_token
        send_text_message(reply_token, "女活佛收下信徒們供奉的紅包後，嘴中喃喃自語……","女活佛收到紅包後看起來相當滿意，她決定等等開始開壇做法……","https://i.imgur.com/AfARYkz.jpg","即刻開壇做法","感覺氣氛好詭異 還是先離開好了")

    def on_enter_state11(self, event):
        print("I'm entering state11")
        reply_token = event.reply_token
        send_text_message(reply_token, "結局實在令人費解！","麗美在隔離偵訊當中突然對著空中大笑，任憑警方如何拷問始終得不到答案……","https://i.imgur.com/1nFbttH.jpg","重新來過","給麗美一巴掌下去")
        

    def on_enter_state12(self, event):
        print("I'm entering state12")
        reply_token = event.reply_token
        send_text_message(reply_token, "將女活佛帶回警局隔離偵訊","賴警官見狀趕緊對空鳴槍、阻止女活佛繼續殺人，並且將她扭送法辦！","https://i.imgur.com/zmVOjK4.jpg","念大悲咒試圖改善情況","向警方承認吸食安非他命")
        
    def on_enter_state13(self, event):
        print("I'm entering state13")
        reply_token = event.reply_token
        send_text_message(reply_token, "女活佛在做法的現場打死人，手中的木棍一鞭重過一鞭……","麗美眼神中帶著強烈的殺氣，完全不像是佛祖在世那般的慈悲為懷……","https://i.imgur.com/XjEFkg2.jpg","對對對這就是我要的","真好 我也想加入戰局")
        
