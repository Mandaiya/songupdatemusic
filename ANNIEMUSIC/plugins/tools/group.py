from pyrogram import filters
from pyrogram.types import Message

from ANNIEMUSIC import app
from config import OWNER_ID


@app.on_message(filters.video_chat_started)
async def on_voice_chat_started(_, message: Message):
    await message.reply_text("🎙 **𝙾𝚗 𝙿𝚊𝚗𝚗𝚒𝚝𝚊𝚗𝚐𝚊 𝙳𝚊𝚠𝚠 𝙾𝚗 𝙿𝚊𝚗𝚗𝚒𝚝𝚊𝚗𝚐𝚊𝚊**")


@app.on_message(filters.video_chat_ended)
async def on_voice_chat_ended(_, message: Message):
    await message.reply_text("🔕 **𝙸𝚗𝚊𝚗𝚐𝚊 𝚕𝚎𝚢𝚢 𝚊𝚝𝚑𝚞𝚔𝚞𝚕𝚊𝚒𝚢𝚎𝚎 𝚌𝚕𝚘𝚜𝚎 𝚙𝚊𝚗𝚗𝚒𝚝𝚎𝚗𝚐𝚊.**")


@app.on_message(filters.video_chat_members_invited)
async def on_voice_chat_members_invited(_, message: Message):
    inviter = message.from_user.mention if message.from_user else "Someone"
    invited_list = []

    for user in message.video_chat_members_invited.users:
        try:
            invited_list.append(f"[{user.first_name}](tg://user?id={user.id})")
        except:
            continue

    if invited_list:
        users = ", ".join(invited_list)
        await message.reply_text(f"Oru manuchan koopuduran heh {inviter} ɪɴᴠɪᴛᴇᴅ {users} Vc ku vangaleey 😉")


@app.on_message(filters.command("leavegroup") & filters.user(OWNER_ID))
async def leave_group(_, message: Message):
    await message.reply_text("👋 **Bye... buyee Leaving the group...**")
    await app.leave_chat(chat_id=message.chat.id, delete=True)
