from src.libraries.image import *
from src.libraries.gosen_choyen import generate
from nonebot import on_command, on_message, on_notice, on_regex
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message
import re

from src.libraries.img_template import img_template_parser, edit_base_img

high_eq = on_regex(r'低情商.+高情商.+')


@high_eq.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = '低情商(.+)高情商(.+)'
    groups = re.match(regex, str(event.get_message())).groups()
    left = groups[0].strip()
    right = groups[1].strip()
    if len(left) > 15 or len(right) > 15:
        await high_eq.send("▿ aya Image Creator - 文字过多\n为了图片质量，请不要多于15个字符嗷。")
        return
    img_p = Image.open(path)
    draw_text(img_p, left, 0)
    draw_text(img_p, right, 400)
    await high_eq.send(Message([{
        "type": "text",
        "data": {
            "text": f"aya Image Creator - 低高情商  credit to Killua-Blitz/Kiba\n"
        }
    },{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(img_p), encoding='utf-8')}"
        }
    }]))


jlpx = on_command('金龙盘旋')


@jlpx.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(' ')
    if len(argv) != 3:
        await jlpx.send("▿ aya Image Creator - 参数不足\n金龙盘旋需要三个参数！")
        return
    url = await get_jlpx('盘旋', argv[0], argv[1], argv[2])
    await jlpx.send(Message([{
        "type": "text",
        "data": {
            "text": f"aya Image Creator - 金龙盘旋\n credit to Killua-Blitz/Kiba\n"
        }
    },{
        "type": "image",
        "data": {
            "file": f"{url}"
        }
    }]))

jlpx1 = on_command('金龙飞升')


@jlpx1.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(' ')
    if len(argv) != 3:
        await jlpx1.send("▿ aya Image Creator - 参数不足\n金龙飞升需要三个参数！")
        return
    url = await get_jlpx('飞升', argv[0], argv[1], argv[2])
    await jlpx1.send(Message([{
        "type": "text",
        "data": {
            "text": f"aya Image Creator - 金龙飞升\n credit to Killua-Blitz/Kiba\n"
        }
    },{
        "type": "image",
        "data": {
            "file": f"{url}"
        }
    }]))

jlpx2 = on_command('金龙酷炫')


@jlpx2.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(' ')
    if len(argv) != 2:
        await jlpx2.send("▿ aya Image Creator - 参数不足\n金龙酷炫需要两个参数！")
        return
    url = await get_jlpx('酷炫', argv[0], argv[1])
    await jlpx2.send(Message([{
        "type": "text",
        "data": {
            "text": f"aya Image Creator - 金龙酷炫\n credit to Killua-Blitz/Kiba\n"
        }
    },{
        "type": "image",
        "data": {
            "file": f"{url}"
        }
    }]))


gocho = on_command('gocho')


@gocho.handle()
async def _(bot: Bot, event: Event, state: T_State):
    argv = str(event.get_message()).strip().split(' ')
    if len(argv) != 2:
        await jlpx.send("▿ aya Image Creator - 参数不足\nGocho 需要两个参数！")
        return
    i = generate(argv[0], argv[1])
    await gocho.send(Message([{
        "type": "text",
        "data": {
            "text": f" aya Image Creator - Gocho  credit to Killua-Blitz/Kiba\n"
        }
    },{
        "type": "image",
        "data": {
            "file": f"base64://{str(image_to_base64(i), encoding='utf-8')}"
        }
    }]))


img_template = on_command("img_template", aliases={"imgt"})


@img_template.handle()
async def _(bot: Bot, event: Event):
    arg = event.get_message()
    try:
        base, img = await img_template_parser(arg)
        b64 = await edit_base_img(base, img)
        await img_template.send(Message([{
            "type": "image",
            "data": {
                "file": f"base64://{str(b64, encoding='utf-8')}"
            }
        }]))
    except Exception as e:
        await img_template.send(f"▿ aya Image Templator - Exception\n[Exception Occurred]\n{str(e)}")