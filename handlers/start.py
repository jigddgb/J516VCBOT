import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CZp7eIAACpv1jYIbWhI9JPBkvLLSLwPxc-8yu2QACDgcAAruXGFbarx8_grqJYh4E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()}ย , ๐ฅ\n\n
เน This is [{bn}](t.me/{bu}) ,ย  !
โป The most Powerful telegram music  bot with some awesome and useful features.

โโโโโโโโโโโโโโโโโโ
เน  All of my command can be used with My command handle : ( / . โข $ ^ ~ + * ? )
โป Made ๐ค by : [๐๐๐ฌ๐ฅ](https://t.me/Finex_xD) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โย แดแดแด แดแด แดสsแด สแดแด ษขแดส", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "๐จ Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "๐จ Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "๐ค Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "๐จโ๐ป Developer ", url=f"https://t.me/Finex_xD"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "โ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "๐ก Git repo", url="https://te.legra.ph/file/fcf07ac0577d969e25cdd.mp4"
"
                    )]
            ]
       ),
    )

