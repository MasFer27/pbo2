#NAMA : FERLI
#NIM  : 210511140
#KELAS: TI21 D

import asyncio

async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in async_generator():
        try:
            print(value)
        except StopAsyncIteration:
            print("Async generator is exhausted")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
