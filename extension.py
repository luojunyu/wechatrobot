#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,requests, json, chatcore, io, time, random, re, ConfigParser, os
from config import *
from utils import *
from scrapy import *
from chatcore import *
import random
reload(sys)
sys.setdefaultencoding("utf-8")
lastSequenceId = ''
def auto_reply(msg, uid):
    if TULING_KEY:
        url = "http://www.tuling123.com/openapi/api"
        user_id = uid.replace('@', '')[:30]
        body = {'key': TULING_KEY, 'info': msg.encode('utf8'), 'userid': user_id}
        r = requests.post(url, data = body)
        respond = json.loads(r.text)
        result = ''
        code = respond['code']
        text = respond['text']
        if code == 100000: # TEXT
            result = text

        elif code == 200000: # URL
            result = text + '\n' + respond['url']
        elif code == 302000: # News list
            for item in respond['list']:
                result += u'【'+ item['source'] + u'】' + item['article'] + '\n' + item['detailurl'] + '\n\n'
        elif code == 308000: # Cook menu
            for item in respond['list']:
                result += u'【'+ item['name'] + u'】' + item['info'] + '\n' + item['detailurl'] + '\n\n'
        return result
    else:
        return u'我知道啦'

## return: if True consume this action.
def process_command(content, from_user_id, from_user_name):
    isAdmin = (from_user_name == ADMIN_NAME)
    content = content.lstrip()

    # Face emoji
    if re.match('\[\S+\]\Z', content):
        chatcore.send(content, from_user_id)
        return True

    #预约一起打篮球
    if u'打球' in content or u'篮球' in content or  u'球场' in content or u'篮球场' in content:
        msg = u'走，一起去篮球场打篮球吧：\n' + getDate() + u"\n\n【人员如下】：\n"
        position = 0
        for member in getMembers():
            position = position + 1
            msg = msg + str(position) + ". " + member + "\n"
        msg = msg + u"\n你可以@我跟我说‘报名’就可以预约一起打篮球啦~"
        chatcore.send(msg, from_user_id)
        return True

    if u'报名' in content or u'想来' in content:
        chatcore.send(addMember(from_user_name), from_user_id)
        return True


    if u'不报名' in content or u'不想来' in content:
        chatcore.send(u'好吧大佬', from_user_id)
        return True

    #发送图片
    if u'狗狗的图片' in content or u'狗狗图片' in content:
        i = random.randint(1,5)
        img='dog'+ str(i) +'.jpg'
        adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/dog/'+img
        send_image(adr, from_user_id)
        chatcore.send(u'我养的狗狗可爱么，嘻嘻ლ(＾ω＾ლ)[Shy]', from_user_id)
        return True

    if u'猫咪' in content or u'猫咪图片' in content:
        i = random.randint(1,10)
        img='cat'+ str(i) +'.jpg'
        adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/cat/'+img
        chatcore.send_image(adr, from_user_id)
        chatcore.send(u'我养的猫咪可爱么，嘻嘻ლ(＾ω＾ლ)[Shy]', from_user_id)
        return True

    if u'你的照片' in content or u'你的自拍' in content:
        i = random.randint(1,10)
        img='myself'+ str(i) +'.jpg'
        adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/myself/'+img
        chatcore.send_image(adr, from_user_id)
        chatcore.send(u'我不管，本宝宝最可爱，嘻嘻ლ(＾ω＾ლ)', from_user_id)
        return True

    if u'二哈图片' in content or u'二哈照片' in content or u'二哈表情' in content:
        j = random.randint(0,12)
        for i in range(j*10+1,j*10+11):
            img='erha('+ str(i) +').jpg'
            adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/erha/'+img
            chatcore.send_image(adr, from_user_id)
        return True

    if u'可爱表情包' in content :
        i = random.randint(1,102)
        img='xiaorener('+ str(i) +').jpg'
        adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/xiaorener/'+img
        chatcore.send_image(adr, from_user_id)
        return True

    if u'一堆可爱的表情' in content :
        j = random.randint(0,9)
        for i in range(j*10+1,j*10+11):
            img='xiaorener('+ str(i) +').jpg'
            adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/xiaorener/'+img
            chatcore.send_image(adr, from_user_id)
        return True

    if u'一打熊表情' in content :
        j = random.randint(0,6)
        for i in range(j*10+1,j*10+11):
            img='xiongbenxiong('+ str(i) +').jpg'
            adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/xiongbenxiong/'+img
            chatcore.send_image(adr, from_user_id)
        return True

    if u'测试集' in content :
        for i in range(18):
            img = 'test' + str(i) + '.jpg'
            adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/gooddata/'+img
            chatcore.send_image(adr, from_user_id)
        return True

    if u'熊本熊' in content :
        i = random.randint(1,67)
        img='xiongbenxiong('+ str(i) +').jpg'
        adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/xiongbenxiong/'+img
        chatcore.send_image(adr, from_user_id)
        return True


    if u'。。。' in content or u'...' in content or u'…' in content or u'哦' in content or u'嗯' in content or u'额' in content:
        i = random.randint(1,25)
        img='o('+ str(i) +').jpg'
        adr = 'C:/Users/Administrator/Desktop/wechatrobot-master/imagedata/o/'+img
        chatcore.send_image(adr, from_user_id)
        chatcore.send(u'这句我识别不了，所以没法接呢~嘻嘻[Hey]', from_user_id)
        return True

    #获取淘宝信息
    if u'我想买' in content or u'我要买' in content:
        send_image(img_spyder(content), from_user_id)
        chatcore.send(u'这家店铺是在'+ city_spyder(content) +u'的'+ nick_spyder(content) + '\n\n' +
                      u'价格是:'+ price_spyder(content) + u'元\n\n' +
                      u'运费是:' + fee_spyder(content) + u'元\n\n' +
                      u'评论人数是:' + str(comment_spyder(content))
                      , from_user_id)
        return True

    if u'谁最可爱' in content :
        chatcore.send(u'这个世界上当然是我最可爱啦', from_user_id)
        return True

    if u'谁最漂亮' in content:
        chatcore.send(u'我不知道，我只知道你 花容月貌 蕙心兰质 嫣然一笑 艳如桃李 涎玉沫珠 煦色韶光 沉鱼落雁 闭月羞花 国色天姿 回眸一笑 白媚众生 生不如死', from_user_id)
        return True

    if u'你觉得' in content:
        chatcore.send(u'我觉得你的美貌如沉鱼落雁 闭月羞花 国色天姿 回眸一笑 白媚众生 生不如死', from_user_id)
        return True

    if u'你爸' in content:
        chatcore.send(u'我爸爸是风流倜傥的罗爸爸', from_user_id)
        return True


    if u'加我加我' in content:
        chatcore.add_friend(from_user_id, verifyContent=u'嘻嘻，我可以添加你为好友吗？')
        chatcore.send(u'好的，我已经添加 ' + from_user_name + u' 为好友了', from_user_id)
        return True

    if u'自我介绍' in content or u'打个招呼' in content or 'help' in content:
        chatcore.send(GROUP_HELP, from_user_id)
        return True

    if u'Draw' in content or u'draw' in content:
        drawPic(content[4:])
        chatcore.send_image(fileDir='assets/draw_pic.png', toUserName=from_user_id)
        return True

    if u'小黄图' in content or u'小黄片' in content:
        for url in SEX_PIC_URL:
            send_image(url, from_user_id)
        return True

    if u'[Alarm]' in content or u'提醒我' in content:
        time = content[content.index(u'提醒我') + 3:]
        chatcore.send(u'好的爸爸，已经帮你开启: ' + time, from_user_id)
        return True

    if u'头像' in content:
        chatcore.send_image(chatcore.get_head_img(chatroomUserName=from_user_id), from_user_id)
        return True

    if u'群信息' in content or u'群成员' in content:
        reply = ''
        group_info = chatcore.update_chatroom(from_user_id)
        chat_room_owner_id = group_info['ChatRoomOwner']
        chatRoomOwnerName = ''
        memberList = group_info['MemberList']
        if group_info['NickName']:
            reply += u'群名称：' + group_info['NickName'] + u'\n----------------\n群成员：(' + str(len(memberList)) +')\n'
        for member in memberList:
            if chat_room_owner_id == member['UserName']:
                chatRoomOwnerName = member['NickName']
            reply += member['NickName'] + u'\n'
        reply += u'----------------\n群主：' + chatRoomOwnerName
        chatcore.send(reply, from_user_id)
        return True

    ## Administrator command

    if u'妹子' in content:
        if isAdmin:
            data = scrapy_av()
            random_item = random.randrange(0, len(data)-1)
            send_image('http://mvpday.com' + data[random_item][1], from_user_id)
            chatcore.send(u'这个妹子是：' + data[random_item][0], from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True
# View friends list
    if u'Search' in content:
        if isAdmin:
            keyword = content[content.index(u'Search') + 6:]
            result = ''
            search_result = chatcore.search_friends(name = keyword)
            if isinstance(search_result, list):
                for item in search_result:
                    result += jsonify(item) + '\n'
            elif isinstance(search_result, dict):
                result += jsonify(search_result) + '\n'
            chatcore.send(u'没有搜索到结果' if result == '' else result, from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True



    if u'叫爸爸' in content or u'叫爸爸' in content:
        if isAdmin:
            chatcore.send(u'爸爸好~，爸爸有什么吩咐吗？', from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True
#Group sends a message
    if u'GroupSend' in content :
        if isAdmin:
            friends = chatcore.get_friends()
            group_send(friends, content[content.index(u'GroupSend') + 9:])
            chatcore.send(u'已经给 ' + str(len(friends)) + u' 位好友发送了消息' )
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True
#check the detail information about user
    if u'Info' == content:
        if isAdmin:
            chatcore.send(jsonify(chatcore.search_friends()), from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True

    if u'Friends' in content:
        if isAdmin:
            friends = chatcore.get_friends()
            friend_result = u'共计获取到 ' + str(len(friends)) + u' 位好友信息\n\n'
            for friend in friends:
                gender = u'男' if friend['Sex'] == 1 else u'女'
                friend_result += friend['NickName'] + ' ---- ' + friend['Alias'] + ' ---- ' + gender + '\n'
            chatcore.send(friend_result, from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True
    if u'每日福利' in content:
        if isAdmin:
            chatcore.send(u"嘻嘻~稍等", from_user_id)
            chatcore.send_video(u'assets/cat.mp4', from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True

    if u'开放权限' in content:
        if isAdmin:
            OPEN_AUTH = True
            chatcore.send(u"爸爸，权限已经开放啦~", from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True

    if u'关闭权限' in content:
        if isAdmin:
            OPEN_AUTH = False
            chatcore.send(u"爸爸，权限已经关闭了~", from_user_id)
        else:
            chatcore.send(u'这个指令爸爸说了不能给别人用哦~T_T', from_user_id)
        return True

    return False

def group_send(users, content):
    for user in users:
        chatcore.send(content, user['UserName'])

# Send image by URL
def send_image(url, from_user_id):
    r = requests.get(url, stream=True)
    imageStorage = io.BytesIO()
    for block in r.iter_content(1024):
        imageStorage.write(block)
    imageStorage.seek(0)
    chatcore.send_image(imageStorage, from_user_id)

# 获取加入打篮球的名单、成员、添加成员
def getDate():
    cf = ConfigParser.ConfigParser()
    cf.read("were.ini")
    return cf.get("configure", "date")

def getMembers():
    cf = ConfigParser.ConfigParser()
    cf.read("were.ini")
    return cf.get("configure", "member").encode('utf-8').split(",")

def addMember(name):
    cf = ConfigParser.ConfigParser()
    cf.read("were.ini")
    member = cf.get("configure", "member")
    if name in member.split(","):
        return u'大佬你不是已经报名了吗？'
    else:
        cf.set("configure", "member", member + "," + name.encode('utf-8'))
        writeConfig(cf);
        return u'@' + name + u' 已经用笔帮你记在小本本上啦~' + getDate() + u' 我们不见不散哦！'

def writeConfig(cf):
    with open("were.ini","w+") as f:
        cf.write(f)
