import bot
import getpass


email = input('Enter the email ID for facebook account: ')
passWord = getpass.getpass(prompt='Enter the password of your Facebook account: ')


bot = bot.Bot(email, passWord)
bot.listen()
