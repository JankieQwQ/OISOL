import std.basic
import std.formatprint
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

    def outputJavaScriptFile(filename):
        readFile = open(filename,'r')
        writeFile = open(filename,'w')
        rawText = readFile.readlines()
        print('- 开始编译，时间戳 {}'.format(std.basic.getUnixtime()))
        t = ''
        m = ''
        r = ''
        lines = rawText
        for line in lines:
            if line.startswith("#include"):
                included_file = line.split("<")[1].split(">")[0]
                with open(included_file, 'r') as inc_file:
                    r += inc_file.read() + '\n'
            else:
                t += line
        print(' - Import 文件完成')
        with open('/template/main.js', 'r') as f:
            m = str(f.read())

        r = m + '\n' + r + t
        print(' - 追加 Std Template 文件完成')
        writeFile.write(r)
        readFile.close()
        writeFile.close()
    