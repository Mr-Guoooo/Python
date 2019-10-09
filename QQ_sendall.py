# -*- coding:utf-8 -*-
"""
Python QQ
Batch send QQ message to your friends
"""
from pyqq import QQ   class QQMessage():
    def __init__(self):
        qq_num = raw_input('Input QQ:')
        qq_pwd = raw_input('Input Password:')
        qq_msg = raw_input('Input Message:')
        #是否发送给所有好友
        all_friends = False
        <span id="more-147"></span>
        if qq_num == '' or qq_pwd == '' or qq_msg == '':
            return   qq_main = QQ(qq_num,qq_pwd)
        qq_main.login()   #获取好友列表
        if all_friends:
            friends_list = qq_main.get_all_friends()
        else:
            friends_list = qq_main.get_online_friends()
        #批量给所有好友发送信息
        for friend in friends_list:
            #检查是否发送成功
            send_status = qq_main.send(friend['uin'],qq_msg)
            if (send_status):
                print 'Message to'+ str(friend['uid'])   if __name__ == '__main__':
    QQMessage()