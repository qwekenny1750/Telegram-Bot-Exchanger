import time
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.reply_kb import *
from keyboard.inline_kb import *
from commands.answers import *
from parsing.parser import ExchangeParser

ex_router = Router()

class UserExchanging(StatesGroup):
    first_cur = State()
    last_cur = State()
    count_cur = State()

class Entering(StatesGroup):
    entering1 = State()
    entering2 = State()

class FSM_Events(UserExchanging, Entering):
    pass


class Exchanger:
    def __init__(self, router: Router):
        self.rt = router
        

    def current_list(self):
        self.currents: list = [
            'USD','EUR','JPY','GBP','CAD','AUD','CHF','CNY','INR','BRL','RUB','MXN','ZAR',
            'KZT','UAH','PLN','TRY','SEK','NOK','DKK','HKD','SGD','NZD','PHP','THB','IDR',
            'MYR','VND','AED','SAR','EGP','ARS','CLP','COP','NGN','KES','PKR','BDT','LKR',
            'BTC','ETH','XRP','ADA','SOL','DOT','BNB','DOGE','SHIB','LTC','BCH','XLM','LINK',
            'UNI','MATIC','AVAX','TRX','ETC','XMR','ZEC','DASH','ATOM','NEAR','FIL','ICP',
            'AAVE','MKR','COMP','USDT','USDC','DAI','FRAX','TUSD'
        ] 
        return self.currents
    
    @staticmethod
    def is_real(s: str) -> bool:
        try: 
            float(s)
            return True
        except ValueError:
            return False

    def register_callback_wrappers(self):
        self.rt.callback_query.register(self.ex1, F.data.in_(self.current_list()),  StateFilter(FSM_Events.first_cur))
        self.rt.callback_query.register(self.ex2, F.data.in_(self.current_list()),  StateFilter(FSM_Events.last_cur))
        self.rt.message.register(self.exit, StateFilter(FSM_Events.count_cur))
        self.rt.message.register(self.exchanging, F.text == 'Get the course 💶')
        self.rt.callback_query.register(self.iteration_pages_next1_t1, F.data == 'next1', StateFilter(FSM_Events.first_cur))
        self.rt.callback_query.register(self.iteration_pages_next2_t1, F.data == 'next2', StateFilter(FSM_Events.first_cur))
        self.rt.callback_query.register(self.iteration_pages_last1_t1, F.data == 'last1', StateFilter(FSM_Events.first_cur))
        self.rt.callback_query.register(self.iteration_pages_last2_t1, F.data == 'last2', StateFilter(FSM_Events.first_cur))
        self.rt.callback_query.register(self.iteration_pages_next1_t2, F.data == 'next1', StateFilter(FSM_Events.last_cur))
        self.rt.callback_query.register(self.iteration_pages_next2_t2, F.data == 'next2', StateFilter(FSM_Events.last_cur))
        self.rt.callback_query.register(self.iteration_pages_last1_t2, F.data == 'last1', StateFilter(FSM_Events.last_cur))
        self.rt.callback_query.register(self.iteration_pages_last2_t2, F.data == 'last2', StateFilter(FSM_Events.last_cur))
        self.rt.callback_query.register(self.Exentering1, F.data == 'enterM', StateFilter(FSM_Events.first_cur))
        self.rt.message.register(self.Exentering1_2, StateFilter(FSM_Events.first_cur))
        self.rt.callback_query.register(self.Exentering2, F.data == 'enterM', StateFilter(FSM_Events.last_cur))
        self.rt.message.register(self.Exentering2_2, StateFilter(FSM_Events.last_cur))
        




    async def exchanging(self, message: Message, state: FSMContext):
        await state.set_state(FSM_Events.first_cur)
        await message.answer('Start exchanging...', reply_markup=ReplyKeyboardRemove())
        self.kex1 = await message.answer(start_exchanging_msg, reply_markup=exchange_kb1)

    async def ex1(self, callback: CallbackQuery, state: FSMContext):
        await state.update_data(frm=callback.data)
        await callback.answer('Done...')
        await state.set_state(FSM_Events.last_cur)
        await self.kex1.delete()
        time.sleep(1)
        self.kex2 = await callback.message.answer(start_exchanging_msg2, reply_markup=exchange_kb1)

    async def ex2(self, callback: CallbackQuery, state: FSMContext):
        await state.update_data(to=callback.data)
        await self.kex2.delete()
        await state.set_state(FSM_Events.count_cur)
        await callback.message.answer(ent_count)

    async def exit(self, message: Message, state: FSMContext):
        count = message.text.replace(',', '.')
        trying = self.is_real(count)
        if not trying:
            await state.clear()
            await message.answer(error_value, reply_markup=start_kb)
        else:
            await state.update_data(cnt=count)
            data = await state.get_data()
            await message.answer('Waiting server answer...')
            e = ExchangeParser(data["cnt"], data["frm"], data["to"])
            e.connection()
            result = e.parse()
            await message.answer(resEx(data["frm"], data["cnt"], result),reply_markup=start_kb)
            await state.clear()



    async def iteration_pages_next1_t1(self, callback: CallbackQuery, state: FSMContext):
        await callback.answer('')
        await state.update_data(frm=callback.data)
        self.kex1 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb2)

    async def iteration_pages_next2_t1(self, callback: CallbackQuery,  state: FSMContext):
        await callback.answer('')
        await state.update_data(frm=callback.data)
        self.kex1 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb3)

    async def iteration_pages_last1_t1(self, callback: CallbackQuery,  state: FSMContext):
        await callback.answer('')
        await state.update_data(frm=callback.data)
        self.kex1 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb1)
    
    async def iteration_pages_last2_t1(self, callback: CallbackQuery,  state: FSMContext):
        await callback.answer('')
        await state.update_data(frm=callback.data)
        self.kex1 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb2)



    async def iteration_pages_next1_t2(self, callback: CallbackQuery,  state: FSMContext):
        await callback.answer('')
        await state.update_data(to=callback.data)
        self.kex2 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb2)

    async def iteration_pages_next2_t2(self, callback: CallbackQuery, state: FSMContext):
        await callback.answer('')
        await state.update_data(to=callback.data)
        self.kex2 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb3)


    async def iteration_pages_last1_t2(self, callback: CallbackQuery, state: FSMContext):
        await callback.answer('')
        await state.update_data(to=callback.data)
        self.kex2 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb1)
    
    async def iteration_pages_last2_t2(self, callback: CallbackQuery, state: FSMContext):
        await callback.answer('')
        await state.update_data(to=callback.data)
        self.kex2 = await callback.message.edit_text(start_exchanging_msg, reply_markup=exchange_kb2)



    async def Exentering1(self, callback: CallbackQuery, state: FSMContext):
        await callback.answer('')
        await callback.message.answer('Enter your currency (FROM):')

    async def Exentering1_2(self, message: Message, state: FSMContext):
        if message.text.upper() not in self.current_list():
            await message.answer('Your currency not exists in our list. Try again!', reply_markup=start_kb)
            await state.clear()
        else:
            await message.answer('Ok, next..')
            await state.update_data(frm=message.text)
            await state.set_state(FSM_Events.last_cur)
            await self.kex1.delete()
            time.sleep(1)
            self.kex2 = await message.answer(start_exchanging_msg2, reply_markup=exchange_kb1)

    async def Exentering2(self, callback: CallbackQuery, state: FSMContext):
        await callback.answer('')
        await callback.message.answer('Enter your currency (FROM):')

    async def Exentering2_2(self, message: Message, state: FSMContext):
        if message.text.upper() not in self.current_list():
            await message.answer('Your currency not exists in our list. Try again!', reply_markup=start_kb)
            await state.clear()
        else:
            await message.answer('Done...')
            await state.update_data(to=message.text)
            await self.kex2.delete()
            await state.set_state(FSM_Events.count_cur)
            await message.answer(ent_count)


ex = Exchanger(ex_router)
ex.register_callback_wrappers()
ex.current_list()


