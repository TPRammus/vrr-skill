from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
from .VRRRequester import VRRRequester

#https://mycroft.ai/documentation/skills/introduction-developing-skills/


class Vrr(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.requester=VRRRequester()
        
    #handles how can i get {to} request,
    #assuming VRRRRequester.home is already set
    @intent_file_handler('to.intent')
    def handle_smallquery(self,message):
        b = message.data.get("b")
        if self.requester.hasHome() :
            #home is set, return route from home
            query_response=self.requester.originToDestination(self.requester.home,b)
            self.speak(query_response)
        else:
            #home is not set, request home address
            #TODO
            myhome=self.get_response('gethome.intent')
            
            
        
    #handles how can i get {from} {to} request
    @intent_file_handler('how.intent')
    def handle_query(self,message):
        a = message.data.get("a")
        b = message.data.get("b")
        query_response = self.requester.originToDestination(a,b)
        self.speak(query_response)
        

    @intent_file_handler('vrr.intent')
    def handle_vrr(self, message):
        self.speak_dialog('vrr')


def create_skill():
    return Vrr()

