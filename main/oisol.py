import std.basic
class OISOLError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
    def logger(self):
        print('[Error] [Unixtime: {}] {}'.format(std.basic.getUnixtime(),self.msg))

class version:
    def __init__(self,num1,num2,num3) -> None:
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def __len__(self):
        return len(self.num1) + len(self.num2) + len(self.num3)
    
    def __repr__(self):
        try:
            print(self.num1 + self.num2 + self.num3)
        except:
            raise RuntimeError
        
class OISOL:
    def __init__(self,version,filename) -> None:
        self.version = version
        self.filename = filename
    
    def getOisolSTD() -> version:
        ver = version('0','2','3')
        return ver

