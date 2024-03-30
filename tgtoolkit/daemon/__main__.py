from asyncio import run,Future
from tomllib import load as decode_toml

from .. import Client

def main():
    async def async_main():
        with open("tgtools.toml", "rb") as fp:
            conf = decode_toml(fp)

        async with Client(API_ID, API_HASH) as client:
            # for key,values in conf.items():
            #     await globals()[key](client, **values)
            await Future()

    try:
        run(async_main())
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

