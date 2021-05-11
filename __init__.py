from mycroft import MycroftSkill, intent_file_handler


class RateOfPay(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pay.of.rate.intent')
    def handle_pay_of_rate(self, message):
        self.speak_dialog('pay.of.rate')


def create_skill():
    return RateOfPay()

