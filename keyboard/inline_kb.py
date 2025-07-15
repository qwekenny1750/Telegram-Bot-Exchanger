from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

exchange_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USD', callback_data='USD'),
            InlineKeyboardButton(text='EUR', callback_data='EUR'),
            InlineKeyboardButton(text='JPY', callback_data='JPY'),
            InlineKeyboardButton(text='BTC', callback_data='BTC'),
            InlineKeyboardButton(text='GBP', callback_data='GBP')
        ],
        [
            InlineKeyboardButton(text='CAD', callback_data='CAD'),
            InlineKeyboardButton(text='AUD', callback_data='AUD'),
            InlineKeyboardButton(text='CHF', callback_data='CHF'),
            InlineKeyboardButton(text='CNY', callback_data='CNY'),
            InlineKeyboardButton(text='INR', callback_data='INR')
        ],
        [
            InlineKeyboardButton(text='BRL', callback_data='BRL'),
            InlineKeyboardButton(text='RUB', callback_data='RUB'),
            InlineKeyboardButton(text='MXN', callback_data='MXN'),
            InlineKeyboardButton(text='ZAR', callback_data='ZAR'),
            InlineKeyboardButton(text='KZT', callback_data='KZT')
        ],
        [
            InlineKeyboardButton(text='UAH', callback_data='UAH'),
            InlineKeyboardButton(text='PLN', callback_data='PLN'),
            InlineKeyboardButton(text='TRY', callback_data='TRY'),
            InlineKeyboardButton(text='SEK', callback_data='SEK'),
            InlineKeyboardButton(text='NOK', callback_data='NOK')
        ],
        [
            InlineKeyboardButton(text='DKK', callback_data='DKK'),
            InlineKeyboardButton(text='HKD', callback_data='HKD'),
            InlineKeyboardButton(text='SGD', callback_data='SGD'),
            InlineKeyboardButton(text='NZD', callback_data='NZD'),
            InlineKeyboardButton(text='PHP', callback_data='PHP')
        ],
        [
            InlineKeyboardButton(text='Enter manually', callback_data='enterM'),
            InlineKeyboardButton(text='Next page ➡️', callback_data='next1')
        ]
        

    ]
)

exchange_kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='THB', callback_data='THB'),
            InlineKeyboardButton(text='IDR', callback_data='IDR'),
            InlineKeyboardButton(text='MYR', callback_data='MYR'),
            InlineKeyboardButton(text='VND', callback_data='VND'),
            InlineKeyboardButton(text='AED', callback_data='AED')
        ],
        [
            InlineKeyboardButton(text='SAR', callback_data='SAR'),
            InlineKeyboardButton(text='EGP', callback_data='AUD'),
            InlineKeyboardButton(text='ARS', callback_data='ARS'),
            InlineKeyboardButton(text='CLP', callback_data='CLP'),
            InlineKeyboardButton(text='COP', callback_data='COP')
        ],
        [
            InlineKeyboardButton(text='NGN', callback_data='NGN'),
            InlineKeyboardButton(text='KES', callback_data='KES'),
            InlineKeyboardButton(text='PKR', callback_data='PKR'),
            InlineKeyboardButton(text='BDT', callback_data='BDT'),
            InlineKeyboardButton(text='LKR', callback_data='LKR')
        ],
        [
            InlineKeyboardButton(text='ETH', callback_data='ETH'),
            InlineKeyboardButton(text='XRP', callback_data='XRP'),
            InlineKeyboardButton(text='ADA', callback_data='ADA'),
            InlineKeyboardButton(text='SOL', callback_data='SOL'),
            InlineKeyboardButton(text='DOT', callback_data='DOT')
        ],
        [
            InlineKeyboardButton(text='BNB', callback_data='BNB'),
            InlineKeyboardButton(text='DOGE', callback_data='DOGE'),
            InlineKeyboardButton(text='SHIB', callback_data='SHIB'),
            InlineKeyboardButton(text='LTC', callback_data='LTC'),
            InlineKeyboardButton(text='BCH', callback_data='BCH')
        ],
        [
            InlineKeyboardButton(text='⬅️ Last page', callback_data = 'last1'),
            InlineKeyboardButton(text='Enter manually', callback_data='enterM'),
            InlineKeyboardButton(text='Next page ➡️', callback_data='next2')
        ]
        

    ]
)

exchange_kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='XLM', callback_data='XLM'),
            InlineKeyboardButton(text='LINK', callback_data='LINK'),
            InlineKeyboardButton(text='UNI', callback_data='UNI'),
            InlineKeyboardButton(text='MATIC', callback_data='MATIC'),
            InlineKeyboardButton(text='AVAX', callback_data='AVAX')
        ],
        [
            InlineKeyboardButton(text='TRX', callback_data='TRX'),
            InlineKeyboardButton(text='ETC', callback_data='ETC'),
            InlineKeyboardButton(text='XMR', callback_data='XMR'),
            InlineKeyboardButton(text='ZEC', callback_data='ZEC'),
            InlineKeyboardButton(text='DASH', callback_data='DASH')
        ],
        [
            InlineKeyboardButton(text='ATOM', callback_data='ATOM'),
            InlineKeyboardButton(text='NEAR', callback_data='NEAR'),
            InlineKeyboardButton(text='FIL', callback_data='FIL'),
            InlineKeyboardButton(text='ICP', callback_data='ICP'),
            InlineKeyboardButton(text='AAVE', callback_data='AAVE')
        ],
        [
            InlineKeyboardButton(text='MKR', callback_data='MKR'),
            InlineKeyboardButton(text='COMP', callback_data='COMP'),
            InlineKeyboardButton(text='USDT', callback_data='USDT'),
            InlineKeyboardButton(text='USDC', callback_data='USDC'),
            InlineKeyboardButton(text='DAI', callback_data='DAI')
        ],
        [
            InlineKeyboardButton(text='FRAX', callback_data='FRAX'),
            InlineKeyboardButton(text='TUSD', callback_data='TUSD')
        ],
        [
            InlineKeyboardButton(text='⬅️ Last page', callback_data = 'last2'),
            InlineKeyboardButton(text='Enter manually', callback_data='enterM'),
        ]
        

    ]
)