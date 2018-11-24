from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
from .VRRRequester import VRRRequester

#https://mycroft.ai/documentation/skills/introduction-developing-skills/


class Vrr(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        self.requester=VRRRequester()
        
    #handles how can i get {to} request,
    #assuming VRRRRequester.home is already set
    
    @intent_file_handler('to.intent')
    def handle_smallquery(self,message):
        b = message.data.get("b")
        if self.requester.hasAHome() :
            #home is set, return route from home
            query_response=self.requester.originToDestination(self.requester.home,b)
            self.speak(query_response)
        else:
            #home is not set, request home address
            self.speak('where do you live')
            
    @intent_file_handler('gethome.intent')
    def handle_get_street(self,message):
        #todo make more flexible
        street = message.data.get('street')
        success = self.requester.setHome(street)
        if not (success == null):
            self.speak('no such station '+street)
        else:
            self.speak('set home to '+street)
        
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

