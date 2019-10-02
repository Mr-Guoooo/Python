<<<<<<< HEAD
'''
    name:check.py
    Explian:
'''

def is_Zh(s):
    '检查给定字符串是否包含中文字符'
    for c in s:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False

def is_AllZh(s):
    '检查给定字符串是否是中文'
    for c in  s:
        if '\u4e00' <= c <= '\u9fa5':
            continue
        return False
    return True

def is_IP(ipAddr):
    '检查所给字符串是否为IP地址'
    import re
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:  
        return False

#def check_ip(ipAddr): 
#'检查所给字符串是否为IP'
#    import sys 
#    import os
#    addr=ipAddr.strip().split('.') #切割IP地址为一个列表 
#    #print addr 
#    if len(addr) != 4: #切割后列表必须有4个参数 
#        print "check ip address failed!"
#        sys.exit() 
#    for i in range(4): 
#        try: 
#            addr[i]=int(addr[i]) #每个参数必须为数字，否则校验失败 
#        except: 
#            print "check ip address failed!"
#            sys.exit() 
#        if addr[i]<=255 and addr[i]>=0:  #每个参数值必须在0-255之间 
#            pass
#        else: 
#            print "check ip address failed!"
#            sys.exit() 
#        i+=1
#    else: 
#        print "check ip address success!"
#if len(sys.argv)!=2: #传参加本身长度必须为2 
#    print "Example: %s 10.0.0.1 "%sys.argv[0] 
#    sys.exit() 
#else: 
#    check_ip(sys.argv[1]) #满足条件调用校验IP函数
# push test


=======
'''
    name:check.py
    Explian:
'''

def is_Zh(s):
    '检查给定字符串是否包含中文字符'
    for c in s:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False

def is_AllZh(s):
    '检查给定字符串是否是中文'
    for c in  s:
        if '\u4e00' <= c <= '\u9fa5':
            continue
        return False
    return True

def is_IP(ipAddr):
    '检查所给字符串是否为IP地址'
    import re
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:  
        return False
