import coc
import asyncio

client = coc.Client('nikhilsharmalku@gmail.com', 'password')

async def get_some_player(tag):
    player = await client.get_player(tag)

    print(player.name)
    # alternatively,
    print(str(player))

async def get_five_clans(name):
    players = await client.search_clans(name=name, limit=5)
    for n in players:
        print(n, n.tag)

async def main():
    await get_some_player('tag')
    await get_five_clans('name')
    await client.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())