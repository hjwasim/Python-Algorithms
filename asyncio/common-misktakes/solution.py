import time
import asyncio
import aiohttp

BASE_URL = "https://ponyapi.net/v1/character/"

def get_data(person: str):
    try:
       p = person['data']['0']
       return f'{p["id"]}, {p["name"]}, {p["occupation"]}, {[k for k in p["kind"]]}'
    except Exception as e:
        return f"Error: {e}"

async def get_data_non_blocking(url: str, session: aiohttp.ClientSession):
    try:
        session_timeout = aiohttp.ClientTimeout(total=30)
        async with session.get(url, timeout=session_timeout) as response:
            return await response.json()
    except aiohttp.ClientResponseError as e:
        return str(e)

async def get_people():
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1,100):
            tasks.append(asyncio.create_task(get_data_non_blocking(f"{BASE_URL}{str(i)}", session)))
        person_data_list = await asyncio.gather(*tasks)
        for person_data in person_data_list:
            print(get_data(person_data))
            
async def main():
    await get_people()

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Took {end - start:.2f} seconds")