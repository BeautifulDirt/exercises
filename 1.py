from abc import ABCMeta, abstractmethod
import re

class Connection():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, ip, login, password):
        self.ip = ip
        self.login = login
        self.password = password

    @abstractmethod
    def valid_ip(self):
        self.__regex_num = re.compile('^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\:([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5]))?$') 
        self.__m = self.__regex_num.match(self.ip)
        if self.__m is not None:
            return self.ip
        else:
            return "ip not valid"

    @abstractmethod
    def valid_password(self):
        if (len(self.password) > 7) and (len(self.password) < 16):
            return self.password
        else:
            return "password not valid"
        
class Telnet(Connection):

    def connection(self):
        return "connection to telnet " + self.valid_ip()

    def close_connection(self):
        return "close connection to telnet " + self.valid_ip()

    def send_command(self):
        return "send a command to telnet " + self.valid_ip()

    def get_printout(self):
        return "printout to telnet " + self.valid_ip()

class SSL(Connection):

    def connection(self):
        return "open ssl " + self.valid_ip()

    def close_connection(self):
        return "close ssl " + self.valid_ip()

    def send_command(self):
        return "send a command to ssl " + self.valid_ip()

    def get_printout(self):
        return "printout to ssl " + self.valid_ip()

if __name__ == '__main__':
    a = Telnet(ip='10.1.1.1', login='admin', password='12345679')
    b = SSL(ip='10.1.1.1', login='admin', password='12345679')

    print(a.connection())
    print(b.connection())