import asyncio
import aiohttp
import aiofiles
from typing import Any
from bs4 import BeautifulSoup


class AsyncDanbooru:
    def __init__(self, username=None, api_key=None, host="Danbooru"):
        self.__host = host.lower()
        self.__session = aiohttp.ClientSession
        self.__base = f"https://{self.__host}.donmai.us/"
        if username and api_key:
            self.__params = dict(login=username, api_key=api_key)
        else:
            self.__params = dict()

    async def autocomplete(self,
                           query: str = None,
                           _type: str = "tag_query",
                           limit: int = 10
                           ):
        _ad = {
            "search[query]": query,
            "search[type]": _type,
            "limit": limit
        }
        self.__params.update(_ad)
        async with aiohttp.ClientSession() as session:
            _da = await session.get(
                url=self.__base + "autocomplete.json",
                params=self.__params
            )
            return await _da.json()



