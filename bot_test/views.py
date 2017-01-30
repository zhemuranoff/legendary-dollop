import json
import telebot
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

API_TOKEN = '279802369:AAG11qQrJlySYTmozSq4Jno0ekNP7RbBdlc'
bot_test = telebot.TeleBot(API_TOKEN)

# Create your views here.
@csrf_exempt
def index(self):
    json_string = json.loads(self.body.decode('utf8'))
    update = telebot.types.Update.de_json(json_string)
    bot_test.process_new_updates([update])
    return JsonResponse({}, status=200)

@bot_test.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot_test.reply_to(message, message.text)
    