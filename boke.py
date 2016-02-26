# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import commands

TOKEN = 'xD'

def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text': 
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
            f = open('/var/log/boke/logUsuarios.log', 'a')
            f.write(mensaje + "\n")
            f.close()
            #print mensaje

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
bot.set_update_listener(listener) #le decimos al bot que utilice como funcion escuchadora nuestra funcion 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['imagenboke']) # Indicamos que lo siguiente va a controlar el comando 
def command_getimagen(m): # Definimos una funcion que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversacion para poder responder.
    commands.getoutput('fswebcam -r 1600x800 --jpeg 90 -d /dev/video0 /home/pi/bokeh.jpg')
    bot.send_photo( cid, open( '/home/pi/bokeh.jpg', 'rb')) # Con la funcion 'send_photo()'

@bot.message_handler(commands=['saludo']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_saludo(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algun fallo
