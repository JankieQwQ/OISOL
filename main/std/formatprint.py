import basic

def error(message,code=-1) -> bool:
    print('[Error] [Unixtime: {}] {}'.format(basic.getUnixtime(),'Code: ' + str(code) + ',' + message))

def warn(message,code=-1) -> bool:
    print('[Warn] [Unixtime: {}] {}'.format(basic.getUnixtime(),'Code: ' + str(code) + ',' + message))

def info(message,code=-1) -> bool:
    print('[Info] [Unixtime: {}] {}'.format(basic.getUnixtime(),'Code: ' + str(code) + ',' + message))
