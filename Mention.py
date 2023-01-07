import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","28496124")
api_hash = os.environ.get("API_HASH","dcadf01f9a76befff2eccc932c6eabd1")
bot_token = os.environ.get("TOKEN","5840432215:AAGhOu9yvCG6ualVnNIkcOvqrMzJIyNu7O0")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

emoji_calisan = []

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("●** ᴍᴇʀʜᴀʙᴀ ❤️**\n\n● **ɢʀᴜʙᴜɴᴜᴢᴅᴀᴋɪ ᴛᴜᴍ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʙɪʟɪʀɪᴍ , ʙᴇɴɪ ɢʀᴜʙᴜɴᴜᴢᴀ ᴇᴋʟᴇʏɪᴘ ʏᴇᴛᴋɪ ᴠᴇʀᴍᴇɴɪᴢ ɢᴇʀᴇᴋɪʀ . . !** \n\n● **ᴛᴜᴍ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴏɢʀᴇɴᴍᴇᴋ ɪᴄɪɴ /help ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴɪɴ . . !**",
                    buttons=(
                   
		      [Button.url('🎉  𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  🎉', 'https://t.me/StarTaggerBot?startgroup=a')],
                      [Button.url('📝  𝗗𝗲𝘀𝘁𝗲𝗸 𝗚𝗿𝘂𝗯𝘂  📝',  'https://t.me/StarBotDestek')], 
                      [Button.url('😎  𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  😎', 'https://t.me/ByWolk')],
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "📝 **ᴇᴛɪᴋᴇᴛ ᴛᴀɢɢᴇʀ ᴋᴏᴍᴜᴛʟᴀʀɪ **\n\n**» /utag < ᴍᴇsᴀᴊɪɴɪᴢ > \nɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ 5-ʟɪ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ .  .  !**\n\n**» /tag  < ᴍᴇsᴀᴊɪɴɪᴢ > \nɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ . . !**\n\n**» /cancel => ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪɴɪ ᴅᴜʀᴅᴜʀᴜʀ . . !**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  𝗕𝗲𝗻𝗶 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  🎉', 'https://t.me/StarTagBot?startgroup=a')],
                      [Button.url('📝  𝗗𝗲𝘀𝘁𝗲𝗸 𝗚𝗿𝘂𝗯𝘂  📝',  'https://t.me/StarBotDestek')],
                      [Button.url('😎  𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  😎', 'https://t.me/ByWolk')],
                    ),
                    link_preview=False
                   )
	
@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**📝 ᴇᴛɪᴋᴇᴛ ᴛᴀɢɢᴇʀ ᴋᴏᴍᴜᴛʟᴀʀɪ\n\n» /utag < ᴍᴇsᴀᴊɪɴɪᴢ > => ɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ 5-ʟɪ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ .  .  !\n» /tag  < ᴍᴇsᴀᴊɪɴɪᴢ > => ɢʀᴜʙᴛᴀᴋɪ ᴋᴜʟʟᴀɴɪᴄɪʟᴀʀᴀ ᴛᴇᴋ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ . . !\n» /cancel => ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪɴɪ ᴅᴜʀᴅᴜʀᴜʀ . . !\n\n✵ ʙɪʀ ᴄᴏᴋ ᴏᴢᴇʟʟɪɢᴇ sᴀʜɪᴘ @StarTaggerBot 'ᴜ ɢʀᴜʙᴜɴᴜᴢᴀ ʀᴀʜᴀᴛʟɪᴋʟᴀ ᴇᴋʟᴇʏɪᴘ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . ! **"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🎉  𝗕𝗼𝘁𝘂 𝗚𝗿𝘂𝗯𝗮 𝗘𝗸𝗹𝗲  🎉', 'https://t.me/startaggerbot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😻 😼 😽 🙀 😿 😾 🔞 🌹 ".split (" ")


@client.on(events.NewMessage(pattern="^/jssjejs ?(.*)"))
async def mentionall(event):
  global emoji_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir😐**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Geçmiş mesajlar için etiket ede bilmiom**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗒𝖺𝗉𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄**")
  else:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 sebep 𝗒𝖺𝗓𝗂𝗇...!**")
  
  if mode == "text_on_cmd":
    emoji_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("** 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    emoji_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in emoji_calisan:
        await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝖺𝗋𝗂𝗒𝗅𝖺 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗅𝖽𝗎 ...**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global emoji_calisan
  emoji_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜʙᴛᴀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajlara Cevab Vermeyin")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖻𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 𝗌𝖾𝖻𝖾𝗉 𝗒𝗈𝗄**")
  else:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})** , "
      if event.chat_id not in anlik_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ɢʀᴜʙᴛᴀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀsɪɴɪᴢ . . !**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**● ʙᴜ ᴋᴏᴍᴜᴛᴜ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ . . !**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  else:
    return await event.respond("**● ᴇᴛɪᴋᴇᴛ ɪsʟᴇᴍɪɴɪ ʙᴀsʟᴀᴛᴍᴀᴋ ɪᴄɪɴ \n< sᴇʙᴇᴘ > ɢɪʀɪɴ ʏᴀᴅᴀ ʙɪʀ ᴍᴇsᴀᴊɪ ʏᴀɴɪᴛʟᴀʏɪɴ . . !**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**● ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ɪsʟᴇᴍɪ ʙᴀsᴀʀɪʏʟᴀ ᴅᴜʀᴅᴜʀᴜʟᴅᴜ . . !**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admin ?(.*)"))
async def mentionall(tagadmin):

	if admintag.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=cp):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)


print(">> Bot Başlatıldı. Üyelere etiket atabilirim. <<")
client.run_until_disconnected()
