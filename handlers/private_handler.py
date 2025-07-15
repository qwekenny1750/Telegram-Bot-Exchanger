from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboard.reply_kb import *
from keyboard.inline_kb import *
from commands.answers import *

router = Router()

class CommandHandlers:
    def __init__(self, router: Router):
        self.rt = router
    
    def register_command_wrappers(self):
        self.rt.message.register(self.start_bot, CommandStart())
        self.rt.message.register(self.command_help, Command('help'))
        self.rt.message.register(self.command_menu, Command('menu'))
        self.rt.message.register(self.command_techosup, Command('technosupport'))

    async def start_bot(self, message: Message):
        await message.answer(start_answer(message.from_user.first_name), reply_markup=start_kb)

    async def command_help(self, message: Message):
        await message.answer(help_msg)

    async def command_menu(self, message: Message):
        await message.answer('You went to menu: ', reply_markup=start_kb)

    async def command_techosup(self, message: Message):
        await message.answer(technosup_msg)


class MessageHandlers:
    def __init__(self, router: Router):
        self.rt = router

    def register_message_wrappers(self):
        self.rt.message.register(self.techosup, F.text=='Technosupport ⚙️')
        self.rt.message.register(self.cmdhelp, F.text == 'All commands')
    
    async def techosup(self, message: Message):
        await message.answer(technosup_msg)

    async def cmdhelp(self, message: Message):
        await message.answer(help_msg)

    async def exchanging(self, message: Message):
        await message.answer(start_exchanging_msg, reply_markup=exchange_kb1)




cst = CommandHandlers(router)
cst.register_command_wrappers()

mhd = MessageHandlers(router)
mhd.register_message_wrappers()

