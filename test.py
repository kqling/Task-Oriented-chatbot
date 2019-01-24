from module.NLU.nlu  import *
from module.DM.manage import  *
from module.NLG.generate import  *

class Bot(object):
    def __init__(self):
        self.nlu=RuleBasedNLU()
        self.manager=Manager()
        self.generator=NLG()


    def reply(self,sent):
        dialog_act=self.nlu.execute(sent)
        self.manager.update_state(dialog_act)
        sys_act=self.manager.select_action(dialog_act)
        print(self.generator.generate_sentence(sys_act))










if __name__=="__main__":
    bot=Bot()
    print('您好，这里是小孔面馆，很高兴为您服务.')
    while True:
        sent=input('用户请输入:')
        if sent=='好的' or sent=='谢谢':
            break
        elif '不需要了' in sent:
            print('好的呢，欢迎您下次光临')
            break
        else:
            bot.reply(sent)





