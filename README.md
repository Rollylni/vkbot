# VkBot
[![python](https://img.shields.io/pypi/pyversions/vkbots?color=blue&style=for-the-badge)](https://pypi.org/project/vkbots/) 
[![PyPi](https://img.shields.io/pypi/v/vkbots?color=blue&style=for-the-badge)](https://pypi.org/project/vkbots/)
[![downloads](https://img.shields.io/pypi/dm/vkbots?style=for-the-badge)](https://pypi.org/project/vkbots/)

библиотека для созданий LongPoll-ботов с помощью декораторов!

* [Пример](https://github.com/Rollylni/spike)

## Кто такие LongPoll-боты?
**Bots Long Poll** позволяет работать с событиями из вашего сообщества ВКонтакте  
[Подробнее...](https://vk.com/dev/bots_longpoll)

## Установка
```sh
  pip3 install vkbots
```

## Пример
```python
from vkbots import VkBot

bot = VkBot("myconfig.ini", "mylogger.ini")
bot.prefix = "/" #установка префикса для команд, пример: /ping

@bot.task(10, 5)
def task():
    """ эта функция будет вызываться каждые 10 секунд, 5 - кол.во повторений
    """
    print(" выполнен!")
    
@bot.command("ping", aliases=["пинг"])
def test(user, chat, args, obj):
    """ эта функция сработает если пользователь напишет боту /пинг или /ping
    """
    chat.sendMessage("{}, пъонг!".format(user.getName(True)))
    
if __name__ == "__main__":
    bot.start()
```
