# -*- coding: utf-8 -*-
from Goperation.linepy import *
from Goperation.akad import *
from time import sleep
from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup
from Liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, wikipedia, subprocess, errno
with open('token.json', 'r') as fp:
    connecting = json.load(fp)
if connecting['token'] == "":
     client = LINE("panutchakorn_2533@hotmail.com","takumi2533")
else:
    client=LINE(authToken=connecting['token'])
with open('cctv.json', 'r') as fp:
    cctv = json.load(fp)
with open('admin.json', 'r') as fp:
    manage = json.load(fp)
print("#=================[ W E L C O M E   T O  G - O P E R A T I O N ]======================#")
client.log("YOUR TOKEN : {}".format(str(client.authToken)))
print("#=================[ W E L C O M E   T O  G - O P E R A T I O N ]======================#")
clientMid = client.profile.mid
clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = OEPoll(client)
botStart = time.time()
msg_dict = {}
msg_send = {}
lcol = "#800000"
tcol = "#ffffff"
settings = {
    "setKey": False,
    "ChangeVideoProfile": False,
    "ChangeVideoProfile2": False,
    "changePictureProfile": False,
    "changeGroupPicture": {}
}

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def cTime_to_datetime(unixtime):
    tz = pytz.timezone("Asia/Bangkok")
    timeNow = datetime.now(tz=tz)
    return datetime.fromtimestamp(str(timeNow))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Hours %02d Minute %02d Secs' % (hours, mins, secs)
def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time
def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': client.authToken,
        'X-Line-Application': client.server.APP_NAME,
        'X-Line-ChannelId': '1602876096',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

def sendOpera(to, profile):
    try:
        goperation = "https://obs.line-scdn.net/" + profile.pictureStatus
    except:
    	goperation = "https://obs.line-scdn.net/0hP_lfR1H3D3BRHyeUYWFwJ21aAR0mMQk4KSsXRX0bVxQoLRwgOH5FFnQeURAoJ0khbXhGEndLVBV6"
    opera1 = {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "md",
        "aspectMode": "cover",
        "aspectRatio": "1.30:1.26",
        "url": goperation,
        "position": "absolute",
        "align": "center",
        "offsetTop": "8px",
        "offsetStart": "2px",
        "action": {
          "type": "uri",
          "uri": goperation
        }
      },
      {
        "type": "image",
        "aspectMode": "cover",
        "aspectRatio": "2.40:2.10",
        "offsetTop": "0px",
        "offsetBottom": "0.5px",
        "offsetStart": "2px",
        "offsetEnd": "2px",
        "size": "full",
        "gravity": "top",
        "url": "https://i.ibb.co/cJqyvG1/20200507-224553.png"
      }
    ],
    "paddingAll": "0px",
    "spacing": "none",
    "backgroundColor": "#000000",
    "height": "245px",
    "width": "260px"
  },
  "action": {
    "type": "uri",
    "uri": "https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html?m=1" #jangan di hapus
  }
  }
    opera2 = {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "md",
        "aspectMode": "cover",
        "aspectRatio": "1.30:1.26",
        "url": goperation,
        "position": "absolute",
        "align": "center",
        "offsetTop": "8px",
        "offsetStart": "2px",
        "action": {
          "type": "uri",
          "uri": goperation
        }
      },
      {
        "type": "image",
        "aspectMode": "cover",
        "aspectRatio": "2.40:2.10",
        "offsetTop": "0px",
        "offsetBottom": "0.5px",
        "offsetStart": "2px",
        "offsetEnd": "2px",
        "size": "full",
        "gravity": "top",
        "url": "https://i.ibb.co/LRjXWjN/20200507-225055.png"
      }
    ],
    "paddingAll": "0px",
    "spacing": "none",
    "backgroundColor": "#000000",
    "height": "245px",
    "width": "260px"
  },
  "action": {
    "type": "uri",
    "uri": "https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html?m=1" #jangandihapus
  }
}

    opera3 = {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "md",
        "aspectMode": "cover",
        "aspectRatio": "1.30:1.26",
        "url": goperation,
        "position": "absolute",
        "align": "center",
        "offsetTop": "8px",
        "offsetStart": "2px",
        "action": {
          "type": "uri",
          "uri": goperation
        }
      },
      {
        "type": "image",
        "aspectMode": "cover",
        "aspectRatio": "2.40:2.10",
        "offsetTop": "0px",
        "offsetBottom": "0.5px",
        "offsetStart": "2px",
        "offsetEnd": "2px",
        "size": "full",
        "gravity": "top",
        "url": "https://i.ibb.co/98f2Qcy/20200507-224745.png"
      }
    ],
    "paddingAll": "0px",
    "spacing": "none",
    "backgroundColor": "#000000",
    "height": "245px",
    "width": "260px"
  },
  "action": {
    "type": "uri",
    "uri": "https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html?m=1"#jangandihapus
  }
}
    opera = [opera1,opera2,opera3]
    senorita = {"type": "flex","altText": "The SKT - Operation","contents": {"type": "carousel","contents": opera}}
    client.sendTemp(to,senorita)

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Angopera "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def clientBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 55:
            try:
                print ("[ 55 ] READ MESSAGE")
                if op.param1 in cctv['Point']:
                    if op.param2 not in cctv['Point3'][op.param1]:
                       try:uprofile = "https://obs.line-scdn.net/" + client.getContact(op.param2).pictureStatus
                       except:uprofile = "https://imagizer.imageshack.com/v2/377x338q90/922/Z9ocJr.jpg"
                       Minum = client.getContact(op.param2).displayName
                       reading = {"type": "flex","altText": "Kesayangan membaca obrolan.","contents":{"type": "carousel","contents": [{"type": "bubble","size": "nano","body": {"type": "box","layout": "vertical","contents": [{"type": "image","url": uprofile,"size": "full","aspectMode": "cover","aspectRatio": "2:2.70","gravity": "top"},{"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "text","text": "• " + Minum,"size": "xs","color": "#ffffff","weight": "bold","offsetBottom": "2px","offsetTop": "1px","offsetStart": "-1px","wrap": False,"align": "start"}],"position": "relative"},{"type": "text","text": "Hello,","size": "xs","weight": "bold","maxLines": 20,"align": "start","position": "absolute","offsetTop": "0px","offsetBottom":"-5px","gravity": "top","offsetStart": "3px","color": "#F10202"}],"position": "absolute","offsetBottom": "0px","offsetStart": "0px","offsetEnd": "0px","paddingAll": "16px","paddingTop": "12px","backgroundColor": "#000000"},{"type": "box","layout": "vertical","contents": [{"type": "text","text": "Reader","color": "#ffffff","align": "center","size": "xxs","offsetTop": "0px"}],"position": "absolute","cornerRadius": "20px","offsetTop": "8px","backgroundColor": "#ff334b","offsetStart": "7px","height": "15px","width": "40px"}],"paddingAll": "0px","offsetTop": "0px","offsetBottom": "20px","position": "relative"}}]}}
                       client.sendTemp(op.param1,reading)
                       cctv['Point3'][op.param1][op.param2] = True
                       with open('cctv.json', 'w') as fp:
                           json.dump(cctv, fp, sort_keys=True, indent=4)
                    else:
                    	pass
                else:
                    pass
            except Exception as error:client.sendMessage(msg.to, "{}".format(str(error)))

        if op.type == 55:
            try:
                if op.param1 in cctv['readPoint']:
                    if op.param2 in cctv['readMember'][op.param1]:
                        pass
                    else:
                        cctv['readMember'][op.param1] += op.param2
                        cctv['ROM'][op.param1][op.param2] = op.param2
                        with open('cctv.json', 'w') as fp:
                            json.dump(cctv, fp, sort_keys=True, indent=4)
                else:
                   pass
            except:
                pass


        if op.type == 25:
            try:
                msg = op.message
                msg = msg
                ang = msg.text
                msg_id = msg.id
                if msg.toType == 0 or msg.toType == 2:
                 if msg.contentType == 2:
                    if settings['ChangeVideoProfile'] == True:
                        client.downloadObjectMsg(msg.id,'path','video.mp4')
                        print('[NOTIF] VIDEO PROFILE PROCESSING')
                        client.sendMessage(msg.to, "Send picture to be profiled")
                        settings['ChangeVideoProfile']=False
                        settings['ChangeVideoProfile2']=True
                 if msg.contentType == 1:
                    if settings['ChangeVideoProfile2'] == True:
                       client.downloadObjectMsg(msg.id,'path','foto.jpg')
                       client.updateProfileVideoPicture('video.mp4','foto.jpg')
                       print('[NOTIF] UPDATE PROFILE VIDEO SUCCES')
                       client.sendMessage(msg.to, 'Success change profile video.')
                       client.deleteFile('path')
                       settings['ChangeVideoProfile2']=False
                    if settings["changePictureProfile"] == True:
                       path = client.downloadObjectMsg(msg_id)
                       settings["changePictureProfile"] = False
                       client.updateProfilePicture(path)
                       client.deleteFile(path)
                       client.sendMessage(msg.to, "Profile image updated.")
                    if msg.to in settings["changeGroupPicture"]:
                       path = client.downloadObjectMsg(msg_id)
                       del settings["changeGroupPicture"][msg.to]
                       client.updateGroupPicture(msg.to, path)
                       client.deleteFile(path)
                       client.sendMessage(msg.to, "Group image updated.")
            except Exception as error:
                client.sendMessage(msg.to, "{}".format(str(error)))
                traceback.print_tb(error.__traceback__)


        if op.type == 25:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                ang = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 2:
                 if msg.contentType == 0:
                    if ang is None:
                    	pass
                    else:
                        if ang.lower() == ".help":
                           profile = client.getContact(clientMid)
                           threading.Thread(target=sendOpera, args=(msg.to,profile)).start()
                        if ang.lower() == "help":
                           tolol = "Gunakan awalan「. 」\nContoh .help"
                           goblok = "Gunakan awalan「. 」\nContoh .help\nJika bot tidak respon,\nsilahkan ketik '.allowliff'"
                           try:
                              data = {"type": "flex","altText": "SKT-OPERA SELFBOT","contents": {"styles": {"body": {"backgroundColor": "#D34C09"}},"type": "bubble","body": {"contents": [{"contents": [{"contents": [{"text": "{}".format(goblok) ,"size": "md","margin": "none","color": "#FFFFFF","wrap": True,"weight": "regular","type": "text"}],"type": "box","layout": "baseline"}],"type": "box","layout": "vertical"}],"type": "box","spacing": "md","layout": "vertical"}}}
                           except:
                              client.sendReply(msg.id,msg.to,"{}".format(tolol))
                        if ang.lower() == ".me":
                            client.sendContact(msg.to,clientMid)
                        if ang.lower() == ".lurk" or ang.lower() == ".sider" or ang.lower() == ".kick" or ang.lower() == ".invite" or ang.lower() == ".updatename: " or ang.lower() == ".groupname:" or ang.lower() == ".updatebio:":
                            client.sendReplyMessage(msg.id,msg.to,"📌กรุณาดู คำสั่งได้ที่ .help")
                        if ang.lower() == ".reboot":
                            client.sendMessage(msg.to, "Bot Rebooting..")
                            restartBot()
                        if ang.lower() == ".sp" or ang.lower() == ".speed":
                             japri = time.time()
                             client.getProfile()
                             timing = time.time()
                             ngegas = japri - timing
                             client.sendMessage(msg.to, "📌ความเร็ว: %.5f"%ngegas)
                        if ang.lower() == ".runtime":
                           kopi = time.time() - botStart
                           ang = "𝙎𝙆𝙏 𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙧𝙪𝙣𝙣𝙞𝙣𝙜 𝙛𝙤𝙧:\n"+waktu(kopi)
                           client.sendMessage(msg.to,ang)
                        if ang.lower() == ".allowliff":
                            try:
                                allowLiff()
                                client.sendReplyMessage(msg.id, msg.to,"Flex mode enabled")
                            except:
                            	client.sendMessage(msg.to,"Click and verify to use fiture  template.\nhttps://liff.line.me/1602876096-e9QWgjyo")
                        if ang.lower() == ".updatedual":
                           settings['ChangeVideoProfile']=True
                           client.sendMessage(msg.to, "Please send video.")
                        if ang.lower() == ".updatepict":
                           settings['changePictureProfile']=True
                           client.sendMessage(msg.to, "Please send image.")
                        if ang.lower() == ".updategpict":
                           settings['changeGroupPicture'][msg.to] = True
                           client.sendMessage(msg.to, "Please send image.")
                        if ang.lower() == ".gcreator":
                           if msg.toType == 2:
                              japri = client.getGroup(msg.to)
                              if japri.creator:
                                  petruk = client.getGroup(msg.to)
                                  gareng = petruk.creator.mid
                                  msg.text = ""
                                  msg.contentMetadata = {'mid': gareng}
                                  client.sendMessage(msg.to, "Group Creator:")
                                  client.sendMessage(msg.to,"",msg.contentMetadata,13)
                              else:client.sendReplyMessage(msg.id,msg.to,"Group creator galau.")

                        if ang.lower() == "me":
                            if msg.toType == 2:
                                haha = client.getContact(msg._from)
                                datax = {"type": "flex","altText": "SKT-Opera mengirim foto.","contents": {"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "image","url":"https://obs.line-scdn.net/" + "{}".format(client.getContact(msg._from).pictureStatus),"size": "full","aspectMode": "cover","aspectRatio": "60:50","gravity": "center","flex": 1},{"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Image","size": "xs","color": "#ffffff","align": "center","gravity": "center"}],"backgroundColor": "#EC3D44","paddingAll": "2px","paddingStart": "4px","paddingEnd": "4px","flex": 0,"position": "absolute","offsetStart": "18px","offsetTop": "18px","cornerRadius": "100px","width": "48px","height": "25px"}]}],"paddingAll": "0px"},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","contents": [{"type": "image","url": "https://imagizer.imageshack.com/v2/280x200q90/923/H1uMrZ.png","size": "full","aspectMode": "cover","aspectRatio": "80:25","gravity": "center","flex": 1}]}],"paddingAll": "13px","backgroundColor": "#000000","cornerRadius": "2px","margin": "xl"}],"paddingAll": "10px","backgroundColor": "#000000"}},}
                                client.sendTemp(msg.to,datax)
                        if ang.lower() == ".geturl":
                            if msg.toType == 2:
                                entot = client.getGroup(msg.to)
                                if entot.preventedJoinByTicket == True:
                                   entot.preventedJoinByTicket = False
                                   client.updateGroup(entot)
                                   set = client.reissueGroupTicket(msg.to)
                                   client.sendReplyMessage(msg.id,msg.to, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                   client.updateGroup(entot)
                                   set = client.reissueGroupTicket(msg.to)
                                   client.sendReplyMessage(msg.id,msg.to, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))

                        if ang.lower() == ".ginfo":
                            if msg.toType == 2:
                                group = client.getGroup(msg.to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Not Found"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Clossed"
                                    gTicket = "Nothing"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                japri = "🔷 รายละเอียด กลุ่มนี้ 🔷"
                                japri += "\n\n• ชื่อกลุ่ม : {}".format(str(group.name))
                                japri += "\n• ID กลุ่ม :\n {}".format(group.id)
                                japri += "\n• สร้างกลุ่มโดย : {}".format(str(gCreator))
                                japri += "\n• จำนวนสมาชิก : {}".format(str(len(group.members)))
                                japri += "\n• สมาชิกที่เชิญ : {}".format(gPending)
                                japri += "\n• 𝙂𝙧𝙤𝙪𝙥 𝙌𝙧 : {}".format(gQr)
                                japri += "\n• 𝙂𝙧𝙤𝙪𝙥 𝙏𝙞𝙘𝙠𝙚𝙩 : {}".format(gTicket)
                                client.sendReplyMessage(msg.id,msg.to, str(japri))

                        if ang.lower() == ".myfriendlist":
                         if msg.toType == 2:
                            contactlist = client.getAllContactIds()
                            contacts = client.getContacts(contactlist)
                            num=1
                            msgs="🔷𝙈𝙮 𝙁𝙧𝙞𝙚𝙣𝙙𝙡𝙞𝙨𝙩:\n"
                            for ids in contacts:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friendlist: %i" % len(contacts)
                            client.sendReplyMessage(msg.id, msg.to, msgs)

                        if ang.lower() == "creator":
                             credit = "uc6e436ae77d2d1f5b5f6bd13ea7b671c"
                             client.sendMessage(msg.to,"Bot creator:")
                             client.sendContact(msg.to,credit)

                        if ang.lower() == ".groupid":
                         if msg.toType == 2:
                            gid = client.getGroup(msg.to)
                            client.sendReplyMessage(msg.id,msg.to, "ID กลุ่ม : \n" + gid.id + "\n\nชื่อกลุ่ม : \n" + str(gid.name))

                        if ang.lower() == ".panduan" or ang.lower() == "panduan":
                           data = {"type": "flex","altText": "The SKT - Operation","contents": {"type": "bubble","styles": {"body": {"backgroundColor": "#000000"}},"body": {"type": "box","layout": "vertical","spacing": "lg","contents": [{"type": "image","url": "https://imagizer.imageshack.com/img922/9913/pz3ZBp.png","size": "xxl","aspectRatio": "6.50:2","aspectMode": "cover","action": {"type": "uri","uri": "http://line.me/ti/p/~@kmj4856d"}},{"type": "box","layout": "horizontal","spacing": "xl","contents": [{"type": "image","url":"https://lh3.googleusercontent.com/avr-Ht9lKzM9RdG0fr3Ev4cacXfUhHzKqSb3XHyqSQVrYhtMhyH__pZN6HuXu-9Zbdw","size": "full","aspectRatio": "1:1","aspectMode": "cover","action": {"type": "uri","uri":"line://home/public/profile?id=kmj4856d"}},{"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "text","text": "Panduan","size": "lg","weight": "bold","color": "#D32608","wrap": True},{"type": "text","text": "Cara menggunakan perintah pada simple selfbot G-Operation.\nKlik tombol READ.","size": "sm","color": "#ffffff","wrap": True},{"type": "button","style": "primary","color":"#800000","action": {"type": "uri","label": "READ","uri": "https://www.jurustupai.com/2020/05/panduan-menggunakan-perintah-pada.html?m=1"}}]}]}]}}}
                           client.sendTemp(msg.to,data)

                        if ang.lower() == ".groupict":
                         if msg.toType == 2:
                            hoax = client.getGroup(msg.to)
                            if hoax.pictureStatus is None or hoax.pictureStatus == "":
                                client.sendMessage(msg.to,"Group picture not found")
                            else:
                                ang = "https://obs.line-scdn.net/"+ hoax.pictureStatus
                                client.sendImageWithURL(msg.to,ang)

                        if ang.lower() == ".mygroups":
                         if msg.toType == 2:
                            gruplist = client.getGroupIdsJoined()
                            kontak = client.getGroups(gruplist)
                            num=0
                            msgs="👺ൠ  ΜЎ Ğ𝐑𝐎Ữρ𝔩ⒾŞŦ  👍😡:\n"
                            for ids in kontak:
                               msgs+="\n%i - %s" % (num, ids.name) + " (" + str(len(ids.members)) + ")"
                               num=(num+1)
                            msgs+="\n\n            「 Total : %i Groups 」" % len(kontak)
                            client.sendMessage(msg.to,"{}".format(str(msgs)))

                        if ang.lower() == ".adminlist":
                         if msg.toType == 2:
                            if manage["admin"] == {}:
                               client.sendReplyMessage(msg.id, msg.to,"ΛDMIПᄂIƧƬ ΣMPƬY!")
                            else:
                               radmin = ""
                               hoax = manage['admin']
                               num = 1
                               for uid in hoax:
                                   try:
                                      admins = client.getContact(uid)
                                      radmin += "\n%i. " % num + admins.displayName
                                      num = (num+1)
                                   except:
                                      radmin += "\n%i. Unknown" % num
                                      num = (num+1)
                               try:
                                  client.sendReplyMessage(msg.id, msg.to, "𝕊𝕂𝕋-𝕆𝕡𝕖𝕣𝕒𝕥𝕚𝕠𝕟\n• ᴀᴅᴍɪɴʟɪꜱᴛ:\n" + radmin + "\n\nTotal: " + str(len(hoax)) + " Users.")
                               except Exception as e:
                                  client.sendReplyMessage(msg.id, msg.to,"{}".format(str(e)))

                        if ang.lower().startswith(".music: "):
                            try:
                                music = ang.replace(".music: ","")
                                putar = requests.get("http://mnazria.herokuapp.com/api/joox?search={}".format(str(urllib.parse.quote(music))))
                                data = putar.text
                                data = json.loads(data)
                                angling = "🎵 𝙹𝙾𝙾𝚇 𝙼𝚄𝚂𝙸𝙲 𝙰𝚄𝙳𝙸𝙾"
                                angling += "\n\n• 𝙈𝙪𝙨𝙞𝙘 𝙨𝙚𝙖𝙧𝙘𝙝: {}".format(music)
                                angling += "\n• 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜.."
                                client.sendReplyMessage(msg.id,msg.to,angling)
                                client.sendImageWithURL(msg.to,"{}".format(str(data["picture"])))
                                client.sendAudioWithURL(msg.to,"{}".format(str(data["mp3"])))
                            except Exception as e:
                                client.sendReplyMessage(msg.id, msg.to,"{}".format(str(e)))

                        if ang.lower().startswith(".instagram: "):
                            try:
                                instagram = ang.replace(".instagram: ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                insta_ = "📲「𝙄𝙣𝙨𝙩𝙖𝙜𝙧𝙖𝙢 𝙄𝙣𝙛𝙤」\n\n"
                                insta_ += "◉  𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙉𝙖𝙢𝙚 : " + text[-3] + " " + text[-2] +"\n"
                                insta_ += "◉  𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 𝙄𝘿 : " + text[-1] + "\n"
                                insta_ += "◉  𝙁𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 : " + text[0] + "\n"
                                insta_ += "◉  𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 : " + text[2] + "\n"
                                insta_ += "◉  𝙋𝙤𝙨𝙩𝙨 : " + text[4] + "\n"
                                insta_ += "◉  𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙐𝙍𝙇 :\n" + "https://www.instagram.com/" + instagram
                                insta_ += ""
                                client.sendMessage(msg.to,"{}".format(str(insta_)))
                            except Exception as e:client.sendReplyMessage(msg.id, msg.to,"{}".format(str(e)))

                        if ang.lower().startswith(".youtube: "):
                            try:
                                query = ang.lower().replace(".youtube: ","")
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    url = 'https://www.youtube.com/results'
                                    params = {'search_query':query}
                                    r = s.get(url, params=params)
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    for a in soup.select('.yt-lockup-title > a[title]'):
                                        if '&list=' not in a['href']:
                                           dl=("https://www.youtube.com" + a['href'])
                                           splitin = dl.split("?v=")[1]
                                           data = {"type": "flex","altText": "The G - Operation","contents": {"type": "bubble","styles": {"body": {"backgroundColor": "#000000"}},"body": {"type": "box","layout": "vertical","spacing": "lg","contents": [{"type": "image","url": "https://imagizer.imageshack.com/img922/9913/pz3ZBp.png","size": "xxl","aspectRatio": "5.50:2","aspectMode": "cover","action": {"type": "uri","uri": "http://line.me/ti/p/~@kmj4856d"}},{"type": "box","layout": "horizontal","spacing": "xl","contents": [{"type": "image","url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(splitin),"size": "full","aspectRatio": "1:1","aspectMode": "cover","action": {"type": "uri","uri":"line://home/public/profile?id=kmj4856d"}},{"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "text","text": "Youtube","size": "lg","weight": "bold","color": "#800000","wrap": True},{"type": "text","text": "{}".format(a['title']),"size": "sm","color": "#ffffff","wrap": True},{"type": "button","style": "primary","color": "#800000","action": {"type": "uri","label": "OPEN","uri": "https://www.youtube.com"+a['href']}}]}]}]}}}
                                           client.sendTemp(msg.to,data)
                                           break
                            except Exception as e:client.sendReplyMessage(msg.id, msg.to,"{}".format(str(e)))

                        if ang.lower().startswith(".image: "):
                            try:
                                 search = ang.lower().replace(".image: ","")
                                 url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                                 raw_html = (download_page(url))
                                 items = []
                                 items = items + (_images_get_all_items(raw_html))
                                 path = random.choice(items)
                                 print (path)
                                 client.sendImageWithURL(msg.to,path)
                            except Exception as e:client.sendMessage(msg.to, str(e))

                        if ang.lower().startswith(".groupname: "):
                         if msg.toType == 2:
                            angg = client.getGroup(msg.to)
                            angg.name = ang.replace(".groupname: ","")
                            client.updateGroup(angg)

                        if ang.lower().startswith(".updatebio: "):
                         if msg.toType == 2:
                            jap = ang.split(".updatebio: ")
                            string = jap[1]
                            if len(string) <= 500:
                               profile = client.getProfile()
                               profile.statusMessage = string
                               client.updateProfile(profile)
                               client.sendReplyMessage(msg.id,msg.to, "Status bio changed to:\n" + string)
                            else:client.sendReplyMessage(msg.id,msg.to,"Maksimal 500 karakter.")

                        if ang.lower().startswith(".updatename: "):
                         if msg.toType == 2:
                            jap = ang.split(".updatename: ")
                            string = jap[1]
                            if len(string) <= 500:
                               profile = client.getProfile()
                               profile.displayName = string
                               client.updateProfile(profile)
                               client.sendReplyMessage(msg.id,msg.to, "Profile name changed to:\n" + string)
                            else:client.sendReplyMessage(msg.id,msg.to,"Maksimal 500 karakter.")


                        if ang.lower().startswith(".line: "):
                            ang_id = ang.replace(".line: ","")
                            line_id = client.findContactsByUserid(line_id)
                            if True:
                                client.sendMessage(msg.to,"http://line.me/ti/p/~" + angg_id)
                                client.sendContact(msg.to,line_id.mid)
                            else:client.sendReplyMessage(msg.id,msg.to,"Invalid Id name")


                        if ang.lower().startswith(".kick"):
                         if msg.toType == 2:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', msg.text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  for mention in mentionees:
                                     client.kickoutFromGroup(msg.to,[mention['M']])
                             else:pass


                        if ang.lower() == ".kickall":
                         if msg.toType == 2:
                             hoax = client.getGroup(msg.to)
                             client.sendMessage(msg.to,"𝙂𝙤𝙤𝙙𝙗𝙮𝙚 𝘽𝙞𝙩𝙘𝙝 ~")
                             for angg in hoax.members:
                                 if angg.mid not in manage["admin"]:
                                     client.kickoutFromGroup(msg.to,[angg.mid])
                             client.sendMessage(msg.to,"𝗚𝗿𝗼𝘂𝗽 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗰𝗹𝗲𝗮𝗿𝗲𝗱")


                        if ang.lower().startswith(".addadmin "):
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                if target in manage["admin"]:
                                    client.sendReplyMessage(msg.id,msg.to, "𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙞𝙣 𝙖𝙙𝙢𝙞𝙣.")
                                else:
                                      try:
                                         manage["admin"][target] = True
                                         with open('admin.json', 'w') as fp:
                                             json.dump(manage, fp, sort_keys=True, indent=4)
                                         client.sendReplyMessage(msg.id,msg.to,client.getContact(target).displayName +" 𝙖𝙙𝙙 𝙩𝙤 𝙖𝙙𝙢𝙞𝙣.")
                                      except Exception as error:
                                         client.sendMessage(msg.to,"[ERROR]\n{}".format(str(error)))


                        if ang.lower().startswith(".deladmin "):
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            targets = []
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                if target not in manage["admin"]:
                                    client.sendReplyMessage(msg.id,msg.to, "𝙐𝙨𝙚𝙧 𝙣𝙤𝙩 𝙞𝙣 𝙖𝙙𝙢𝙞𝙣")
                                else:
                                    try:
                                        del manage["admin"][target]
                                        with open('admin.json', 'w') as fp:
                                            json.dump(manage, fp, sort_keys=True, indent=4)
                                        client.sendReplyMessage(msg.id,msg.to,client.getContact(target).displayName +" яємσνє∂ ƒяσм α∂мιη.")
                                    except Exception as error:
                                        client.sendMessage(msg.to,"[ ERROR]\n{}".format(str(error)))


                        if ang.lower().startswith(".invite"):
                         if msg.toType == 2:
                             if msg.contentMetadata is not None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                   targets.append(x["M"])
                                for target in targets:
                                   client.findAndAddContactsByMid(target)
                                   client.inviteIntoGroup(msg.to, [target])
                                   client.sendMessage(msg.to, client.getContact(target).displayName + " нαѕ вєєη ιηνιтє∂.")
                             else:pass


                        if ang.lower().startswith(".getmid "):
                           if msg.toType == 2:
                              key = eval(msg.contentMetadata["MENTION"])
                              key1 = key["MENTIONEES"][0]["M"]
                              mi = client.getContact(key1)
                              client.sendReplyMessage(msg.id,msg.to,key1)


                        if ang.lower().startswith(".getpict "):
                         if msg.toType == 2:
                           if msg.contentMetadata is not None:
                              targets = []
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:
                                  profile = client.getContact(target)
                                  angimg = "https://obs.line-scdn.net/" + profile.pictureStatus
                                  client.sendImageWithURL(msg.to, angimg)
                           else:client.sendReplyMessage(msg.id,msg.to,"No image found")


                        if ang.lower().startswith(".getcover "):
                         if msg.toType == 2:
                           if msg.contentMetadata is not None:
                              targets = []
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:
                                  profile = client.getContact(target)
                                  angimg = client.getProfileCoverURL(target)
                                  client.sendImageWithURL(msg.to, angimg)
                           else:client.sendReplyMessage(msg.id,msg.to,"No image found")


                        if ang.lower().startswith(".getstatus "):
                         if msg.toType == 2:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = client.getContact(key1)
                            if contact.statusMessage is None or contact.statusMessage =="":
                               client.sendReplyMessage(msg.id,msg.to,"𝙎𝙩𝙖𝙩𝙪𝙨 𝙣𝙤𝙩 𝙛𝙤𝙪𝙣𝙙.")
                            else:
                               client.sendReplyMessage(msg.id, msg.to, "§.•´¨'°÷•..× ｓt𝐚𝕋𝕌𝔰 ｍＥｓ𝓢𝓪𝔾є ×,.•´¨'°÷•..§\n" + contact.statusMessage)


                        if ang.lower() == ".sider on":
                            if msg.toType == 2:
                                if msg.to in cctv["Point"]:
                                    cctv["Point3"][msg.to] = {}
                                    with open('cctv.json', 'w') as fp:
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"𝘾𝙝𝙚𝙘𝙠 𝙧𝙖𝙙𝙖𝙧 𝙧𝙚𝙨𝙩𝙖𝙧𝙩𝙞𝙣𝙜..")
                                else:
                                    cctv["Point"][msg.to]= True
                                    cctv["Point3"][msg.to] = {}
                                    with open('cctv.json', 'w') as fp:
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"𝘾𝙝𝙚𝙘𝙠 𝙧𝙖𝙙𝙖𝙧 𝙧𝙪𝙣𝙣𝙞𝙣𝙜..")


                        if ang.lower() == ".sider off":
                            if msg.toType == 2:
                                if msg.to in cctv["Point"]:
                                    del cctv["Point"][msg.to]
                                    with open('cctv.json', 'w') as fp:
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"𝘾𝙝𝙚𝙘𝙠 𝙧𝙖𝙙𝙖𝙧 𝙙𝙞𝙨𝙖𝙗𝙡𝙚𝙙.")
                                else:
                                    client.sendReplyMessage(msg.id,msg.to,"𝘾𝙝𝙚𝙘𝙠 𝙧𝙖𝙙𝙖𝙧 𝙖𝙡𝙧𝙚𝙖𝙙𝙮 𝙙𝙞𝙨𝙖𝙗𝙡𝙚𝙙.")

                        if ang.lower() == '.lurk on':
                            tz = pytz.timezone("Asia/Bangkok")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to in cctv['readPoint']:
                                    try:
                                        del cctv['readPoint'][msg.to]
                                        del cctv['readMember'][msg.to]
                                        del cctv['readTime'][msg.to]
                                    except:
                                        pass
                                    cctv['readPoint'][msg.to] = msg.id
                                    cctv['readMember'][msg.to] = ""
                                    cctv['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    cctv['ROM'][msg.to] = {}
                                    with open('cctv.json', 'w') as fp:
                                        json.dump(cctv, fp, sort_keys=True, indent=4)
                                    client.sendReplyMessage(msg.id,msg.to,"𝗦𝗽𝘆 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗘𝗻𝗮𝗯𝗹𝗲𝗱")
                            else:
                                 try:
                                   del cctv['readPoint'][msg.to]
                                   del cctv['readMember'][msg.to]
                                   del cctv['readTime'][msg.to]
                                   with open('cctv.json', 'w') as fp:
                                       json.dump(cctv, fp, sort_keys=True,indent=4)
                                 except:
                                     pass
                                 cctv['readPoint'][msg.to] = msg.id
                                 cctv['readMember'][msg.to] = ""
                                 cctv['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                 cctv['ROM'][msg.to] = {}
                                 with open('cctv.json', 'w') as fp:
                                     json.dump(cctv, fp, sort_keys=True, indent=4)
                                 client.sendReplyMessage(msg.id, msg.to, "𝐒𝐞𝐭 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐩𝐨𝐢𝐧𝐭:\n" + readTime)


                        if ang.lower() == '.lurk off':
                            tz = pytz.timezone("Asia/Bangkok")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to not in cctv['readPoint']:
                                client.sendReplyMessage(msg.id,msg.to,"𝐒𝐞𝐭 𝐒𝐩𝐲 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐄𝐧𝐚𝐛𝐥𝐞𝐝.")
                            else:
                                try:
                                        del cctv['readPoint'][msg.to]
                                        del cctv['readMember'][msg.to]
                                        del cctv['readTime'][msg.to]
                                        with open('cctv.json', 'w') as fp:
                                            json.dump(cctv, fp, sort_keys=True,indent=4)
                                except:
                                      pass
                                client.sendReplyMessage(msg.id, msg.to, "𝐃𝐞𝐥𝐞𝐭𝐞 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐩𝐨𝐢𝐧𝐭:\n" + readTime)

                        if ang.lower() == '.lurk reset':
                            if msg.toType == 2:
                                tz = pytz.timezone("Asia/Bangkok")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in cctv["readPoint"]:
                                    try:
                                        cctv["readPoint"][msg.to] = True
                                        cctv["readMember"][msg.to] = {}
                                        cctv["readTime"][msg.to] = readTime
                                        cctv["ROM"][msg.to] = {}
                                        with open('cctv.json', 'w') as fp:
                                            json.dump(cctv, fp, sort_keys=True,indent=4)
                                    except:
                                        pass
                                    client.sendReplyMessage(msg.id, msg.to, "𝐑𝐞𝐬𝐞𝐭 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐩𝐨𝐢𝐧𝐭:\n" + readTime)
                                else:
                                    client.sendMessage(msg.id, msg.to, "Type '.lurk on' first.")

                        if ang.lower() == '.lurkers':
                            if msg.toType == 2:
                                tz = pytz.timezone("Asia/Bangkok")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nTime : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in cctv['readPoint']:
                                    if cctv["ROM"][msg.to].items() == []:
                                        client.sendReplyMessage(msg.id, msg.to,"Reader None")
                                    else:
                                        chiya = []
                                        for rom in cctv["ROM"][msg.to].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Group reader:\n\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@Goperation\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        client.sendReplyMessage(msg.id, msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendReplyMessage(msg.id, msg.to,"Lurk on first.")

                        if ang.lower() == '.mention' or ang.lower() == '@' or ang.lower() == "tagall":
                         if msg.toType == 2:
                            group = client.getGroup(msg.to)
                            midMembers = [contact.mid for contact in group.members]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "🔘 ขออนุญาติ เริ่ม tag เรียกสมาชิก 🔘\n"
                                dataMid = []
                                for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention.mid)
                                    no += 1
                                    ret_ += "\n{}. @!\n".format(str(no))
                                ret_ += "\n\n ⚫「 Total {} Members 」💯 ".format(str(len(dataMid)))
                                sendMention(msg.to, ret_, dataMid)
            except Exception as error:
                client.sendMessage(msg.to, "[GOP ERROR]\n{}".format(str(error)))
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        client.sendMessage(msg.to, "[GOP ERROR]\n{}".format(str(error)))
        traceback.print_tb(error.__traceback__)

while True:
    try:
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        client.sendMessage(msg.to, "[GOP ERROR]\n{}".format(str(error)))
        traceback.print_tb(error.__traceback__)
#===============[ NOTE ]======================]
# LINE PYTHON3: LINEPY
# AUTHOR : FADHIIL RACHMAN & HELLO WORLD
# SB COMMAND CREATED BY : ANG
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
# JANGAN MELAKUKAN PERUBAHAN PADA SCRIPT KECUALI ANDA YAKIN DAN TAU
# PUBLISHED ON: https://www.jurustupai.com/2020/05/cara-membuat-simple-selfbot-template.html
