class Translation(object):
    START_TEXT =Hello
Welcome to Telegram API ID & HASH
Enter Your Telegram 📞Phone Number 📞
__with country code eg.+9141985053855__

/start at any stage to re-enter your details
    AFTER_RECVD_CODE_TEXT = """I see!
now please send the Telegram code that you received from Telegram!
this code is only used for the purpose of getting the APP ID from my.telegram.org
if you do not trust this bot dev, please host this bot yourself
by opening https://github.com/LEGEND-AI/API-SCRAPPER and clicking on the Pink Button

/start at any stage to re-enter your details"""

    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."

    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@It_Bot_supporters"

    CANCELLED_MESG = "Bye! Please re /start the bot conversation"

    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"

    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
