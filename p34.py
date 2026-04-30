import asyncio
import aiohttp

urls = ["youtube.com", "reddit.com", "x.com"]

async def fetch_status(session, url):
    try:
        async with session.get(url, timeout = 5) as response:
            return url, response.status
    except asyncio.TimeoutError:
        return url, "Timeout"
    except aiohttp.ClientError:
        return url, "Connection Error"

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        result = await asyncio.gather(*tasks)
        for url, status in result:
            print(url, '->', status)

asyncio.run(main())