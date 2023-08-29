from utils.notify import Notify


class GenericNotifyTestClass(Notify):
    def send(self, message):
        print(message)
        return True
