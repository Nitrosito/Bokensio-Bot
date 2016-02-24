# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import commands

TOKEN = '<TOKEN VA AQUI>' # Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['imagenboke']) # Indicamos que lo siguiente va a controlar el comando '/roto2'.
def command_roto2(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    commands.getoutput('fswebcam -r 1600x1200 --jpeg 100 -d /dev/video0 /home/nitrosito/test2.jpg')
    bot.send_photo( cid, open( 'test2.jpg', 'rb')) # Con la función 'send_photo()'
        #bot.send_photo( cid, open( 'roto2.png', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto de nuestro querido :roto2:

@bot.message_handler(commands=['miramacho']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_miramacho(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
