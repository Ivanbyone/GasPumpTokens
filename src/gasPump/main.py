""" """

import os
import json
import asyncio

import aiohttp


class GPRequests:

    GP_LINK_TOKEN_LIST = "https://api.gas111.com/api/v1/tokens/list"

    @classmethod
    async def fetch_gas_pump(cls, session) -> dict | None:
        async with session.get(GPRequests.GP_LINK_TOKEN_LIST, ssl=False) as response:
            try:
                query = await response.json()
                token_info = query[0]
                with open(os.path.abspath("new_token.json")) as f:
                    old_token = json.load(f)
                if old_token.get("ticker") != token_info.get("ticker"):
                    with open(os.path.abspath("new_token.json"), "w") as f:
                        json.dump(token_info, f)
                    result = {
                        "name": token_info.get("name"),
                        "ticker": token_info.get("ticker"),
                        "token_address": token_info.get("token_address"),
                        "image_url": token_info.get("image_url"),
                        "description": token_info.get("description")
                    }
                    return result
                else:
                    result = None
                    return result
            except ValueError:
                result = None
                return result

    @staticmethod
    async def make_regular_requests(interval: int):
        async with aiohttp.ClientSession(trust_env=True) as s:
            while True:
                regular = await GPRequests.fetch_gas_pump(s)
                if regular is not None:
                    return regular
                await asyncio.sleep(interval)
