import aiohttp, asyncio, random, requests, socket

def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

async def meme():
    global res
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res =  await r.json()
            return res['data']['children'] [random.randint(0, 25)]['data']['url']

def main():
    global image
    if is_connected("1.1.1.1") == False:
        print('! Internet Connection is not present.')
        exit()
    elif is_connected("1.1.1.1") == True:
        print('> Internet Connection is present, proceeding with program execution.\n')
        pass

    img_url = asyncio.get_event_loop().run_until_complete(meme()) 
    img_data = requests.get(img_url)
    print(img_url)

    try:
        with open(f'reddit_meme.{img_url[-3:]}', 'wb') as handler: handler.write(img_data.content)
        print(f'Meme successfully saved to src/reddit_meme.{img_url[-3:]}')
    except:
        pass

if __name__ == '__main__': main()
