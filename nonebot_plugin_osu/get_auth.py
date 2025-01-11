from nonebot import (
    on_command,
    on_startswith,
    require,
    get_plugin_config
)
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.adapters.onebot.v11 import (
    Bot,
)
from .config import Config
from nonebot import require
require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store
from urllib.parse import urlencode
import requests
import json

# 从nonebot配置读入client_id和client_secret
plugin_config = get_plugin_config(Config)
client_id = plugin_config.osu_api_client_id
client_secret = plugin_config.osu_api_client_secret

getauth_matcher = on_command("osugetauth", aliases={"osu获取授权", "获取osu授权"})
@getauth_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    params = {
        'client_id': client_id,
        # 'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': 'public'
    }
    url = f"https://osu.ppy.sh/oauth/authorize?{urlencode(params)}"
    await getauth_matcher.send(f"请前往此链接完成授权，完成后复制页面链接并发送\n{url}")

gettoken_matcher = on_startswith("https://osu.ppy.sh/oauth/authorize", block = True)
@gettoken_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    # 解析url中的code参数和state参数
    url = event.get_plaintext()
    code = url.split("code=")[1].split("&")[0]

    # 使用code换取access_token
    # 下次一定
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": 'authorization_code'
    }
    response = requests.post("https://osu.ppy.sh/oauth/token", headers=headers, data=data)
    if response.status_code == 200:
        # response.json() 就是access_token
        # 存储access_token，而且不同user_id都有各自的access_token
        access_token_dir = store.get_plugin_data_dir / "access_token.json"
        access_token_dir.parent.mkdir(parents=True, exist_ok=True)
        with open(access_token_dir, '+') as f:
            access_tokens = json.load(f)
            access_tokens[event.user_id] = response.json()
            json.dump(access_tokens, f)

    else:
        await gettoken_matcher.finish(f"获取access token失败: {response.json()}")
        # raise Exception(f"Failed to get access token: {response.status_code}")

    