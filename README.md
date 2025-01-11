<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png?raw=true" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg?raw=true" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-osu

_✨ 玩osu!玩的 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/SZ2528/nonebot-plugin-osu.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-osu">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-osu.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>


## 📖 介绍

这里是插件的详细介绍部分

~~下次一定~~

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-osu

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-osu
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-osu
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-osu
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-osu
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_osu"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| `osu_api_client_id` | 是 | 无 | 在帐户设置页面上注册 OAuth 应用程序 |
| `osu_api_client_secret` | 是 | 无 | 在帐户设置页面上注册 OAuth 应用程序 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 指令1 | 主人 | 否 | 私聊 | 指令说明 |
| 指令2 | 群员 | 是 | 群聊 | 指令说明 |
### 效果图
如果有效果图的话
