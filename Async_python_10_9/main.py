import asyncio
import aiofiles
from aiofiles import os as aos
import time

f_summa = 0


async def read_f(fname: str, sem: asyncio.Semaphore) -> None:
    global f_summa
    async with sem:
        async with aiofiles.open(file=fname, mode='r', encoding='utf-8') as f:
            content = int((await f.readline()).rstrip())
            if content % 2 == 0:
                f_summa += content


async def main():
    path: str = r"C:\Users\***\PycharmProjects\forstepik\files"
    sem: asyncio.Semaphore = asyncio.Semaphore(1000)
    temp_check = await aos.listdir(path)
    tasks = [asyncio.create_task(read_f(f"{path}\{filename}", sem)) for filename in temp_check]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Time: {end_time - start_time}")
    print(f_summa)


asyncio.run(main())
