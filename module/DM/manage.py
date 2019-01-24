from copy import copy

from .state import *
class Manager(object):

    def __init__(self):
        self.state=State()

    def update_state(self,dialog_act):
        self.state.update(dialog_act)

    def select_action(self,dialog_act):
        system_act=copy(dialog_act)
        if not self.state.has('type'):
            system_act['sys_act_type']='REQUEST_TYPE'
        elif not self.state.has('taste'):
            system_act['sys_act_type']='REQUEST_TASTE'
        elif not self.state.has('number'):
            system_act['sys_act_type'] = 'REQUEST_NUMBER'
        else:
            noodle_type=self.state.get_type()
            noodle_taste = self.state.get_taste()
            noodle_number = self.state.get_number()

            system_act['noodle']={'type':noodle_type,'taste':noodle_taste,'number':noodle_number}
            system_act['sys_act_type']='INFORM_NOODLE'
            self.state.clear()

        return system_act
