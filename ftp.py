import cmd
from ftpretty import ftpretty

class FTPApp(cmd.Cmd):
    def __init__(self):
        super().__init__()
        hostname = input("Enter hostname: ")
        try:
            port = int(input("Enter port"))
        except ValueError:
            print("Not a valid port.")
            self.__init__()
        username = input("Enter username: ")
        passwd = input("Enter password: ")
        connection_type = input("Are you connecting to an FTP(1) or FTPS(2) server? ")
        if connection_type not in ["1", "2"]:
            self.__init__()
        elif connection_type == "1":
            try:
                self.conn = ftpretty(host=hostname, port=port, user=username, password=passwd)
            except:
                print("Server isn't on or doesn't exist. Please try again.")
                self.__init__()
        else:
            try:
                self.conn = ftpretty(host=hostname, port=port, user=username, password=passwd, secure=True)
            except:
                print("Server isn't on or doesn't exist. Please try again.")
                self.__init__()
    def _confirm(self):
        if input("Are you sure? [Y/N]: ").lower() == "y":
            return True
        else:
            return False
    def do_cd(self, arg):
        try:
            self.conn.cd(arg)
        except Exception as e:
            print(str(e))
    def do_pwd(self, arg):
        print(self.conn.pwd())
    def do_nlst(self, arg):
        try:
            nlst_return = self.conn.conn.nlst(arg)
        except Exception as e:
            print(str(e))
        else:
            for name in nlst_return:
                print(name)
    def do_mlsd(self, arg):
        try:
            mlsd_return = self.conn.conn.nlst(arg)
        except Exception as e:
            print(str(e))
        else:
            for item in mlsd_return:
                print(item)
    def do_dir(self, arg):
        try:
            dir_return = self.conn.conn.dir(arg)
        except Exception as e:
            print(str(e))
        else:
            for item in dir_return:
                print(item)
    def do_put(self, arg):
        arg = arg.split(" ")
        source = arg[0]
        try:
            destination = arg[1]
        except IndexError:
            print("Format of put:\nput [local] [remote]")
        else:    
            self.conn.put(source, destination)
            print("Successfully uploaded file.")
    def do_puttree(self, arg):
        arg = arg.split(" ")
        source = arg[0]
        try:
            destination = arg[1]
        except IndexError:
            print("Format of put:\nputtree [local] [remote]")
        else:    
            self.conn.put_tree(source, destination)
            print("Successfully uploaded folder")
    def do_get(self, arg):
        arg = arg.split(" ")
        source = arg[0]
        try:
            destination = arg[1]
        except IndexError:
            print("Format of put:\nget [remote] [local]")
        else:    
            self.conn.get(source, destination)
            print("Successfully downloaded file")
    def do_gettree(self, arg):
        arg = arg.split(" ")
        source = arg[0]
        try:
            destination = arg[1]
        except IndexError:
            print("Format of put:\ngettree [remote] [local]")
        else:    
            self.conn.get_tree(source, destination)
            print("Successfully downloaded folder")
    def do_getwelcome(self, arg):
        print(self.conn.conn.getwelcome())
    def do_mkdir(self, arg):
        self.conn.mkdir(arg)
        print("Successfully created directory")
    def do_del(self, arg):
        try:
            if self._confirm():
                self.conn.delete(arg)
        except Exception as e:
            print(str(e))
    def do_rename(self, arg):
        arg: list = arg.split(" ")
        if len(arg) != 2:
            print("Format of rename:\nrename [toName] [fromName]")
        try:
            self.conn.rename(arg[0], arg[1])
        except Exception as e:
            print(str(e))
    def do_size(self, arg):
        try:
            self.conn.conn.size(arg)
        except Exception as e:
            print(str(e))
    def do_quit(self, arg):
        self.conn.close()

    