import textwrap

def start_answer(user):
    answer = textwrap.dedent(f"""\
    Hello, <b>{user}</b>!
    This bot helps you find out the exchange
    rate of the currency you are interested in.
    Tap "Get the course 💶" to begin:

    """)
    return answer

def resEx(From, amount1, amount2) -> str:
    result_of_exchanging = textwrap.dedent(f"""\
    {amount1} <b>{From}</b>  =  <b>{amount2}</b>

    """)
    return result_of_exchanging
    
technosup_msg = 'Hello! Technosupport: > @xxx'

help_msg = textwrap.dedent("""\
    <b>/start</b> - start bot
    <b>/menu</b> - go to the main menu
    <b>/help</b> - get discription about commands
    <b>/technosupport</b> - ask question
    """)

start_exchanging_msg = textwrap.dedent("""\
    Select the currency <b>FROM</b>
    which you want to transfer the rate 👇:
    """)
start_exchanging_msg2 = textwrap.dedent("""\
    Select the currency <b>TO</b>
    which you want to transfer the rate:
    """)

ent_count = textwrap.dedent("""\
    Enter the <b>AMOUNT</b> you want to exchange
    in format <b>xxx</b> or <b>xxx.x</b>
    """)

error_value = "Your number does not meet the standard. Dont use third-party characters except 1234567890.,/nTry again!"

