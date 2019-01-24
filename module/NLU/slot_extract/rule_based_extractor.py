import re
class RuleBaseExtrator(object):
    def __init__(self):
        self.__noodle_type=['豌豆杂酱面','红烧牛肉面','肥肠面','素面']
        self.__noodle_taste=['变态辣','中辣','微辣','不辣']
        self.__noodle_number=['1','2','3','4']

    def __extract_type(self,text):
        noodle_type=[c_type for c_type in self.__noodle_type if c_type in text]
        c_type=noodle_type[0] if len(noodle_type)>0 else ''
        return c_type

    def __extract_taste(self,text):
        noodle_taste=[c_taste for c_taste in self.__noodle_taste if c_taste in text]
        taste=noodle_taste[0] if len(noodle_taste)>0 else ''
        return taste

    def __extract_number(self,text):
        pattern=re.compile('\d+|[一二三四五六七八九]')
        res=re.findall(pattern,text)
        if len(res)==1:
            return str(res)
        else:
            return ''

    def execute(self,text):
        slot={'TYPE':self.__extract_type(text),'TASTE':self.__extract_taste(text),'NUMBER':self.__extract_number(text)}
        return slot
