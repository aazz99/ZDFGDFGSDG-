#   سورس تایم روی اسم 
import rubika
#  کتابخانه روبیکا ایمپورت میکنیم 
from rubika.client import Bot
#     کلاس بوت ایمپورت میکنیم از کتابخانه 
import requests
#       کتابخانه ریکوست ایمپورت میکنیم 
from requests import get
#      کلاس جت ایمپورت میکنیم 
import time 
#     کتابخانه تایم ایپورت میکنیم 
from time import sleep
#    کلاس سلیپ یا خواب ایمپورت میکنیم 
bot = Bot("tdzyvycwzmqlkiwvhhtngigybmipijpg")
#     بجای AUTH اوث خودتان را وارد کنید 
while True:
#حلقه while را روشن بزارید 	
	sleep (10)
#    سلیپ بزارید روی 10 تا هر 10 ثانیه اپدیت بشه 	
	api_time = requests.get('http://api.codebazan.ir/time-date/?td=time').text
#       api ست کنیم 	
	bot.editProfile(first_name=api_time)
#       کلاش ادیت پروفایل  میزاریم و داخلش روی فیرست نام  api_time  میزاریم 	
	print (f'good {api_time}')
#	و میزاریم پرینت کنه 
#           (((((  پایان   )))))
#    Code By Reback
#Dev : https://rubika.ir/admins_ads
#Ch-  : @ANJOMAN_PYDROiD