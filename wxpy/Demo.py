# 导入模块
from wxpy import *

# 初始化机器人，扫码登陆
bot = Bot()

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径

found = bot.friends().search('蔡宇恒')[0]


while True:
    found.send("扣 脚!")


