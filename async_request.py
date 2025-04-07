import aiohttp
import asyncio


async def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data


async def main():
    data = await fetch_data()
    print(data)

if __name__ == "__main__":
    asyncio.run(main())