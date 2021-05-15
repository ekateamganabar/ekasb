#================================#
#======DRAGON`KILLERÎ¾=======#
#====ID LINE : ownerdkbot=====#
#================================#
# -*- coding: utf-8 -*-
from BEAPI import *
from py_translator import TEXTLIB
from Dkbots import *
from tornado import ioloop
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from tmp.Instagram import InstagramScraper
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from gtts import gTTS
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bSoup
from multiprocessing import Pool
from bs4.element import Tag
import requests as uReq
from datetime import datetime
from googletrans import Translator
from zalgo_text import zalgo
import ast, codecs, json, os, pytz, re, LineService, random, sys, time, urllib.parse, subprocess, threading, pyqrcode, pafy, asyncio, humanize, os.path, traceback
from threading import Thread
from io import StringIO
from multiprocessing import Pool,Process
import subprocess as cmd
import platform
import requests, json
from urllib.parse import urlencode
from random import randint
from shutil import copyfile
from thrift import transport, protocol, server
from Dkbots.thrift.Thrift import *
from Dkbots.thrift.TMultiplexedProcessor import *
from Dkbots.thrift.TSerialization import *
from Dkbots.thrift.TRecursive import *
from Dkbots.thrift.protocol import TCompactProtocol
from Dkbots.thrift.transport import THttpClient
from Naked.toolshed.shell import execute_js 
from threading import Thread,Event
from shutil import copyfile
import requests, uvloop
import wikipedia as wiki
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
requests.packages.urllib3.disable_warnings()
import html5lib
import requests,json,urllib3
from datetime import timedelta, date
from datetime import datetime
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
from humanfriendly import format_timespan, format_size, format_number, format_length
import pytz, pafy, livejson, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, tweepy, codecs, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

loop = uvloop.new_event_loop()
#==============token=======================
#==============email=======================
try:
    with open('token1.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    cl = LINE()
cl = LINE("nirwanabjn@gmail.com","ekafiutama1",appName="IOSIPAD\t9.18.1\tiPhone 8\t12.4.1")
clientMid = cl.profile.mid
clientMID = cl.profile.mid
#==============email=======================
creator = ["ucea4db871e2f6b401ac278f6999ccf58"]
owner = ["ub7974b32506814d4cb71d18897e67afa"]
admin = ["ub7974b32506814d4cb71d18897e67afa"]
staff = ["ub7974b32506814d4cb71d18897e67afa"]  
#==============mid========================
	
clientProfile = cl.getProfile()
myBOG = cl.profile.mid
clientSettings = cl.getSettings()
oepoll = OEPoll(cl)
mid = cl.getProfile().mid
stickerOpen = codecs.open("sticker.json","r","utf-8")
stickertOpen = codecs.open("stickertemplate.json","r","utf-8")
stickers = json.load(stickerOpen)
stickerstemplate = json.load(stickertOpen)
 

KAC = [cl]
ABC = [cl]
Bots = [mid]
Bots = [myBOG]
admin = [mid]
owner = [mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots

desmac = "DESKTOPMAC\t6.7.0\tMAC\t10"
chrome = "CHROMEOS\t2.4.3\tChrome OS\t10"


color1 = {'vid': '#696969'}
prohibitedWords = ['Asu', 'Jancuk', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
protectqr = []
protectkick = []
protectjoin = []
steals = []
protectinvite = []
smuleBEAPI = []
protectcancel = []
protectJs = []
welcome = []
offbot = []
temp_flood = {}
ssnd = []
msg_image={}
msg_video={}
msg_sticker={}
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
groupName = {}
groupImage = {}
list = []
userKicked = []

#WARNA
merah = "#FF2800"
kuning = "#FFFD00"
hijau = "#83FF00"
biru = "#00DAFF"
ungu = "#C323FF"
ping = "#FF17CE"
hitam = "#000000"
putih = "#FFFFFF"
abuabu = "#000000cc"
sp_putih = {"type": "separator","color": "#FFFFFF"}
sp_hitam = {"type": "separator","color": "#000000"}
sp_kuning = {"type": "separator","color": "#FFFD00"}
sp_biru = {"type": "separator","color": "#00DAFF"}
sp_hijau = {"type": "separator","color": "#83FF00"}
sp_merah = {"type": "separator","color": "#FF2800"}
sp_ungu = {"type": "separator","color": "#C323FF"}
sp_ping = {"type": "separator","color": "#FF17CE"}
sp_abuabu = {"type": "separator","color": abuabu}
style_hijau={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":hijau}}
style_merah={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":merah}}
style_biru={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":biru}}
style_kuning={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":kuning}}
style_ungu={"header":{"backgroundColor":abuabu},"body":{"backgroundColor":abuabu},"footer":{"backgroundColor":abuabu,"separator":True,"separatorColor":ungu}}
style_putih={"header":{"backgroundColor":putih},"body":{"backgroundColor":putih},"footer":{"backgroundColor":putih,"separator":True,"separatorColor":hitam}}
style_hitam={"header":{"backgroundColor":hitam},"body":{"backgroundColor":hitam},"footer":{"backgroundColor":hitam,"separator":True,"separatorColor":putih}}
image1 = "https://i.ibb.co/LtwXd3f/1620998142951.jpg"
image2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRpT_8vMV73l-9im6Idu5unZOBNQ1QqiKJmtjuaIIPSTCtXApmd"
image3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRpT_8vMV73l-9im6Idu5unZOBNQ1QqiKJmtjuaIIPSTCtXApmd"
Gambar = (image1,image2,image3)
logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSk_wEerfoWmvALRkxFqBmcNU-ArkQz7Kh5P_oR1JuokMP5G60Y"
Warna = (merah,kuning,hijau,biru,ping,ungu)
warnanya1 = random.choice(Warna)
warnanya2 = random.choice(Warna)
warnanya3 = random.choice(Warna)

set={
    "token": True
}

settings = {
    "Picture":False,
    "server": "VPS",
    "responGc":False,
    "kick": False,
    "welcome": True,
    "changevp":False,
    "sticker": [],
    "Videos":{},
    "group":{},
    "apiKey": "8e3cf182-807a-4186-9261-a6c8741a9237",
    "access_key": "0066725464abd96d2cee00863ad9067f",
    "access_token": "ec6a73ed66f5704bf4d071a2174fb736238aaeb6",
    "ChangeVideoProfilevid":False,
    "groupPicture":False,
    "changeVideoAndPictureProfile":False,
    "changeCover":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "changevp": False,
    "spamCall": True,
    "joincom": "sᴇʟᴀᴍᴀᴛ ʙᴇʀɢᴀʙᴜɴɢ sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ",
    "leave": "ᴅɪʜ...... ᴋᴀʙᴜʀ ᴅɪᴀ",
    "changePicture":False,
    "autoJoinTicket":False,
    "detectTemplate": True,
    "detectMention":False,
    "checkPost":False,
    "keyCommand": " ",
    "setKey": False,
    "tatan": "Dkbots",
    "commentPost": "◄━━◈⟦ASSALAMUALAIKUM⟧◈━━►\n            🛡Dzulkifli DK DESIGN🛡\n╔•═══════════════\n║╠═╦═✪ PROMOTION ✪═╦═\n╠•═══════════════\n╠•══✪「ᴏᴘᴇɴ ᴏʀᴅᴇʀ」✪════\n║┣[]► SCRIPT BOT PROTECT\n║┣[]► SCRIPT BOT WAR\n║┣[]► SCRIPT BOT SIRI\n║┣[]► SCRIPT SB ONLY\n║┣[]► SCRIPT SB TEMPLATE\n║┣[]► SONGBOOK SMULE\n╠════════════════\n╠•══✪「ʙᴏᴛ ᴏʀᴅᴇʀ」✪═════\n║┣[]► sʙ ᴏɴʟʏ \n║┣[]► sʙ + ᴀsɪsᴛ\n║┣[]► sʙ + ᴀsɪsᴛ + ɢʜᴏsᴛ\n║┣[]► sʙ + ᴀsɪsᴛ + ɢʜᴏsᴛ + ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 6 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 10 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 20 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 25 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n╠•══✪「sᴇᴛ - ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ」✪═\n║┣[]► ᴏᴡɴᴇʀ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n║┣[]► ᴀᴅᴍɪɴ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n║┣[]► sᴛᴀғғ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n║┣[]► ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ sᴍᴜʟᴇ\n║┣[]► ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ᴇᴠᴇɴᴛ\n║┣[]► ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ᴏʟsʜᴏᴘ\n╠════════════════\n╠•══✪「==CATATAN==」✪════\n║BARANG SIAPA YG MERATAKAN\n║ROOM SMULE/EVENT/OLSHOP\n║MENGATASNAMAKAN DK BOTS/\n║DRAGON KILLER BOTS/DKBOTS\n║ATAU DK DRAGON KILLER\n║HUBUNGI SAYA LANGSUNG\n╠════════════════\n╠•══✪「ᴅᴀғᴛᴀʀ ʜᴀʀɢᴀ」✪════\n║JIKA ANDA BERMINAT SILAHKAN\n║                ✪ HUBUNGI ✪\n║WA     : -\n║LINE   : ownerdk / dkbot / dragonkillerbots\n║http://line.me/ti/p/~ownerdk\n║http://line.me/ti/p/~ownerdk\n║http://line.me/ti/p/~ownerdk\n╠════════════════\n║SALAM SANTUN PERSAHABATAN\n║            ✪ TERIMA KASIH ✪\n╚════════════════\n ◄━━◈⟦WASSALAMUALAIKUM⟧◈━━►",
    "idline": "http://line.me/ti/p/~nirwanabjn",
    "lebel": "⟗SELF V2020 ⟗",
    "conpp":False,
    "copy":False,
    "autoblock":False,
    "unsendMessage":False,
    "messageSticker": {
        "addName": null,
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "51626498",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "welcomeSticker": {
                "STKID": "22002738",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "leaveSticker": {
                "STKID": "52002755",
                "STKPKGID": "1153",
                "STKVER": "1"
            },
            "readerSticker": {
                "STKID": "52114132",
                "STKPKGID": "11539",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "52002762",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "sleepSticker": null,
            "welcomeSticker": {
                "STKID": "4893632",
                "STKPKGID": "4107",
                "STKVER": "1"
            }
        }
    },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "conpp":False,
        "copy": False,
        "status": False,
        "ChangeVideoProfilevid":{},
        "ChangeVideoProfilePicture":{},
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False,
    "userAgent": [
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0',              
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:51.0) Gecko/20100101 Firefox/51.0',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
        'Mozilla/5.0 (iPad; CPU OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 \'Mobile/14C92 Safari/602.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, lik0e Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 \'Mobile/14C92 Safari/602.1'
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    'BDAY':True,
    'mylove':True,
    "TIKTOK":False,
    "INSTAGRAM":False,
    "detectTemplate": False,
    "staff":[],
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "chatbot":True,
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "sharesmule":True,
    "reject":True,
    "Respontag":False,
    "notifCall":True,
    "detectBio":False,
    "detectName":False,
    "detectPp":False,
    "detectvp2":False,
    "detectvp":False,
    "prankCall":True,
    "responGc":True,
    "changeDual":False,
    "contact":False,
    'autoJoin':True,
    'autoJoinbypass':False,
    'autoJoinjs':False,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "bcg_audio":False,
    "bcg_video":False,
    "bcg_image":False,
    "unsend":False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "undang":False,
    "selfbot":True,
    "smule":True,
    "yutube":True,
    "warna": "#7FFFD4",
    "warna1": "#FFD700",
    "warna2": "#FF7F00",
    "warna3": "#BF00FF",
    "tagall": "halo",
    "notifProfile":False,
    "cekpc": "Pm ku gosong semm??",
    "size":"micro",
    "BAGNOTIFPROFILE":"https://i.ibb.co/p3cB9yD/ezgif-com-gif-maker-1.png",
    "BAGBDAY":"https://i.pinimg.com/736x/99/e9/6d/99e96d2fe182f73d7a3c2f64e70fd806.jpg",
    "BAGHELP":"https://i.ibb.co/LtwXd3f/1620998142951.jpg",
    "mention":"Deteksi Cctv Member",
    "mention2":"Deteksi Cctv Member",
    "Respontag":"Yg nge tag moga panjang umur",
    "welcome":"Selamat datang semoga betah dan jangan lupa cek note",
    "comment":"Like like & like by GANABAR",
    "message":"Terimakasih sudah add Aku sob",
    }

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": "",
	"coverId": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

cctv2 = {
    "cyduk2":{},
    "point2":{},
    "sidermem2":{}
}

dkbot_killer = {
    "sharesmule": True
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
	
coverId = cl.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
settings["myProfile"]["displayName"] = clientProfile.displayName
settings["myProfile"]["statusMessage"] = clientProfile.statusMessage
settings["myProfile"]["pictureStatus"] = clientProfile.pictureStatus

responsename = cl.getProfile().displayName
 
with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
#boters = codecs.open("Notifbot.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
#Notifbot = json.load(boters)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
                                    
def smuleBEAPI(to, url):
    try:
        api = BEAPI('rangga09')
        res = api.smulePost("https://www.smule.com/c/1232746914_3991127254")
        cl.sendImageWithURL(to, res['result']['performance']['cover_url'])
        cl.sendMessage(to, res['result']['performance']['title'])
        if 'video' in res['result']['performance']['type']:
            cl.sendVideoWithURL(to, res['result']['performance']['video_media_url'])
        else:
            cl.sendAudioWithURL(to, res['result']['performance']['media_url'])
    except Exception as e:
        cl.sendMessage(to, "{}".format(e))

def tiktokBEAPI(to, url):
    try:
        api = BEAPI('rangga09')
        res = api.musicallyDown(url)
        cl.sendVideoWithURL(to, res["result"]["download"])
    except Exception as e:
        cl.sendMessage(to, "{}".format(e))


def youtubeBEAPI(to, url):
    try:
        api = BEAPI('rangga09')
        res = api.youtubeMp4Search(url)
        cl.sendVideoWithURL(to,res['result']['url'])
    except Exception as e:
        cl.sendMessage(to, "{}".format(e))

def loginBEAPI(to, userku, appNyaku):
    #from BEAPI import *
    try:
        api = BEAPI(Apikey["rangga09"])
        #api = "tByQDzRa8z8D"
        cert = None
        res = api.lineQr(sysname="BE-Team", appName=appNyaku, cert=cert)
        cl.sendMessage(to,"QR Link: " + res["result"]["qr_link"])
        if not cert:
            cl.sendMessage(to,"Pincode: " + res["result"]["cb_pincode"])
            for num in range(60):
                resx = api.sendGet(res["result"]["cb_pincode"].replace(api.host,""))
                if resx["result"] != "not ready":
                   cl.sendMessage(to,"Your Pincode: " + resx["result"])
                   break
                time.sleep(1)
            if resx["result"] == "not ready": raise Exception("login timeout!!")
        for num in range(60):
            resx = api.sendGet(res["result"]["cb_token"].replace(ap.host,""))
            if resx["result"] != "not ready":
                cl.sendMessage(userku, resx["result"]["token"])
                sendMention(to, 'Check PM @!',[userku])
                cert, authToken= resx["result"]["cert"], resx["result"]["token"]
                break
            time.sleep(1)
        if resx["result"] == "not ready": raise Exception("login timeout!!")
    except Exception as e:
        cl.sendMessage(to, "{}".format(e))

def removeCmdv(text, key=""):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(" ")
    return text_.replace(sep[0] + " ", "")

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def searchRecentMessages(to,id):
    for a in cl.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def videoyt1(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp4=a.url
            mp3=a.url
       cl.sendAudioWithURL(to,mp3)
       cl.sendVideoWithURL(to,mp4)

def videoyt(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp4=a.url
       data = {
                    "type": "video",
                    "originalContentUrl": mp4,
                    "previewImageUrl": "https://media.tenor.com/images/6d7761cb85acdb185ca243821e1b7339/tenor.gif",
                    }
       cl.postTemplate(to, data)


def audioyt(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp3=a.url
       cl.sendAudioWithURL(to,mp3)
              
def fileMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output FileYoutube.mp4 {}'.format(link))
    try:
        cl.sendFile(to, "FileYoutube.mp4")
        time.sleep(2)
        os.remove('FileYoutube.mp4')
    except Exception as e:
        cl.sendMessage(to, ' 「 ERROR 」')
    
def fileMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output FileYoutube.mp3 {}'.format(link))
    try:
        cl.sendFile(to, 'FileYoutube.mp3')
        time.sleep(2)
        os.remove('FileYoutube.mp3')
    except Exception as e:
        cl.sendMessage(to, ' 「 ERROR 」')
#=====================================================
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output video.mp3 {}'.format(link))
    try:
        cl.sendAudio(to, 'video.mp3')
        time.sleep(2)
        os.remove('video.mp3')
    except Exception as e:
        cl.sendMessage(to, "Error")

def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output video.mp4 {}'.format(link))
    try:
        cl.sendVideo(to, "video.mp4")
        time.sleep(2)
        os.remove('video.mp4')
    except Exception as e:
        cl.sendMessage(to, "Error")
        
def fileYtMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output FileYoutube.mp4 {}'.format(link))
    try:
        cl.sendFile(to, "FileYoutube.mp4")
        time.sleep(2)
        os.remove('FileYoutube.mp4')
    except Exception as e:
        cl.sendMessage(to, ' 「 ERROR 」')
    
def fileYtMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output FileYoutube.mp3 {}'.format(link))
    try:
        cl.sendFile(to, 'FileYoutube.mp3')
        time.sleep(2)
        os.remove('FileYoutube.mp3')
    except Exception as e:
        cl.sendMessage(to, ' 「 ERROR 」')
#=====================================================    
def notifProfile(to, mid):
    try:
        arrData = ""
        valerinda = cl.getContact(op.param2)
        anu = valerinda.displayName
        cl.sendMessage(to, "Hemmm... "+anu+" Ketahuan Ganti Photo Profile")
        image = "http://dl.profile.line-cdn.net/" + valerinda.pictureStatus
        cl.sendImageWithURL(to, image)
    except Exception as error:
        print (error)

def Pertambahan(a,b):
    jum = a+b
    print(a, "+",b," = ",jum)
def Pengurangan(a,b):
    jum = a-b
    print(a, "-",b," = ",jum)
def Perkalian(a,b):
    jum = a*b
    print(a, "x",b," = ",jum)
def Pembagian(a,b):
    jum = a/b
    print(a, ":",b," = ",jum)
def Perpangkatan(a,b):
    jum = a**b
    print(a,"Pangkat ",b," = ",jum )

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '?', '', '╰']]:
            result += '\n ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id'].replace("https://","")
def cytmp4(url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
def cytmp3(url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.audiostreams[-1]
    return result.url

def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+cl.google_url_shorten(links)
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah
            
def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = cl.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def a2():
    now2 = datetime.datetime.now()
    nowT = datetime.datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in mid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            cl.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        cl.sendMessage(to, 'Apalo !')
    elif cmd.startswith('exc\n'):
      if sender in mid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','cl.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        cl.sendMessage(to, 'Apalo !')

def generateLink(to, ryn, rynurl=None):
    path = cl.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.jpg')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    url = 'https://fahminogameno.life/uploadimage/action.php'
    r = requests.post(url, data=data, files=files)
    cl.sendMessage(to, '%s\n%s' % (r.status_code,r.text))
    cl.sendMessage(to, '{}{}'.format(rynurl,urlEncode('https://fahminogameno.life/uploadimage/images/ryngenerate.png')))

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items            

def cek(mid):
    if mid in (Bots):
        return True
    else:
        return False

def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def yutup(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "Dkᴮᴼᵀˢ"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
    
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    cl.sendMessage(to, text, contentMetadata=annda)
    


#========================
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            cl.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        cl.sendMessage(to, 'Apalo !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','cl.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        cl.sendMessage(to, 'Apalo !')

def backupData():
    try:
        backup = settings
        f = codecs.open('setingan.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False  
		    

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
	
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': client.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        cl.updateProfilePicture(path_p, 'vp')

def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def convertYoutubeMp4(url):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.streams[-1]
    return result.url


def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def sendSticker(to,version,packageId,stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    cl.sendMessage(to, '', contentMetadata, 7)

def getToken(to,header):
    token_key = "rangga09"
    result = json.loads(requests.get("https://api.boteater.us/line_qr_v2?header="+header+"&auth="+token_key).text)
    cl.sendMessage(to,"QR Link: "+result["result"]["qr_link"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    cl.sendMessage(to,result["result"]["pin_code"])
    result = json.loads(requests.get(result["result"]["callback"]+"&auth="+token_key).text)
    if result["status"] != 200:
        raise Exception("Timeout!!!")
    cl.sendMessage(to,result["result"]["token"])

def Pertambahan(a,b):
    jum = a+b
    print(a, "+",b," = ",jum)
def Pengurangan(a,b):
    jum = a-b
    print(a, "-",b," = ",jum)
def Perkalian(a,b):
    jum = a*b
    print(a, "x",b," = ",jum)
def Pembagian(a,b):
    jum = a/b
    print(a, ":",b," = ",jum)
def Perpangkatan(a,b):
    jum = a**b
    print(a,"Pangkat ",b," = ",jum )

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output Syahrul.mp3 {}'.format(link))
    try:
        cl.sendAudio(to, 'Syahrul.mp3')
        time.sleep(2)
        os.remove('Syahrul.mp3')
    except Exception as e:
        cl.sendMessage(to, ' 「 ERROR 」\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output Syahrul.mp4 {}'.format(link))
    try:
        cl.sendVideo(to, "Syahrul.mp4")
        time.sleep(2)
        os.remove('Syahrul.mp4')
    except Exception as e:
        cl.sendMessage(to, ' 「 ERROR 」\nMungkin Link Nya Salah GaN~', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+cl.getContact(mid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~ownerdk'})

def yutup(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "Dk-bot"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def searchRecentMessages(to,id):
    for a in cl.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def convertYoutubeMp4(url):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.streams[-1]
    return result.url

def convertYoutubeMp3(ur):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.audiostreams[-1]
    return result.url

def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]  

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def inSteals(from_):
    global steals
    if from_ in steals:
        return True
    return False
def appendSteals(from_):
    try:
        global steals
        if from_ in steals:
            return
        return steals.append(from_)
    except:
        return False
def clearSteals():
    global steals
    steals = []
    return
def slyric(to,text):
        try:
            r = requests.get("https://api.genius.com/search?q="+text+"&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data = r.json()
            hits = data["response"]["hits"][0]["result"]["api_path"]
            title= "\nTitle: "+data["response"]["hits"][0]["result"]["title"].strip()
            oleh = "\nArtis: "+data["response"]["hits"][0]["result"]["primary_artist"]["name"].strip()
            g = data["response"]["hits"][0]["result"]['song_art_image_thumbnail_url']
            r1 = requests.get("https://api.genius.com"+hits+"?&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data1 = r1.json()
            path = data1["response"]["song"]["path"]
            release = data1["response"]["song"]["release_date"]
            page_url = "http://genius.com" + path
            page = requests.get(page_url)
            html = BeautifulSoup(page.text, "html.parser")
            [h.extract() for h in html('script')]
            lyrics = html.find("div", class_="lyrics").get_text().strip()
            pesan = " 「 Lyric 」"+title+oleh+'\n'+lyrics
            k = len(pesan)//10000
            for aa in range(k+1):
                sendTextTemplate0(to,'{}'.format(pesan[aa*10000 : (aa+1)*10000]))
        except:
            sendTextTemplate0(to,"「 404 」\nStatus: Error\nReason: I'cant found lyric {}".format(text))
def picFinder(name):    
        try:
            rgram = requests.get('http://www.instagram.com/{}'.format(name))
            rgram.raise_for_status()
            selenaSoup=BeautifulSoup(rgram.text,'html.parser')
            pageJS = selenaSoup.select('script')
            for i, j in enumerate(pageJS):
                pageJS[i]=str(j)
            picInfo = sorted(pageJS,key=len, reverse=True)[0]
            allPics = json.loads(str(picInfo)[52:-10])['entry_data']['ProfilePage'][0]
            return allPics
        except requests.exceptions.HTTPError:
            return '\t \t ### ACCOUNT MISSING ###'

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+cl.google_url_shorten(links)
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']

def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Dzulkifli "
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
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            #mention = "@x\n"
            slen = str(len(textx))
            #elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            #textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Kak.. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention2"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
         
def logError(text):
    cl.log("[ DKBOTS ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def videosm(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp4=a.url
       cl.sendVideoWithURL(to,mp4)

def audiosm(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp3=a.url
       cl.sendAudioWithURL(to,mp3)

def videoyt(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp4=a.url
       data = {
                    "type": "video",
                    "originalContentUrl": mp4,
                    "previewImageUrl": "https://media.tenor.com/images/6d7761cb85acdb185ca243821e1b7339/tenor.gif",
                    }
       cl.postTemplate(to, data)


def videoyt1(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp4=a.url
       cl.sendVideoWithURL(to,mp4)

def audioyt(to,text):
       t = pafy.new(text)
       v=t.streams
       for a in v:
            mp3=a.url
       cl.sendAudioWithURL(to,mp3)
#============

def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def sendFlexxi(to, data):
  token = self.issueLiffView(to)
  url = 'https://api.line.me/message/v3/share'
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % token.accessToken
  }
  data = {
    'messages': [data]
  }
  res = requests.post(url, headers=headers, data=json.dumps(data))
  return res

def issueLiff(to, liff="1602687308-GXq4Vvk9"):
   anu = LiffContext(chat=LiffChatContext(to))
   itu = LiffViewRequest(liffId=liff, context=anu)
   lol = cl.liff.issueLiffView(itu)
   token = lol.accessToken
   return token 

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '?', '', '╰']]:
            result += '\n ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'
        
def sendtemp(data, mtoken=None):
     url = 'https://api.line.me/message/v3/share'
     header = {
            'Authorization': 'Bearer ' + mtoken,
            'User-Agent': 'Line/8.14.0',
            'Content-Type': 'application/json'
            }
     anu = _session.post(url=url, data=json.dumps(data), headers=header)
     return anu
##
def sendTemplate(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1602687308-GXq4Vvk9', context = xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)

def issueLiff(to, liff="1602687308-GXq4Vvk9"):
   anu = LiffContext(chat=LiffChatContext(to))
   itu = LiffViewRequest(liffId=liff, context=anu)
   lol = cl.liff.issueLiffView(itu)
   token = lol.accessToken
   return token 


def sendTemplate2(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

uagent = {
    "User-Agent": "Mozilla\t5.0"
}
  
def sendTemplateb(to, text):
  warnanya = ("#FF2800","#FFFD00","#C323FF","#FFFFFF")
  collor = ("#00FF00","#0000FF","#CCFF00","#9900FF")
  warna = random.choice(warnanya)
  coll = random.choice(collor)
  data = { "type": "flex","altText": " GANABAR","contents":
  {"type": "bubble","styles":{"body":{"backgroundColor":"#00FF00"}},"type":"bubble","size": "nano","body":{"contents":[{"contents":[{"type":"separator","color":coll},{"contents":[
  {"type":"separator","color":coll},
  {"text":text,"size":"xxs","align":"center","color": warna,"wrap":True,"weight":"bold","type":"text"},
  {"type":"separator","color":coll}
  ],"type":"box","spacing":"md","layout":"horizontal"},
  {"type":"separator","color":coll}
  ],"type":"box","layout":"vertical"},
  ],"type":"box","spacing":"xs","layout":"vertical"}},}
  cl.sendFlex(to, data)
def sendTemplate2 (to,text):
  data = { "type": "flex","altText": " GANABAR","contents":
  {"type": "bubble","styles":{"body":{"backgroundColor":"#00FF00"},"footer":{"backgroundColor":"#800000"}},"type":"bubble","body":
  {"contents":[{"contents":[{"type":"separator","color":"#ffffff"},
  {"contents":[{"type":"separator","color":"#ffffff"},{"type":"separator","color":"#ffffff"},
  {"text":"DarkBoT","size":"md","align":"center","color":"#BE1700","wrap":True,"weight":"bold","type":"text"},
  {"type":"separator","color":"#ffffff"},{"type":"separator","color":"#ffffff"}
  ],"type":"box","spacing":"md","layout":"horizontal"},
  {"type":"separator","color":"#ffffff"}],"type":"box","layout":"vertical"},
  {"contents":[{"type":"separator","color":"#ffffff"},
  {"contents":[{"type":"separator","color":"#ffffff"},{"type":"separator","color":"#ffffff"},
  {"type": "image","url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSk_wEerfoWmvALRkxFqBmcNU-ArkQz7Kh5P_oR1JuokMP5G60Y","size": "full","aspectRatio": "1:1"},
  {"type":"separator","color":"#ffffff"},{"type":"separator","color":"#ffffff"}
  ],"type":"box","spacing":"md","layout":"horizontal"},
  {"type":"separator","color":"#ffffff"}],"type":"box","layout":"vertical"},
  {"contents": [{"type":"separator","color":"#ffffff"},
  {"contents":[{"type":"separator","color":"#ffffff"},
  {"text": text,"size":"xs","color":"#33ffff","wrap":True,"weight":"bold","type":"text"},
  {"type":"separator","color":"#ffffff"}],"type":"box","spacing":"md","layout":"horizontal"},
  {"type":"separator","color":"#ffffff"}],"type":"box","layout":"vertical"},
  ],"type":"box","spacing":"xs","layout":"vertical"}},}
  cl.sendFlex(to, data)
def sendTemplate3(to,text):
  data = {"type": "flex","altText": "membagikan aplikasi","contents": {"type": "bubble","styles": style_biru,"header": {"type": "box","layout": "horizontal","contents": [sp_biru,{"type": "box", "layout": "vertical","contents": [sp_biru,{"type": "text","text": "Selfbot only","size": "xs","color": hijau,"align": "center","wrap": True},sp_biru,{"type": "text","text": "DaRkBoT","size": "xl","color": hijau,"align": "center","wrap": True},{"type":"image","url":image3,"aspectMode":"cover","aspectRatio": "20:13","size":"full"},sp_biru,{"type": "text","text": text,"size": "xs","color": biru,"wrap": True},sp_biru]},sp_biru]}}}
  cl.sendFlex(to, data)
def sendTemplate4(to, text):
  data = { "type": "flex","altText": " GANABAR","contents":
  {"type": "bubble",
  "styles":{"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#800000"}},
   "type":"bubble","body":
   {"contents":[
   {"contents":[
   {"type":"separator","color":"#ffffff"},
   {"type":"separator","color":"#ffffff"},
   {"contents":[
   {"type":"separator","color":"#ffffff"},
   {"type":"separator","color":"#ffffff"},
   {"url": logo,"type":"image"},
   {"type":"separator","color":"#ffffff"},
   {"type":"separator","color":"#ffffff"},
   {"type":"image","url": image1,"size":"xl"},
   {"type":"separator","color":"#ffffff"},
   {"type":"separator","color":"#ffffff"}
   ],"type":"box","spacing":"md","layout":"horizontal"},
   {"type":"separator","color":"#ffffff"},
   {"contents":[
   {"type":"separator","color":"#ffffff"},
   {"text": text,"size":"sm","color":"#33ffff","wrap":True,"weight":"bold","type":"text"},
   {"type":"separator","color":"#ffffff"}
   ],"type":"box","spacing":"md","layout":"horizontal"},
   {"type":"separator","color":"#ffffff"}
   ],"type":"box","layout":"vertical"},
   ],"type":"box","spacing":"xs","layout":"vertical"}},}
  cl.sendFlex(to, data) 
  
def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost  


def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost  

def dktag(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            "animated": True,
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} Dragon_Killer".format(clientProfile.displayName),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": str(wait["Respontag"]),
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} Dragon_Killer".format(clientProfile.displayName),
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)


def dklike(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://l.top4top.io/p_1558gnum30.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/ZmKtkwg/cara-mendapatkan-banyak-like-fanspage-facebook-768x512-png.webp",
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/ZmKtkwg/cara-mendapatkan-banyak-like-fanspage-facebook-768x512-png.webp",
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} Dragon_Killer".format(clientProfile.displayName),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": "Like Sukses",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} Dragon_Killer".format(clientProfile.displayName),
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/ZmKtkwg/cara-mendapatkan-banyak-like-fanspage-facebook-768x512-png.webp",
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/ZmKtkwg/cara-mendapatkan-banyak-like-fanspage-facebook-768x512-png.webp",
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/ZmKtkwg/cara-mendapatkan-banyak-like-fanspage-facebook-768x512-png.webp",
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)


def dkaudio(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"] 
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
    "type": "flex",
    "altText": "{} Dragon_Killer".format(clientProfile.displayName),
    "contents":{
#{
  "type": "bubble",
  "size": "nano",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": Bag1,
        "size": "full",
        "animated": True,
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
        "position": "absolute",
        "aspectMode": "fit",
        "aspectRatio": "1:1",
        "offsetTop": "0px",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "size": "full"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "text",
                    "text": text,
                    "size": "xxs",
                    "color": Font,
                    "decoration": "line-through"
                  }
                ],
                "borderWidth": "2px",
                "borderColor": "#FF69B4",
                "backgroundColor": "#00ffff"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                  }
                ],
                "spacing": "xs",
                "offsetBottom": "30px",
                "offsetStart": "3px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                        "color": Font,
                        "size": "xxs",
                        "flex": 0,
                        "align": "end"
                      }
                    ],
                    "flex": 0,
                    "spacing": "lg"
                  }
                ]
              }
            ],
            "spacing": "xs"
          }
        ],
        "position": "absolute",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#FF69B4"
  }
}
}
    cl.postTemplate(to, data)


def dkbot(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"] 
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
               "type": "flex",
               "altText": "menu", 
               "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"cornerRadius": "xxl",
"borderWidth": "1px",
"borderColor": warnanya1,
"type": "box",
"layout": "horizontal",
"spacing": "md",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": Font,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "5px", #GESER SAMPING 
"backgroundColor": "#00FF00",
"height": "25px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": text,
"size": "xs",
"color": Font,
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "230px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
]
}
}
    cl.postTemplate(to, data)



def dragonkiller(to, text):
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    data = {
    "type": "flex",
    "altText": "{} Dragon_Killer".format(clientProfile.displayName),
    "contents":{
  "type": "bubble",
  "size": Tampilan1,
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {  
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "color": Font,
            "wrap": True,
            "offsetStart": "3px"
          }
        ],
        "margin": "xs",
        "spacing": "md",
        "backgroundColor": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "action": {
          "type": "uri",
          "uri": str(settings["idline"])
        },
        "contents": [
          {
            "type": "text",
            "text": str(settings["lebel"]),
            "align": "center",
            "color": Font,
            "size": "xs"
          }
        ],
        "paddingAll": "2px",
        "backgroundColor": "#00FF00",
        "margin": "xs"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#F7141F",
    "cornerRadius": "10px",
    "spacing": "xs"
  },
  "styles": {
    "body": {
      "backgroundColor": "#ffff00"
    }
  }
}
}
    cl.postTemplate(to, data)

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
        'X-Line-Access': cl.authToken,
        'X-Line-Application': cl.server.APP_NAME,
        'X-Line-ChannelId': '1602687308',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
                
def sendflex(to, data):
    n1 = LiffChatContext(to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

uagent = {
    "User-Agent": "Mozilla\t5.0"
}

def dragonkiller2(to, text):
    Font = wait["warna"]
    Tampilan1 = wait["size"]
    data = {
    "type": "flex",
    "altText": "{} Dragon_Killer".format(clientProfile.displayName),
    "contents":{
  "type": "bubble",
  "size": Tampilan1,
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {  
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "color": Font,
            "wrap": True,
            "offsetStart": "3px"
          }
        ],
        "margin": "xs",
        "spacing": "md",
        "backgroundColor": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "action": {
          "type": "uri",
          "uri": str(settings["idline"])
        },
        "contents": [
          {
            "type": "text",
            "text": str(settings["lebel"]),
            "align": "center",
            "color": Font,
            "size": "xs"
          }
        ],
        "paddingAll": "2px",
        "backgroundColor": "#00FF00",
        "margin": "xs"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#F7141F",
    "cornerRadius": "10px",
    "spacing": "xs"
  },
  "styles": {
    "body": {
      "backgroundColor": "#ffff00"
    }
  }
}
}
    cl.sendFlex(to,data)

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost

 
def sendTextTemplate3(to, text):
    Bag1 = wait["BAGHELP"]
    Font = wait["warna"]
    Tampilan1 = wait["size"]
    data = {
            "type": "flex",
            "altText": "BOTS",
            "contents": {
  "type": "bubble",
  "size": Tampilan1,
      "body": {
    "cornerRadius": "xxl",
    "borderWidth": "5px",
    "borderColor": warnanya1,
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "weight": "bold",
            "wrap": True,
            "color": Font
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 1,
              "style": "primary",
              "color": "#00FF00",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "D",
                  "uri": "http://line.me/ti/p/~nirwanabjn"
              }
          }, {
              "flex": 1,
              "type": "button",
              "style": "primary",
              "color": "#00FF00",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "K",
                  "uri": "http://line.me/ti/p/~nirwanabjn"
              }
          }]
      }]
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplateku(to, text):
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    data = {
            "type": "flex",
            "altText": "GANABAR",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#00FF00"
    },
    "footer": {
      "backgroundColor": "#FF0000"
    }
  },
  "type": "bubble",
  "size": Tampilan1,
      "body": {
    "contents": [
      {
        "contents": [
          {
            "type": "image",
        "url": "https://i.ibb.co/phmqpP3/images-2.jpg",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "type": "image",
        "url": "https://i.ibb.co/7p3FFBt/1541341062445.jpg",
        "size": "xl",
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "type": "image",
        "url": "https://lh6.googleusercontent.com/proxy/LNw-fbsMb8WXu3ogbg0oUzufD7b-nAeq7OIbjS5ctfs4Y759365RSPtnhUgZ-gV9GosIMYpnta2vNDF9Gnt9gVWz1pfI9Q=s0-d", #bbm
        "size": "xl",
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "{}".format(client.getProfile().displayName),
                "size": "md",
                "margin": "none",
                "color": "#7CFC00",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "url": "https://media1.giphy.com/media/bcHAlWJo9DtwQ/200w.webp?cid=19f5b51a5c81ff76716b31794171328d",
                "type": "icon",
                "size": "md"
              },
              {
                "text":  text,
                "size": "xxs",
                "margin": "none",
                "color": Font,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 1,
              "style": "primary",
              "color": "#00FF00",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "D",
                  "uri": "http://line.me/ti/p/~nirwanabjn"
              }
          }, {
              "flex": 1,
              "type": "button",
              "style": "primary",
              "color": "#00FF00",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "K",
                  "uri": "http://line.me/ti/p/~nirwanabjn"
              }
          }]
      }]
  }
}
}
    cl.postTemplate(to, data)                
 
def sendTextTemplate3b(to, text):
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    Bag1 = wait["BAGHELP"]
    data = {
            "type": "flex",
            "altText": "BOTS",
            "contents": {
  "type": "bubble",
  "size": Tampilan1, 
      "body": {
    "cornerRadius": "xxl",
    "borderWidth": "2px",
    "borderColor": warnanya1,
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "weight": "bold",
            "wrap": True,
            "color": Font
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#00FF00"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate3c(to, text):
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    Bag1 = wait["BAGHELP"]
    data = {
            "type": "flex",
            "altText": "BOTS",
            "contents": {
  "type": "bubble",
  "size": Tampilan1,
      "body": {
    "cornerRadius": "xxl",
    "borderWidth": "2px",
    "borderColor": warnanya1,
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "weight": "bold",
            "wrap": True,
            "color": Font
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "696969"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "3:3",
     "aspectMode": "cover",
     "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
     "size": "full",
     "margin": "xl"
  
  }
}
}
    cl.postTemplate(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~nirwanabjn"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)

def dkgc1(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            "animated": True,
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": text,
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Ready Vcall",
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)
def dkgc2(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            "animated": True,
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": text,
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Rehat Vcall",
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def dkgc3(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            "animated": True,
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": text,
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Panggilan Kojom",
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def dkgc4(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "animated": True,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": text,
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Kojom Off",
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def dkgc5(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "animated": True,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": text,
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Live Cermin On",
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def dkgc6(to, text):
    Bag1 = wait["BAGHELP"] 
    Font = wait["warna"]
    Fontb = wait["warna1"]
    warna1 = ("#FF00FF","#DC143C","#FFFF00","#FF4500","#FF00FF","#00BFFF","#FF1493")
    warnanya1 = random.choice(warna1)
    data = {
                            "type":"flex",
                            "altText": "Self",
                            "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            "animated": True,
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "-3px",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "cornerRadius": "3px",
            "offsetStart": "41px",
            "height": "14px",
            "offsetBottom": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "width": "50px",
            "height": "74px",
            "offsetTop": "2px",
            "offsetEnd": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "width": "31px",
            "height": "31px",
            "position": "absolute",
            "offsetBottom": "5px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "31px",
            "height": "31px",
            "offsetTop": "5px",
            "offsetStart": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetTop": "45px",
            "width": "25px",
            "height": "25px",
            "offsetStart": "6px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": "#FF2800",
                "offsetTop": "0px"
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "borderColor": "#ff00ff",
            "offsetStart": "64px",
            "offsetBottom": "65px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "size": "xxs",
                "color": "#00FFFF",
                "wrap": True,
                "text": text,
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "33px",
            "offsetStart": "41px",
            "width": "111px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "LiVe Off",
                "size": "xxs",
                "color": "#00FFFF",
                "offsetTop": "-2px"
              }
            ],
            "position": "absolute",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetBottom": "17px",
            "offsetStart": "59px",
            "height": "15px",
            "width": "93px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "height": "15px",
            "width": "15px",
            "offsetBottom": "17px",
            "offsetStart": "43px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "position": "absolute",
            "width": "13px",
            "height": "8px",
            "offsetBottom": "35px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetEnd": "8px",
            "offsetTop": "1px",
            "cornerRadius": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "13px",
            "height": "13px",
            "borderColor": "#ff00ff",
            "borderWidth": "1px",
            "offsetTop": "1px",
            "offsetStart": "45px",
            "cornerRadius": "30px"
          }
        ],
        "paddingAll": "0px",
        "borderColor": "#ff00ff",
        "borderWidth": "2px",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def dkbots2(to, text):
    #data = {
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    Bag1 = wait["BAGHELP"]
    Tampilan1 = wait["size"]
    data = {
            "type": "flex",
            "altText": "♻Selfʙᴏᴛᴢ™♻",
            "contents": 
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": Tampilan1,
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "animated": True,
            "position": "absolute",
            "size": "full",
            "aspectMode": "cover"
          },
          {
            "type": "image",
            "url": Bag1,
            "animated": True,
            "size": "full",
            "aspectMode": "cover",
            "position": "absolute",
            "aspectRatio": "2:6",
            "flex": 0,
            "offsetBottom": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": Font,
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "size": "xxs",
                "aspectMode": "cover",
                "flex": 0
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": str(settings["lebel"]),
                    "color": Font,
                    "size": "xxs"
                  },
                  {
                    "type": "separator",
                    "color": "#00FFFF"
                  },
                  {
                    "type": "text",
                    "text": "⏱ "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                    "color": Font,
                    "size": "xxs"
                  }
                ],
                "borderColor": "#00FFFF",
                "borderWidth": "1px"
              }
            ],
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": text,
                "wrap": True,
                "size": "xs",
                "color": Font
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/dzee123"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/camera/"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://www.smule.com/KSS_OFFICE"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/cameraRoll/multi"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/timeline"
                }
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "relative",
            "offsetBottom": "0px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#FFD700"
        }
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def backupData():
    try:
        backup = settings
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def dkbots2ji(to, text):
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    data = {
                                       "type": "flex",
                                       "altText": "Self V2020",
                                       "contents": 
{
"type": "bubble",
"size": Tampipan1,
"body": {
"backgroundColor": "#00FF00",
"type": "box",
"layout": "vertical",
"contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#ffffff"            
      },
      {
        "type": "separator",
        "color": "#ffffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#ffffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": Font,
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ⁴",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#ffffff"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dheaken",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#ffffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": Font,
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#ffffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": Font,
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#ffffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#ffffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": Font,
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#ffffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~dkdkbot",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/Dhe4kenZ",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def Kifli1(to, text):
    warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
    warnanya1 = random.choice(warna1)
    data = {
                                        "type": "flex",
                                        "altText": "Self",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
{
"type": "image", #Wall 1
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcScz24KjDq9VEyCU0klrsStZawPbYTS2qtQRQ&usqp=CAU",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:1",
"gravity": "bottom",
"action": {
"uri": "line://nv/profilePopup/mid=u88c891fb131717a670c6903ab066b0ce",
"type": "uri",
}
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Â¥75,000",
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "xxl"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": " ",
                        "color": "#ffffff",
                        "flex": 0,
                        "size": "xxs"
                      }
                    ],
                    "spacing": "sm"
                  }
                ],
                "borderWidth": "3px",
                "cornerRadius": "10px",
                "spacing": "sm",
                "borderColor": warnanya1,
                "margin": "xs",
                "height": "30px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "1px",
            "offsetStart": "1px",
            "offsetEnd": "1px",
            "backgroundColor": "#FF7F00",
            "paddingAll": "1px",
            "paddingTop": "0px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "Â¥75,000",
                    "color": "#ffffffcc",
                    "decoration": "line-through",
                    "gravity": "bottom",
                    "flex": 0,
                    "size": "sm"
                  }
                ],
                "spacing": "xxl"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "  Creator",
                        "color": "#ffffff",
                        "flex": 0,
                        "size": "xxs"
                      }
                    ],
                    "spacing": "sm"
                  }
                ],
                "borderWidth": "2px",
                "cornerRadius": "10px",
                "spacing": "sm",
                "borderColor": warnanya1,
                "margin": "xs",
                "height": "20px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "18px",
            "offsetStart": "6px",
            "offsetEnd": "7px",
            "backgroundColor": "#FF7F00",
            "paddingAll": "0px",
            "paddingTop": "6px"
          },
          {
"type": "box",
"layout": "horizontal",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/QJk6V8j/line-logo-messenger-glossy-png-7.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~dadmom18",   
},
"flex": 1
},{
"type": "image",
"url": "https://i.ibb.co/4tHgtc7/20200608-104257.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/MHTS_____a1213z",
},
"flex": 1
},{
"type": "image",
"url": "https://i.ibb.co/mJhk3PH/Aws-icon.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 1
},{
"type": "image",
"url": "https://i.ibb.co/CJSv8kD/Youku-icon.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "https://youtube.com"
},
"flex": 1
},{
"type": "image",
"url": "https://i.ibb.co/g39VTjy/Photobucket-icon.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/camera/"
},
"flex": 1
},{
"type": "image",
 "url": "https://i.ibb.co/wgGBTyv/Technorati-icon.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "xl",
"action": {
"type": "uri",
"uri": "line://nv/chat",
},
"flex": 1
}
],
"position": "absolute",
"offsetTop": "20px",
"offsetStart": "9px",
"height": "200px",
"width": "105px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"text": text,
"size": "xxs",
"align": "center",
"color": "#ffffff",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"position": "absolute",
"cornerRadius": "7px",
"offsetTop": "4px",
"backgroundColor": warnanya1,
"offsetStart": "9px",
"height": "15px",
"width": "141px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"text": "Self",
"size": "xxs",
"align": "center",
"color": "#ffffff",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "24px",
#"backgroundColor": colornya3,
"offsetStart": "65px",
"height": "15px",
"width": "142px"
}
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def sendTextTemplate0(to, text):
    warna1 = ("#1AE501","#0108E5","#696969","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
    warnanya1 = random.choice(warna1)
    data = {
  "type": "bubble",
  "size": "nano",
"body": {
"backgroundColor": "#00FF00",
"type": "box",
"borderWidth": "2px",
"borderColor": warnanya1,
"cornerRadius": "0px",
"layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "borderWidth": "1px",
            "borderColor": warnanya1,
            "cornerRadius": "10px",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "aspectMode": "cover",
                "size": "full",
                "gravity": "top"
              }
            ],
            "cornerRadius": "100px",
            "width": "30px",
            "height": "30px"
           },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [
                  {
                    "type": "span",
                    "text": text,
                    "color":warnanya1,
                  }
                ],
                "size": "xxs",
                "wrap": True
              }
            ],
          }
        ],
        "spacing": "xs",
        "paddingAll": "0px"
      },
    ],
    "paddingAll": "0px"
  }
}
    cl.postFlex(to, data)

def sendTextTemplate1(to, text):
    Tampilan1 = wait["size"]
    Font = wait["warna"]
    Bag1 = wait["BAGHELP"]
    data = {
                                        "type": "flex",
                                        "altText": "Selfbot",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": Tampilan1,
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "image",
            "url": Bag1,
            "animated": True,
            "gravity": "bottom",
            "size": "xxl",
            "aspectMode": "cover",
            "aspectRatio": "3:1",
            "offsetTop": "0px",
            "action": {
            "uri": "https://youtu.be/VSzi1KfMnNY",
            "type": "uri",
            }
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "#Brown's T-shirts",
                    "size": "xxs",
                    "color": Font,
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Creator",
                        "offsetStart": "30px",
                        "offsetTop": "0px",
                        "color": "#ffffff",
                        "flex": 0,
                        "size": "sm"
                      }
                    ],
                    "spacing": "lg"
                  }
                ],
                "borderWidth": "0px",
                "cornerRadius": "0px",
                "spacing": "xxl",
                "borderColor": "#C71585",
                "margin": "xs",
                "height": "0px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "20px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#FF7F00",
            "paddingAll": "10px",
            "paddingTop": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "text": text,
                "size": "xxs",
                "align": "center",
                "color": Font,
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "position": "absolute",
            "cornerRadius": "5px",
            "offsetTop": "5px",
            "backgroundColor": "#0F7AA8",
            "offsetStart": "5px",
            "height": "15px",
            "width": "150px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
}
    cl.postTemplate(to, data)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~dkdkbot"
           }                                                
 }
]
                          }
                      }
    client.postTemplate(to, data)

def welcomeMembers(to, mid): 
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "bye bye"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)

def searchRecentMessages(to,id):
    for a in cl.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            cl.sendMessage(to, text, {'MSG_SENDER_NAME': cl.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + cl.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            cl.sendMessage(to, text, {'MSG_SENDER_NAME': cl.getContact("u9f8cee586b688da75f20a81487398ed6").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + cl.getContact("u9f8cee586b688da75f20a81487398ed6").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def sendMention2(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            cl.sendMessage(to, text, {'MSG_SENDER_NAME': cl.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + cl.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            cl.sendMessage(to, text, {'MSG_SENDER_NAME': cl.getContact(mid).displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + cl.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)

def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()

def inSteals(from_):
    global steals
    if from_ in steals:
        return True
    return False
def appendSteals(from_):
    try:
        global steals
        if from_ in steals:
            return
        return steals.append(from_)
    except:
        return False
def clearSteals():
    global steals
    steals = []
    return

def slyric(to,text):
        try:
            r = requests.get("https://api.genius.com/search?q="+text+"&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data = r.json()
            hits = data["response"]["hits"][0]["result"]["api_path"]
            title= "\nTitle: "+data["response"]["hits"][0]["result"]["title"].strip()
            oleh = "\nArtis: "+data["response"]["hits"][0]["result"]["primary_artist"]["name"].strip()
            g = data["response"]["hits"][0]["result"]['song_art_image_thumbnail_url']
            r1 = requests.get("https://api.genius.com"+hits+"?&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data1 = r1.json()
            path = data1["response"]["song"]["path"]
            release = data1["response"]["song"]["release_date"]
            page_url = "http://genius.com" + path
            page = requests.get(page_url)
            html = BeautifulSoup(page.text, "html.parser")
            [h.extract() for h in html('script')]
            lyrics = html.find("div", class_="lyrics").get_text().strip()
            pesan = " 「 Lyric 」"+title+oleh+'\n'+lyrics
            k = len(pesan)//10000
            for aa in range(k+1):
                dragonkiller(to,'{}'.format(pesan[aa*10000 : (aa+1)*10000]))
        except:
            dragonkiller(to,"「 404 」\nStatus: Error\nReason: I'cant found lyric {}".format(text))

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            noobcoder.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+noobcoder.google_url_shorten(links)
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah

def a2():
    now2 = datetime.datetime.now()
    nowT = datetime.datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items

def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def helpvirus():
    helpKvirus2 = """
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.
"""
    return helpKvirus2

def helpcek():  
    helpKcek = "• Cek js\n" + \
                  " • Cek idline\n" + \
                  " • Cek lebel\n" + \
                  " • Cek bypas\n" + \
                  " • Cek coment post\n" + \
                  " • Cek mention\n" + \
                  " • Cek sider\n" + \
                  " • Cek spam\n" + \
                  " • Cek pesan \n" + \
                  " • Cek respon \n" + \
                  " • Cek welcome\n" + \
                  " • ➥Next Key[ Token ]\n\n" + \
                  "「 Thanks to :↘ ̶ ̶D̶ᴋ̶ ̶ʙ̶ᴏ̶ᴛ̶ ̶ ̶ \n"                 
    return helpKcek
 
def helpset():  
    helpKset = "• Setbaghelp:「Text」 \n" + \
                  " • Set lebel:「Text」\n" + \
                  " • Set idline:「Text」\n" + \
                  " • Set mention:「Text」\n" + \
                  " • Set sider:「Text」\n" + \
                  " • Set pesan:「Text」\n" + \
                  " • Set respon:「Text」\n" + \
                  " • Set leave:「Text」\n" + \
                  " • Set welcome:「Text」\n" + \
                  " • Set warnahtext「Text」\n" + \
                  " • Set warnahbody「Text」\n" + \
                  " • Set coment:「Text」\n"
    return helpKset

def helpsetgroup():
    helpK3 = "      ◀  SETTING SELF▶ \n" + \
                  " •──────•\n" + \
                  " • Cek coment post\n" + \
                  " • Cek mention\n" + \
                  " • Cek sider\n" + \
                  " • Cek spam\n" + \
                  " • Cek pesan \n" + \
                  " • Cek respon \n" + \
                  " • Cek welcome\n" + \
                  " • Setbaghelp: \n" + \
                  " • Set mention:「Text」\n" + \
                  " • Set sider:「Text」\n" + \
                  " • Set pesan:「Text」\n" + \
                  " • Set respon:「Text」\n" + \
                  " • Set leave:「Text」\n" + \
                  " • Set welcome:「Text」\n" + \
                  " • Set coment:「Text」\n" + \
                  " •➥Next Key [ Protection ]\n" + \
                  " •───────────────•\n" + \
                  "「 Thanks to :↘ ̶ ̶Dᴋ̶ ̶ʙ̶ᴏ̶ᴛ̶ ̶ ̶  •\n • DRAGON-KILLER •\n"
    return helpK3
 
def helpmedia(): 
    helpK2 = " • Menu\n" + \
                  " • /vid「txt」\n" + \
                  " • /audiocal「txt」\n" + \
                  " • /musikal「txt」\n" + \
                  " • Hiburanmp3「txt」\n" + \
                  " • Joox「txt」\n" + \
                  " • .joox「txt」\n" + \
                  " • .bokep「txt」\n" + \
                  " • Okep「txt」\n" + \
                  " • Get-mimpi「txt」\n" + \
                  " • Lyrics「txt」\n" + \
                  " • Topnews「txt」\n" + \
                  " • .smuleaudi「Link」\n" + \
                  " • .smulevideo「Link」\n" + \
                  " • Love on\off\n" + \
                  " • Bday on\off\n" + \
                  " • Mylove a@\n" + \
                  " • Bday @\n" + \
                  " • Smuleqr on\off\n" + \
                  " • Rsmule id\n" + \
                  " • Yutubeqr on\off\n" + \
                  " • Xsmule「txt」\n" + \
                  " • !smule「txt」\n" + \
                  " • Chatbot on\off\n" + \
                  " • Bc audio\n" + \
                  " • Bc image\n" + \
                  " • Bc video「txt」\n"
    return helpK2 



 

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "• Getpict @\n" + \
                  "." + key + " Getcover\n" + \
                  "." + key + " Cfoto\n" + \
                  "." + key + " Pplu\n" + \
                  "." + key + " Ppme\n" + \
                  "." + key + " Cvp\n" + \
                  "." + key + " Gname「Text」\n" + \
                  "." + key + " Status\n" + \
                  "." + key + " Url (Ambil link)\n" + \
                  "." + key + " Glist\n" + \
                  "." + key + " Kepoin @\n" + \
                  "." + key + " Payment\n" + \
                  "." + key + " Tf\n" + \
                  "." + key + " Link on|off\n" + \
                  "." + key + " Bye me\n" + \
                  "." + key + " Midcontact (mid)\n" + \
                  "." + key + " Unsend (numb)\n" 
    return helpMessage

def helpjs():
    key = Setmain["keyCommand"]
    key = key.title()
    helpK4 = "◀Menu JS▶ \n" + \
                  "." + key + " /cancell: Numb tatget\n" + \
                  "." + key + " /Unsend1\n" + \
                  "." + key + " Tampol [name]\n" + \
                  "." + key + " /js: Numb\n" + \
                  "." + key + " /bypass: Numb\n" + \
                  "." + key + " /@sepak\n" + \
                  "." + key + " /@bola\n" + \
                  "." + key + " Autojoinbypass on/off\n" + \
                  "." + key + " Autojoinjs on/off\n" + \
                  "." + key + " Glist\n" + \
                  " • ➥Next Key[ Token ]\n\n" + \
                  " •────────•\n" + \
                  "「 Thanks to :↘ ̶ ̶D̶ᴋ̶ ̶ʙ̶ᴏ̶ᴛ̶ ̶ ̶ \n"                 
    return helpK4

def helpadd():
    key = Setmain["keyCommand"]
    key = key.title()
    helpK5 = "◀Menu Add▶ \n" + \
                  "." + key + " Addsticker「Text」\n" + \
                  "." + key + " Dellsticker「Text」\n" + \
                  "." + key + " Liststicker\n" + \
                  "." + key + " Addsuara「Text」\n" + \
                  "." + key + " Dellsuara「Text」\n" + \
                  "." + key + " Listsuara\n" + \
                  "." + key + " Addimg「Text」\n" + \
                  "." + key + " Dellimg「Text」\n" + \
                  "." + key + " Listimg\n" + \
                  "." + key + " Addmp4「Text」\n" + \
                  "." + key + " Dellmp4「Text」\n" + \
                  "." + key + " Listmp4\n" + \
                  "." + key + " Add @\n" + \
                  "." + key + " Block @\n" + \
                  "「 Thanks to :↘ ̶ ̶D̶ᴋ̶ ̶ʙ̶ᴏ̶ᴛ̶ ̶ ̶ \n"                 
    return helpK5
 
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "ProTection\n\n" + \
                  "." + key + "pro-all on\n" + \
                  "." + key + "Protectqr On\n" + \
                  "." + key + "Protectjoin On\n" + \
                  "." + key + "Protectkick On\n" + \
                  "." + key + "Protectcancel On\n" + \
                  "." + key + "• ➥Next Key[ Token ]\n" + \
                  "." + key + "•────────•\n" + \
                  "." + key + "「 Thanks to :↘ ̶ ̶D̶ᴋ̶ ̶ʙ̶ᴏ̶ᴛ̶ ̶ ̶ \n"                 
    return helpMessage1
#=================================================================================
def sendMessage(text, to, _from, toType=0, contentMetadata=0):

    msg = Message()

    if to[0] == "c":

        msg.to = to
        msg._from = _from
        msg.toType = 2

    elif to[0] == "u":
        msg.to = _from
        msg._from = to
        msg.toType = 0

    if contentMetadata:
        msg.contentMetadata = contentMetadata

    msg.text = text

    cl.sendMessage(msg)

def RECEIVE_MESSAGE(op):

    msg = op.message
    # print(msg)
    print(
    " TO: {}\n".format(msg.to),
    "FROM: {}\n".format(msg._from),
    "TEXT: {}\n".format(msg.text),
    "CONTENT TYPE: {}\n".format(msg.contentType),
    "METADATA: {}\n".format(msg.contentMetadata),
    "TYPE: {}\n".format(msg.toType),
    "MESSAGE ID: {}\n".format(msg.id),
    "DATE: {}\n\n".format(msg.createdTime)
    )


def lineBot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            print ("DONE")
            return
        if op.type == 2:
          if wait["notifProfile"] == True:
           if op.param1 in Notifbot["notif"]:
             pass
           else:
                men=op.param1
                contact=cl.getContact(men)
                n1=contact.displayName
                n2=contact.statusMessage
                n3=contact.pictureStatus
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                G = cl.getGroupIdsJoined()
                cgroup = cl.getGroups(G)
                for x in range(len(cgroup)):
                  gMem = [contact.mid for contact in cgroup[x].members]
                  if men in gMem:
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    #mek = "ɴᴏᴛɪғ ᴜᴘᴅᴀᴛᴇ ᴘʀᴏғɪʟᴇ\nsɪ ᴊᴏɴᴇs @! "
                    #mek += "\n •  ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%d-%m-%Y')
                    #mek += "\n •  ᴡᴀᴋᴛᴜ : " + datetime.strftime(timeNow,'%H:%M:%S')
                    #mek += "\n •  ʙɪᴏ :" + contact.statusMessage
                    #sendMentionV2(cgroup[x].id, mek,[op.param1])
                    #cl.sendImageWithURL(cgroup[x].id, str(image))
                    warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                    warnanya1 = random.choice(warna1)
                    Bagnotif = wait["BAGNOTIFPROFILE"]
                    dataa = {
                                              "type": "flex",
                                              "altText": "ɴᴏᴛɪғ ᴜᴘᴅᴀᴛᴇ ᴘʀᴏғɪʟᴇ",
                                              "contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "kilo",
"body": {
"type": "box",
"cornerRadius": "10px",
"layout": "horizontal",
"contents": [
{
"type": "image",
"url": Bagnotif,
"animated":True,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "16:5",
"offsetTop": "0px"
},
#=================
{
"type": "box",
"borderWidth": "2px",
"borderColor": warnanya1,
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px"
}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "2px",
"offsetStart": "5px",
"height": "75px",
"width": "75px"
},  #=======atas pp
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/0hbFz7_LU-PWlHThUm28JCPnsLMwQwYDshPyomDzJHMQ4_fnJqfHtxX2JOal1tK3ltKysiC2Ica106",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "100px",
"offsetTop": "40px", #ATAS BAWAH
"offsetStart": "220px", #KIRI KANAN
"height": "35px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "𝐍𝐎𝐓𝐈𝐅 𝐔𝐏𝐃𝐀𝐓𝐄 𝐏𝐑𝐎𝐅𝐈𝐋𝐄",
"weight": "bold",
"color": warnanya1,
"align": "center",
"size": "xs",
"wrap": True,
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "2px", #ATAS BAWAH
#"backgroundColor": "#FF7F00",
"offsetStart": "70px", #KIRI KANAN
"height": "30px",
"width": "180px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "{}".format(contact.displayName),
"weight": "bold",
"color": warnanya1,
"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "17px", #ATAS BAWAH
#"backgroundColor": "#FF7F00",
"offsetStart": "100px", #KIRI KANAN
"height": "50px",
"width": "130px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "{}".format(contact.statusMessage),
"weight": "bold",
"color": warnanya1,
"align": "center",
"size": "xxs",
"wrap": True,
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "30px", #ATAS BAWAH
#"backgroundColor": "#FF7F00",
"offsetStart": "80px", #KIRI KANAN
"height": "50px",
"width": "170px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                    to = cgroup[x].id
                    cl.postTemplate(to, dataa)



        if op.type == 25 or op.type == 26:        				
          if wait['undang'] == True:
            msg = op.message
            user = msg._from
            kirim = msg.to    	
            if msg.contentType == 13:
                #if wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            dragonkiller(msg.to, _name + " Sudah hadir dalam grup")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(kirim,[target])
                                cl.cl(msg.to,"undang " + _name + "\nSUCCESS..")
                                wait['undang'] = False
                                break
                            except:             
                                 dragonkiller(msg.to, 'Sukse Bos')
                                 wait['undang'] = False
                                 break

        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass

        if op.type == 13:
            if clientMID in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate4(op.param1,"ᴛʀɪᴍᴀᴋᴀsɪʜ sᴜᴅᴀʜ ɪɴᴠɪᴛᴇ ᴋᴇ\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        dragonkiller(op.param1,"Trimakasih sudah invite " + str(ginfo.name))
          

        if op.type == 13 or op.type == 124:
            if clientMID in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate3b(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate3b(op.param1,"Haii " + str(ginfo.name))
            
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass
								
        if op.type == 13 or op.type == 124:
            if clientMID in op.param3:
                if wait["autoJoinbypass"]:
                    cl.acceptGroupInvitation(op.param1)
                    group = cl.getGroup(op.param1)
                    cmd = 'god2.js gid={} token={}'.format(op.param1,cl.authToken)
                    members = [o.mid for o in group.members if o.mid not in admin and o.mid not in Bots and o.mid not in wait["staff"]]
                    for o in group.members:
                        if o.mid not in admin and o.mid not in Bots and o.mid not in wait["staff"]:
                            cmd += ' uid={}'.format(o.mid)
                    success = execute_js(cmd)
                    cl.sendMessage(to, "Haii .. thanks 😂\n.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.\n [[PRIMAZ CYBER]]\n.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.\n [[ PRIMAZ CYBER ]]\n.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A")
                    print(cmd)

        if op.type == 13 or op.type == 124:
            if clientMID in op.param3:
                if wait["autoJoinjs"]:
                    cl.acceptGroupInvitation(op.param1)
                    group = cl.getGroup(op.param1)
                    cmd = 'god1.js gid={} token={}'.format(op.param1,cl.authToken)
                    members = [o.mid for o in group.members if o.mid not in admin and o.mid not in Bots and o.mid not in wait["staff"]]
                    for o in group.members:
                        if o.mid not in admin and o.mid not in Bots and o.mid not in wait["staff"]:
                            cmd += ' uid={}'.format(o.mid)
                    success = execute_js(cmd)
                    cl.sendMessage(to, "Haii .. thanks 😂\n.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.\n [[PRIMAZ CYBER]]\n.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.\n [[ PRIMAZ CYBER ]]\n.1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0.A")
                    print(cmd)


        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                else:
                    Bag1 = wait["BAGHELP"]
                    g = cl.getGroup(op.param1)
                    contact = cl.getContact(op.param2)
                    gname = g.name
                    name = contact.displayName
                    contactlist = cl.getAllContactIds()
                    cover = cl.getProfileCoverURL(op.param2)
                    pp = contact.pictureStatus
                    dk = "GROUP : {}\n".format(gname)+str(settings["joincom"])
                    warna1 = ("#F7141F","#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                    warnanya1 = random.choice(warna1)
                    warna2 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                    warnanya2 = random.choice(warna2)
                    data = {
                     "type": "flex",
                     "altText": "WELLCOME",
                     "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "action": {
          "type": "uri",
          "uri": str(settings["idline"])
        },
        "contents": [
          {
            "type": "image",
             "url": "https://profile.line-scdn.net/" + str(pp),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                   "type": "text",
                   "text": dk,
                   "align": "center",
                   "size": "xxs",
                   "weight": "regular",
                   "color": warnanya2,
                   "wrap": True,
                  }
                ],
                 "paddingAll": "0px",
                "borderWidth": "2px",
                "borderColor": "#00FF00",
                "cornerRadius": "10px",
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "{}".format(name),
                        "size": "xxs",
                        "color": "#F7141F",
                        "flex": 0,
                        "offsetTop": "-3px",
                        "wrap": True,
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "10px",
                "spacing": "sm",
                "borderColor": "#00FF00",
                "margin": "xs",
                "height": "20px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#FF7F00",
            "paddingAll": "5px",
            "paddingTop": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-szpY7e3hLY8/Xgi72YpOl1I/AAAAAAAAPaQ/YoDK99w50vQJVchqll60Tj_YhM-ji_ljACLcBGAsYHQ/s1600/20191229_224215.jpg",  #wa
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "backgroundColor": "#ff334b",
            "offsetStart": "2px",
            "height": "20px",
            "width": "20px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
#
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-bevIwpHmmP0/XgApY74fO8I/AAAAAAAAPZo/icAlLjO2VxQ-ONnnd-TR-norqX0V-YJRwCLcBGAsYHQ/s1600/1574905827922.gif",  #rpm
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "backgroundColor": "#ff334b",
            "offsetStart": "22px",
            "height": "20px",
            "width": "20px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "animated": True,
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "backgroundColor": "#ff334b",
            "offsetStart": "42px",
            "height": "20px",
            "width": "20px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
#
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴡᴇʟᴄᴏᴍᴇ",
                "color": "#FF00FF",
                "align": "center",
                "size": "xxs",
                "offsetTop": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "5px", #besar lingkaran
            "offsetTop": "5px", #jarak atas
            "offsetStart": "75px", #jarak samping
            "backgroundColor": "#00FF00",
            "height": "20px",
            "width": "75px",
            "borderWidth": "1px",
            "borderColor": "#00FF00"
          }
        ],
        "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": warnanya1,
    "cornerRadius": "10px",
    "spacing": "xs"
      }
    }
  ]
}
}
                    cl.postTemplate(op.param1, data)

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    #dragonkiller(msg.to,"─┅==ᴋᴏᴋ ʟᴇғᴛ ᴋᴀᴋ==┅─")
                    pass
                else:
                    g = cl.getGroup(op.param1)
                    contact = cl.getContact(op.param2)
                    gname = g.name
                    name = contact.displayName
                    contactlist = cl.getAllContactIds()
                    cover = cl.getProfileCoverURL(op.param2)
                    pp = contact.pictureStatus
                    dk = "GROUP : {}\n".format(gname)+str(settings["leave"])
                    warna1 = ("#F7141F","#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                    warnanya1 = random.choice(warna1)
                    warna2 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                    warnanya2 = random.choice(warna2)
                    Bag1 = wait["BAGHELP"]
                    data = {
                     "type": "flex",
                     "altText": "tidak diketahui",
                     "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "action": {
          "type": "uri",
          "uri": str(settings["idline"])
        },
        "contents": [
          {
            "type": "image",
             "url": "https://profile.line-scdn.net/" + str(pp),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                   "type": "text",
                   "text": eka,
                   "align": "center",
                   "size": "xxs",
                   "weight": "regular",
                   "color": warnanya2,
                   "wrap": True,
                  }
                ],
                 "paddingAll": "0px",
                "borderWidth": "2px",
                "borderColor": "#00FF00",
                "cornerRadius": "10px",
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "{}".format(name),
                        "size": "xxs",
                        "color": "#F7141F",
                        "flex": 0,
                        "offsetTop": "-3px",
                        "wrap": True,
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "10px",
                "spacing": "sm",
                "borderColor": "#00FF00",
                "margin": "xs",
                "height": "20px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#FF7F00",
            "paddingAll": "5px",
            "paddingTop": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "backgroundColor": "#ff334b",
            "offsetStart": "2px",
            "height": "20px",
            "width": "20px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-bevIwpHmmP0/XgApY74fO8I/AAAAAAAAPZo/icAlLjO2VxQ-ONnnd-TR-norqX0V-YJRwCLcBGAsYHQ/s1600/1574905827922.gif",  #RPM 
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "backgroundColor": "#ff334b",
            "offsetStart": "22px",
            "height": "20px",
            "width": "20px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-VnYHnTOdkEg/XgAsc382ooI/AAAAAAAAPaA/EpdHoZQRsCIo5x-W_VoZ6mNyyhY38JSsgCLcBGAsYHQ/s1600/LINE-sm.png",  #LINE#https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTGsf3qGDE-r4GBhrXTXwG9RZ9gyOK5WMZq04CmwwAhdoPGuTXP
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "backgroundColor": "#ff334b",
            "offsetStart": "42px",
            "height": "20px",
            "width": "20px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ɴᴇxᴛ ᴛɪᴍᴇ",
                "color": "#FF00FF",  #merah muda menyala
                "align": "center",
                "size": "xxs",
                "offsetTop": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "5px", #besar lingkaran
            "offsetTop": "5px", #jarak atas
            "offsetStart": "75px", #jarak samping
            "backgroundColor": "#00FF00",
            "height": "20px",
            "width": "75px",
            "borderWidth": "1px",
            "borderColor": "#00FF00"    #<kuning menyala
          }
        ],
        "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": warnanya1,
    "cornerRadius": "10px",
    "spacing": "xs"
      }
    }
  ]
}
}
                    cl.postTemplate(op.param1, data)

                

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        dragonkiller(op.param1, wait["message"])
        if op.type == 5:
            if settings["autoblock"] == True:
                cl.blockContact(op.param1)
            cl.sendMention(op.param1, "Saya Autoblock ")

        #if op.type == 2:
            #if wait["detectvp"] == True:
                #a = op.param1
                #G = cl.getGroupIdsJoined()
                #contact = cl.getContact(op.param1)
                #cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                #a = cl.getAllContactIds()
                #Bio = "Bio : {}".format(contact.statusMessage)
                #cl.sendMessage(op.param1, str(Bio))
                #sendMentionV2(op.param1, "Kak @!\nProfile Ente Keren\nSubhanallah", [op.param1])

#======ANTI BYPASS=========#


        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

                return
                          
        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        pp = contact.pictureStatus
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        Bag1 = wait["BAGHELP"]
                        data = {
                                      "type": "flex",
                                            "altText": "{}".format(cl.getProfile().displayName),
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            "animated": True,
            "aspectMode": "cover",
            "aspectRatio": "2:1",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ","
              }
            ],
            "position": "absolute",
            "borderWidth": "1px",
            "width": "144px",
            "height": "67px",
            "borderColor": "#ff0000",
            "offsetTop": "5px",
            "offsetStart": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
                "size": "xxs",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "offsetEnd": "5px",
            "offsetTop": "5px",
            "borderColor": "#ff0000",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": str( cl.getProfileCoverURL(op.param2)),
                "size": "xxs",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "offsetTop": "5px",
            "offsetStart": "5px",
            "borderColor": "#ff0000",
            "borderWidth": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ","
              }
            ],
            "position": "absolute",
            "borderColor": "#ff0000",
            "borderWidth": "1px",
            "width": "62px",
            "offsetStart": "46px",
            "offsetTop": "5px",
            "height": "13px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CCTV",
                "size": "xxs",
                "color": "#00FFFF",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetStart": "49px",
            "offsetTop": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ","
              }
            ],
            "position": "absolute",
            "borderColor": "#ff0000",
            "borderWidth": "1px",
            "width": "62px",
            "height": "30px",
            "offsetStart": "46px",
            "offsetTop": "17px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " Selfbot",
                "size": "sm",
                "color": "#00FFFF",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetStart": "6px",
            "offsetBottom": "4px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ",",
                "offsetTop": "100px"
              }
            ],
            "position": "absolute",
            "width": "144px",
            "borderColor": "#ff0000",
            "borderWidth": "1px",
            "offsetStart": "5px",
            "height": "14px",
            "offsetBottom": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ">>>",
                "color": "#00FFFF",
                "size": "xxs",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetBottom": "18px",
            "offsetStart": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": str(wait["mention"]),
                "color": "#00FFFF",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "offsetStart": "49px",
            "offsetTop": "33px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(op.param2).displayName),
                "size": "xxs",
                "color": "#00FFFF",
                "weight": "bold"
              }
            ],
            "position": "absolute",
            "offsetBottom": "18px",
            "offsetStart": "30px",
            "width": "118px"
          }
        ],
        "paddingAll": "0px",
        "cornerRadius": "10px",
        "borderColor": "#ff0000",
        "borderWidth": "3px"
      }
    }
  ]
}
}
                #sendTemplate(op.param1, data)
                        cl.postTemplate(op.param1, data)



        if op.type == 55:
            if cctv2['cyduk2'][op.param1]==True:
                if op.param1 in cctv2['point2']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv2['sidermem2'][op.param1]:
                        pass
                    else:
                        cctv2['sidermem2'][op.param1] += "\n " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        pp = contact.pictureStatus
                        warna1 = ("#F7141F","#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                        warnanya1 = random.choice(warna1)
                        warna2 = ("#00FF00","#474851","#FF0000","#4682B4","#6A5ACD","#FFFFFF","#FF00FF","#00FF00","")
                        warnanya2 = random.choice(warna2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        data = {
                         "type": "flex",
                         "altText": "Sider member",
                         "contents":{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "action": {
          "type": "uri",
          "uri": str(settings["idline"])
        },
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(op.param2).displayName),
                    "size": "xxs",
                    "color": "#FFFF00",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": str(wait["mention2"]),
                    "color": "#ebebeb",
                    "size": "xxs",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": str(settings["lebel"]),
                        "size": "xxs",
                        "color": "#F7141F",
                        "flex": 0,
                        "offsetTop": "-3px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "sm"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "borderWidth": "1px",
                "cornerRadius": "10px",
                "spacing": "sm",
                "borderColor": "#00FF00",
                "margin": "xs",
                "height": "20px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#FF7F00",
            "paddingAll": "5px",
            "paddingTop": "3px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-poSq23PqwFk/XgArY6xmCyI/AAAAAAAAPZ0/k5mRWtH_TV4n28tP_Rfo7kRVhNgmVzUZwCLcBGAsYHQ/s1600/20191223_104832.jpg",   #youtube
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "2px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "30px",
            "width": "30px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-bevIwpHmmP0/XgApY74fO8I/AAAAAAAAPZo/icAlLjO2VxQ-ONnnd-TR-norqX0V-YJRwCLcBGAsYHQ/s1600/1574905827922.gif",  #smule
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "33px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "30px",
            "width": "30px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://1.bp.blogspot.com/-VnYHnTOdkEg/XgAsc382ooI/AAAAAAAAPaA/EpdHoZQRsCIo5x-W_VoZ6mNyyhY38JSsgCLcBGAsYHQ/s1600/LINE-sm.png",  #streaming
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "position": "absolute",
            "offsetTop": "65px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "30px",
            "width": "30px",
            "borderWidth": "2px",
            "borderColor": warnanya1,
            "cornerRadius": "50px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CCTV",
                "color": warnanya2,
                "align": "center",
                "size": "xxs",
                "offsetTop": "1px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "10px",
            "offsetTop": "5px",
            "offsetStart": "120px",
            "backgroundColor": "#ff334b",
            "height": "20px",
            "width": "30px",
            "borderWidth": "1px",
            "borderColor": "#ffffff"
          }
        ],
        "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": warnanya1,
    "cornerRadius": "10px",
    "spacing": "xs"
      }
    }
  ]
}
}
                        cl.postTemplate(op.param1, data),


        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])

               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   #contact = cl.getContact(msg._from)
                   #image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           dktag(msg.to, ".")
                           #saints = cl.getContact(msg._from)
                           #cl.sendMessage(msg.to, None, contentMetadata={"STKID":"52002768","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           sendTextTemplate3(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break

                

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sendTextTemplate(msg.to,"「Cek ID Sticker」\n❎STKID : " + msg.contentMetadata["STKID"] + "\n❎  STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n❎STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate3b(msg.to," 『❎』Nama : " + msg.contentMetadata["displayName"] + "\n『❎』  MID : " + msg.contentMetadata["mid"] + "\n 『❎』 Status Msg : " + contact.statusMessage + "\n『❎』 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                s = cl.getProfile().mid
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 and sender != OlengKiller: to = sender
                    else: to = receiver
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:                    	
                            if sender !=  cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if sender != s:
                	            peler["receivercount"] += 1
                            if sender == s:
                	            peler["sendcount"] += 1

                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "Details Post"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\nPenulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\nURL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\nStiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\nTulisan :\n{}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\nFinish"
                                    cl.sendMessage(to, str(ret_))
                                except:
                                    sendTextTemplate3(to, "Post tidak valid")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                                dklike(to, "Done Like Boss !")
            except Exception as error:
                logError(error)
#======================


#==========================================================================================================

        if op.type == 25 or op.type == 26:
            print ("[ 25,26 ] DK TEAMBOT OPERATION")
            msg = op.message 
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 22 and inSteals(sender):
                if msg.toType == 0:to = sender
                true=True
                data = {
                    "type": "flex",
                    "altText": msg.contentMetadata["ALT_TEXT"],
                    "contents": json.loads(msg.contentMetadata['FLEX_JSON'])
                }
                sendTemplate(to, data)
                with open("flex.txt", "w+") as f:
                  f.write(str(json.dumps(data, indent=4, sort_keys=True)))                                 
            if msg.contentType == 4:
                if wait["detectTemplate"] == True:
                    data = {
                        "type": "text",
                        "text": "IYA TAU , ITU TEMPLATE 🤔",
                        "sentBy": {
                            "label": "Detect Template",
                            "iconUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(clientMID).pictureStatus),
                            "linkUrl": "line://nv/profilePopup/mid=ua42e1585852654c8b313a53aced5b165"
                        }
                    }
                    sendTemplate(to, data)
            if msg.contentType == 22:
                if wait["detectTemplate"] == True:
                    data = {
                        "type": "text",
                        "text": "IYA TAU , ITU FLEX 🤔",
                        "sentBy": {
                            "label": "Detect Flex",
                            "iconUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(clientMID).pictureStatus),
                            "linkUrl": "line://nv/profilePopup/mid=ua42e1585852654c8b313a53aced5b165"
                        }
                    }
                    sendTemplate(to, data)                       


            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\nâ”œã€Œ Sticker ID : {}".format(stk_id)
                   ret_ += "\nâ”œã€Œ Sticker Version : {}".format(stk_ver)
                   ret_ += "\nâ”œã€Œ Sticker Package : {}".format(pkg_id)
                   ret_ += "\nâ”œã€Œ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   ret_ += "\nâ•°â”€â”€â”€ã€Œ DK TEAMBOT  ã€"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}         

        if op.type == 26:
            msg = op.message
            sender = msg._from
            to = msg.to
            if msg.contentType == 6:
             if wait["responGc"] == True:
                 a = cl.getContact(sender)
                 if msg.toType == 2:
                     b = msg.contentMetadata['GC_EVT_TYPE']
                     c = msg.contentMetadata["GC_MEDIA_TYPE"]
                     if c == "VIDEO" and b == "S":                    	
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         mek = "Ngajak Vcall \n"
                         mek += "\n 📽GROUP📽 \n" + cl.getGroup(to).name
                         mek += "\n\n✍By: " + cl.getContact(msg._from).displayName
                         mek += "\n\n  📆 Tanggal : " + datetime.strftime(timeNow,'%d-%m-%Y')
                         mek += "\n\n   Waktu : " + datetime.strftime(timeNow,'%H:%M:%S')                     
                         dkgc1(msg.to, str(mek)) 
                         print (mek)
                     elif c == "VIDEO" and b == "E":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         mek = "Kepuasan rehat\n"
                         mek += "\n 📽GROUP📽 \n" + cl.getGroup(to).name
                         mek += "\n\n✍By: " + cl.getContact(msg._from).displayName
                         mek += "\n\n  📆 Tanggal : " + datetime.strftime(timeNow,'%d-%m-%Y')
                         mek += "\n 🕑  Waktu : " + datetime.strftime(timeNow,'%H:%M:%S')
                         dkgc2(msg.to, str(mek))                            
                         print (mek)
                     if c == "AUDIO" and b == "S":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         mek = "Ngajak Call\n"
                         mek += "\n 🎙GROUP🎙 \n" + cl.getGroup(to).name 
                         mek += "\n\n✍By: " + cl.getContact(msg._from).displayName
                         mek += "\n\n 📆  Tanggal : " + datetime.strftime(timeNow,'%d-%m-%Y')
                         mek += "\n 🕑 Waktu : " + datetime.strftime(timeNow,'%H:%M:%S')
                         dkgc3(msg.to, str(mek))                            
                         print (mek)
                     elif c == "AUDIO" and b == "E":
                         tz = pytz.timezone("Asia/Jakarta") 
                         timeNow = datetime.now(tz=tz)
                         mek = "Rehat call\n"
                         mek += "\n 🎙GROUP🎙 \n" + cl.getGroup(to).name 
                         mek += "\n\n✍By: " + cl.getContact(msg._from).displayName
                         mek += "\n\n  📆 Tanggal : " + datetime.strftime(timeNow,'%d-%m-%Y')
                         mek += "\n 🕑  Waktu : " + datetime.strftime(timeNow,'%H:%M:%S')
                         dkgc4(msg.to, str(mek))                            
                         print (mek)
                     if c == "LIVE" and b == "S":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         mek = "Live room\n"
                         mek += "\n 📺GROUP📺 \n" + cl.getGroup(to).name 
                         mek += "\n\n✍By: " + cl.getContact(msg._from).displayName
                         mek += "\n\n  📆 Tanggal : " + datetime.strftime(timeNow,'%d-%m-%Y')
                         mek += "\n 🕑 Waktu : " + datetime.strftime(timeNow,'%H:%M:%S')
                         dkgc5(msg.to, str(mek))                          
                         print (mek)
                     elif c == "LIVE" and b == "E":
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         mek = "Live off\n"
                         mek += "\n 📺GROUP📺 \n" + cl.getGroup(to).name 
                         mek += "\n\n✍By: " + cl.getContact(msg._from).displayName
                         mek += "\n\n 📆 Tanggal : " + datetime.strftime(timeNow,'%d-%m-%Y')
                         mek += "\n 🕑 Waktu : " + datetime.strftime(timeNow,'%H:%M:%S')
                         dkgc6(msg.to, str(mek))
                         print (mek)


        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sendTextTemplate(msg.to,"「Cek ID Sticker」\n『❎』STKID : " + msg.contentMetadata["STKID"] + "\n『❎』  STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n『❎』 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])            
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," 『❎』Nama : " + msg.contentMetadata["displayName"] + "\n『❎』  MID : " + msg.contentMetadata["mid"] + "\n 『❎』 Status Msg : " + contact.statusMessage + "\n『❎』 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

#==========================================================================================================
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        dragonkiller(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        dragonkiller(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        dragonkiller(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        dragonkiller(msg.to,"Contact itu bukan anggota bot rabbits")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        dragonkiller(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        dragonkiller(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        dragonkiller(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        dragonkiller(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate3(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate3b(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate3b(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate3b(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        dragonkiller(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        dragonkiller(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        dragonkiller(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        dragonkiller(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        dragonkiller(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        dragonkiller(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        dragonkiller(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO

               if msg.contentType == 2:
                 if msg._from in admin:
                   if settings["changevp"] == True:
               	    contact = cl.getProfile()
               	    path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               	    path1 = cl.downloadObjectMsg(msg_id)
               	    settings["changevp"] = False
               	    changeVideoAndPictureProfile(path, path1)
               	    sendTextTemplate1(to, "Success change video profile")

#<<=====●BROADCAST VIDEO●==============================================>>
               if msg.contentType == 2:
                 if msg._from in admin:
                   if wait["bcg_video"] == True:
                     aaa = cl.downloadObjectMsg(msg_id)
                     wait["bcg_video"] = False
                     xxx = cl.getGroupIdsJoined()
                     for zzz in xxx:
                         cl.sendVideo(zzz,aaa)
                         cl.sendMessage(zzz, "ʙʀᴏᴀᴅᴄᴀsᴛ ᴠɪᴅᴇᴏ ʙʏ :\nSelfbot kece")
                     sendTextTemplate1(msg.to, "ʙʀᴏᴀᴅᴄᴀsᴛ ᴠɪᴅᴇᴏ sᴜᴄᴄᴇss ᴛᴏ :\n"+format(str(len(xxx)))+" ɢʀᴏᴜᴘs")
#<<=====●BROADCAST IMAGE●==============================================>>
               if msg.contentType == 1:
                 if msg._from in admin:
                   if wait["bcg_image"] == True:
                     aaa = cl.downloadObjectMsg(msg_id)
                     wait["bcg_image"] = False
                     xxx = cl.getGroupIdsJoined()
                     for zzz in xxx:
                         cl.sendImage(zzz,aaa)
                         cl.sendMessage(zzz, "ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴍᴀɢᴇ ʙʏ :\nSelfbots kece")
                     sendTextTemplate1(msg.to, "ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴍᴀɢᴇ sᴜᴄᴄᴇss ᴛᴏ :\n"+format(str(len(xxx)))+" ɢʀᴏᴜᴘs")
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = cl.getProfile()
               		path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = cl.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		dragonkiller(to, "ᴅᴏɴᴇ vɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ")


               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            dragonkiller(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendTextTemplate1(msg.to, "Berhasil menambahkan gambar {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendTextTemplate1(msg.to, "Berhasil menambahkan video {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendTextTemplate1(msg.to, "Berhasil menambahkan sticker {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendTextTemplate1(msg.to, "Berhasil menambahkan mp3 {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate3b("Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")


               if msg.contentType == 3:
                 if msg._from in admin:
                   if wait["bcg_audio"] == True:
                     aaa = cl.downloadObjectMsg(msg_id)
                     wait["bcg_audio"] = False
                     xxx = cl.getGroupIdsJoined()
                     for zzz in xxx:
                         cl.sendAudio(zzz,aaa)
                         time.sleep(0.3)
                         cl.sendMessage(zzz, "ʙc ᴀᴜᴅɪᴏ ")
                     dkbots2(msg.to, "ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴍᴀɢᴇ sᴜᴄᴄᴇss ᴛᴏ :\n"+format(str(len(xxx)))+" ɢʀᴏᴜᴘs")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path1)
                     dkbots2(msg.to, " Succes ~")
                      
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              cl.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              cl.sendVideo(msg.to, videos[video])
 
                        cmd = command(text)
                        if cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               dkbots2(msg.to, str(helpMessage))

                     
                      
                        elif cmd == "help cek":
                          if wait["selfbot"] == True:
                            if msg._from in admin:   
                              helpKcek = helpcek()
                              dkbots2(msg.to, helpKcek)

                        elif cmd == "help set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:   
                              helpKset = helpset()
                              dkbots2(msg.to, helpKset)


                        elif cmd == "help cekset":
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              helpK3 = helpsetgroup() 
                              dkbots2(msg.to, helpK3)
 
                        elif cmd == "help media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              helpK2 = helpmedia()
                              dkbots2(msg.to, helpK2)


 
                        elif cmd == "help js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              helpK4 = helpjs()
                              dkbots2(msg.to, helpK4)

                        elif cmd == "help add":
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                              helpK5 = helpadd()
                              dkbots2(msg.to, helpK5)
                      
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate3(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate3b(msg.to, "Selfbot dinonaktifkan")


                        elif "Token " in str(msg.text):
                            if set["token"] == True:
                                spl = str(msg.text).replace("Token ","")
                                if spl == "mac":
                                    userku = msg._from
                                    loginBEAPI(to, userku, desmac)
                                if spl == "chrome":
                                    userku = msg._from
                                    loginBEAPI(to, userku, chrome)
                                    
                                    
                                            
                        elif cmd == "corona":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpKvirus2 = helpvirus()
                               cl.sendMessage(msg.to, str(helpKvirus2))
                    		

                        elif cmd == "help protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               dkbot(msg.to, str(helpMessage1))
                    		
                        elif cmd == 'autoblock on':
                          if msg._from in admin:
                             settings["autoblock"] = True                                  
                             sendTextTemplate3b(to, "AutoBlock already On")
                              
                        elif cmd == 'autoblock off':
                          if msg._from in admin:
                             settings["autoblock"] = False                                  
                             dragonkiller(to, "AutoBlock already Off")
                        elif cmd == "mycopy":
                          if msg._from in admin:
                            settings["conpp"] = True
                            dragonkiller(to, "Send Contact♪")
							
                        elif cmd == "copy":
                          if msg._from in admin:
                            settings["copy"] = True
                            sendTextTemplate3b(to, "Send Contact♪")

                        elif 'Midcontact ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              anu = msg.text.replace('Midcontact ','')
                              cl.sendContact(to, anu)
                              sendTextTemplate3b(to, "Sukses mngetahui contact mid target♪")
 
                        elif 'Getmid ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              anu = msg.text.replace('Getmid ','')
                              cl.findAndAddContactsByMid(anu)
                              cl.inviteIntoGroup(to,[anu])
                              sendTextTemplate3b(to, "Sukses invite Contact mid target♪")

                        elif cmd == "copy off":
                          if msg._from in admin:
                            settings["copy"] = False
                            sendTextTemplate3b(to, "Done off copy♪")

                        elif ("Gname " in msg.text):
                          if msg._from in admin:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gname ","")
                              cl.updateGroup(X)

                        elif cmd == "system":
                          if msg._from in admin:
                              ac = subprocess.getoutput('lsb_release -a')
                              am = subprocess.getoutput('cat /proc/meminfo')
                              ax = subprocess.getoutput('lscpu')
                              core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
                              for line in ac.splitlines():
                                  if 'Description:' in line:
                                      osi = line.split('Description:')[1].replace('  ','')
                              for line in ax.splitlines():
                                  if 'Architecture:' in line:
                                       architecture =  line.split('Architecture:')[1].replace(' ','')
                              for line in am.splitlines():
                                  if 'MemTotal:' in line:
                                      mem = line.split('MemTotal:')[1].replace(' ','')
                                  if 'MemFree:' in line:
                                      fr = line.split('MemFree:')[1].replace(' ','')
                              md ="╭━━━━━━━━━━\n┃─✥SPES SYSTEM✥─  \n╰━━━━━━━━━━\n"
                              md +="╭━━━━━━━━━━\n┃Script info: {}\n".format(sc)
                              md +="┃OS: {}\n".format(osi)
                              md +="┃Architecture: {}\n".format(architecture)
                              md +="┃CPU : {}CORE\n".format(core)
                              md +="┃Memory: {}\n".format(mem)
                              md +="┃Free: {}\n".format(fr)
                              md +="┃REGION: JAPAN 🇯🇵\n╰━━━━━━━━━━"
                              cl.sendMessage(to,md)

                        elif cmd == "!ginfo":
                          if msg._from in admin:
                            group = cl.getGroup(msg.to)
                            try:
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "SUDAH PUSKUN ORANGNYA"
                            if group.invitee is None:
                                gPending = "0"
                            else:
                                gPending = str(len(group.invitee))
                            if group.preventedJoinByTicket == True:
                                gQr = "Closed"
                                gTicket = "Qr tidak tersedia karna di tutup"
                            else:
                                gQr = "Open"
                                gTicket = "https://me.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                            timeCreated = []
                            timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(group.createdTime) / 1000)))
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            ret_ = "╭━━══[ Group Info ]══━━"
                            ret_ += "\n Nama Group : {}".format(str(group.name))
                            ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                            ret_ += "\nID Group : {}".format(group.id)
                            ret_ += "\n Pembuat : {}".format(str(gCreator))
                            ret_ += "\n Jumlah Member : {}".format(str(len(group.members)))
                            ret_ += "\n Jumlah Pending : {}".format(gPending)
                            ret_ += "\n═━━━Kode Qr/Link━━━═"
                            ret_ += "\n Group Ticket : {}".format(gTicket)
                            ret_ += "\n Group Qr : {}".format(gQr)
                            ret_ += "\n╰━━══[ RIEZ BOTS ]══━━"
                            warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            data = {
                                "type": "flex",
                                "altText": "INFO GROUP",
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": str(ret_),
            "size": "xxs",
            "weight": "bold",
           "wrap": True,
            "color": warnanya1,
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "16:9",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(group.pictureStatus),
    "size": "full",
    "margin": "xl"
  }
}
}
                            cl.postTemplate(to, data)

                        elif cmd == "ginforoom":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                warna1 = ("#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                                warnanya1 = random.choice(warna1)
                                data = {
                                        "type": "flex",
                                        "altText": "INFO GROUP",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": warnanya1
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#C0C0C0"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(G.creator.pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#C0C0C0"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#C0C0C0"
      },
      {
        "contents": [
          {
            "text": "Nama Group : {}".format(G.name),
            "size": "xxs",
            "align": "center",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#C0C0C0"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "ID Group : {}".format(G.id),
                "size": "xxs",
                "margin": "none",
                "color": warnanya1,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Pembuat : {}".format(G.creator.displayName),
                "size": "xxs",
                "margin": "none",
                "color": warnanya1,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Waktu Dibuat : {}".format(str(timeCreated)),
                "size": "xxs",
                "margin": "none",
                "color": warnanya1,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Jumlah Member : {}".format(str(len(G.members))),
                "size": "xxs",
                "margin": "none",
                "color": warnanya1,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Jumlah Pending : {}".format(gPending),
                "size": "xxs",
                "margin": "none",
                "color": warnanya1,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Group Qr : {}".format(gQr),
                "size": "xxs",
                "margin": "none",
                "color": warnanya1,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://obs.line-scdn.net/{}".format(G.pictureStatus),
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Group Ticket : {}".format(gTicket),
                "size": "xxs",
                "weight": "bold",
                "action": {
                  "uri": "http://line.me/ti/p/~ownerdk",
                  "type": "uri",
                  "label": "Add Creator"
                },
                "margin": "none",
                "color": warnanya1,
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))


                        elif cmd == "me" or text.lower() == 'saya':                            	                        
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "position": "relative",
            "margin": "none",
            "align": "center",
            "backgroundColor": "#00FF00",
            "offsetTop": "5px",
            "offsetBottom": "2px",
            "offsetStart": "3px",
            "offsetEnd": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "color": "#00FF00",
                "align": "center",
                "size": "xs",
                "offsetTop": "5px",
                "margin": "none",
                "weight": "bold",
                "style": "italic",
                "decoration": "line-through",
                "position": "relative",
                "gravity": "top",
                "offsetBottom": "5px",
                "offsetStart": "5px",
                "offsetEnd": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "40px",
            "offsetTop": "10px",
            "backgroundColor": "#00FF00",
            "offsetStart": "15px",
            "height": "20px",
            "width": "90px",
            "spacing": "none",
            "margin": "xs",
            "borderColor": "#00FFFF",
            "offsetBottom": "5px",
            "offsetEnd": "5px",
            "paddingAll": "0px",
            "paddingTop": "0px",
            "paddingBottom": "2px",
            "paddingStart": "0px",
            "paddingEnd": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(sender).displayName),
                "size": "xs",
                "color": "#00FF00",
                "weight": "bold",
                "style": "italic",
                "decoration": "line-through",
                "position": "relative",
                "align": "center",
                "gravity": "top",
                "offsetTop": "1px",
                "offsetStart": "0px",
                "margin": "none"
              }
            ],
            "position": "relative",
            "spacing": "xs",
            "margin": "xs",
            "backgroundColor": "#00FFFF",
            "borderWidth": "1px",
            "borderColor": "#FFFF00",
            "cornerRadius": "20px",
            "offsetTop": "3px",
            "offsetBottom": "5px",
            "offsetStart": "3px",
            "offsetEnd": "5px",
            "paddingAll": "1px",
            "paddingTop": "1px",
            "paddingBottom": "1px",
            "paddingStart": "1px",
            "paddingEnd": "3px"
          }
        ],
        "paddingAll": "1px",
        "position": "relative",
        "spacing": "none",
        "margin": "xs",
        "backgroundColor": "#00FF00",
        "borderWidth": "1px",
        "cornerRadius": "5px",
        "offsetTop": "2px",
        "offsetBottom": "2px",
        "offsetStart": "1px",
        "offsetEnd": "5px",
        "borderColor": "#00FF00",
        "paddingTop": "0px",
        "paddingBottom": "3px",
        "paddingStart": "0px",
        "paddingEnd": "5px"
      },
      "styles": {
        "header": {
          "backgroundColor": "#00FF00",
          #"separator": ,
          "separatorColor": "#000000"
        },
        "hero": {
          "backgroundColor": "#FFFF00",
          "separatorColor": "#00FF00",
          #"separator": 
        },
        "body": {
          "backgroundColor": "#FFFF00",
          "separatorColor": "#000080"
        }
      }
    },
    {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": cover,
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top",
            "position": "relative",
            "margin": "none",
            "align": "center",
            "backgroundColor": "#00FF00",
            "offsetTop": "5px",
            "offsetBottom": "3px",
            "offsetStart": "2px",
            "offsetEnd": "3px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#00FF00",
                "align": "center",
                "size": "xs",
                "offsetTop": "3px",
                "margin": "none",
                "weight": "bold",
                "style": "italic",
                "decoration": "line-through",
                "position": "relative",
                "gravity": "top",
                "offsetBottom": "10px",
                "offsetStart": "0px",
                "offsetEnd": "5px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "10px",
            "backgroundColor": "#00FF00",
            "offsetStart": "15px",
            "height": "20px",
            "width": "90px",
            "spacing": "none",
            "margin": "xs",
            "borderWidth": "1px",
            "borderColor": "#FFFF00",
            "offsetBottom": "1px",
            "offsetEnd": "3px",
            "paddingAll": "1px",
            "paddingBottom": "1px",
            "paddingStart": "1px",
            "paddingTop": "1px",
            "paddingEnd": "1px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(cl.getContact(sender).displayName),
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "weight": "bold",
                "style": "italic",
                "decoration": "line-through",
                "position": "relative",
                "align": "center",
                "gravity": "top",
                "offsetTop": "2px",
                "offsetStart": "0px"
              }
            ],
            "position": "relative",
            "spacing": "none",
            "margin": "none",
            "backgroundColor": "#00FFFF",
            "borderWidth": "1px",
            "borderColor": "#FFFF00",
            "offsetTop": "3px",
            "offsetBottom": "5px",
            "offsetStart": "3px",
            "offsetEnd": "5px",
            "paddingAll": "1px",
            "paddingTop": "1px",
            "paddingBottom": "1px",
            "paddingStart": "1px",
            "paddingEnd": "3px",
            "cornerRadius": "20px"
          }
        ],
        "paddingAll": "0px",
        "position": "relative",
        "spacing": "none",
        "margin": "xs"
      },
      "styles": {
        "header": {
          "backgroundColor": "#00FF00",
          "separatorColor": "#00FF00"
        },
        "hero": {
          "backgroundColor": "#00FF00",
          "separatorColor": "#00FF00",
          #"separator": 
        },
        "body": {
          "backgroundColor": "#00FF00",
          "separatorColor": "#000080"
        }
      }
    }
  ]
}
                                cl.postFlex(to, data)

                        elif cmd == "me2":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
        "action": {
          "uri": "http://line.me/ti/p/~nirwanabjn",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#00FF00"
        },
        "footer": {
          "backgroundColor": "#00FF00"
        },
        "header": {
          "backgroundColor": "#00FF00"
        }
      },
      "type": "bubble",
      "size": "nano",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "v3 versi",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~nirwanabjn"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PROFIL",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": cover,
        "action": {
          "uri": "http://line.me/ti/p/~nirwanabjn",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#00FF00"
        },
        "footer": {
          "backgroundColor": "#00FF00"
        },
        "header": {
          "backgroundColor": "#00FF00"
        }
      },
      "styles": {
        "body": {
          "backgroundColor": "#00FF00"
        },
        "footer": {
          "backgroundColor": "#00FF00"
        },
        "header": {
          "backgroundColor": "#00FF00"
        }
      
      },
      "type": "bubble",
      "size": "nano",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "v3 versi",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~nirwanabjn"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "size": "nano",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BERANDA",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)


                        elif cmd == "menu sb":
                          if msg._from in admin:
                            ret = "Help js\n"
                            ret += "Help cek\n"
                            ret += "Help set\n"
                            ret += "Help protect\n"
                            ret += "Help1\n"
                            ret += "Help2\n"
                            ret += "Help3\n"
                            ret += "Help4\n"
                            ret += "Mʏʙɪᴏ\n"
                            ret += "Cvp\n"
                            ret += "Status\n"
                            hello = "{}".format(str(ret))
                            #=====================1
                            ret1 = "Bye me\n"
                            ret1 += "Cchat\n"
                            ret1 += "Adminadd @\n"
                            ret1 += "Admindell @\n"
                            ret1 += "Hajar tag koban\n"
                            ret1 += "Like @tag terget\n"
                            ret1 += "Sɪᴅᴇʀ ᴏɴ\ᴏғғ\n"
                            ret1 += "Media\n"
                            ret1+= "Setgroup\n"
                            ret1 += "Promo\n"
                            ret1 += "Harga\n"
                            ret1 += "Invite\n"
                            hello1 = "{}".format(str(ret1))
                            #=====================2
                            ret2 = "Unban:on\n"
                            ret2 += "Ban「@」\n"
                            ret2 += "Unban「@」\n"
                            ret2 += "Talkban「@」\n"
                            ret2 += "Untalkban「@」\n"
                            ret2 += "Talkban:on/off\n"
                            ret2 += "Untalkban:on\n"
                            ret2 += "Banlist\n"
                            ret2 += "Talkbanlist\n"
                            ret2 += "Clearban\n"
                            ret2 += "Refresh\n"
                            hello2 = "{}".format(str(ret2))
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            tanggal =" "+ datetime.strftime(timeNow,'%d-%m-%Y')
                            warna1 = ("#1AE501","#0108E5","#696969","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            Bag1 = wait["BAGHELP"]
                            data = {
                                       "type": "flex",
                                       "altText": "menu",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret)),
"size": "xs",
"color": "#FFFF00",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
{ # =================================
"type": "bubble",
"size": "micro",
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret1)),
"size": "xs",
"color": "#FFFF00",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
{ # =================================
"type": "bubble",
"size": "micro",
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret2)),
"size": "xs",
"color": "#FFFF00",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
]
}
}
                            cl.postTemplate(to, data)



                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               Font = wait["warna"]
                               Fontb = wait["warna1"]
                               Bag1 = wait["BAGHELP"]
                               Tampilan1 = wait["size"]
                               data = {
                                       "type": "flex",
                                       "altText": "♻Selfʙᴏᴛᴢ™♻",
                                       "contents": 
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": Tampilan1,
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "position": "absolute",
            "size": "full",
            #"animated": True,
            "aspectMode": "cover"
          },
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
            #"animated": True,
            "aspectMode": "cover",
            "position": "absolute",
            "aspectRatio": "2:6",
            "flex": 0,
            "offsetBottom": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": Font,
                "animated": True,
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "size": "xxs",
               # "animated": True,
                "aspectMode": "cover",
                "flex": 0
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": str(settings["lebel"]),
                    "color": Font,
                    "size": "xxs"
                  },
                  {
                    "type": "separator",
                    "color": "#00FFFF"
                  },
                  {
                    "type": "text",
                    "text": "⏱ "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                    "color": Font,
                    "size": "xxs"
                  }
                ],
                "borderColor": "#00FFFF",
                "borderWidth": "1px"
              }
            ],
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "╭「Self」\n║❂➣ Menu\n║❂➣ Help js\n║❂➣ Help cek\n║❂➣ Help set\n║❂➣ Help protect\n║❂➣ Help add\n║❂➣ Help1\n║❂➣ Help2\n║❂➣ Help3\n║❂➣ Help4\n║❂➣ Help media\n║❂➣ Help cekset\n╰「Selfʙᴏᴛᴢ™」",
                "wrap": True,
                "size": "xxs",
                "color": Font
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/dzee123"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/camera/"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://www.smule.com/KSS_OFFICE"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/cameraRoll/multi"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/timeline"
                }
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "relative",
            "offsetBottom": "0px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#FFD700"
        }
      }
    },
    {
      "type": "bubble",
      "size": Tampilan1,
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "position": "absolute",
            "size": "full",
            #"animated": True,
            "aspectMode": "cover"
          },
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
           # "animated": True,
            "aspectMode": "cover",
            "position": "absolute",
            "aspectRatio": "2:6",
            "flex": 0,
            "offsetBottom": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": Font,
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "size": "xxs",
             #   "animated": True,
                "aspectMode": "cover",
                "flex": 0
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": str(settings["lebel"]),
                    "color": Font,
                    "size": "xxs"
                  },
                  {
                    "type": "separator",
                    "color": "#00FFFF"
                  },
                  {
                    "type": "text",
                    "text": "⏱ "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                    "color": Font,
                    "size": "xxs"
                  }
                ],
                "borderColor": "#00FFFF",
                "borderWidth": "1px"
              }
            ],
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "╭「Selfʙᴏᴛᴢ™」\n║❂➣ Unban @\n║❂➣ Ban @\n║❂➣ Talkban @\n║❂➣ Untalkban @\n║❂➣ Banlist\n║❂➣ Talkbanlist\n║❂➣ Clearban\n║❂➣ Refresh\n║❂➣ Getmid @\n║❂➣ Scall: Number\n║❂➣ Scall\n║❂➣ Scall number @\n║❂➣ Stag: number\n║❂➣ Stag @\n╰「Selfʙᴏᴛᴢ™」",
                "wrap": True,
                "size": "xxs",
                "color": Font
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/dzee123"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/camera/"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://www.smule.com/KSS_OFFICE"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/cameraRoll/multi"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/timeline"
                }
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "relative",
            "offsetBottom": "0px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#FFD700"
        }
      }
    },
    {
      "type": "bubble",
      "size": Tampilan1,
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "position": "absolute",
            "size": "full",
           # "animated": True,
            "aspectMode": "cover"
          },
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
          #  "animated": True,
            "aspectMode": "cover",
            "position": "absolute",
            "aspectRatio": "2:6",
            "flex": 0,
            "offsetBottom": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": Font,
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "size": "xxs",
                #"animated": True,
                "aspectMode": "cover",
                "flex": 0
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": str(settings["lebel"]),
                    "color": Font,
                    "size": "xxs"
                  },
                  {
                    "type": "separator",
                    "color": "#00FFFF"
                  },
                  {
                    "type": "text",
                    "text": "⏱ "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                    "color": Font,
                    "size": "xxs"
                  }
                ],
                "borderColor": "#00FFFF",
                "borderWidth": "1px"
              }
            ],
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "╭「Selfʙᴏᴛᴢ™」\n║❂➣ Bye ᴍᴇ\n║❂➣ Cchat\n║❂➣ Adminadd @\n║❂➣ Admindell @\n║❂➣ Hajar tag korban\n║❂➣ Like @target\n║❂➣ Rental\n║❂➣ Setgroup\n║❂➣ Promo\n║❂➣ Harga\n║❂➣ Invite\n╰「Selfʙᴏᴛᴢ™」",
                "wrap": True,
                "size": "xxs",
                "color": Font
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/dzee123"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/camera/"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://www.smule.com/KSS_OFFICE"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/cameraRoll/multi"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/timeline"
                }
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "relative",
            "offsetBottom": "0px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#FFD700"
        }
      }
    },
    {
      "type": "bubble",
      "size": Tampilan1,
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": Bag1,
            "position": "absolute",
            "size": "full",
           # "animated": True,
            "aspectMode": "cover"
          },
          {
            "type": "image",
            "url": Bag1,
            "size": "full",
           # "animated": True,
            "aspectMode": "cover",
            "position": "absolute",
            "aspectRatio": "2:6",
            "flex": 0,
            "offsetBottom": "0px"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": str(settings["lebel"]),
                "size": "xxs",
                "color": Font,
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": Bag1,
                "size": "xxs",
               # "animated": True,
                "aspectMode": "cover",
                "flex": 0
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": str(settings["lebel"]),
                    "color": Font,
                    "size": "xxs"
                  },
                  {
                    "type": "separator",
                    "color": "#00FFFF"
                  },
                  {
                    "type": "text",
                    "text": "⏱ "+ datetime.strftime(timeNow,'%Y-%m-%d'),
                    "color": Font,
                    "size": "xxs"
                  }
                ],
                "borderColor": "#00FFFF",
                "borderWidth": "1px"
              }
            ],
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "╭「Selfʙᴏᴛᴢ™」\n│❂➣Respongc on/off\n│❂➣Sider on/off\n│❂➣Autorespon on/off \n│❂➣Unsend on/off \n│❂➣Autoblock on/off \n│❂➣Broadcat:\n│❂➣Bc teman: \n│❂➣Grouplist \n│❂➣Infogroup\n│❂➣Infomem\n╰「Selfʙᴏᴛᴢ™」",
                "wrap": True,
                "size": "xxs",
                "color": Font
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "https://youtube.com"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/dzee123"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/camera/"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://www.smule.com/KSS_OFFICE"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/cameraRoll/multi"
                }
              },
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "line://nv/timeline"
                }
              }
            ],
            "borderWidth": "1px",
            "borderColor": "#00FFFF",
            "position": "relative",
            "offsetBottom": "0px"
          }
        ],
        "paddingAll": "0px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#FFD700"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)

   
                        elif cmd == ".help":
                          if msg._from in admin:
                            ret = "HELP JS\n"
                            ret += "HELP CEK\n"
                            ret += "HELP SET\n"
                            ret += "HELP PROTECT\n"
                            ret += "HELP1\n"
                            ret += "HELP2\n"
                            ret += "HELP3\n"
                            ret += "HELP4\n"
                            ret += "HELP MEDIA\n"
                            ret += "HELP CEKSET\n"
                            hello = "{}".format(str(ret))
                            #=====================1
                            ret1 = "BYE ME\n"
                            ret1 += "CCHAT\n"
                            ret1 += "ADMINADD @\n"
                            ret1 += "ADMINDELL @\n"
                            ret1 += "HAJAR TAG KORBAN\n"
                            ret1 += "LIKE @ TARGET\n"
                            ret1 += "SIDER ON/OFF\n"
                            ret1 += "RENTAL\n"
                            ret1+= "SETGROUP\n"
                            ret1 += "PROMO\n"
                            ret1 += "HARGA\n"
                            ret1 += "INVITE\n"
                            hello1 = "{}".format(str(ret1))
                            #=====================2
                            ret2 = "UNBAN ON/OFF\n"
                            ret2 += "BAN「@」\n"
                            ret2 += "UNBAN「@」\n"
                            ret2 += "TALKBAN「@」\n"
                            ret2 += "UNTALKBAN「@」\n"
                            ret2 += "TALKBAN:ON/OFF\n"
                            ret2 += "UNTALKBAN:ON/OFF\n"
                            ret2 += "BANLIST\n"
                            ret2 += "TALKBANLIST\n"
                            ret2 += "CLEARBAN\n"
                            ret2 += "REFRESH\n"
                            ret2 += "GETMID\n"
                            hello2 = "{}".format(str(ret2))
                            #=====================3
                            ret3 = "RESPONGC「ᴏɴ/ᴏғғ」\n"
                            ret3 += "WELCOME「ᴏɴ/ᴏғғ」\n"
                            ret3 += "SIDER「ᴏɴ/ᴏғғ」\n"
                            ret3 += "AUTORESPON「ᴏɴ/ᴏғғ」\n"
                            ret3 += "UNSEND「ᴏɴ/ᴏғғ」\n"
                            ret3 += "AUTOBLOCK「ᴏɴ/ᴏғғ」\n"
                            ret3 += "BROADCAST「Text」\n"
                            ret3 += "BC TEMAN:「Text」\n"
                            ret3 += "GROUPLIST「Num」\n"
                            ret3 += "INFOGROUP「Num」\n"
                            ret3 += "INFOMEM「Num」\n"
                            hello3 = "{}".format(str(ret3))
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            tanggal =" "+ datetime.strftime(timeNow,'%d-%m-%Y')
                            warna1 = ("#1AE501","#0108E5","#696969","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8")
                            warnanya1 = random.choice(warna1)
                            Bag1 = wait["BAGHELP"]
                            Tampilan1 = wait["size"]
                            data = {
                                       "type": "flex",
                                       "altText": "menu",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": Tampilan1,
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret)),
"size": "xs",
"color": "#FF00FF",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
{ # =================================
"type": "bubble",
"size": Tampilan1,
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret1)),
"size": "xs",
"color": "#FF00FF",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
{ # =================================
"type": "bubble",
"size": Tampilan1,
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret2)),
"size": "xs",
"color": "#FF00FF",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
{ # =================================
"type": "bubble",
"size": Tampilan1,
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bag1,
"animated": True,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": str(settings["lebel"]),
"color": warnanya1,
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "3px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#00FF00",
"height": "20px",
"width": "150px"
},
# ===========KATA KATA
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text":"{}".format(str(ret3)),
"size": "xs",
"color": "#FF00FF",
"wrap": True,
"offsetStart": "3px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "26px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"height": "220px",
"width": "150px"
}
],
"paddingAll": "0px"
}
},
]
}
}
                            cl.postTemplate(to, data)


                       
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "Me Message",
                                        "contents": {
  "type": "bubble",
  "size": "nano",
      "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "{}".format(status.displayName),
            "size": "xxs",
            "weight": "bold",
            "wrap": True,
            "color": "#7FFF00"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "align": "center",
            "size": "xxs",
            "weight": "bold",
            "color": "#FF00FF",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#00FF00"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "3:3",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
    "size": "full",
    "align": "center",
  
  }
}
}
                                cl.postTemplate(to, data)
 


                         
                        
                        elif cmd == "menu1":
                                with open("help.json","r") as f:
                                    data = json.load(f)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                            if len(ret_) >= 20:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "size": "nano",
                                                        "label": "{}".format(str(fn["name"])),
                                                        "uri": "{}".format(str(fn["linkliff"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                                "type": "template",                                    
                                                "altText": "Help Message",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": ret_[aa*10 : (aa+1)*10]
                                                }
                                            }
                                        cl.postTemplate(to, data)
                                                                                                                
                        elif cmd.startswith("bc1: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://media1.giphy.com/media/fnKtAO0GLeiD6/200w.webp?cid=19f5b51a5c454d542f704f7a6395da37",
        "action": {
          "uri": "http://line.me/ti/p/yWFvdLpiHp",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "size": "nano",
           "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BRODCAST",
            "size": "xxs",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~dkdkbot"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "TEAM",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   cl.postFlex(group, data)





#============================================================

#===========COMEN PANGGILAN======
                        elif cmd == 'listblock':
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            dragonkiller(to, msgs)

                        elif cmd.startswith("block"):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.generateReplyMessage(msg.id)
                                dragonkiller(msg.id, to, "sᴜᴄᴄᴇs ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ" + str(contact.displayName) + "ᴇɴᴛᴇʀ ᴛʜᴇ ʙʟᴏᴄᴋʟɪsᴛ")

                        elif cmd.startswith("stag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
                        elif cmd.startswith("scall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                        elif cmd.startswith("stag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        sendTextTemplate1(msg.to,"Jumlah melebihi 1000")
                        elif msg.text.lower().startswith("scalltag "):
                          if msg._from in admin:
                           if 'MENTION' in msg.contentMetadata.keys()!= None:
                               names = re.findall(r'@(\w+)', text)
                               mention = eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               lists = []
                               for mention in mentionees:
                                   if mention["M"] not in lists:
                                       lists.append(mention["M"])
                               for ls in lists:
                                   contact = cl.getContact(ls)                          
                                   jmlh = int(wait["limit"])
                                   sendTextTemplate1(msg.to, "Succes {} Call Grup".format(str(wait["limit"])))
                                   if jmlh <= 1000:
                                     for x in range(jmlh):
                                         try:
                                             mids = [contact.mid]
                                             cl.acquireGroupCallRoute(msg.to)
                                             cl.inviteIntoGroupCall(msg.to,mids)
                                         except Exception as e:
                                             sendTextTemplate1(msg.to,str(e))
                                     else:
                                         sendTextTemplate1(msg.to,"")


                        elif cmd == "scall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sendTextTemplate1(to, "Mengundang {} Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                         cl.acquireGroupCallRoute(to)
                                         cl.inviteIntoGroupCall(to, contactIds=members)
                                     except:
                                         pass
                                else:
                                    cl.sendMessage(to,"Jumlah melebihi batas")

                        elif cmd.startswith('stag '):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            num = int(sep[1])                           
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0,num):
                                        cl.sendMention(to, "@!", [ls])
#===========================================================

                        elif cmd.startswith("bc teman: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                bctxt = msg.text.replace("bc teman: ", "")
                                a = cl.getAllContactIds()
                                dragonkiller(to, "sᴜᴄᴄᴇss ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴏ "+str(len(a))+" ғʀɪᴇɴᴅ")
                                for manusia in a:
                                    C = cl.getContact(myBOG)
                                    mids = [C.mid]
                                    text = "ʙʀᴏᴀᴅᴄᴀsᴛ ғʀɪᴇɴᴅ:\n{}\nʙʀᴏᴀᴅᴄᴀsᴛ: @!".format(str(bctxt))
                                    sendMentionV2(manusia, text, mids)
                        elif text.lower().startswith("flex ") and msg._from in admin and to not in chatbot["botMute"]:
                          if msg._from in admin:
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = [] 
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            if lists != []:
                              for x in lists:
                                appendSteals(x)
                              dragonkiller(to, "Waiting target send flex message!")               
                        elif text.lower() == "clearflex" and msg._from in admin and to not in chatbot["botMute"]:
                          if msg._from in admin:
                            clearSteals()
                            dragonkiller(to, "Data flex message is cleared now & set to off.")                                    
                        elif cmd.startswith("like "):
                          if msg._from in admin:
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(sender), str(result), "◄━━◈⟦ASSALAMUALAIKUM⟧◈━━►\n            🛡Dzulkifli DK DESIGN🛡\n╔•═══════════════\n║╠═╦═✪ PROMOTION ✪═╦═\n╠•═══════════════\n╠•══✪「ᴏᴘᴇɴ ᴏʀᴅᴇʀ」✪════\n║┣[]► SCRIPT BOT PROTECT\n║┣[]► SCRIPT BOT WAR\n║┣[]► SCRIPT BOT SIRI\n║┣[]► SCRIPT SB ONLY\n║┣[]► SCRIPT SB TEMPLATE\n║┣[]► SONGBOOK SMULE\n╠════════════════\n╠•══✪「ʙᴏᴛ ᴏʀᴅᴇʀ」✪═════\n║┣[]► sʙ ᴏɴʟʏ \n║┣[]► sʙ + ᴀsɪsᴛ\n║┣[]► sʙ + ᴀsɪsᴛ + ɢʜᴏsᴛ\n║┣[]► sʙ + ᴀsɪsᴛ + ɢʜᴏsᴛ + ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 6 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 10 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 20 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n║┣[]► sʙ 25 ᴀsɪsᴛ 6 ɢʜᴏsᴛ 1 ᴀɴᴛɪ ᴊs\n╠•══✪「sᴇᴛ - ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ」✪═\n║┣[]► ᴏᴡɴᴇʀ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n║┣[]► ᴀᴅᴍɪɴ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n║┣[]► sᴛᴀғғ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n║┣[]► ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ sᴍᴜʟᴇ\n║┣[]► ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ᴇᴠᴇɴᴛ\n║┣[]► ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ᴏʟsʜᴏᴘ\n╠════════════════\n╠•══✪「==CATATAN==」✪════\n║BARANG SIAPA YG MERATAKAN\n║ROOM SMULE/EVENT/OLSHOP\n║MENGATASNAMAKAN GK BOTS/\n║DRAGON KILLER BOTS/GHEO BOTS\n║ATAU DK DRAGON KILLER\n║HUBUNGI SAYA LANGSUNG\n╠════════════════\n╠•══✪「ᴅᴀғᴛᴀʀ ʜᴀʀɢᴀ」✪════\n║JIKA ANDA BERMINAT SILAHKAN\n║                ✪ HUBUNGI ✪\n║WA     : -\n║LINE   : dkbot / dkbot / dragonkillerbots\n║http://line.me/ti/p/~dkbot\n║http://line.me/ti/p/~dkbot\n║http://line.me/ti/p/~dkbot\n╠════════════════\n║SALAM SANTUN PERSAHABATAN\n║            ✪ TERIMA KASIH ✪\n╚════════════════\n ◄━━◈⟦WASSALAMUALAIKUM⟧◈━━►")
                                    dragonkiller(msg.to, 'like comend\n '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    dragonkiller(receiver, str(e))



                                
                        elif cmd == "menu":      
                          if msg._from in admin:
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/BBQGP5r/FB-IMG-15716621639974310.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "B8860B"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Musik Joox",
                   "uri": "https://www.joox.com/id/me"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/Tbygb8S/1541341062445.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Sound Clouds",
                   "uri": "https://m.soundcloud.com/soundcloud"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/FVhdsJh/FB-IMG-15716621323117393.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Smulle ID",
                   "uri": "https://googleweblight.com/i?u=https://www.smule.com/search?q%3D%2523Login&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/ZY7NZBs/3608024724-e7714bcedd-z.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbots",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Google",
                   "uri": "https://www.google.com/"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/b27wkKk/1486988-9996a116-d7f4-488a-8bd6-98d20162ee86.png",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbots",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Google Play Store",
                   "uri": "https://www.google.com/url?q=https://play.google.com/&sa=U&ved=2ahUKEwie_5O3q9LpAhXzjOYKHRrLAkAQFjAVegQIDBAB&usg=AOvVaw0FXCzlPRUsJMhmiBw-wBdj"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/Kqg7Qmy/header.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Game Online",
                   "uri": "https://googleweblight.com/i?u=https://www.games.co.id/&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/BKRYPsm/unnamed.png",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbots",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Main Game",
                   "uri": "https://googleweblight.com/i?u=https://www.games.co.id/&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/ysYBxrv/images-3.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Photo Editor",
                   "uri": "https://googleweblight.com/i?u=https://pixlr.com/id/&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/d4TcJjL/textpro-me.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Text Neon Editor",
                   "uri": "https://googleweblight.com/i?u=https://cooltext.com/Logo-Design-Neon&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/KGqL2SK/tv-704887.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "TV Online",
                   "uri": "https://googleweblight.com/i?u=https://www.mivo.com/mobile/live-streaming-allchannel&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)
                                data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/1qzvnLR/images-1.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Notepad",
                   "uri": "https://googleweblight.com/i?u=https://www.rapidtables.com/tools/notepad.html&hl=id-ID"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/st7DcZT/youtube-logo-black-background.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Get Channel",
                   "uri": "https://youtu.be/VSzi1KfMnNY"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/61SWtyx/images-4.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Facebook",
                   "uri": "https://m.facebook.com/login/"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/JmK8WqQ/twitter.png",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#474851"
        },
        "header": {
          "backgroundColor": "#474851"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Twitter",
                   "uri": "https://mobile.twitter.com/login"
                 }
               }
            ]
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/mhh8f8T/images-5.jpg",
        "action": {
          "uri": "https://line.me/ti/p/~dkdkbot",
          "type": "uri"
        },
        "type": "image",
        "size": "full",
        "aspectRatio": "16:9"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#0000FF"
        },
        "header": {
          "backgroundColor": "#0000FF"
        }
      },
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "flex": 2,
            "contents": [
              {
                 "type": "button",
                 "style": "secondary",
                 "color": "#FF00FF",
                 "height": "sm",
                 "action": {
                   "type": "uri",
                   "label": "Instagram",
                   "uri": "https://www.instagram.com/"
                 }
               }
            ]
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                cl.postFlex(to, data)


                        elif cmd == "help1":
                          if msg._from in admin:               
                             dkbots2(msg.to, 
                             "╭─╼「 DESIGN 」\n"
                             "│╭───────── \n"
                             "│├   SIMPLE DESIGN \n"
                             "│├Versi v3:3\n"                     
                             "│├01.Me \n"                                         
                             "│├03.Bye me \n"
                             "│├04.Sider on \n"                       
                             "│├07.Cchat \n"                       
                             "│├08.Restart \n"                             
                             "│├09.Info @\n"
                             "│├10.Status \n"                       
                             "│├11.Url \n"                             
                             "│├12.Link on|off \n"
                             "│├13.Getpict @ \n"                       
                             "│├14.Getvid @ \n"                             
                             "│├15.Glist \n"
                             "│├16.Getcover @ \n"                       
                             "│├17.Getname \n"                             
                             "│├18.Getbio @ \n"
                             "│├19.Getmid @ \n"                       
                             "│├20.Respon on|off\n "                                                                                           
                             "│╰───────── \n"
                             "╰─╼「 Selfвoт ᴘʀᴏᴛᴇᴄᴛ ]\n")
                         
                        elif cmd == "help2":
                          if msg._from in admin:               
                             dkbots2(msg.to, 
                             "╭─╼「 DESIGN 」\n"
                             "│╭───────── \n"
                             "│├   SIMPLE DESIGN \n"
                             "│├Versi v3:3\n"                     
                             "│├01.Setkey \n"                       
                             "│├02.Resetkey \n"                             
                             "│├03.Mid \n"
                             "│├04.Mid @ \n"                       
                             "│├05.Crash \n"                             
                             "│├06.About \n"
                             "│├07.Reject \n"                       
                             "│├08.Myname \n"                             
                             "│├09.Mycopy @\n"
                             "│├10.Mybackup \n"                       
                             "│├11.Bc \n"                             
                             "│├12.Runtime \n"
                             "│├13.Gpict \n"                       
                             "│├14.Woy \n"                             
                             "│├15.Mimicadd @ \n"
                             "│├16.Mimicdell @ \n"                       
                             "│├17.Mimic on|off \n"                             
                             "│├18.Mimiclist \n"
                             "│├19.Scall: \n"                       
                             "│├20.Gcall\n\n "                                                  
                             "│╰───────── \n"
                             "╰─╼「 Selfвoт ᴘʀᴏᴛᴇᴄᴛ]")
                            
                        elif cmd == "help3":
                          if msg._from in admin:               
                             dkbots2(msg.to, 
                             "╭─╼「 DESIGN 」\n"
                             "│╭───────── \n"
                             "│├Versi v3:3\n"                     
                             "│├01.Welcome on|off \n"                       
                             "│├02.Sider on|off \n"                             
                             "│├03.Autorespon on|off \n"
                             "│├04.Autojoin on|off \n"                       
                             "│├05.Autoleave on|off \n"                             
                             "│├06.Contact on|off \n"
                             "│├07.Autoadd on|off \n"                       
                             "│├08.Hajar @ \n"                             
                             "│├09.Myname: text\n"
                             "│├10.Autoblock on|off \n"                       
                             "│├11.Brodcash: \n"                             
                             "│├12.Runtime \n"
                             "│├13.Gpict \n"                       
                             "│├14.Woy \n"                             
                             "│├15.Mimicadd @ \n"
                             "│├16.Mimicdell @ \n"                       
                             "│├17.Mimic on|off \n"                             
                             "│├18.Mimiclist \n"
                             "│├19.Scall: \n"                       
                             "│├20.Gcall\n "                                                  
                             "│╰───────── \n"
                             "╰─╼「 Selfвoт ᴘʀᴏᴛᴇᴄᴛ 」\n")
                             
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "DK Versi v3:3\n\n"
                                if wait["sticker"] == True: md+="Sticker On\n"
                                else: md+="Sticker Off\n"
                                if wait["contact"] == True: md+="Contact On\n"
                                else: md+="Contact Off\n"
                                if wait["chatbot"] == True: md+="Chatbot On\n"
                                else: md+="Chatbot Off\n"
                                if wait["talkban"] == True: md+="Talkban On\n"
                                else: md+="Talkban Off\n"
                                if wait["Mentionkick"] == True: md+="Notag On\n"
                                else: md+="Notag Off\n"
                                if wait["detectMention"] == True: md+="Respon On\n"
                                else: md+="Respon Off\n"
                                if wait["autoJoin"] == True: md+="Autojoin On\n"
                                else: md+="Autojoin Off\n"
                                if wait["yutube"] == True: md+="Qryutubee On\n"
                                else: md+="Qryutube Off\n"
                                if wait["smule"] == True: md+="Qrsmule On\n"
                                else: md+="Qrsmule Off\n"
                                if wait["autoJoinbypass"] == True: md+="Autojoinbypass On\n"
                                else: md+="Autojoinbypass Off\n"
                                if wait["autoJoinjs"] == True: md+="Autojoinjs On\n"
                                else: md+="Autojoinjs Off\n" 
                                if wait["autoAdd"] == True: md+="Autoadd On\n"
                                else: md+="Autoadd Off\n"
                                if msg.to in welcome: md+="Welcome On\n"
                                else: md+="Welcome Off\n"
                                if wait["autoLeave"] == True: md+="Leave On\n"
                                else: md+="Leave Off\n"
                                if wait["unsend"] == True: md+="Unsend On\n"
                                else: md+="Unsend Off\n"
                                if wait["responGc"] == True: md+="Respongc On\n"
                                else: md+="Respongc Off\n"
                                if msg.to in protectqr: md+="Protecturl On\n"
                                else: md+="Protecturl Off\n"
                                if msg.to in protectjoin: md+="Protectjoin On\n"
                                else: md+="Protectjoin Off\n"
                                if msg.to in protectkick: md+="Protectkick On\n"
                                else: md+="Protectkick Off\n"
                                if msg.to in protectcancel: md+="Protectcancel On\n"
                                else: md+="Protectcancel Off\n"
                                dkbots2(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                     
                        elif cmd == "crash":
                          if msg._from in admin:
                            cl.sendContact(to, "ua5cb98c3cf03a8df62d9859b831f6c2e',")

#============Chatbots================#
                        elif cmd == "chatbot on" or text.lower() == 'chatbots on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["chatbot"] = True
                                cl.sendMessage(msg.to,"✔ AutoChat Actived")
                                
                        elif cmd == "chatbot off" or text.lower() == 'chatbots off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["chatbot"] = False
                                cl.sendMessage(msg.to," ↘ AutoChat 🚫 nonaktived")
                        
                        elif cmd == 'sepi':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Hooh gara2 kk sih gak mandi (¬_¬)")
                               
                        elif cmd == 'naik':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Moh ah takut di modusin (¬_¬)")

                        elif cmd == 'nah':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Nah neh noh ¯\_(ツ)_/¯ ")                               
                               
                        elif cmd == 'siang':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Iya kk Mat siang mat aktivitas (￣へ￣)") 

                        elif cmd == 'malam':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Iya malam k waktunya bikin ╮(╯▽╰)╭")
                               
                        elif cmd == 'sp':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to," 🔀 Internet gratisan ¯\_(ツ)_/¯")
                               cl.sendMessage(to,"↘0.005076800537109375 Perdetik")
                               
                        elif cmd == 'assalamualaikum':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to," Waalaikumsalam ")
                               cl.sendMessage(to,"Σ(O_O；)")

                        elif cmd == 'waalaikumsalam':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to," Moga yg jwb salam jodoh nya banyak ")
                               cl.sendMessage(to,"╮(╯▽╰)╭ ")

                        elif cmd == 'typo':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to," Tenggelamkan ae yg Typo¯\_(ツ)_/¯")
                               cl.sendMessage(to,"")                               
                             
                        elif cmd == 'kuy':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to," Kemana k ¯\_(ツ)_/¯")
       
                        elif cmd == 'pagi':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Pagi juga kk Mandi gih biar gak jones terus ヽ(｀⌒´)ノ")
                               
                        elif cmd == 'halo':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Halo juga kk apa kabar ?Σ(⊙▽⊙) ")
       
                        elif cmd == 'me':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"ma mie ayam campur telur -_-")       
                               
                        elif cmd == 'oke':
                            if wait["chatbot"] == True:
                               cl.sendMessage(to,"Oke aja deh gue daripada bonyok (╥_╥)")

                                
                        elif cmd == "about":
                                groups = cl.getGroupIdsJoined()
                                contacts = cl.getAllContactIds()
                                blockeds = cl.getBlockedContactIds()
                                crt = "ua5cb98c3cf03a8df62d9859b831f6c2e"
                                supp = "ua5cb98c3cf03a8df62d9859b831f6c2e"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "About",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#7CFC00"
    }
  },
  "type": "bubble",
  "size": "nano",
       "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image"
          
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "{}".format(cl.getProfile().displayName),
                "size": "md",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#800080"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Model: Rombakan",
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Groups: {}".format(str(len(groups))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Friend: {}".format(str(len(contacts))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Block: {}".format(str(len(blockeds))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Versi : DK",
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/RHZ5TvY/1579755402916.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "Minat",
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  
  }
}
}
                                cl.postTemplate(to, data)

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ginvited = cl.getGroupIdsInvited()
                               if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                    cl.rejectGroupInvitation(gid)
                                  sendTextTemplate3b(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                               else:
                                  sendTextTemplate3b(msg.to, "Tidak ada undangan yang tertunda")



                        elif cmd == "/@sepak":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               xyz = cl.getGroup(to)
                               mem = [c.mid for c in xyz.members]
                               targets = []
                               for x in mem:
                                 if x not in ["uc064aa14c3318017de4624b779e1420c",cl.profile.mid]:targets.append(x)
                               if targets:
                                 imnoob = 'satu.js gid={} token={} app={}'.format(to, cl.authToken, "IOSIPAD\t9.18.0\tiPhone OS\t12.1.1")
                                 for target in targets:
                                   imnoob += ' uid={}'.format(target)
                                 success = execute_js(imnoob)
                                 if success:cl.sendMessage(to, "Success kick %i members." % len(targets))
                                 else:cl.sendMessage(to, "Failed kick %i members." % len(targets))
                               else:cl.sendMessage(to, "Target not found.")

                        elif cmd == "/@bola":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               xyz = cl.getGroup(to)
                               if xyz.invitee == None:pends = []
                               else:pends = [c.mid for c in xyz.invitee]
                               targp = []
                               for x in pends: 
                                 if x not in ["uc064aa14c3318017de4624b779e1420c",cl.profile.mid]:targp.append(x)
                               mems = [c.mid for c in xyz.members]
                               targk = []
                               for x in mems:
                                 if x not in ["uc064aa14c3318017de4624b779e1420c",cl.profile.mid]:targk.append(x)
                               imnoob = 'dua.js gid={} token={}'.format(to, cl.authToken)
                               for x in targp:imnoob += ' uid={}'.format(x)
                               for x in targk:imnoob += ' uik={}'.format(x)
                               execute_js(imnoob)
 
                        elif cmd.startswith('/cancell: '):
                         #if settings["kick"] == True:
                            if msg._from in admin:
                               text = text.split(" ")
                               number =msg.text.replace(text[0] + " ","")
                               if number.isdigit():
                                   groups = cl.getGroupIdsJoined()
                                   if int(number) < len(groups) and int(number) >= 0:
                                       groupid = groups[int(number)-1]
                                       try:
                                           #projoin.append(groupid)
                                           x = cl.getGroup(groupid)
                                           anu = x.id
                                           if x.invitee == None:nama = []
                                           else:nama = [contact.mid for contact in x.invitee]
                                           targets = []
                                           for a in nama:
                                               if a not in admin:
                                                   targets.append(a)
                                           nami = [contact.mid for contact in x.members]
                                           targetk = []
                                           cms = 'cancell.js gid={} token={}'.format(anu,cl.authToken)
                                           for a in nami:
                                               if a not in admin:
                                                   targetk.append(a)
                                           for y in targets:
                                               cms += ' uid={}'.format(y)
                                           for y in targetk:
                                               cms += ' uik={}'.format(y)
                                           success = execute_js(cms)
                                           if success:
                                               sendTextTemplate3b(to,"Succes Cancell \n " + str(x.name))  
                                           else:
                                               sendTextTemplate3b(to,"Limit Bose")
                                       except:pass
 
                        elif cmd.startswith('/bypass: '):
                         #if settings["kick"] == True:
                            if msg._from in admin:
                               text = text.split(" ")
                               number =msg.text.replace(text[0] + " ","")
                               if number.isdigit():
                                   groups = cl.getGroupIdsJoined()
                                   if int(number) < len(groups) and int(number) >= 0:
                                       groupid = groups[int(number)-1]
                                       try:
                                           #projoin.append(groupid)
                                           x = cl.getGroup(groupid)
                                           anu = x.id
                                           if x.invitee == None:nama = []
                                           else:nama = [contact.mid for contact in x.invitee]
                                           targets = []
                                           for a in nama:
                                               if a not in admin:
                                                   targets.append(a)
                                           nami = [contact.mid for contact in x.members]
                                           targetk = []
                                           cms = 'bypass.js gid={} token={}'.format(anu,cl.authToken)
                                           for a in nami:
                                               if a not in admin:
                                                   targetk.append(a)
                                           for y in targets:
                                               cms += ' uid={}'.format(y)
                                           for y in targetk:
                                               cms += ' uik={}'.format(y)
                                           success = execute_js(cms)
                                           if success:
                                               sendTextTemplate3b(to,"Succes Baypass \n " + str(x.name))
                                           else:
                                               sendTextTemplate3b(to,"Limit Bose")
                                       except:pass
  
                        elif cmd.startswith('/js: '):
                         #if settings["kick"] == True:
                            if msg._from in admin:
                               text = text.split(" ")
                               number =msg.text.replace(text[0] + " ","")
                               if number.isdigit():
                                   groups = cl.getGroupIdsJoined()
                                   if int(number) < len(groups) and int(number) >= 0:
                                       groupid = groups[int(number)-1]
                                       try:
                                           #projoin.append(groupid)
                                           x = cl.getGroup(groupid)
                                           anu = x.id
                                           if x.invitee == None:nama = []
                                           else:nama = [contact.mid for contact in x.invitee]
                                           targets = []
                                           for a in nama:
                                               if a not in admin:
                                                   targets.append(a)
                                           nami = [contact.mid for contact in x.members]
                                           targetk = []
                                           cms = 'simple.js gid={} token={}'.format(anu,cl.authToken)
                                           for a in nami:
                                               if a not in admin:
                                                   targetk.append(a)
                                           for y in targets:
                                               cms += ' uid={}'.format(y)
                                           for y in targetk:
                                               cms += ' uik={}'.format(y)
                                           success = execute_js(cms)
                                           if success:
                                               sendTextTemplate3b(to,"Succes Js \n " + str(x.name))
                                           else:
                                               sendTextTemplate3b(to,"Limit Bose")
                                       except:pass

                        elif cmd == "cpp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                dragonkiller(msg.to,"➥Kirim fotonya.....")

                        elif cmd == "cfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"] = True
                                dragonkiller(msg.to,"Kirim fotonya.....")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	dragonkiller(to, "Kirim video Sayang")

                        elif cmd == ".me":
                          if msg._from in admin:
                            cl.sendContact(to, sender)
                        elif cmd == "ss":
                          if msg._from in admin:
                            sendMentionV2(to, "@!", [sender])
                            cl.sendContact(to, sender)
                        elif cmd == "mymid":
                          if msg._from in admin:
                            cl.sendMessage(to, "[ MID ]\n{}".format(sender))
                        elif cmd == "myname":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            dragonkiller(to, "{}".format(contact.displayName))
                        elif cmd == "mybio":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            dragonkiller(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                        elif cmd == "mypict":
                          if msg._from in admin:
                            cl.sendContact(to, sender)
                            contact = cl.getContact(sender)
                            cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif cmd == "myvideoprofile":
                            contact = cl.getContact(sender)
                            cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        
                        elif cmd.startswith("mycopy "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.cloneContactProfile(ls)
                                    sendTemplate(to, "Berhasil mengclone profile {}".format(contact.displayName))


                        elif cmd == "mybackup":
                            try:
                                clientProfile = cl.getProfile()
                                clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                cl.updateProfileAttribute(8, clientProfile.pictureStatus)
                                cl.updateProfile(clientProfile)
                                coverId = str(settings["myProfile"]["coverId"])
                                cl.updateProfileCoverById(coverId)
                                dragonkiller(to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                            except Exception as e:
                                dragonkiller(to, "Succes restore profile")
                                logError(error)
                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "MID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif cmd.startswith("addme "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "ᴀᴅᴅ sᴜᴄᴄᴇs" + str(contact.displayName) + "ʀɴᴀᴍᴇ")

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate11(msg.to, "✨ Nama : "+str(mi.displayName)+"\n✨ Mid : " +key1+"\n✨ Status Msg"+str(mi.statusMessage))
                               sendTextTemplate(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd.startswith("getmid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "[ Mid User ]"
                                for ls in lists:
                                    ret_ += "\n{}".format(str(ls))
                                cl.sendMessage(to, str(ret_))
                        elif cmd.startswith("getname "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    dragonkiller(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                        elif cmd.startswith("getbio "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    dragonkiller(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))

                        elif cmd == "mycover":
                            channel = cl.getProfileCoverURL(sender)          
                            path = str(channel)
                            cl.sendImageWithURL(to, path)
#<<=====●MUSIC SMULE SEARCH●==============================================>>



#------------------------------------============================------------------------------------#

#===========BOT UPDATE============#                            
                        elif cmd.startswith("image "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                textnya = msg.text.replace(sep[0] + " ","")
                                path = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=00FF00,70&chf=bg,s,000000"
                                cl.sendImageWithURL(msg.to,path)
                                
                        elif cmd.startswith("image2 "):
                          if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=ppqeuy&text={}".format(txt)
                                #cl.sendImageWithURL(to, url)                          
                                data = {
                                                "type": "template",
                                                "altText": "PICTURE",
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": url,
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri":url,
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                cl.postTemplate(to, data)


                        elif cmd.startswith("image3 "): 
                          if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=ppqeuy&text={}".format(txt)
                                #cl.sendImageWithURL(to, url)                                
                                data = {
                                                "type": "template",
                                                "altText": "PICTURE",
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": url,
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri":url,
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                cl.postTemplate(to, data)


                        elif cmd.startswith("image4 "): #fscosplay
                           if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=ppqeuy&text={}".format(txt)
                                cl.sendImageWithURL(to, url)

                        elif cmd.startswith("bio: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               separate = msg.text.split(" ")
                               string = msg.text.replace(separate[0] + " ","")
                               profile_G = cl.getProfile()
                               profile_G.statusMessage = string
                               cl.updateProfile(profile_G)
                               sendTextTemplat0(msg.to, "sucses.\nbio : {}".format(str(string)))

#======================-----------✰ ᴅkʙᴏᴛ ✰-----------======================#

                        elif cmd == "mypict":
                          if msg._from in admin:
                            cl.sendContact(to, sender)
                            contact = cl.getContact(sender)
                            res = '╭───「 contact 」'
                            if contact:
                                res += '\n├ MID : ' + contact.mid
                                res += '\n├ Display Name : ' + str(contact.displayName)
                                if contact.displayNameOverridden: res += '\n├ Display Name : ' + str(contact.displayNameOverridden)
                                res += '\n├ Status Message : ' + str(contact.statusMessage)
                            res += '\n╰───「 Finish 」'
                            if cmd == 'mypict':
                                if contact:
                                    if contact.pictureStatus:
                                        data = {
                "type": "template",
                "altText": "MY PROFILE",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "✺Contact✺",
                        "uri": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                        cl.postTemplate(to, data)
                                    cover = cl.getProfileCoverURL(contact)
                                    data = {
                "type": "template",
                "altText": "MY PROFILE",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": cover,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "COVER",
                        "uri": cover,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                    cl.postTemplate(to, data)

                        elif cmd.startswith('ppme'):
                          if msg._from in admin:
                            #textt = removeCmd(cmd, text)
                            #texttl = textt.lower()
                            cl.sendContact(to, sender)
                            contact = cl.getContact(sender) 
                            res = '╭───「 contact 」'
                            if contact:
                                res += '\n├ MID : ' + contact.mid
                                res += '\n├ Display Name : ' + str(contact.displayName)
                                if contact.displayNameOverridden: res += '\n├ Display Name : ' + str(contact.displayNameOverridden)
                                res += '\n├ Status Message : ' + str(contact.statusMessage)
                            res += '\n╰───「 Finish 」'
                            if cmd == 'ppme':
                                if contact:
                                    if contact.pictureStatus:
                                        data = {
                "type": "template",
                "altText": "MY PROFILE",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "✺Contact✺",
                        "uri": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                        cl.postTemplate(to, data)
                                    cover = cl.getProfileCoverURL(contact)
                                    data = {
                "type": "template",
                "altText": "MY PROFILE",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": cover,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "COVER",
                        "uri": cover,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                    cl.postTemplate(to, data)
                        
                        elif cmd.startswith('pplu'):
                          if msg._from in admin:
                            profile = cl.getContact(to) if msg.toType == 0 else None
                            res = '╭───「 Profile 」'
                            if profile:
                                res += '\n├ MID : ' + profile.mid
                                res += '\n├ Display Name : ' + str(profile.displayName)
                                if profile.displayNameOverridden: res += '\n├ Display Name : ' + str(profile.displayNameOverridden)
                                res += '\n├ Status Message : ' + str(profile.statusMessage)
                            res += '\n╰───「 Finish 」'
                            if cmd == 'pplu':
                                if profile:
                                    if profile.pictureStatus:
                                        data = {
                "type": "template",
                "altText": "MY PROFILE",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": "https://obs.line-scdn.net/{}".format(profile.pictureStatus),
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "✺ℙrofile✺",
                        "uri": "https://obs.line-scdn.net/{}".format(profile.pictureStatus),
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                        cl.postTemplate(to, data)
                                    cover = cl.getProfileCoverURL(profile.mid)
                                    data = {
                "type": "template",
                "altText": "MY PROFILE",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": cover,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "COVER",
                        "uri": cover,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                    cl.postTemplate(to, data)
                                #dragonkiller(to, parsingRes(res).format_map(SafeDict(key=text.title())))

                        elif cmd.startswith("getcover "):
                            if cl != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        channel = cl.getProfileCoverURL(ls)
                                        path = str(channel)
                                        #cl.sendImageWithURL(to, str(path))								   
                                        data = {
                "type": "template",
                "altText": "Profile",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": path,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "✺Cover✺",
                        "uri": path,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                        cl.postTemplate(to, data)
 
                        elif cmd.startswith("getpict"):
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = cl.getContact(ls)
                                        channel = cl.getProfileCoverURL(ls)
                                        path = str(channel)
                                        data = {
                "type": "template",
                "altText": "Profile",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "✺ρRofile✺",
                        "uri": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                        cl.postTemplate(to, data)
                                        data = {
                "type": "template",
                "altText": "Profile",
                "template": {
                  "type": "image_carousel",
                  "columns": [
                    {
                      "imageUrl": path,
                      "layout": "horizontal",
                      "action": {
                        "type": "uri",
                        "label": "✺Cover✺",
                        "uri": path,
                        "area": {
                          "x": 447,
                          "y": 356,
                          "width": 1040,
                          "height": 1040
                        }
                      }
                    }
                  ]
                }
              }
                                        cl.postTemplate(to, data)

                        elif cmd.startswith("getvid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(to, str(path))
						   
								                    
                        elif text.lower() == "cchat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   dragonkiller(msg.to, "          done kk")
                               except:
                                   pass
                        
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	dragonkiller(to, "sʜᴀʀᴇ ᴠɪᴅᴇᴏɴʏᴀ")

                        elif cmd == "bc audio":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["bcg_audio"] = True
                            #cl.sendMessage(msg.to,"Kirim foto yg mau di broadcast")
                            data = {
                                "type": "text",
                                "text": "Kirim audio yg mau di broadcast",
                                "sentBy": {
                                    "label": "⟗Selfbot",
                                    "iconUrl": "https://i.ibb.co/j6vg2tm/1543637675013.jpg",
                                    "linkUrl": "line://app/1563216514-3laRoKqK?type=foimage&img=https://i.ibb.co/j6vg2tm/1543637675013.jpg",
                                }
                            }
                            cl.postTemplate(to, data)

                        elif cmd == "bc image":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["bcg_image"] = True
                            #cl.sendMessage(msg.to,"Kirim foto yg mau di broadcast")
                            data = {
                                "type": "text",
                                "text": "Kirim foto yg mau di broadcast",
                                "sentBy": {
                                    "label": "⟗Selfbot",
                                    "iconUrl": "https://i.ibb.co/j6vg2tm/1543637675013.jpg",
                                    "linkUrl": "line://app/1563216514-3laRoKqK?type=foimage&img=https://i.ibb.co/j6vg2tm/1543637675013.jpg",
                                }
                            }
                            cl.postTemplate(to, data)
                        elif cmd == "bc video":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	wait["bcg_video"] = True
                            #cl.sendMessage(msg.to,"Kirim video yg mau di broadcast")
                            data = {
                                "type": "text",
                                "text": "Kirim video yg mau di broadcast",
                                "sentBy": {
                                    "label": "⟗Selfbot🕸 ",
                                    "iconUrl": "https://i.ibb.co/j6vg2tm/1543637675013.jpg",
                                    "linkUrl": "line://app/1563216514-3laRoKqK?type=foimage&img=https://i.ibb.co/j6vg2tm/1543637675013.jpg",
                                }
                            }
                            cl.postTemplate(to, data)

                        elif cmd.startswith("brodcash: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))
                                   
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               dragonkiller(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   dragonkiller(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate3b(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate3b(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               dragonkiller(to,"Waaiiit..... ⏳")
                               Setmain["restartPoint"] = msg.to
                               time.sleep(3)
                               dragonkiller(to,"███▒▒▒▒▒▒▒")
                               time.sleep(2)
                               dragonkiller(to,"█████▒▒▒▒▒")
                               time.sleep(2)
                               dragonkiller(to,"██████████")
                               time.sleep(2)
                               dragonkiller(to,"~Bots Actived..✔")
                               restartBot()
          
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               dragonkiller(msg.to,bot)
                            
                        elif cmd == "groups":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate3(msg.to, "『❎』ᴅᴀʀᴋ ɪɴғᴏ\n\n『❎』 Nama Group : {}".format(G.name)+ "\『❎』 ID Group : {}".format(G.id)+ "\『❎』 Pembuat : {}".format(G.creator.displayName)+ "\n『❎』 Waktu Dibuat : {}".format(str(timeCreated))+ "\n『❎』 Jumlah Member : {}".format(str(len(G.members)))+ "\n『❎』 Jumlah Pending : {}".format(gPending)+ "\n『❎』 Group Qr : {}".format(gQr)+ "\『❎』 Group Ticket : {}".format(gTicket))
                                sendTextTemplate(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

#===================>>>>MEDIA<<<<=======================================================================================================

                        elif cmd.startswith("bmkg"):
                          if msg._from in admin:
                            r=requests.get("http://dolphinapi.herokuapp.com/api/bmkg")
                            data=r.text
                            data=json.loads(data)
                            ret_ = "╭──[「 New Info BMKG」]"
                            ret_ += "\n├ Info : {}".format(str(data["result"]["desc"]))
                            ret_ += "\n╰──[ Finish ]"                             
                            dragonkiller(to, str(ret_))
                            cl.sendImageWithURL(to, data["result"]["image"])


                        elif cmd.startswith("mywaifu"):
                          if msg._from in admin:
                            r=requests.get("http://dolphinapi.herokuapp.com/api/waifu")
                            data=r.text
                            data=json.loads(data)
                            ret_ = "╭──[「 Description Waifu」]"
                            ret_ += "\n├ Name : {}".format(str(data["result"]["title"]))
                            ret_ += "\n╰──[ Finish ]"                             
                            sendTextTemplate0(to, str(ret_))
                            cl.sendImageWithURL(to, data["result"]["image"])


                        elif cmd.startswith("skill "):
                          if msg._from in admin:
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = cl.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = cl.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return dragonkiller(to,"not found name "+midn)
                           for target in targets:
                               cl.kickoutFromGroup(msg.to,[target])


                        elif cmd.startswith("add @"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:                                                                                                                                      
                                       try:
                                          cl.findAndAddContactsByMid(target)
                                          dragonkiller(to,"ᴡᴇs ʙᴏs\ndone add")
                                       except:
                                           pass



                        elif cmd.startswith("block @"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:                                                                                                                                      
                                       try:
                                          cl.blockContact(target)
                                          dragonkiller(to,"ᴡᴇs ʙᴏs")
                                       except:
                                           pass

                        elif cmd.startswith("unsend1"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                args = msg.text.lower().replace("Unsend1","")
                                mes = 0
                                try:
                                    mes = int(args[1])
                                except:
                                    mes = 12
                                    M = cl.getRecentMessagesV2(to, 100)
                                    MId = []
                                    for ind,i in enumerate(M):
                                        if ind == 0:
                                            pass
                                        else:
                                            if i._from == cl.profile.mid:
                                                MId.append(i.id)
                                                if len(MId) == mes:
                                                    break
                                    def unsMes(id):
                                        cl.unsendMessage(id)
                                    for i in MId:
                                        thread1 = threading.Thread(target=unsMes, args=(i,))
                                        thread1.start()
                                        thread1.join()
                                    dragonkiller(to, ' 📂「 Unsend 」📂\n pesan {} (sukses)'.format(len(MId))) 
                                    cl.unsendMessage(msg_id) 

                        elif cmd.startswith("unsendgroup"):
                          if msg._from in admin or msg._from in Bots:
                            args = msg.text.lower().replace("unsendgroup ","")
                            dan = text.split(" ")
                            groups = cl.getGroupIdsJoined()
                            try:
                                listGroup = groups[int(dan[1])-1]
                                group = cl.getGroup(listGroup)
                                mes = 0
                                try:
                                    mes = int(args[1])
                                except:
                                    mes = 10
                                M = cl.getRecentMessagesV2(group.id, 101)
                                MId = []
                                for ind,i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == cl.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                                break
                                def unsMes(id):
                                    cl.unsendMessage(id)
                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.start()
                                    thread1.join()
                                dragonkiller(to, "Success unsend {} message".format(len(MId)))
                            except:
                                    pass

                        elif cmd.startswith("tampol "):
                          if settings["kick"] == True:
                            if msg._from in admin:
                                pisah = text.split("Tampol ")
                                nk0 = text.replace(pisah[0]+"Tampol ","")
                                nk1 = nk0.lstrip()                                                           
                                _name = nk1
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for i in gs.members:
                                    if _name in i.displayName:
                                        targets.append(i.mid)
                                if targets == []:
                                  cl.sendMessage(msg.to,"target not found")
                                else:
                                    for target in targets:
                                        if target in Rteam:
                                           pass
                                        else:
                                            cl.kickoutFromGroup(msg.to,[target])
                                            time.sleep(0.00001)

                        elif cmd.startswith("ginfo"):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "『❎』 ᴅᴀʀᴋ ɢʀᴏᴜᴘ ɪɴғᴏ\n"
                                ret_ += "\n『❎』 Nama Group : {}".format(G.name)
                                ret_ += "\n『❎』 ID Group : {}".format(G.id)
                                ret_ += "\n『❎』 Pembuat : {}".format(gCreator)
                                ret_ += "\n『❎』 Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n『❎』 Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n『❎』 Jumlah Pending : {}".format(gPending)
                                ret_ += "\n『❎』 Group Qr : {}".format(gQr)
                                ret_ += "\n『❎』 Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                dragonkiller(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "『❎』 "+ str(no) + ". " + mem.displayName
                                dragonkiller(to,"『❎』 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass


                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               dragonkiller(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "invite":
                          if msg._from in admin:
                                wait['undang'] = True
                                sendTextTemplate3(to,"Send Contact For Invite Target")
#
 #============================================#
#===========Promo============#
                        elif cmd == "promo":
                          if msg._from in admin:
                             cl.sendMessage(msg.to,"──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~dkbots\nline.me/ti/p/~ownerd\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")      
                             dragonkiller(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih😊😊")

                        elif cmd == "harga":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "╭══════════\n║⚫─[     DAFTAR HARGA     ]─⚫ \n║SELFBOT ONLY = 75K /BLN\n║2 ASSIST = 100K /BLN\n║5 ASSIST = 200K /BLN\n║10 ASSIST = 300K /BLN\n║\n║PROTECT ANTIJS\n║\n║2 BOT + ANTIJS = 150K /BLN\n║5 BOT + ANTIJS = 300K /BLN\n║10 BOT + ANTIJS = 500K /BLN\n║\n║12 BOT WAR+ ANTIJS = 500K /BLN\n║\n║═ই\═ANDA BERMINAT\n║ SILAHKAN ADD CONTACT \n║ DIBAWAH INI   \n║\n║http://line.me/ti/p/~ownerdk\n║       TERIMA KASIH      \n║\n╰════════════")
                               dragonkiller(msg.to, "Yuck di Order.... ")

#===========Hiburan============#

    

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               dragonkiller(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")


                        elif msg.text.lower() in wait["tagall"]:
                          if msg._from in admin:        
                            if wait["selfbot"] == True:
                              if msg._from in owner or msg._from in admin or msg._from in staff:  
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    cl.sendMessage(to, "◀Mention {} Member▶".format(str(len(nama)))) 
           
                        elif cmd == "link on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   sendTextTemplate3b(msg.to, "Url Opened")

                        elif cmd == "link off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate3b(msg.to, "Url Closed")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#                    
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate3b(msg.to,"Nama diganti jadi " + string + "")
               

                        elif cmd == 'woy':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gname = cl.getGroup(msg.to)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n Halo {} '.format(str(gname.name))
                                            atas += '\n Halo {} Sekawan'.format(str(len(local)))
                                        cl.sendMessage(msg.to, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(msg.to, str(error))
               
                        elif cmd == "protect list":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                dragonkiller(msg.to," Dark Protection\n\n 『❎』PROTECT URL :\n"+ma+"\n『❎』 PROTECT KICK :\n"+mb+"\n『❎』PROTECT JOIN :\n"+md+"\n『❎』 PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))
   
                        elif cmd == "bye me":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate3(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)
                      
                        
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendTextTemplate3b(msg.to, "「Speed witing」")
                               elapsed_time = time.time() - start
                               dragonkiller(msg.to, "{}". format (str(elapsed_time/10)))
                               
                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate3b(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate3b(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate3b(msg.to, "Sudak tidak aktif")

                        elif cmd == "sider2 on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate3b(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv2['point2'][msg.to]
                                  del cctv2['sidermem2'][msg.to]
                                  del cctv2['cyduk2'][msg.to]
                              except:
                                  pass
                              cctv2['point2'][msg.to] = msg.id
                              cctv2['sidermem2'][msg.to] = ""
                              cctv2['cyduk2'][msg.to]=True

                        elif cmd == "sider2 off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv2['point2']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv2['cyduk2'][msg.to]=False
                                  sendTextTemplate3b(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate3b(msg.to, "Sudak tidak aktif")

                        elif cmd.startswith("mimicadd"):
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    settings["mimic"]["target"][target] = True
                                    dragonkiller(msg.to,"Added♪")
                                    break
                                except:
                                    dragonkiller(msg.to,"Failed♪")
                                    break
                        elif cmd.startswith("mimicdel"):
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    del settings["mimic"]["target"][target]
                                    sendTemplate(msg.to,"Clear Target♪")
                                    break
                                except:
                                    dragonkiller(msg.to,"Failed♪")
                                    break
                                    
                        elif cmd == "mimiclist":
                            if settings["mimic"]["target"] == {}:
                                sendTemplate(msg.to,"No Target♪")
                            else:
                                mc = "MimicList♪\n"
                                for mi_d in settings["mimic"]["target"]:
                                    mc += "\n♪ "+cl.getContact(mi_d).displayName
                                mc += "\n\non top list mimic"
                                dragonkiller(msg.to,mc)
                                
                        elif cmd.startswith("mimic"):
                            sep = text.split(" ")
                            mic = text.replace(sep[0] + " ","")
                            if mic == "on":
                                if settings["mimic"]["status"] == False:
                                    settings["mimic"]["status"] = True
                                    dragonkiller(msg.to,"On♪")
                            elif mic == "off":
                                if settings["mimic"]["status"] == True:
                                    settings["mimic"]["status"] = False
                                    dragonkiller(msg.to,"Off♪")
#===========conten.type============#                    
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    sendTextTemplate3(to, str(ret_))
                                except:
                                    sendTextTemplate3(to, "Post tidak valid")
							                                           

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))


                        elif 'idline: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('idline: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
								  

#===========Protection============#
                        elif 'Wellcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Wellcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Wellcome sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Sambutan diaktifkan\nDi Group : " +str(ginfo.name)
                                  dragonkiller(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Sambutan sudah tidak aktif"
                                    dragonkiller(msg.to, "「Dinonaktifkan」\n" + msgs)



                        elif 'protectqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('protectqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  dragonkiller(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    dragonkiller(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  dragonkiller(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    dragonkiller(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  dragonkiller(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    dragonkiller(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  dragonkiller(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    dragonkiller(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'pro-all ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('pro-all ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  dragonkiller(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    dragonkiller(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#                     
                        elif ("Hajar " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate3b(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           dragonkiller(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           dragonkiller(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.remove(target)
                                           dragonkiller(to,"Admin Expelled ✔ By " + cl.getContact(sender).displayName)
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del staff[target]
                                           f=codecs.open('staff.json','w','utf-8')
                                           json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           dragonkiller(to,"Staff Expelled ✔ By " + cl.getContact(sender).displayName)
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sendTextTemplate3b(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")
								
                        elif cmd == "admin:off" or text.lower() == 'admin:off':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                dragonkiller(msg.to,"Deteksi admin dinonaktifkan")

                        elif cmd == "staff:off" or text.lower() == 'staff:off':
                            if msg._from in admin:
                                wait["addstaff"] = False
                                dragonkiller(msg.to,"Deteksi staff dinonaktifkan")

                        elif cmd == "bot:off" or text.lower() == 'bot:off':
                            if msg._from in admin:
                                wait["addbots"] = False
                                dragonkiller(msg.to,"Deteksi bots dinonaktifkan")


                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                settings["changePicture"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                dragonkiller(msg.to,"Berhasil di Refresh...")

                        elif cmd == "admin cek" or text.lower() == 'admin cek':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        
                        elif msg.contentType == 13:
                            if settings["conpp"] == True:
                                _name = msg.contentMetadata["displayName"]
                                copy = msg.contentMetadata["mid"]
                                groups = cl.getGroup(msg.to)
                                targets = []
                                for s in groups.members:
                                    if _name in s.displayName:
                                        print ("[Target] Copy")
                                        break                             
                                else:
                                        targets.append(copy)
                                if targets == []:
                                    dragonkiller(msg.to, "Not Found...")
                                    pass
                                else:
                                    for target in targets:
                                        try:
                                            cl.cloneContactProfile(target)
                                            cl.sendMessage(msg.to, "Clone Contact Profile and Cover Done")
                                            settings['conpp'] = False
                                            break
                                        except:
                                                 msg.contentMetadata = {'mid': target}
                                                 settings["conpp"] = False
                                                 break
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                dragonkiller(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                dragonkiller(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                dragonkiller(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                dragonkiller(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "autorespon on" or text.lower() == 'autorespon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                dragonkiller(msg.to,"Auto autorespon diaktifkan")

                        elif cmd == "autorespon off" or text.lower() == 'autorespon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                dragonkiller(msg.to,"Auto autorespon dinonaktifkan")
 
                        elif cmd == "respongc on" or text.lower() == 'respongc on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responGc"] = True
                                dragonkiller(msg.to,"Respongc diaktifkan")

                        elif cmd == "respongc off" or text.lower() == 'respongc off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responGc"] = False
                                dragonkiller(msg.to,"Respongc dinonaktifkan")


                        elif cmd == "detetctvp on" or text.lower() == 'detectvp on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectvp"] = True
                                dragonkiller(msg.to,"Respondtetcvp diaktifkan")

                        elif cmd == " detectvp off" or text.lower() == 'detectvp off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectvp"] = False
                                dragonkiller(msg.to,"Responvp dinonaktifkan")

                        if cmd == "unsend on":
                            if msg._from in admin:
                               wait["unsend"] = True
                               data = {
                                   "type": "text",
                                   "text": "╭❂➣\n│Unsend Mode on\n╰❂➣",
                                   "sentBy": {
                                       "label": "⟗Selfbots🕸",
                                       "iconUrl": "https://i.ibb.co/9THQxM0/1543637675013.jpg",
                                       "linkUrl": "line://app/1563216514-3laRoKqK?type=foimage&img=https://1.bp.blogspot.com/-dRjfpWq8I4g/Xca8rX8RTmI/AAAAAAAAOhA/Dn9Ep4yl5XE3i53n2VG-w5R-7RGpPb7HACEwYBhgL/s1600/20191031_101855.jpg",  #https://i.ibb.co/tKkFR5r/001.png
                                   }
                               }
                               cl.postTemplate(to, data)
                        if cmd == "unsend off":
                            if msg._from in admin:
                               wait["unsend"] = False
                               data = {
                                   "type": "text",
                                   "text": "╭❂➣➣\n│Unsend Mode Off\n❂➣",
                                   "sentBy": {
                                       "label": "⟗Selfbots",
                                       "iconUrl": "https://i.ibb.co/9THQxM0/1543637675013.jpg",
                                       "linkUrl": "line://app/1563216514-3laRoKqK?type=foimage&img=https://1.bp.blogspot.com/-dRjfpWq8I4g/Xca8rX8RTmI/AAAAAAAAOhA/Dn9Ep4yl5XE3i53n2VG-w5R-7RGpPb7HACEwYBhgL/s1600/20191031_101855.jpg",  #https://i.ibb.co/tKkFR5r/001.png
                                   }
                               }
                               cl.postTemplate(to, data)




                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                dragonkiller(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                dragonkiller(msg.to,"Autojoin dinonaktifkan")
#tambah
                        elif cmd == "smuleqr on" or text.lower() == 'smuleqr on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["smule"] = True
                                dragonkiller(msg.to,"Autodownload smule diaktifkan")

                        elif cmd == "smuleqr off" or text.lower() == 'smuleqr off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["smule"] = False
                                dragonkiller(msg.to,"Autodownload smule dinonaktifkan")
 
                        elif cmd == "yutubeqr on" or text.lower() == 'yutubeqr on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["yutube"] = True
                                dragonkiller(msg.to,"Autodownload Link yutube diaktifkan")
 
                        elif cmd == "yutubeqr off" or text.lower() == 'tubeqr off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["yutube"] = False
                                dragonkiller(msg.to,"Autodownload Link yutube dinonaktifkan")

                        elif cmd == "autojoinbypass on" or text.lower() == 'autojoinbypass:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinbypass"] = True
                                dragonkiller(msg.to,"Autojoin bypasskikil diaktifkan")

                        elif cmd == "autojoinbypass off" or text.lower() == 'autojoinbypass:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinbypass"] = False
                                dragonkiller(msg.to,"Autojoinkikil bypass dinonaktifkan")

                        elif cmd == "autojoinjs on" or text.lower() == 'autojoinjs:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinjs"] = True
                                dragonkiller(msg.to,"Autojoin Kickalljs diaktifkan")

                        elif cmd == "autojoinjs off" or text.lower() == 'autojoinjs:off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinjs"] = False
                                dragonkiller(msg.to,"Autojoin kikilJs dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                dragonkiller(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                dragonkiller(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                dragonkiller(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                dragonkiller(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                dragonkiller(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                dragonkiller(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                Kifli1(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                dragonkiller(msg.to,"Notag dinonaktifkan")

                        elif cmd == "antibypass on" or cmd == "probypass on":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Bots:
                                settings["anbypass"] = True
                                dkbots2(msg.to,"Probypass diaktifkan")

                        elif cmd == "love on" or text.lower() == 'love on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mylove"] = True
                                sendTextTemplate0(to,"ʟᴏᴠᴇ ᴛᴇᴍᴘʟᴀᴛᴇ sᴇᴛ ᴛᴏ ᴏɴ")

                        elif cmd == "love off" or text.lower() == 'love off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mylove"] = False
                                sendTextTemplate0(to,"ʟᴏᴠᴇ ᴛᴇᴍᴘʟᴀᴛᴇ sᴇᴛ ᴛᴏ ᴏғғ")

                        elif cmd == "bday on" or text.lower() == 'bday on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["BDAY"] = True
                                sendTextTemplate0(to,"ᴛᴇᴍᴘʟᴀᴛᴇ sᴇᴛ ᴛᴏ ᴏɴ")

                        elif cmd == "bday off" or text.lower() == 'bday off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait[" BDAY"] = False
                                sendTextTemplate0(to,"ᴛᴇᴍᴘʟᴀᴛᴇ sᴇᴛ ᴛᴏ ᴏғғ")


##
#=============CMD ON/OFF============
                        elif ("Kepoin " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate0(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg : "+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd.startswith("bcvoice "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                bctxt = cmd.replace("bcvoice ", "")
                                bc = ("Broadcast voice")
                                cb = (bctxt + bc)
                                tts = gTTS(cb, lang='id', slow=False)
                                tts.save('tts.mp3')
                                n = cl.getGroupIdsJoined()
                                for Ngentot in n:
                                    cl.sendAudio(Ngentot, 'tts.mp3')

                        elif cmd.startswith('.call '):
                            if msg._from in admin:
                                sep = text.split(" ")
                                num = int(sep[1])
                                try:                           
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            for var in range(0,num):
                                                group = cl.getGroup(to);nama = [contact.mid for contact in group.members]
                                                members = [ls]
                                                cl.call.inviteIntoGroupCall(to,nama,mediaType=2)
                                            sendMentionV2(to, "Succesfully Spamcall to @!", [ls])
                                except Exception as error:
                                    cl.sendMessage(to, str(error))


                        elif text.lower() == 'test':
                            if msg._from in admin:
                               get_profile_time_start = time.time() /6
                               get_profile = cl.getProfile()
                               get_profile_time = time.time() /6 - get_profile_time_start
                               speed = "{}".format(str(get_profile_time /6))
                               Kifli1(msg.to, speed)


                        elif cmd == "tiktok on" or text.lower() == 'tiktok on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["TIKTOK"] = True
                                sendTextTemplate0(msg.to,"𝚝𝚒𝚔𝚝𝚘?? 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚜 𝚖𝚘𝚍𝚎 𝚘𝚗")

                        elif cmd == "tiktok off" or text.lower() == 'tiktok off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["TIKTOK"] = False
                                sendTextTemplate0(msg.to,"𝚝𝚒𝚔𝚝𝚘𝚔 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚜 𝚖𝚘𝚍𝚎 𝚘𝚏𝚏")

                        elif cmd == "instagram on" or text.lower() == 'instagram on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["INSTAGRAM"] = True
                                sendTextTemplate0(msg.to,"𝚒𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚜 𝚖??𝚍𝚎 𝚘𝚗")

                        elif cmd == "instagram off" or text.lower() == 'instagram off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["INSTAGRAM"] = False
                                sendTextTemplate0(msg.to,"𝚒𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚜 𝚖𝚘𝚍𝚎 𝚘𝚏𝚏")


                        elif cmd == "notif pp on":
                              if msg._from in admin:
                                if wait["notifProfile"] == True:
                                    cl.sendMessage(to, "Notif Profile telah aktif")
                                else:
                                    wait["notifProfile"] = True
                                    sendTextTemplate0(to, "Berhasil mengaktifkan Notif Profile")
                        elif cmd == "notif pp off":
                              if msg._from in admin:
                                if wait["notifProfile"] == False:
                                    cl.sendMessage(to, "Notif Profile telah nonaktif")
                                else:
                                    wait["notifProfile"] = False
                                    sendTextTemplate0(to, "Berhasil menonaktifkan Notif Profile")

#===========COMMAND BLACKLIST============#
                        elif 'https://www.instagram.com/p/' in text.lower():
                          if wait["INSTAGRAM"] == True:
                            try:
                                sep = text.split("https://www.instagram.com/p/")
                                split= text.replace(sep[0] + "https://www.instagram.com/p/","")
                                url = "https://www.instagram.com/p/{}".format(split)
                                apiKey = "tByQDzRa8z8D"
                                headers = {"apiKey": "tByQDzRa8z8D"}
                                r = requests.get("https://beapi.me/instapost?url="+url,headers=headers)
                                data = r.text
                                data = json.loads(data)
                                for media in data["result"]["media"]:
                                       if media["is_video"]:
                                             sendTextTemplate0(to, "iⁿˢᵗaᵍʳaᵐ ᵈoʷⁿˡoaᵈˢ")
                                             data = {
                                                            "type": "video",
                                                            "originalContentUrl": media["video"],
                                                            "previewImageUrl": media["img"],
                                                         }
                                             cl.postTemplate(to, data)
                                       else:
                                             data = {
                                                            "type": "image",
                                                            "originalContentUrl": media["img"],
                                                            "previewImageUrl": media["img"],
                                                            "sentBy": {
                                                                     "label": data["result"]["owner"]["username"],
                                                                     "iconUrl": data["result"]["owner"]["profile_pic_url"],
                                                                     "linkUrl": "https://www.instagram.com/p/{}".format(split)
                                                            }
                                                         }
                                             cl.postTemplate(to, data)
                            except Exception as e:
                            	cl.sendMessage(to, str(e))


                        elif 'https://beapi.me/tiktok' in text.lower():
                          if wait["TIKTOK"] == True:
                            try:
                                sep = text.split("https://beapi.me/tiktok")
                                split= text.replace(sep[0] + "https://beapi.me/tiktok","")
                                url = "https://beapi.me/tiktok{}".format(split)
                                api = BEAPI("tByQDzRa8z8D")
                                #headers = {"apiKey": "tByQDzRa8z8D"}
                                res = api.musicallyDown('https://beapi.me/tiktok') 
                                data = res.text
                                data = json.loads(data)
                                data = {
                                           "type": "video",
                                           "originalContentUrl": data["result"]['itemInfos']['video']['urls_nowm'][0],
                                           "previewImageUrl": data["result"]['itemInfos']['coversOrigin'][0],
                                      }
                                cl.postTemplate(to, data)
                                print(data)
                            except Exception as e:
                            	cl.sendMessage(to, str(e))

                        elif ("Bday " in msg.text): 
                          if wait["BDAY"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               bdr1 = ("#00CCFF","#1AE501","#00FFFF","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8","#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#696969")
                               bdr = random.choice(bdr1)
                               warna1 = ("https://i.ibb.co/KzB0gBJ/1563145660726.jpg","https://i.ibb.co/NVSwn8g/1563144843308.jpg","https://i.ibb.co/8DRsgf6/1563145116258.jpg","https://i.ibb.co/jDY5p8B/1563144879473.jpg","https://i.ibb.co/2WQdfk2/1563144893323.jpg","https://i.ibb.co/Nt7PKxG/1563144845106.jpg","https://i.ibb.co/Nt7PKxG/1563144845106.jpg","https://i.ibb.co/dDMGSCT/1563144886821.jpg","https://i.ibb.co/Vp6ydMY/1563144805434.jpg")
                               warnanya1 = random.choice(warna1)
                               Bagbday = wait["BAGBDAY"]
                               to = msg.to
                               dataa = {
                            "type": "flex",
                            "altText": "HAPPY BIRTHDAY",
                            "contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "kilo",
"body": {
"type": "box",
"cornerRadius": "10px",
"layout": "horizontal",
"contents": [
{
"type": "image",
"url": warnanya1,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "16:13",
"offsetTop": "0px"
},
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bagbday,
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "16:13",
"offsetTop": "0px",
"offsetStart": "0px"
}],
"position": "absolute",
"borderWidth": "2px",  #BORDER
"borderColor": bdr,
"cornerRadius": "10px",
"offsetTop": "6px",
"offsetStart": "5px",
"height": "200px",
"width": "250px"
},
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(key1).pictureStatus),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"offsetStart": "0px"
}],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "22px",
"offsetStart": "85px",
"height": "195px",
"width": "90px"
},
#=================
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://tinyurl.com/yb6eoyw8", #HAPPY BIRTHDAY
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px"
}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "110px",
"offsetStart": "170px",
"height": "100px",
"width": "100px"
},  #=======
#=================
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                               cl.postTemplate(to, dataa)
                            
                        elif ("Mylove " in msg.text): 
                          if wait["mylove"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               bdr1 = ("#00CCFF","#1AE501","#00FFFF","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8","#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#696969")
                               bdr = random.choice(bdr1)
                               warna1 = ("https://i.ibb.co/KzB0gBJ/1563145660726.jpg","https://i.ibb.co/NVSwn8g/1563144843308.jpg","https://i.ibb.co/8DRsgf6/1563145116258.jpg","https://i.ibb.co/jDY5p8B/1563144879473.jpg","https://i.ibb.co/2WQdfk2/1563144893323.jpg","https://i.ibb.co/Nt7PKxG/1563144845106.jpg","https://i.ibb.co/Nt7PKxG/1563144845106.jpg","https://i.ibb.co/dDMGSCT/1563144886821.jpg","https://i.ibb.co/Vp6ydMY/1563144805434.jpg")
                               warnanya1 = random.choice(warna1)
                               to = msg.to
                               dataa = {
                            "type": "flex",
                            "altText": "MY LOVE",
                            "contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "kilo",
"body": {
"type": "box",
"cornerRadius": "10px",
"layout": "horizontal",
"contents": [
{
"type": "image",
"url": warnanya1,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "16:13",
"offsetTop": "0px"
},
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(key1).pictureStatus),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"offsetStart": "0px"
}],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "35px",
"offsetStart": "130px",
"height": "154px",
"width": "100px"
},
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"offsetStart": "0px"
}],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "35px",
"offsetStart": "30px",
"height": "153px",
"width": "100px"
},
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://tinyurl.com/yb2m9mux",   #pass
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "16:13",
"offsetTop": "0px",
"offsetStart": "0px"
}],
"position": "absolute",
"borderWidth": "2px",  #BORDER
"borderColor": bdr,
"cornerRadius": "10px",
"offsetTop": "6px",
"offsetStart": "5px",
"height": "200px",
"width": "250px"
},
#=================
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://tinyurl.com/yb6eoyw8", #minnimouse mouse
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "1:1",
"offsetTop": "0px"
}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "120px",
"offsetStart": "170px",
"height": "100px",
"width": "100px"
},  #=======
#=================
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                               cl.postTemplate(to, dataa)


                        elif cmd.startswith("unsend "): #x
                          if msg._from in admin:
                                args = removeCmd("uns", text)
                                mes = 0
                                try:
                                   mes = int(args[1])
                                except:
                                    mes = 1
                                M = cl.getRecentMessagesV2(to, 101)
                                MId = []
                                for ind,i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == cl.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                                break
                                def unsMes(id):
                                    cl.unsendMessage(id)
                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.start()
                                    thread1.join()
                                cl.unsendMessage(msg_id)


                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           dragonkiller(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           dragonkiller(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           dragonkiller(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif cmd == "tagpm":
                          if msg._from in admin:
                            profile = cl.getContact(msg.to)
                            sendMentionV2(msg.to, msg.to,"Halo ",wait["cekpc"])

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           dragonkiller(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                dragonkiller(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                dragonkiller(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                dragonkiller(msg.to,"『❎ᴅᴋ ᴋɪɴɢ ʙᴏᴛ❎』Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                dragonkiller(msg.to,"『❎ᴅᴋ ᴋɪɴɢ ʙᴏᴛ❎』Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    dragonkiller(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        dragonkiller(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              dragonkiller(msg.to,"Sukses membersihkan " +mc)

                        elif cmd == "link id" or text.lower() == 'link id':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              cl.sendMessage(msg.to,"http://line.me/ti/p/~dkdkbot")

#==================================================
 
                        elif cmd.startswith("getidline "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    checkticket = cl.getContact(ls)
                                    cl.sendMention(to, "@!: {}".format(checkticket), [ls])
                        elif cmd.startswith("groupvideocall "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            num = int(txt)
                            cl.sendMessage(to, "Berhasil Invite Ke Dalam VideoCall Group :)")
                            for anu in range(0,num):
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.inviteIntoGroupVideoCall(to, contactIds=members)
#======================= Akhir Fungsi =========================

                        elif 'Like ' in text.lower():
                            try:
                                typel = [1001,1002,1003,1004,1005,1006]
                                key = eval(msg.contentMetadata["MENTION"])
                                u = key["MENTIONEES"][0]["M"]
                                a = cl.getContact(u).mid
                                s = cl.getContact(u).displayName
                                hasil = channel.getHomeProfile(mid=a)
                                st = hasil['result']['feeds']
                                for i in range(len(st)):
                                    test = st[i]
                                    result = test['post']['postInfo']['postId']
                                    channel.like(str(sender), str(result), likeType=random.choice(typel))
                                    channel.comment(str(sender), str(result), 'Auto Like by LIBERATION\n http://line.me/ti/p/KTS6MCiOZe')
                                sendTextTemplate3(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                            except Exception as e:
                                cl.sendMessage(receiver, str(e))
                        elif text == "kojom":
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.acquireGroupCallRoute(to)
                                cl.inviteIntoGroupCall(to, contactIds=members)
                                dragonkiller(to, "Done invite group call") 
#===================== Fungsi Broadcast =======================
#============================ADD STICKER TEMPLATE====================================â‰ 


#=========== [ Add Image ] ============#
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                sendTextTemplate1(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                sendTextTemplate1(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimg":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             dkbots2(to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addmp4 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Silahkan kirim videonya...") 
                            else:
                                sendTextTemplate1(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp4 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                sendTextTemplate1(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listmp4":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             dkbots2(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addsuara "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                sendTextTemplate1(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsuara "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                sendTextTemplate1(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listsuara":
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             dkbots2(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                sendTextTemplate1(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendTextTemplate1(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                dkbots2(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             dkbots2(to, ret_)
#===========MEDIA============#
                        elif cmd.startswith("topnews"):
                              if msg._from in admin:
                                  dpk=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=dpk.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  cl.sendMessage( to, str(hasil))
                                  cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith(".bokep "):
                           if msg._from in admin:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.xvideos.com/?k={}".format(str(search)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    data = soup.findAll('div', attrs={'class':'thumb'})
                                    if len(cond) == 1:
                                        num = 0
                                        ret_ = "Result xvideos"
                                        for a in data:
                                            num += 1
                                            link = "https://www.xvideos.com"+a.find('a')['href']
                                            ret_ += "\n {}. {}".format(str(num), str(link))
                                        ret_ += "\n Total {} Video".format(str(len(data)))
                                        cl.sendMessage(to, str(ret_))
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data):
                                            a = data[num - 1]
                                            with requests.session() as s:
                                                s.headers['user-agent'] = 'Mozilla/5.0'
                                                r = s.get("https://www.tubeoffline.com/downloadFrom.php?host=Xvideos&video=https://www.xvideos.com{}".format(str(a.find('a')['href'])))
                                                soup = BeautifulSoup(r.content, 'html5lib')
                                                pict = soup.select("img[src*=img]")[0]
                                                img = pict['src']
                                                data = soup.findAll('div', attrs={'id':'videoDownload'})
                                                print(a)
                                                for b in data:
                                                    down = b.select("a[href*=vid]")[0]
                                                    load = down['href']
                                                    with requests.session() as web:
                                                        web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                        r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(str(load)))
                                                        data = r.text
                                                        data = json.loads(data)
                                                        ret_ = "Link Download\n"+data["data"]["url"]
                                                    cl.sendImageWithURL(to, img)
                                                    cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    cl.sendMessage(msg.to,ret_)

                        elif cmd.startswith("okep"):
                          if msg._from in admin:
                            try:
                                x = text.split(" ")
                                y = text.replace(x[0] + " ","")
                                r = requests.get("https://mnazria.herokuapp.com/api/porn?search={}"+y)
                                data = r.text
                                data = json.loads(data)
                                for bokep in data["result"]:
                                    ret_ = "╭───〔 DETAIL PORN VIDEOS 〕"
                                    ret_ += "\n├ Actor : {}".format(str(bokep["actors"]))
                                    ret_ += "\n├ Duration : {}".format(str(bokep["duration"]))
                                    ret_ += "\n├ Title : {}".format(str(bokep["title"]))
                                    ret_ += "\n├ Link : {}".format(str(bokep["url"]))
                                    ret_ += "\n╰───〔 SELAMAT MENONTON 〕"
                                    cl.sendReplyMessage(msg.id,to, ret_)
                                    cl.sendVideoWithURL(to, str(bokep["url"]))
                                    break
                            except Exception as error:
                        	    cl.sendMessage(msg.id, to, str(error))


                        elif cmd.startswith(".joox"):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            r = requests.get("https://mnazria.herokuapp.com/api/jooxnich?search={}".format(str(urllib.parse.quote(urutan))))
                            data = r.text
                            data = json.loads(data)
                            Hasilnya = data
                            A = str(Hasilnya["result"]["msong"])
                            B = str(Hasilnya["result"]["msinger"])
                            C = str(Hasilnya["result"]["album_url"])
                            D = str(Hasilnya["result"]["mp3Url"])
                            warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                            warnanya1 = random.choice(warna1)
                            data = {
                                       "type": "flex",
                                       "altText": "music joox",
                                       "contents": {
"type":"bubble",
"size":"micro",
"body":{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": C,
"size":"full",
"aspectRatio":"1:1",
"aspectMode":"cover"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"filler"
}
],
"position":"absolute",
"paddingAll":"10px",
"width":"300px",
"height":"150px",
"backgroundColor":"#00000abc"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url":"https://imgur.com/M4ArvLT.png",
"size":"full",
"aspectRatio":"2:1",
"aspectMode":"fit"
}
],
"paddingAll":"0px",
"position":"absolute",
"width":"300px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": C,
"size":"xl",
"aspectRatio":"1:1",
"aspectMode":"cover"
}
],
"position":"absolute",
"cornerRadius":"100px",
"offsetTop":"4.9px",
"offsetStart":"5.4px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url":"https://i.ibb.co/WBsn5pN/20200105-143351.png",
"size":"xxs",
"action":{
"type":"uri",
"label":"action",
"uri":"http://line.me/ti/p/~ownerdk"}
}
],
"position":"absolute",
"offsetBottom":"1px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": A,
"weight":"bold",
"color":"#ffffff",
"size":"xs",
"align":"center"
}
],
"position":"absolute",
"offsetTop":"100px",
"offsetStart":"20px",
"width":"117.5px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": B,
"color":"#ffffff",
"size":"xxs",
"align":"center"
}
],
"position":"absolute",
"offsetTop":"120px",
"offsetStart":"20px",
"width":"117.5px"
}
],
"paddingAll":"0px"
},
"styles":{
"body":{
"backgroundColor":"#000000"
}
}
}
}
                            cl.postTemplate(to, data)
                            cl.sendAudioWithURL(to,D)

                        elif cmd.startswith("joox"):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            r = requests.get("https://mnazria.herokuapp.com/api/jooxnich?search={}".format(str(urllib.parse.quote(urutan))))
                            data = r.text
                            data = json.loads(data)
                            Hasilnya = data
                            A = str(Hasilnya["result"]["msong"])
                            B = str(Hasilnya["result"]["msinger"])
                            C = str(Hasilnya["result"]["album_url"])
                            D = str(Hasilnya["result"]["mp3Url"])
                            E = str(Hasilnya["result"]["public_time"])
                            Bag = ("https://i.ibb.co/KzB0gBJ/1563145660726.jpg","https://i.ibb.co/NVSwn8g/1563144843308.jpg","https://i.ibb.co/8DRsgf6/1563145116258.jpg","https://i.ibb.co/jDY5p8B/1563144879473.jpg","https://i.ibb.co/2WQdfk2/1563144893323.jpg","https://i.ibb.co/Nt7PKxG/1563144845106.jpg","https://i.ibb.co/Nt7PKxG/1563144845106.jpg","https://i.ibb.co/dDMGSCT/1563144886821.jpg","https://i.ibb.co/Vp6ydMY/1563144805434.jpg")
                            Bagnya = random.choice(Bag)
                            warna1 = ("#FFFFFF","#1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8","#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#696969")
                            warnanya1 = random.choice(warna1)
                            warna2 = ("#FF7F00","#9C8E7Ecc","#000000")
                            warnanya2 = random.choice(warna2)
                            data = {
                    "type": "flex",
                    "altText": "music joox",
                    "contents": {
  "type": "carousel",
"contents": [
{
"type": "bubble",
#"size": "micro",
"body": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "image",
"url": Bagnya, # BORDER BELAKANG
"aspectRatio": "10:4.5",
"size": "full",
"gravity": "top",
"aspectMode": "cover",
"offsetTop": "0px"
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "image",
"url": C, # BELAKANG
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "15px",
"offsetTop": "3px",
"offsetBottom": "3px",
"offsetStart": "4px",
"offsetEnd": "4px",
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": Bagnya,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "36px",
"offsetStart": "40px",
"height": "41px",
"width": "200px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ # ijo
{
"type": "image",
"url": Bagnya,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "2px",
"offsetTop": "79px",
"offsetStart": "3px",
"height": "3px",
"width": "294px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #separator putih
{
"type": "image",
"url": Bagnya,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "85px",
"offsetStart": "10px",
"height": "40px",
"width": "187px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #cyber biru
{
"type": "image",
"url": C,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "8px",
"offsetTop": "86px",
"offsetStart": "11px",
"height": "38px",
"width": "185px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh
{
"type": "image",
"url": "https://i.ibb.co/PhZ1xpW/20200106-023226.png", 
"size": "full",
"action": {
"type": "uri",
"uri": "line://calls"
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "87px",
"offsetStart": "11px",
"height": "41px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh 1
{
"type": "image",
"url": "https://i.ibb.co/my0Fy50/20200106-035052.png", 
"size": "full",
"action": {
"type": "uri",
"uri": "line://nv/chat", #chat
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "87px",
"offsetStart": "41px",
"height": "41px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh 2
{
"type": "image",
"url": "https://i.ibb.co/br2cvZr/20200105-123916.png", 
"size": "full",
"action": {
"type": "uri",
"uri": "line://nv/camera/" #camera
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "87px",
"offsetStart": "71px",
"height": "41px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh 3
{
"type": "image",
"url": "https://i.ibb.co/Xtvc389/20200106-034016.png",
"size": "full",
"action": {
"type": "uri",
"uri": "https://youtube.com" #yutube
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "87px",
"offsetStart": "101px",
"height": "41px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh 4
{
"type": "image",
"url": "https://i.ibb.co/1brw3Hk/20200106-032155.png",
"size": "full",
"action": {
"type": "uri",
"uri": "line://nv/cameraRoll/multi"
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "87px",
"offsetStart": "131px",
"height": "41px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #weh 5
{
"type": "image",
"url": "https://i.ibb.co/WBsn5pN/20200105-143351.png",
"size": "full",
"action": {
"type": "uri",
"uri": "https://joox.com" #joox
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "87px",
"offsetStart": "161px",
"height": "41px",
"width": "35px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #list 1
{
"type": "image",
"url": Bagnya,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "18px",
"offsetStart": "68px",
"height": "3px",
"width": "228px"
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "Public Time",
"wrap": True,
"align": "center",
"color": "#ffffff",
"size": "xxs",
"weight": "bold",
"offsetTop": "-1.5px"
}
],
"position": "absolute",
"cornerRadius": "2px",
"borderWidth": "1.1px",
"borderColor": warnanya1,
"offsetTop": "88px",
"backgroundColor": warnanya2,
"offsetStart": "203px",
"height": "16px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": E,
"wrap": True,
"align": "center",
"color": "#ffffff",
"size": "xxs",
"weight": "bold",
"offsetTop": "-1.5px"
}
],
"position": "absolute",
"cornerRadius": "2px",
"borderWidth": "1.1px",
"borderColor": warnanya1,
"offsetTop": "107px",
"backgroundColor": warnanya2,
"offsetStart": "203px",
"height": "16px",
"width": "75px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "MUSIC JOOX", #+ datetime.strftime(timeNow,'%Y-%m-%d'),
"wrap": True,
"align": "center",
"color": "#ffffff",
"size": "xl",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"offsetTop": "-6px",
#"backgroundColor": "#ffff33",
"offsetStart": "60px",
"height": "25px",
"width": "150px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🎶🎶🎶🎶🎶", #+ datetime.strftime(timeNow,'%Y-%m-%d'),
"wrap": True,
"align": "center",
"color": "#ccffff",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"offsetTop": "3px",
#"backgroundColor": "#ffff33",
"offsetStart": "201px",
"height": "15px",
"width": "90px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #4 bunderan
{
"type": "image",
"url": Bagnya,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "60px",
"offsetTop": "8px",
"offsetStart": "7px",
"height": "70px",
"width": "70px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #warna putih
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4hwddT5GVQ1PYEzpQspS5yRKhGgd9LRsMKme8RWz9KW3k0rIu--X4tw4&s=10",
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "39px",
"offsetStart": "38px",
"height": "35px",
"width": "200px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": C,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "5px",
"offsetTop": "40px",
"offsetStart": "37px",
"height": "33px",
"width": "200px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": C,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "60px",
"offsetTop": "11px",
"offsetStart": "10px",
"height": "63px",
"width": "63px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image", #baru edit
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4hwddT5GVQ1PYEzpQspS5yRKhGgd9LRsMKme8RWz9KW3k0rIu--X4tw4&s=10",
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "60px",
"offsetTop": "13px",
"offsetStart": "12px",
"height": "59px",
"width": "59px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": C,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:4",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "60px",
"offsetTop": "13px",
"offsetStart": "12px",
"height": "59px",
"width": "59px"
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": A,
"wrap": True,
#"align": "center",
"color": "#ffffff",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"offsetTop": "20px",
#"backgroundColor": "#3333FF",
"offsetStart": "80px",
"height": "15px",
"width": "155px"
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "ᴄʀᴇᴀᴛᴏʀ",
"wrap": True,
#"align": "center",
"color": "#ffffff",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"offsetTop": "20px",
#"backgroundColor": "#3333FF",jam
"offsetStart": "239px",
"height": "15px",
"width": "70px"
},
{
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": B,
"wrap": True,
#"align": "center",
"color": "#ffffff",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"offsetTop": "45px",
#"backgroundColor": "#3333FF",
"offsetStart": "80px",
"height": "30px",
"width": "160px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": C,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "38px",
"offsetStart": "242px",
"height": "38px",
"width": "38px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": C,
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "3px",
"offsetTop": "39px",
"offsetStart": "243px",
"height": "36px",
"width": "36px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://i.imgur.com/zDaYaaW.jpg",
"gravity": "top",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "3:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c",
"type": "uri",
}
}
],
"position": "absolute",
"cornerRadius": "100px",
"offsetTop": "39px",
"offsetStart": "243px",
"height": "36px",
"width": "36px"
}
],
"paddingAll": "0px"
}
},
]
}
}
                            cl.postTemplate(msg.to, data)
                            cl.sendAudioWithURL(to,D)
                        elif cmd.startswith("/vid"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                apiKey = "rangga09"
                                headers = {"apiKey": "rangga09"}
                                r = requests.get("https://beapi.me/ytmp4?search="+urutan,headers=headers)
                                data = r.text
                                data = json.loads(data)
                                data = {
                                           "type": "video",
                                           "originalContentUrl": data["result"]["url"],
                                           "previewImageUrl": "https://media.tenor.com/images/8d6be8856763b9e75c561c6ee9bb716e/tenor.gif",
                                      }
                                cl.postTemplate(to, data)
                                cl.sendVideoWithURL(to, str(data["result"]["url"]))
                            except Exception as error:
                                cl.sendMessage(msg.id, to, str(error))

                        elif cmd.startswith("lyrics "):
                          if msg._from in admin:
                            anu = removeCmd("lyrics", text)
                            slyric(to, text)


                        elif cmd.startswith("/audiocal "):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                apiKey = "primaz02"
                                headers = {"apiKey": "primaz02"}
                                r = requests.get("https://beapi.me/joox?search="+urutan,headers=headers)
                                data = r.text
                                data = json.loads(data)
                                i = data
                                k = str(i["result"][0]["mp3Url"])
                                a = str(i["result"][0]["title"])
                                b = str(i["result"][0]["artist"])
                                c = str(i["result"][0]["album_url"])
                                warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                                warnanya1 = random.choice(warna1)
                                data = {
                                       "type": "flex",
                                       "altText": "music joox",
                                       "contents": {
"type":"bubble",
"body":{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": c,
"size":"full",
"aspectRatio":"2:1",
"aspectMode":"cover"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"filler"
}
],
"position":"absolute",
"paddingAll":"10px",
"width":"300px",
"height":"150px",
"backgroundColor":"#00000abc"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url":"https://imgur.com/M4ArvLT.png",
"size":"full",
"aspectRatio":"2:1",
"aspectMode":"fit"
}
],
"paddingAll":"0px",
"position":"absolute",
"width":"300px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": c,
"size":"xl",
"aspectRatio":"1:1",
"aspectMode":"cover"
}
],
"position":"absolute",
"cornerRadius":"100px",
"offsetTop":"4.9px",
"offsetStart":"5.4px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url":"https://i.ibb.co/WBsn5pN/20200105-143351.png",
"size":"xxs",
"action":{
"type":"uri",
"label":"action",
"uri":"http://line.me/ti/p/~ownerdk"}
}
],
"position":"absolute",
"offsetBottom":"1px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text":b,
"weight":"bold",
"color":"#ffffff",
"size":"xs",
"align":"center"
}
],
"position":"absolute",
"offsetTop":"58px",
"offsetStart":"166px",
"width":"117.5px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": a,
"color":"#ffffff",
"size":"xxs",
"align":"center"
}
],
"position":"absolute",
"offsetTop":"80px",
"offsetStart":"166px",
"width":"117.5px"
}
],
"paddingAll":"0px"
},
"styles":{
"body":{
"backgroundColor":"#000000"
}
}
}
}
                                cl.postTemplate(to, data)
                                cl.sendAudioWithURL(to,k)
                            except Exception as error:
                                cl.sendMessage(to, "error\n" + str(error))
                                print (error)

                        elif cmd.startswith("/musikal "):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                apiKey = "primaz03"
                                headers = {"apiKey": "primaz03"}
                                r = requests.get("https://beapi.me/joox?search="+urutan,headers=headers)
                                data = r.text
                                data = json.loads(data)
                                i = data
                                k = str(i["result"][0]["mp3Url"])
                                a = str(i["result"][0]["title"])
                                b = str(i["result"][0]["artist"])
                                c = str(i["result"][0]["album_url"])
                                warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                                warnanya1 = random.choice(warna1)
                                data = {
"type": "flex",
"altText": "musik joox",
"contents": {
"type": "carousel",
"contents": [{
"styles": {
"body": {
"backgroundColor": "#9C8E7Ecc"
}},
"type": "bubble",
"size":"micro",
"body": {
"borderWidth": "2.5px",
"cornerRadius": "10px",
"backgroundColor": "#FF7F00",
"borderColor": warnanya1,"type": "box","layout": "vertical",
"contents": [{
"contents": [{
"contents": [{
"contents": [{
"contents": [{
"url": "https://i.ibb.co/wYyzywp/20200215-141809.png",
"type": "image",
"aspectMode": "cover",
"gravity": "top",
"aspectRatio": "2:2",
"size": "xxs",
"action": {
"type": "uri",
"uri": "line://nv/profilePopup/mid=u52196f2a728d7ece0d7ed1f1270ab77c",
}},{
"type": "separator",
"color": warnanya1,
},{
"type": "separator",
"color": warnanya1,
},{
"contents": [{
"type": "text",
"text": "ᴍᴜsɪᴋ ʜɪʙᴜʀᴀɴ",
"weight": "bold",
"color": "#ffffff",
"offsetTop": "-1.3px",
"align": "center",
"size": "xxs",
}],
"borderWidth": "1px",
"cornerRadius": "10px",
"borderColor": warnanya1,
"backgroundColor": "#2f2f4f",
"height": "17px",
"offsetTop": "1.1px",
"type": "box",
"layout": "vertical",
"flex": 5
},{
"type": "separator",
"color": warnanya1,
},{
"type": "separator",
"color": warnanya1,
},{
"url": "https://i.ibb.co/wYyzywp/20200215-141809.png",
"type": "image",
"aspectMode": "cover",
"gravity": "top",
"aspectRatio": "2:2",
"size": "xxs",
"action": {
"type": "uri",
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c"
}}],
"type": "box",
"layout": "horizontal"
}],
"type": "box",
"layout": "vertical",
"flex": 3,
}],
"type": "box",
"layout": "horizontal"
}],
"borderWidth": "1.5px",
"borderColor": warnanya1,
"cornerRadius": "0px",
"backgroundColor": "#00FF00",
"type": "box",
"layout": "vertical"
},{
"contents": [{
"contents": [{
"contents": [{
"type": "image",
"url": c,
"size": "full",
"aspectRatio": "1:1.3",
"aspectMode": "cover",
"gravity": "top",
"action": {
"type": "uri",
"uri": "line://nv/profilePopup/mid=uc064aa14c3318017de4624b779e1420c"
}}],
"borderWidth": "1.5px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"offsetTop": "2px",
"offsetStart": "3px",
"height": "117.5px",
#"backgroundColor": "#0000ff",
"width": "96px",
"type": "box",
"layout": "vertical",
"flex": 3,
},{
"contents": [{
"type": "image",
"url": "https://i.ibb.co/kSMSnWn/20190427-191235.png",
"size": "xxs",
"offsetTop": "1px",
"action": {
"type": "uri",
"uri": "line://nv/camera/", #calls
}},{
"type": "image",
"url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
"size": "xxs",
"offsetTop": "3px",
"action": {
"type": "uri",
"uri": "https://youtube.com", #Galeri
}},{
"type": "image",
"url": "https://i.ibb.co/7YVnNPF/20190625-190410.png",
"size": "xxs",
"offsetTop": "5px",
"action": {
"type": "uri",
"uri": "https://joox.com",
}},{
"type": "image",
"url": "https://i.ibb.co/Xtvc389/20200106-034016.png",
"size": "xxs",
"offsetTop": "7px",
"action": {
"type": "uri",
"uri": "https://youtube.com", #yutube
}}],
"borderWidth": "1.5px",
"borderColor": warnanya1,
"cornerRadius": "5px",
"offsetTop": "2px",
"offsetStart": "4px",
"height": "117.5px",
"width": "30px",
"backgroundColor": "#FF7F00",
"type": "box",
"layout": "vertical",
"flex": 1,
}],
"backgroundColor": "#00FF00", #008000",
"offsetTop": "0px",
"height": "123px",
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": warnanya1,
},{
"contents": [{
"contents": [{
"text": a,
"size": "xxs",
"offsetTop": "-1.5px",
"align": "center",
"color": "#ffffff",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
#"offsetTop": "2px",
"borderWidth": "1.3px",
"borderColor": warnanya1,
"backgroundColor": "#FF7F00",
"layout": "vertical"
}],
"borderWidth": "7.5px",
"borderColor": warnanya1,
"type": "box",
"layout": "horizontal"
}],
"height": "156.5px", #"198px",
"borderWidth": "1.5px",
"borderColor": warnanya1,
"type": "box",
"layout": "vertical"
},{
"contents": [{
"contents": [{
"contents": [{
"contents": [{
"url": "https://i.ibb.co/wYyzywp/20200215-141809.png",
"type": "image",
"action": {
"type": "uri",
"uri": "https://wa.me/6281314992717",
}},{"type": "separator",
"color": warnanya1,
},{
"type": "separator",
"color": warnanya1,
},{
"contents": [{
"type": "text",
"text": b,
"weight": "bold",
"color": "#ffffff",
"offsetTop": "-1.5px",
"align": "center",
"size": "xxs",
}],
"borderWidth": "1.5px",
"cornerRadius": "10px",
"borderColor": warnanya1,
"backgroundColor": "#00FF00",
"height": "17px",
"offsetTop": "1.1px",
"type": "box",
"layout": "vertical",
"flex": 5
},{
"type": "separator",
"color": warnanya1,
},{
"type": "separator",
"color": warnanya1,
},{
"url": "https://i.ibb.co/wYyzywp/20200215-141809.png",
"type": "image",
"action": {
"type": "uri",
"uri": "https://wa.me/6283899850723",
}}],
"type": "box",
"layout": "horizontal"
}],
"type": "box",
"layout": "vertical",
"flex": 3,
}],
"type": "box",
"layout": "horizontal"
}],
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "0px",
"backgroundColor": "#00FF00",
"type": "box",
"layout": "vertical"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},
"styles": {
"footer": {
"separator": True
}
}
}
]
}
}
                                cl.postTemplate(to, data)
                                cl.sendAudioWithURL(to,k)
                            except Exception as error:
                                cl.sendMessage(to, "error\n" + str(error))
                                print (error)



#=======================#
                        elif cmd.startswith("bio: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               separate = msg.text.split(" ")
                               string = msg.text.replace(separate[0] + " ","")
                               profile_G = cl.getProfile()
                               profile_G.statusMessage = string
                               cl.updateProfile(profile_G)
                               sendTextTemplate0(msg.to, "sucses.\nbio : {}".format(str(string)))


                        elif cmd == "/mek" or text.lower() == 'mek':
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                tanggal =" "+ datetime.strftime(timeNow,'%d-%m-%Y')
                                warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                                warnanya1 = random.choice(warna1)
                                data = {
"type":"flex",
"altText":"𝓂𝓎 𝓅𝓇ℴ𝒻𝒾𝓁ℯ",
"contents":{
"type":"carousel",
"contents":[
{
"type":"bubble",
"size":"kilo",
"body":{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://i.ibb.co/Yk8Y2HX/FB-IMG-16203046991251260.jpg",
"size":"full",
"animated":True,
"aspectMode":"cover",
"aspectRatio":"16:9",
"gravity":"top"
},
# =========================================
#======================
#    USER DISPLAYNAME   #
#======================
{
"type": "box",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "{}".format(cl.getContact(sender).displayName),
"color": "#ffffff",
#"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px",
"style": "italic",
"decoration": "underline"
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "83px", #ATAS BAWAH
"offsetStart": "120px", #GESER SAMPING
"height": "17px",
"width": "110px"
},
{
"type": "box",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "{} ".format(status.statusMessage),
"color": "#00FF00",
 #"align": "center",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "107px", #ATAS BAWAH
"offsetStart": "112px", #GESER SAMPING
"height": "17px",
"width": "110px"
},
#====================
{
"type": "box",
"layout": "horizontal",
"contents": [ #dsini
{
"type": "image", 
"url": cover,
"size": "full",
"animated":True,
"aspectMode": "cover",
"size": "full",
"gravity": "top",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "200px",
"width": "26px",
"height": "26px",
"offsetTop": "111px", #ATAS BAWAH
"offsetStart": "78px", #KIRI KANAN
},
# ===========PROFILE

{
"type": "box",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [ #dsini
{
"type": "image", 
"url": "https://i.ibb.co/09wr5fy/ezgif-com-gif-maker-4.png",
"size": "full",
"animated":True,
"aspectMode": "cover",
"size": "full",
"gravity": "top",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "200px",
"width": "90px",
"height": "75px",
"offsetTop": "25px", #ATAS BAWAH
"offsetStart": "47px", #KIRI KANAN
},


{
"type": "box",
"borderColor": warnanya1,
"layout": "horizontal",
"contents": [ #dsini
{
"type": "image", 
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
"size": "full",
"aspectMode": "cover",
"size": "full",
"animated":True,
"gravity": "top",
"action": {
"type": "uri",
"uri": "line://nv/timeline",
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "200px",
"width": "55px",
"height": "55px",
"offsetTop": "36px", #ATAS BAWAH
"offsetStart": "64px", #KIRI KANAN
},
{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://i.ibb.co/p3cB9yD/ezgif-com-gif-maker-1.png","animated":True,"size":"full"}],
"position":"absolute","width":"180px","offsetTop":"0px","offsetStart":"0px"},
],
"paddingAll":"0px",
"borderWidth":"0px",
"cornerRadius":"5px"
}
}
]
}
}
                                cl.postTemplate(to, data)



                        elif ".smuleaudio " in msg.text.lower():
                          if msg._from in admin:
                            try:
                                apiKey = BEAPI('primaz03')
                                result = apiKey.smulePost("https://www.smule.com/c/1232746914_3991127254")
                                search = (msg.text).replace('.smuleaudio ', "").strip()
                                kr_ = "Judul: "+str(result["result"]['performance']["title"])
                                kr_ += "\nPembuat: "+str(result["result"]['performance']["performed_by_url"])
                                kr_ += "\nPesan: "+str(result["result"]['performance']["message"])
                                hasil = "record\n"+str(kr_)
                                cl.sendImageWithURL(to, result['result']['performance']['cover_url'])
                                warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                                warnanya1 = random.choice(warna1)
                                data = {
"type":"flex",
"altText":"sᴍᴜʟᴇ ʀᴇᴄᴏʀᴅ",
"contents":{
"type":"carousel",
"contents":[
{
"type":"bubble",
"size":"kilo",
"body":
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",  #background#
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlVx_K8OyTsUHvh8WJu5UF-LlLVDYRMWT8I3If6n_pBA5HSgvc&usqp=CAU",
"size":"full",
"aspectMode":"cover",
"aspectRatio":"16:9",
"gravity":"top"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image", #icon smule#
#"url": dl,
"url":"https://i.ibb.co/CntKh4x/20190525-152240.png"
}
],
"width":"55px",
"height":"55px"
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text":"ＳＭＵＬＥ ＲＥＣＯＲＤ",
"color":warnanya1,
"size":"sm",
"align":"center"
}
]
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": "%s" % result["result"]['performance']["title"],
"size":"xxs",
"align":"center",
"wrap":True,
"color":warnanya1,
}
],
"offsetTop":"5px"
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image", # icon SMULE#
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTO5PgKwZSPZcKZLM4fkRMpahjSuMeEH3g2XuFPgtPa72ftCLan&usqp=CAU",
}
],
"width":"35px",
"height":"35px"
}
]
}
]
}
]
}
],
"position":"absolute",
"cornerRadius":"5px",
"offsetTop":"5px",
"width":"245px",
"offsetStart":"5px",
"borderWidth":"1px",
"borderColor":warnanya1,
},
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": "%s" % result["result"]['performance']["performed_by_url"],
"size":"xxs",
"color":warnanya1,
"wrap":True,
"offsetStart":"3px"
}
]
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": "🎶𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗖🎶\n{}".format(result["result"]['performance']["message"]),
"size":"xxs",
"color":warnanya1,
"wrap":True,
"offsetStart":"3px"
}
]
}
],
"position":"absolute",
"borderWidth":"1px",
"borderColor":warnanya1,
"offsetTop":"65px", #ATAS BAWAH
"width":"245px",
"offsetStart":"5px", #GESER SAMPING
"height":"75px",
"cornerRadius":"5px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"size":"full",
"aspectMode":"cover"
}
],
"width":"40px",
"height":"40px"
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text":"ＳＥＮＤＥＲ",
"align":"center",
"size":"sm",
"color":warnanya1,
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"text",
"text": "{}".format(cl.getContact(sender).displayName),
"align":"center",
"size":"sm",
"color":warnanya1,
"offsetTop":"5px"
}
]
}
]
}
],
"position":"absolute",
"width":"245px",
"offsetTop":"320px", #ATAS BAWAH
"borderWidth":"1px",
"borderColor":warnanya1,
"offsetStart":"5px", #GESER SAMPING
"cornerRadius":"5px"
}
],
"paddingAll":"0px",
"borderWidth":"2px",
"borderColor":warnanya1,
"cornerRadius":"10px"
}
}
]
}
}
                                cl.postTemplate(to, data)
                                cl.sendAudioWithURL(msg.to, result['result']['performance']['media_url'])
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif ".smulevideo " in msg.text.lower():
                          if msg._from in admin:
                            try:
                                apiKey = "primaz03"
                                headers = {"apiKey": apiKey}
                                search = (msg.text).replace('.smulevideo ', "").strip()
                                result = json.loads(requests.get("https://beapi.me/smule/post?url="+search,headers=headers).text)
                                kr_ = "Judul: "+str(result["result"]['performance']["title"])
                                kr_ += "\nPembuat: "+str(result["result"]['performance']["performed_by_url"])
                                kr_ += "\nPesan: "+str(result["result"]['performance']["message"])
                                hasil = "record\n"+str(kr_)
                                cl.sendImageWithURL(to, result['result']['performance']['cover_url'])
                                #dl = result["result"]['performance']["image_link"]
                                warna1 = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#FF0000","#006400","#00FFFF","#800000","#BC8F8F","#800080","#FFFF00","#8B0000","#FF1493","#FF00FF","#00FF00")
                                warnanya1 = random.choice(warna1)
                                data = {
"type":"flex",
"altText":"sᴍᴜʟᴇ ʀᴇᴄᴏʀᴅ",
"contents":{
"type":"carousel",
"contents":[
{
"type":"bubble",
"size":"kilo",
"body":
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",  #background#
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlVx_K8OyTsUHvh8WJu5UF-LlLVDYRMWT8I3If6n_pBA5HSgvc&usqp=CAU",
"size":"full",
"aspectMode":"cover",
"aspectRatio":"16:9",
"gravity":"top"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image", #icon smule#
#"url": dl,
"url":"https://i.ibb.co/CntKh4x/20190525-152240.png"
}
],
"width":"55px",
"height":"55px"
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text":"ＳＭＵＬＥ ＲＥＣＯＲＤ",
"color":warnanya1,
"size":"sm",
"align":"center"
}
]
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": "%s" % result["result"]['performance']["title"],
"size":"xxs",
"align":"center",
"wrap":True,
"color":warnanya1,
}
],
"offsetTop":"5px"
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image", # icon SMULE#
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTO5PgKwZSPZcKZLM4fkRMpahjSuMeEH3g2XuFPgtPa72ftCLan&usqp=CAU",
}
],
"width":"35px",
"height":"35px"
}
]
}
]
}
]
}
],
"position":"absolute",
"cornerRadius":"5px",
"offsetTop":"5px",
"width":"245px",
"offsetStart":"5px",
"borderWidth":"1px",
"borderColor":warnanya1,
},
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": "%s" % result["result"]['performance']["performed_by_url"],
"size":"xxs",
"color":warnanya1,
"wrap":True,
"offsetStart":"3px"
}
]
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text": "🎶𝗦𝗧𝗔??𝗨?? 𝗢𝗖🎶\n{}".format(result["result"]['performance']["message"]),
"size":"xxs",
"color":warnanya1,
"wrap":True,
"offsetStart":"3px"
}
]
}
],
"position":"absolute",
"borderWidth":"1px",
"borderColor":warnanya1,
"offsetTop":"65px", #ATAS BAWAH
"width":"245px",
"offsetStart":"5px", #GESER SAMPING
"height":"75px",
"cornerRadius":"5px"
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"box",
"layout":"horizontal",
"contents":[
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"image",
"url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"size":"full",
"aspectMode":"cover"
}
],
"width":"40px",
"height":"40px"
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"box",
"layout":"vertical",
"contents":[
{
"type":"text",
"text":"ＳＥＮＤＥＲ",
"align":"center",
"size":"sm",
"color":warnanya1,
},
{
"type":"separator",
"color":warnanya1,
},
{
"type":"text",
"text": "{}".format(cl.getContact(sender).displayName),
"align":"center",
"size":"sm",
"color":warnanya1,
"offsetTop":"5px"
}
]
}
]
}
],
"position":"absolute",
"width":"245px",
"offsetTop":"320px", #ATAS BAWAH
"borderWidth":"1px",
"borderColor":warnanya1,
"offsetStart":"5px", #GESER SAMPING
"cornerRadius":"5px"
}
],
"paddingAll":"0px",
"borderWidth":"2px",
"borderColor":warnanya1,
"cornerRadius":"10px"
}
}
]
}
}
                                cl.postTemplate(to, data)
                                cl.sendVideoWithURL(msg.to, res['result']['performance']['video_media_url'])
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                                
#CODING SMULE DOWNLOAD
#===========COMMAND SET============#
                        elif 'Set warnahtext ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set warnahtext ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1( to, "Gagal mengganti")
                              else:
                                  wait["warna"] = spl
                                  sendTextTemplate1( to, "warna text diganti jadi")

                        elif 'Set warnahbody ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set warnahbody ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1( to, "Gagal mengganti")
                              else:
                                  wait["warna1"] = spl
                                  sendTextTemplate1( to, "warna body diganti jadi")


                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

 
                        elif 'Set mention: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set mention: ','')
                              if spl in [""," ","\n",None]:
                                  dragonkiller(msg.to, "Gagal mengganti Key mention all member")
                              else:
                                  wait["tagall"] = spl
                                  sendTextTemplate3b(msg.to, "key mention member ~ :\n\n{}".format(str(spl)))

                        elif cmd.startswith("set welcome: "):
                          if wait["selfbot"] == True:    
                            if msg._from in admin or msg._from in Bots:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   dkbots2(msg.to, "Gagal mengganti key welcome")
                               else:
                                   settings["joincom"] = str(key)
                                   dkbots2(msg.to, "「Setkey」\nKey welcome diganti jadi「{}」".format(str(key)))

                        elif cmd.startswith("set leave: "):
                          if wait["selfbot"] == True:    
                            if msg._from in admin or msg._from in Bots:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   dkbots2(msg.to, "Gagal mengganti key Leave")
                               else:
                                   settings["leave"] = str(key)
                                   dkbots2(msg.to, "「Setkey」\nKey Leave diganti jadi「{}」".format(str(key)))



                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  dragonkiller(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate3b(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  dragonkiller(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate3b(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set ukuran: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set ukuran: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate3( to, "Gagal mengganti Ukuran Template")
                              else:
                                  wait["size"] = spl
                                  sendTextTemplate3b( to, "succes mengganti Ukuran temlate")

                        elif 'Setbaghelp: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Setbaghelp: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate3( to, "Gagal mengganti Background Help")
                              else:
                                  wait["BAGHELP"] = spl
                                  sendTextTemplate3b( to, "succes mengganti Background Help")

                        elif 'Set idline: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set idline: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate3b( to, "Gagal mengganti Id line")
                              else:
                                  settings["idline"] = spl
                                  sendTextTemplate3b( to, "succes mengganti Id Line")

                        elif 'Set lebel: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set lebel: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate3( to, "Gagal mengganti lebel tmplate")
                              else:
                                  settings["lebel"] = spl
                                  sendTextTemplate3b( to, "succes mengganti lebel tmplate")

####pertambaan 
                        elif text.lower() == "cek idline":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪ Message Idline tmplate :\n\n" + str(settings["idline"]))
                               cl.sendMessage(msg.to,"http://line.me/ti/p/~dkdkbot")
                               cl.sendMessage(to, "ubah copas url id line ssukamu")

                        elif text.lower() == "cek ukuran":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪ Message ukuran tmplate :\n\n" + str(wait["size"]))

                        elif text.lower() == "cek lebel":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪ Message Idline tmplate :\n\n" + str(settings["lebel"]))


                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪ Message Sider :\n\n" + str(wait["mention"]))
                        elif text.lower() == "cek coment post":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪Message Coment Post :\n\n" + str(settings["commentPost"]))
                        elif text.lower() == "cek mention":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪Mention all member:\n\n" + str(wait["tagall"]))                        
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, "➪Message New Add :\n\n" + str(wait["message"]))
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, " ➪Message Welcome  :\n\n" + str(settings["joincom"]))
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, " ➪Message Welcome  :\n\n" + str(settings["leave"]))
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate3b(msg.to, " ➪Message Respon :\n\n" + str(wait["Respontag"]))

                        elif cmd == "tf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, " ━━━┅┅━━\n"
"╰۞GANABAR\n"
"╭━━━━━━━━━━━━━━\n"
"║╭❉🔷ℙ𝔸𝕐𝕄𝔼ℕ𝕋🔷\n"
"║│??𝐭𝐫𝐚𝐧𝐬𝐟𝐞𝐫 𝐯𝐢𝐚🔻\n"
"║│🏦𝐁𝐀𝐍𝐊 𝐁𝐑𝐈\n"
"║│💵641-601-017-123-537\n"
"║│👱HERMINTO\n"
"║│📲083899850723\n"
"║│📲083899850723\n"
"║┝─────────────\n"
"║╰❉ ஜ۩۞GANABAR۞۩ஜ\n"
"╰━━━━━━━━━━━━━━")

                        elif cmd == "trans":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, " ━━━┅┅━━\n"
"╰۩۞GANABAR\n"
"╭━━━━━━━━━━━━━━\n"
"║╭❉🔷ℙ𝔸𝕐𝕄𝔼ℕ𝕋🔷\n"
"║│🔻𝐭𝐫𝐚𝐧𝐬𝐟𝐞𝐫 𝐯𝐢𝐚🔻\n"
"║│🏦𝐁𝐀𝐍𝐊 𝐁𝐑𝐈\n"
"║│💵641-601-017-123-537\n"
"║│👱HERMINTO\n"
"║│📲083899850723\n"
"║│📲083899850723\n"
"║┝─────────────\n"
"║╰❉ ஜ۩۞GANABAR۞۩ஜ\n"
"╰━━━━━━━━━━━━━━")
                        
#
                        elif cmd.startswith("rsmule "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://smule.com/{}/performances/json".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["list"] != []:
                                ret_ = []
                                yt = []
                                for music in a["list"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "size": "micro",
                                        "styles": {
                                            "body": {
                                               "backgroundColor": "#00FF00",
                                               "separator": True,
                                               "separatorColor": "#FF0000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#7CFC00",
                                                "separator": True,
                                               "separatorColor": "#FF0000"
                                           }
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "{}".format(music['cover_url']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=Keknya%20Gw%20Cakep%20Deh"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://www.mumbrella.asia/content/uploads/2018/10/Smule-logo.jpg",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#FF0000"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "title",
                                                    "color": "#FF0000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                 }, {
                                                    "type": "separator",
                                                    "color": "#FF0000"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['title'],
                                                    "color": "#00FF00",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                         },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Youtube",
                                                        "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                 }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#FF0000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=https://www.smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                }]
                                            },
                                            {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#FF0000",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=https://www.smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append("https://smule.com/{}/{}".format(str(search), str(music["web_url"])))
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Search Smule Resorting",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                     }
                                    cl.postTemplate(to, data)

                        elif cmd.startswith("xsmule "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://smule.com/{}/performances/json".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["list"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["list"]:
                                        ret_.append({
                                            "type": "bubble",
                                            "size": "micro",
                                            "styles": {
                                                "body": {
                                                   "backgroundColor": "#00FF00",
                                                   "separator": True,
                                                   "separatorColor": "#FF0000"
                                                },
                                                "footer": {
                                                    "backgroundColor": "#228B22",
                                                    "separator": True,
                                                   "separatorColor": "#FF0000"
                                               }
                                            },
                                            "hero": {
                                                "type": "image",
                                                "url": "{}".format(music['cover_url']),
                                                "size": "full",
                                                "aspectRatio": "20:13",
                                                "aspectMode": "cover",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "line://nv/profilePopup/mid=uf839b976d7caafe65dc03625ba5ae01c"
                                                }
                                            },
                                            "body": {
                                            "borderWidth": "1px",
                                            "borderColor": "#FF0000",
                                            "cornerRadius": "0px",
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "box",
                                                    "spacing": "none",
                                                    "flex": 0, #1
                                                    "layout": "vertical",
                                                    "contents": [{
                                                        "type": "text",
                                                        "text": "%s" % music['title'],
                                                        "color": "#00FF00",
                                                        "size": "xxs",
                                                        "weight": "bold",
                                                        "flex": 0,
                                                        "wrap": True,
                                                        "gravity": "top"
                                                    }],
                                                    "flex": 0,
                                                    "layout": "vertical"
                                                }]
                                            },
                                            "footer": {
                                            "borderWidth": "1px",
                                            "borderColor": "#FF0000",
                                            "cornerRadius": "0px",
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [{
                                                        "type": "button",
                                                        "flex": 2, #2
                                                        "style": "primary",
                                                        "color": "#00FF00",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "SM",
                                                            "uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                     }, {
                                                        "flex": 3, #3
                                                        "type": "button",
                                                        "margin": "xs",
                                                        "style": "primary",
                                                        "color": "#00FF00",
                                                        "height": "sm",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "MP3",
                                                            "uri": "line://app/1602879096-oDmLpDNO/?type=text&text=.smuleaudio%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                        }
                                                    }]
                                                },
                                                {
                                                    "type": "button",
                                                    "margin": "xs",
                                                    "style": "primary",
                                                    "color": "#00FF00",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "MP4",
                                                        "uri": "line://app/1602879096-oDmLpDNO/?type=text&text=.smulevideo%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
                                                    }
                                                }]   
                                            }
                                        }
                                    )
                                        yt.append("https://smule.com/{}/{}".format(str(search), str(music["web_url"])))
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Search Smule Resorting",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        cl.postTemplate(to, data)

                        elif cmd.startswith("!smule "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = requests.get("https://smule.com/{}/performances/json".format(str(search)))
                                data = r.text
                                a = json.loads(data)
                                if a["list"] != []:
                                    ret_ = []
                                    yt = []
                                    for music in a["list"]:
                                        warna1 = ("1AE501","#0108E5","#E50AE0","#E50F00","#DEE500","#47E1E5","#C82EF8","#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785","#696969")
                                        warnanya1 = random.choice(warna1)
                                        ret_.append({                                        
"type": "bubble",
"size": "micro",
"body": {
"type": "box",
"borderWidth": "1px",
"borderColor": warnanya1,
"cornerRadius": "10px",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "{}".format(music['cover_url']),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:6",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=ucea4db871e2f6b401ac278f6999ccf58",
"type": "uri",
}
},
{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "ＳＭＵＬＥ ＲＥＣＯＲＤ",
"color":  "#FFFF00",
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "4px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING 
"backgroundColor": "#FF7F00",
"height": "20px",
"width": "150px"
},

{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
#"text": "%s" % music['message'],
 "text": "Status Oc \n{}".format(music["message"]),
"color":  "#E50AE0",
"wrap": True,
"align": "center",
"size": "xxs",
"weight": "bold",
"offsetTop": "-2px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "40px", #ATAS BAWAH
"offsetStart": "0px", #GESER SAMPING
"backgroundColor": "#FF7F00",
"height": "60px",
"width": "160px"
},

{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "sᴍᴜʟᴇ ᴀᴜᴅɪᴏ",
"color":  "#FFFF00",
"align": "center",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px",
"action": {
"type": "uri",
"uri": "line://app/1602879096-oDmLpDNO/?type=text&text=.smuleaudio%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "103px", #ATAS BAWAH
"offsetStart": "6px",
"backgroundColor": "#FF7F00",
"height": "16px",
"width": "68px"
},
{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "sᴍᴜʟᴇ ᴠɪᴅᴇᴏ",
"color":  "#FFFF00",
"align": "center",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px",
"action": {
"type": "uri",
"uri": "line://app/1602879096-oDmLpDNO/?type=text&text=.smulevideo%20https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "103px", #ATAS BAWAH
"offsetStart": "80px",
"backgroundColor": "#FF7F00",
"height": "16px",
"width": "71px"
},
{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "%s" % music['title'],
"color":  "#E50AE0",
"wrap": True,
"align": "center",
"size": "xxs",
"weight": "bold",
"offsetTop": "-2px"
}
],
"position": "absolute",
"cornerRadius": "0px",
"offsetTop": "122px", #ATAS BAWAH
"offsetStart": "0px", #GESER SAMPING
"backgroundColor": "#FF7F00",
"height": "37px",
"width": "160px"
},
{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [ #dsini
{
"type": "image",  # PP GROUP
"url": "https://www.mumbrella.asia/content/uploads/2018/10/Smule-logo.jpg",
"size": "full",
"aspectMode": "cover",
"size": "full",
"gravity": "top",
"action": {
"type": "uri",
"uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "200px",
"width": "30px",
"height": "30px",
"offsetTop": "175px", #ATAS BAWAH
"offsetStart": "15px", #KIRI KANAN
},
#======================
{
"type": "box",
"borderWidth": "2px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [ #dsini
{
"type": "image",  # PP GROUP
"url": "https://www.mumbrella.asia/content/uploads/2018/10/Smule-logo.jpg",
"size": "full",
"aspectMode": "cover",
"size": "full",
"gravity": "top",
"action": {
"type": "uri",
"uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "200px",
"width": "50px",
"height": "50px",
"offsetTop": "161px", #ATAS BAWAH
"offsetStart": "52px", #KIRI KANAN
},
#======================
{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [ #dsini
{
"type": "image",  # PP GROUP
"url": "https://www.mumbrella.asia/content/uploads/2018/10/Smule-logo.jpg",
"size": "full",
"aspectMode": "cover",
"size": "full",
"gravity": "top",
"action": {
"type": "uri",
"uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "200px",
"width": "30px",
"height": "30px",
"offsetTop": "175px", #ATAS BAWAH
"offsetStart": "110px", #KIRI KANAN
},
{
"type": "box",
"borderWidth": "1px",
"borderColor":  warnanya1,
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "ＳＭＵＬＥ ＳＥＡＲＣＨ",
"color":  "#FFFF00",
"align": "center",
"size": "xs",
"weight": "bold",
"offsetTop": "0px",
"action": {
"type": "uri",
"uri": "https://smule.com/{}/{}".format(str(search), str(music["web_url"]))
},         
"flex": 0
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "213px", #ATAS BAWAH
"offsetStart": "4px", #GESER SAMPING
"backgroundColor": "#FF7F00",
"height": "20px",
"width": "150px"
}
],
#"backgroundColor": "#00FF00",
"paddingAll": "0px"
}
}
)
                                        yt.append("https://smule.com/{}/{}".format(str(search), str(music["web_url"])))
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "flex",
                                            "altText": "Search Smule Recording",
                                            "contents": {
                                                "type": "carousel",
                                                "contents": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        cl.postTemplate(to, data)

 
                        if "https://youtu.be" in msg.text.lower():
                          if msg._from in admin:
                            if wait["yutube"] == True:
                                try:
                                    Dzulkiflidk = msg.text.split(" ")
                                    Makassar = msg.text.replace(Dzulkiflidk[0] + " ","")
                                    Kiflilovedea = urllib.parse.quote(Makassar)
                                    Apikey = "primaz03"
                                    headers = {
                                        "apiKey":Apikey,
                                        }
                                    DKBots = json.loads(requests.get("https://beapi.me/ytmp4?url="+Kiflilovedea,headers=headers).text)
                                    cl1="╭─「 ɴᴏᴛɪꜰ ʏᴏᴜᴛᴜʙᴇ 」─────"
                                    cl1+="\n├🔹 ᴏᴘᴇɴ ᴏʀᴅᴇʀ ʙᴏᴛ ʟɪɴᴇ"
                                    cl1+="\n├🔹 ᴍɪɴᴀᴛ ᴘᴍ ᴍʏ ᴄʀᴇᴀᴛᴏʀ"
                                    cl1+="\n├🔹 ᴡʜᴀᴛꜱᴀᴘᴘ: 083899850723"
                                    cl1+="\n├🔹 ɪᴅʟɪɴᴇ: nirwanabjn"
                                    cl1+="\n╰─ 「 ᴡᴀɪᴛ ᴠɪᴅɪᴏɴʏᴀʜ 」 ─────"
                                    cl.sendMessage(msg.to, cl1)
                                    Gadis = (Makassar)
                                    BisaDesah = Gadis.replace("watch?v=", "")
                                    DKEntog = pafy.new(BisaDesah)
                                    EdanKeun = DKEntog.streams
                                    GabutuhDrama = DKEntog.getbestaudio()
                                    GabutuhDrama.bitrate
                                    DesyBasah = DKEntog.getbest()
                                    DesyBasah.resolution, DesyBasah.extension
                                    for SundaWanien in EdanKeun:
                                        Sampurasun = GabutuhDrama.url
                                        Sampurasun1 = DesyBasah.url
                                        Sampurasun2 = SundaWanien.url
                                    cl.sendAudioWithURL(msg.to, Sampurasun)
                                    cl.sendVideoWithURL(msg.to, Sampurasun1)
                                except:
                                    pass


                        elif 'https://www.smule.com' in msg.text.lower() or 'https://link.smule.com/' in msg.text.lower() or 'https://www.smule.com/c/' in msg.text.lower() or 'https://www.smule.com/p/' in msg.text.lower():
                          if msg._from in admin:
                            if wait["smule"] == True:
                                Dzulkiflidk = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                Bossdkbot = re.findall(Dzulkiflidk, text)
                                DKBot = []
                                for Ainx in Bossdkbot:
                                    if Ainx not in DKBot:
                                        DKBot.append(Ainx)
                                for TeamBot in DKBot:
                                    AnakGadis = TeamBot
                                    Apikey = "primaz03"
                                    headers = {
                                        "apiKey":Apikey,
                                        }
                                    res = json.loads(requests.get("https://beapi.me/smule/post?url="+AnakGadis,headers=headers).text)
                                    PerawanBasah="╭──「 Smule Recording」─────"
                                    PerawanBasah+="\n├⌬ Song : " +res["result"]['performance']["artist"]
                                    PerawanBasah+="\n├⌬ Judul : " +res["result"]['performance']["title"]
                                    PerawanBasah+="\n├⌬ ID Smule : " +res["result"]['performance']["owner"]["handle"]
                                    PerawanBasah+="\n├⌬ Status :  " +res["result"]['performance']["message"]
                                    PerawanBasah+="\n╰──「 Tunggu Vidio Nyah」─────"
                                    sendTextTemplate0(msg.to, PerawanBasah)
                                    cl.sendAudioWithURL(msg.to, res['result']['performance']['media_url'])
                                    cl.sendVideoWithURL(msg.to, res['result']['performance']['video_media_url'])

 

                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    sendTextTemplate3b(to, str(ret_))
                                except:
                                    sendTextTemplate3b(to, "Post tidak valid")

                        elif msg.contentType == 7:
                            if settings["checkSticker"] == True:
                                stk_id = msg.contentMetadata['STKID']
                                stk_ver = msg.contentMetadata['STKVER']
                                pkg_id = msg.contentMetadata['STKPKGID']
                                ret_ = "â•”â•â•[ Sticker Info ]"
                                ret_ += "\nâ”œâ‰½ STICKER ID : {}".format(stk_id)
                                ret_ += "\nâ”œâ‰½ STICKER PACKAGES ID : {}".format(pkg_id)
                                ret_ += "\nâ”œâ‰½ STICKER VERSION : {}".format(stk_ver)
                                ret_ += "\nâ”œâ‰½ STICKER URL : line://shop/detail/{}".format(pkg_id)
                                ret_ += "\nâ•šâ•â•[ Finish ]"
                                cl.sendMessage(to, str(ret_))


                            elif msg.contentType == 13:
                                if settings["conpp"] == True:
                                    _name = msg.contentMetadata["displayName"]
                                    copy = msg.contentMetadata["mid"]
                                    groups = cl.getGroup(msg.to)
                                    targets = []
                                    for s in groups.members:
                                        if _name in s.displayName:
                                            print ("[Target] Copy")
                                            break                             
                                        else:
                                            targets.append(copy)
                                    if targets == []:
                                        dragonkiller(msg.to, "Not Found...")
                                        pass
                                    else:
                                        for target in targets:
                                            try:
                                                cl.cloneContactProfile(target)
                                                dragonkiller(msg.to, "Clone Contact Profile and Cover Done")
                                                settings['conpp'] = False
                                                break
                                            except:
                                                     msg.contentMetadata = {'mid': target}
                                                     settings["conpp"] = False
                                                     break
                            elif msg.contentType == 13:
                                if settings["copy"] == True:
                                    _name = msg.contentMetadata["displayName"]
                                    copy = msg.contentMetadata["mid"]
                                    groups = cl.getGroup(msg.to)
                                    targets = []
                                    for s in groups.members:
                                        if _name in s.displayName:
                                            print ("[Target] Copy")
                                            break                             
                                        else:
                                            targets.append(copy)
                                    if targets == []:
                                        dragonkiller(msg.to, "TARGET TIDAK DI TEMUKAN")
                                        pass
                                    else:
                                        for target in targets:
                                            try:
                                                cl.cloneContactProfile(target)
                                                dragonkiller(msg.to, "BERHASIL MENIRU PROFIL!!!")
                                                settings['copy'] = False
                                                break
                                            except:
                                                     msg.contentMetadata = {'mid': target}
                                                     settings["copy"] = False
                                                     break  
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplate1(msg.to, "Masuk : %s" % str(group.name))                                     
#=================================================================================							 
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɢᴀᴍʙᴀʀ ᴅɪʜᴀᴘᴜs  」\n• ❂➣ ᴘᴇɴɢɪʀɪᴍ : "
                                ret_ = "• ❂➣ ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\n• ❂➣ ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n⟗   ⃢🕸Ganabar_bot  ⟗"
                                ret_ += "\nCreator:  line.me/ti/p/~nirwanabjn" 
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs  」\n"
                                ret_ += "「🔑」 ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n「🔑」ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n「🔑」ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• ➣ᴘᴇsᴀɴɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n 「🔑」Tim Ganabar_bot🕸 ⃢   ⟗"
                                ret_ += "\nCreator:  line.me/ti/p/~nirwanabjn" 
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 sᴛɪᴄᴋᴇʀ ᴅɪʜᴀᴘᴜs」\n"
                                ret_ += "「🔑」➣ ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n•「🔑」 ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\n•「🔑」 ᴡᴀᴋᴛᴜ ɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n⟗「🔑」 Ganabar_bot🕸 ⃢   ⟗"
                                ret_ += "\nCreator:  line.me/ti/p/~nirwanabjn" 
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                dkbots2(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)



        if op.type == 55:
            print ("PESAN TELAH DI BACA!!!")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#================================================================================
        if op.type == 25 or op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != cl.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                        if text.lower() == tatan:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                group.preventedJoinByTicket = False
                                cl.updateGroup(group)
                                groupUrl = cl.reissueGroupTicket(to)
                                baby = ["ucea4db871e2f6b401ac278f6999ccf58"]
                                for titit in baby:
                                    cl.sendMessage(titit, "https://line.me/R/ti/g/{}".format(groupUrl))
                        else:
                            for txt in textsadd:
                                if text.lower() == txt:
                                    img = textsadd[text.lower()]['CHAT']
                                    group = cl.getGroup(to)
                                    midMembers = [contact.mid for contact in group.members]
                                    data = random.choice(midMembers)
                                    cl.sendMessage(to, "{}".format(img), contentMetadata={"MSG_SENDER_NAME":"{}".format(cl.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(cl.getContact(data).pictureStatus)})
                            for immg in images:
                                if text.lower() == immg:
                                    img = images[text.lower()]["IMAGE"]
                                    cl.sendImage(to, img)
                            for sticker in stickers:
                                if text.lower() in sticker:
                                   sid = stickers[text.lower()]["STKID"]
                                   spkg = stickers[text.lower()]["STKPKGID"]
                                   cl.sendReplySticker(msg_id, to, spkg, sid)
                            for sticker in stickers:
                                if msg._from in admin:
                                  if text.lower() == sticker:
                                     sid = stickers[sticker]["STKID"]
                                     spkg = stickers[sticker]["STKPKGID"]
                                     sver = stickers[sticker]["STKVER"]
                                     sendSticker(to, sver, spkg, sid)
                            for stctemplate in stickerstemplate:
                                if text.lower() == stctemplate:                                  
                                    stk_id = stickerstemplate[text.lower()]["STKID"]                                    
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "{}".format(stc),
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://instagram.com/qalmi"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
                thread1 = threading.Thread(target=lineBot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
#==============kepo2305===========#
print ("===========[Login Bot Kepo Sukses]==========")
#thread = th