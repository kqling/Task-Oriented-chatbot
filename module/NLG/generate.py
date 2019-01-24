import sys
class NLG(object):
    def __init__(self):
        pass

    def generate_sentence(self,sys_act):
        sent=''

        system_act_type = sys_act['sys_act_type']
        if system_act_type == "REQUEST_TYPE":
            sent += "小孔面馆目前正在售卖肥肠面，红烧牛肉面，豌豆杂酱面，素面，请问您想点什么类型的面呢？"
        elif system_act_type == "REQUEST_TASTE":
            sent += "那要什么口味呢？我们有变态辣，中辣，微辣和不辣呢。"
        elif system_act_type == "REQUEST_NUMBER":
            sent += "您需要点几份呢？"
        elif system_act_type == "INFORM_NOODLE":
            noodle = sys_act['noodle']
            sent += "已经为你预订成功。\n\
            再次确认下你的订单：面类型{0}，{1}，{2}碗。\n 希望再次可以为您服务！".format(noodle['type'],
                                                                                  noodle['taste'],
                                                                                  noodle['number'])

        else:
            print("ERROR")
            sys.exit(1)

        return sent
