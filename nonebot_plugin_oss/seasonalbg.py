import json
import logging
import random
import urllib
import time
import hashlib
import requests
import nonebot
from .config import Config
from nonebot.rule import Rule
from nonebot import (
    get_bot,
    on_command,
    on_startswith,
    on_keyword,
    on_fullmatch,
    on_message,
    on_regex,
    require,
    get_plugin_config
)
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageEvent
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER, GROUP_MEMBER
from nonebot.typing import T_State
from nonebot.log import logger
from nonebot.params import ArgPlainText, CommandArg, ArgStr
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupIncreaseNoticeEvent,
    MessageSegment,
    Message,
    GroupMessageEvent,
    Event,
    escape,
)
from ossapi import OssapiAsync

# 从nonebot配置读入client_id和client_secret
plugin_config = get_plugin_config(Config)
client_id = plugin_config.oss_api_client_id
client_secret = plugin_config.oss_api_client_secret

w = on_command("seasonalbg", aliases={"季节背景"}, priority = 5)

@w.handle()
async def _(bot: Bot, event: MessageEvent):
    api = OssapiAsync(client_id = client_id, client_secret = client_secret)
    seasonalbg = await api.seasonal_backgrounds()
    bg = random.choice(seasonalbg.backgrounds)
    # print(bg)
    # await w.send(str(bg.url))
    await w.send("osu! seasonal background"+MessageSegment.image(bg.url))