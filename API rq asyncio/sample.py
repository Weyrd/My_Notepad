import asyncio
import aiohttp
import json

import numpy as np
import pandas as pd
import seaborn as sns


class API():

    def __init__(self, loop):
        # asyncio
        self.loop = loop
        self.session = None
        self.ENDPOINT = {
            "franchisehistory": "https://stats.nba.com/stats/franchisehistory?LeagueID=00&Season=2022-23",
            "playersTraditional": "https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2022-23&SeasonSegment=&SeasonType=Regular Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight="
        }

    async def start_session(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv: 106.0) Gecko/20100101 Firefox/106.0",
            "Referer": "https://www.nba.com/",
        }
        self.session = aiohttp.ClientSession(headers=headers)


    async def get_data(self, endpoint):
        # self.connectAmazonEx1()
        print("Geting data")


        async with self.session.get(self.ENDPOINT[endpoint]) as response:
            data = await response.json() 
        
        return data

    
    # save append to json
    def saveJson(self, data):
        print("save json")
        with open('products.json', 'w') as f:
            json.dump(data, f, indent=4)

    # clsoe session
    async def close_session(self):
        await self.session.close()


class Main():

    def __init__(self, api, loop):
        self.api = api
        self.loop = loop

    
    async def start_api_loop(self):
        try: await self.api.start_session()
        except Exception as e: print(f"Error Starting Session : {'```{}: {}```'.format(type(e).__name__, e)}")


    async def get_nba_1(self):
        # Get NBA Data
        try:
            response = await self.api.get_data("franchisehistory")
            await self.do_things_with_data_1(response)

        except Exception as e:print(f"Error : {'```{}: {}```'.format(type(e).__name__, e)}")

    async def run(self):
        await self.start_api_loop()
        await self.get_nba_1()
    
    def quit(self):
        self.loop.run_until_complete(self.api.close_session())
        self.loop.stop()
        self.loop.close()



    async def do_things_with_data_1(self, data):
        print(data)
    


        

# Run
if __name__ == "__main__":
    # new loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    api = API(loop)
    main = Main(api, loop)
    try:
        main.loop.run_until_complete(main.run())
    
    except Exception as e:
        print(f"Error loop : {'```{}: {}```'.format(type(e).__name__, e)}")
    finally:
        main.quit()

