from asyncio import run
from . import Client

async def main():
    async with Client(API_ID, API_HASH) as client:
        pass

if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        pass
