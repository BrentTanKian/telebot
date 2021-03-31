from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

def get_cats_url():
    contents = requests.get('https://www.reddit.com/r/Cats/random/.json',
                            headers={'User-agent': 'your bot 0.1'}).json()
    newcontents = str(contents)
    pattern = r'(?<=url_overridden_by_dest\': ).*'
    match = re.search(pattern, newcontents)
    newstr = match.group(0)
    pattern1 = r'\'(.*?)\''
    match1 = re.search(pattern1, newstr)
    almost_url = match1.group(0)
    url = almost_url.replace("'", '')
    url = str(url)
    return url

def get_rabbits_url():
    contents = requests.get('https://www.reddit.com/r/Rabbits/random/.json',
                            headers={'User-agent': 'your bot 0.1'}).json()
    newcontents = str(contents)
    pattern = r'(?<=url_overridden_by_dest\': ).*'
    match = re.search(pattern, newcontents)
    newstr = match.group(0)
    pattern1 = r'\'(.*?)\''
    match1 = re.search(pattern1, newstr)
    almost_url = match1.group(0)
    url = almost_url.replace("'", '')
    url = str(url)
    return url

def get_mtg_url():
    contents = requests.get('https://api.scryfall.com/cards/random').json()
    url = contents['image_uris']['large']
    return url

def get_dog_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_dog_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_dog_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_rabbit_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_rabbits_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

def get_cat_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_cats_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


@run_async
def bop(update, context):
    url = get_dog_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def mtg(update, context):
    url = get_mtg_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def rabbit(update, context):
    url = get_rabbit_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def cat(update,context):
    url = get_cat_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('INSERT YOUR TOKEN NUMBER HERE', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('mtg', mtg))
    dp.add_handler(CommandHandler('rabbit', rabbit))
    dp.add_handler(CommandHandler('cat', cat))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()