import random
from ossapi import OssapiAsync
from .config import Config
from nonebot import (
    on_command,
    get_plugin_config
)
from nonebot.adapters.onebot.v11 import (
    Bot,
    MessageEvent,
    MessageSegment,
)

# 从nonebot配置读入client_id和client_secret
plugin_config = get_plugin_config(Config)
client_id = plugin_config.oss_api_client_id
client_secret = plugin_config.oss_api_client_secret

seasonalbg_matcher = on_command("seasonalbg", aliases={"季节背景"}, priority = 5)

@seasonalbg_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    api = OssapiAsync(client_id = client_id, client_secret = client_secret)
    seasonalbg = await api.seasonal_backgrounds()
    bg = random.choice(seasonalbg.backgrounds)
    # print(bg)
    # await seasonalbg_matcher.send(str(bg.url))
    await seasonalbg_matcher.send("osu! seasonal background"+MessageSegment.image(bg.url))