from ftplib import FTP, FTP_TLS
import cmd

class FTPConnect:
    def __init__(self):
        conn_type = input("Are you connecting to a regular FTP(1) server or an FTPS(2) server")
        if conn_type not in ["1", "2"]:
            self.__init__()
        elif conn_type == "1":
            self.conn = FTP()
        else:
            self.conn = FTP_TLS()
            self.conn.prot_p()
        host = input("Enter hostname: ")
        port = input("Enter port, default is 21: ")
        if not port:
            port = "21"
        try:
            port = int(port)
        except (ValueError, TypeError):
            self.__init__()
        try:
            self.conn.connect(host, port)
        except:
            print("Server is down or connection details are wrong. Try again.")
    def login(self):
        anonymous = input("Would you like to be anonymous? [Y/N]").lower()
        if anonymous not in ["y", "n"]:
            self.login()
        elif anonymous == "y":
            self.conn.login()
        else:
            user = input("Enter username: ")
            pswd = input("Enter password: ")
            self.conn.login(user, pswd)
    def interface(self):
        while True:
            command = input("Enter FTP keyword: ")
            try:
                self.conn.voidcmd(command)
            except Exception:
                try:
                    self.conn.retrlines(command)
                except Exception as e:
                    print(str(e))
