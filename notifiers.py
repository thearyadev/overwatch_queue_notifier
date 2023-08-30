from utils.notify import Notify


class Discord(Notify):
    def send(self, message):
        print(message)
        return True


class Telegram(Notify):
    def send(self, message):
        print(message)
        return True


class Slack(Notify):
    def send(self, message):
        print(message)
        return True


class Email(Notify):
    def send(self, message):
        print(message)
        return True


class Twilio(Notify):
    def send(self, message):
        print(message)
        return True
