class State(object):

    def __init__(self):
        self.__state={'type':None,'taste':None,'number':None}

    def update(self,dialog_act):
        self.__state['type']=dialog_act.get('TYPE',self.__state['type'])
        self.__state['taste'] = dialog_act.get('TASTE', self.__state['taste'])
        self.__state['number'] = dialog_act.get('NUMBER', self.__state['number'])

    def has(self,name):
        return self.__state.get(name)!= None


    def clear(self):
        self.__init__()

    def has(self, name):
        return self.__state.get(name) != None

    # state map many get function
    def get_type(self):
        return self.__state['type']

    def get_taste(self):
        return self.__state['taste']

    def get_number(self):
        return self.__state['number']

    def __str__(self):
        import pprint
        return pprint.pformat(self.__state)