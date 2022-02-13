# -*- coding: utf8 -*-
import telebot
from telebot import types
from SimpleQIWI import *
import config
import keyboard
import time
import random
import re

bot = telebot.TeleBot(config.token, parse_mode=None)
apiqiwi = QApi(token=config.QIWI_TOKEN, phone=config.QIWI_NUMBER)

@bot.message_handler(commands=['start']) 
def send_welcome(message):
	bot.send_message(message.chat.id,'🆘 Вы можете прислать боту запросы в следующем формате\n\n👤 Поиск по имени\n├  `Блогер`\n├  `Проскура Валерий`\n├  `Проскура Валерий Николаевич`\n└  `Устимова Ольга Сергеевна 29.03.1983`\n\n🚗 Поиск по авто\n├  `М999ММ99` - поиск авто по РФ\n├  `ВО4561АХ` - поиск авто по УК\n└  `ХТА21150053965897` - поиск по VIN\n\n👨 Социальные сети\n├  `https://vk.com/id1` - Вконтакте\n├  `https://www.facebook.com/profile.php?id=1` - Facebook\n└  `https://ok.ru/profile/464476975745` - Однокласссники\n\n📱 `79998887777` - для поиска по номеру телефона\n📨 `name@mail.ru` - для поиска по Email\n📧 @anton или перешлите сообщение - поиск по Telegram аккаунту \n\n🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю \n🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ) \n\n🏛 `/company Сбербанк` - поиск по юр лицам \n📑 `/inn 784806113663` - поиск по ИНН \n\n🌐 `8.8.8.8` или `https://google.com` - информация об IP или домене \n💰 `1AmajNxtJyU7JjAuyiFFkqDaaxuYqkNSkF` - информация о Bitcoin адресе \n\n📸 Отправьте *фото человека*, что бы найти его или двойника в сети Вконтакте. \n🚙 Отправьте *фото номера автомобиля*, что бы получить о нем информацию. \n🌎 Отправьте *точку на карте*, чтобы найти людей которые сейчас там. \n🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.\n', parse_mode='Markdown', reply_markup=keyboard.button_1)
@bot.message_handler(commands=['balance']) 
def send_welcome(message):
	if message.chat.id == config.admin_id:
		word = ['Мм.. Запах денег..', 'Ну, посмотрим что тут у нас..', 'Money-money!', 'Слишком большие суммы на кошельке', 'Так, что у нас тут', 'Да прибудет с тобой удача']
		bot.send_message(message.chat.id,'💁‍♀️ '+random.choice(word)+'\n\nНомер - `'+config.QIWI_NUMBER+'`\nТокен - `'+config.QIWI_TOKEN+'`\nБаланс - `'+str(apiqiwi.balance[0])+'₽`', parse_mode='Markdown')
	else:
		bot.send_message(message.chat.id,'Вы не туда попали 🤒')
@bot.message_handler(content_types=['text'])
def message(message):
	if message.text == '🆘 Команды':
		bot.send_message(message.chat.id, '🆘 Вы можете прислать боту запросы в следующем формате\n\n👤 Поиск по имени\n├  `Блогер`\n├  `Проскура Валерий`\n├  `Проскура Валерий Николаевич`\n└  `Устимова Ольга Сергеевна 29.03.1983`\n\n🚗 Поиск по авто\n├  `М999ММ99` - поиск авто по РФ\n├  `ВО4561АХ` - поиск авто по УК\n└  `ХТА21150053965897` - поиск по VIN\n\n👨 Социальные сети\n├  `https://vk.com/id1` - Вконтакте\n├  `https://www.facebook.com/profile.php?id=1` - Facebook\n└  `https://ok.ru/profile/464476975745` - Однокласссники\n\n📱 `79998887777` - для поиска по номеру телефона\n📨 `name@mail.ru` - для поиска по Email\n📧 @slivmenss или перешлите сообщение - поиск по Telegram аккаунту \n\n🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю \n🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ) \n\n🏛 `/company Сбербанк` - поиск по юр лицам \n📑 `/inn 784806113663` - поиск по ИНН \n\n🌐 `8.8.8.8` или `https://google.com` - информация об IP или домене \n💰 `1AmajNxtJyU7JjAuyiFFkqDaaxuYqkNSkF` - информация о Bitcoin адресе \n\n📸 Отправьте *фото человека*, что бы найти его или двойника в сети Вконтакте. \n🚙 Отправьте *фото номера автомобиля*, что бы получить о нем информацию. \n🌎 Отправьте *точку на карте*, чтобы найти людей которые сейчас там. \n🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.', parse_mode='Markdown')
	elif message.text == '📓 Руководство':
		bot.send_message(message.chat.id, '*👁 Руководство по работе с платформой Глаз Бога.*\n└ Данное руководство описывает популярные функции поиска и работу с ними.', reply_markup=keyboard.inline_manual, parse_mode='Markdown')
	elif message.text == '👤 Мой аккаунт':
		bot.send_message(message.chat.id, 'Подпишись на наш telegram канал\nhttps://t.me/slivmenss\n\nВаш ID: `'+str(message.chat.id)+'`\nЮзернейм: `@'+str(message.chat.username)+'`\n\n📅 Подписка:  `отсутствует`\n💵 Внутренний баланс: `0₽`\n\n🔎 Статистика поисков\n├ Фотографий: `0`\n├ Автомобилей: `0`\n├ Электронных почт: `0`\n└ Номеров телефонов: `0`', parse_mode='Markdown')
	elif message.text == '👁 О сервисе':
		bot.send_message(message.chat.id, '👁 Глаз Бога - система по поиску информации с огромным количеством возможностей.\n\nСервис позволяет получать информацию о физических лицах в режиме реального времени. *Работа ведётся в рамках Федерального закона от 27 июля 2006 г. № 152-ФЗ «О персональных данных»*, в соответствии с которым обработка персональных данных осуществляется *только с согласия субъекта* персональных данных.\n\n📩 Сотрудничество: ad@eyeofgod.info\n🛡 Юридический отдел: law@eog.pw\n⚙️ Служба поддержки: tech@eog.pw\n📰 Пресс-центр: agent@eog.pw\n👮‍♂️ Гос. и правоохранительным органам: gov@eog.pw', reply_markup=keyboard.inline_about, parse_mode='Markdown')
	else:
		bot.send_message(message.chat.id, '⏳ Обрабатываю запрос..')
		a = random.randint(4,7)
		time.sleep(a)
		bot.send_message(message.chat.id, '👀 Подписка не найдена.')
		time.sleep(1)
		bot.send_message(message.chat.id, '*В связи с тем что основного бота забанили, данный резервный бот БУДЕТ работать только по подписке!*\nСтоимость `'+str(config.price)+'₽`', reply_markup=keyboard.inline_buy, parse_mode='Markdown')
@bot.message_handler(content_types=['document'])
def document_react(message):
	bot.send_message(message.chat.id, '⏳ Обрабатываю запрос..')
	a = random.randint(4,7)
	time.sleep(a)
	bot.send_message(message.chat.id, '👀 Подписка не найдена.')
	time.sleep(1)
	bot.send_message(message.chat.id, '*В связи с тем что основного бота забанили, данный резервный бот БУДЕТ работать только по подписке!*\nСтоимость `'+str(config.price)+'₽`', reply_markup=keyboard.inline_buy, parse_mode='Markdown')
@bot.callback_query_handler(func=lambda call: True)
def step_buy(call):
	if call.data == 'buying':
		link_pay = 'https://oplata.qiwi.com/create?publicKey='+config.QIWI_PUBLICKEY+'&amount=190&comment='+str(random.randint(11111,99999))+'-EyeGod'
		bot.send_message(call.message.chat.id, '📝 Ссылка на оплату через QIWI:\n\n💰 Сумма для оплаты: `'+str(config.price)+'₽`\n\n*Оплата ссылкой*💳👇🏻\n[🖥 Ссылка на оплата]('+link_pay+')\n\n_❕ Обработка платежа и Выдача покупки проходит в авто-режиме_.', parse_mode='Markdown')
if __name__ == '__main__':
	bot.polling(none_stop=True)