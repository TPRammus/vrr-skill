from mycroft import MycroftSkill, intent_file_handler


class Vrr(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vrr.intent')
    def handle_vrr(self, message):
        self.speak_dialog('vrr')


def create_skill():
    return Vrr()

