from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config
from . import seasonalbg

__plugin_meta__ = PluginMetadata(
    name="osu!搜索歌曲",
    description="玩osu!玩的",
    usage="下次一定",
    type="application",
    homepage="https://github.com/SZ2528/nonebot-plugin-oss",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

config = get_plugin_config(Config)

