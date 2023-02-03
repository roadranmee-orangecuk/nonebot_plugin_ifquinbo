from .check import cc
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11.message import Message

ifquinbo = on_keyword(['奎恩哥勃了没'])


@ifquinbo.handle()
async def _():
    msg = cc()
    await ifquinbo.finish(Message(msg))
