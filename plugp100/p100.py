import asyncio
from plugp100 import TapoApiClient

async def on():
    # create generic tapo api
    sw = TapoApiClient("192.168.1.107", "yuripeyamashita@gmail.com", "tp21Yu861223")
    await sw.login()
    await sw.on()
    # await sw.set_brightness(100)
    # print(await sw.get_state())

async def off():
    # create generic tapo api
    sw = TapoApiClient("192.168.1.107", "yuripeyamashita@gmail.com", "tp21Yu861223")
    await sw.login()
    await sw.off()
    # await sw.set_brightness(100)
    # print(await sw.get_state())


while(1):
    x = input("...:")
    if(x == "0"):
        asyncio.run(off())
    elif(x == "1"):
        asyncio.run(on())
    elif(x == "2"):
        break
