from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder

#https://mycroft.ai/documentation/skills/introduction-developing-skills/


class Vrr(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
        
    @intent_file_handler('how.intent')
    def handle_query(self,message):
        a = message.data.get("a")
        b = message.data.get("b")
        self.speak(' say public transit from '+a+' to '+b)
        

    @intent_file_handler('vrr.intent')
    def handle_vrr(self, message):
        self.speak_dialog('vrr')


def create_skill():
    return Vrr()

