# import asyncio

from plugp100 import TapoApiClient


async def main():
    # create generic tapo api
    sw = TapoApiClient("192.168.1.107", "yuripeyamashita@gmail.com", "tp21Yu861223")
    await sw.login()
    await sw.on()
    # await sw.set_brightness(100)
    # print(await sw.get_state())
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.run_until_complete(asyncio.sleep(0.1))
# loop.close()
main()
