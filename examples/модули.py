### модули 

import message # подключаем python файл  и можем использвать его функции например
message.hello()

import message as msg # подключаем python файл, даем его короткое имя  msg, и можем использвать его функции например
msg.hello()

from message import hello, bye  # подключаем только функции hello и bye из message

from message import * # подключаем все message

help("modules")   # выведет в консоль все популярные модули