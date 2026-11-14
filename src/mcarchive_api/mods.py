import httpx
from urllib.parse import urlencode

def build_query(params: dict) -> str:
    return "?" + urlencode(params)

def get_mods(keyword:str="",game_version:str="",author:str="",x_fields:str="{slug,name}",headers:dict={"Accept":"application/json"}) -> list:
    headers_1 = {
        "X-Fields": x_fields,
    }
    params = {
        "keyword": keyword,
        "game_version": game_version,
        "author": author
    }
    query_str = build_query(params)
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/mods/"+query_str,headers=headers_1)
    return response.json()

def get_mods_by_slug(slug:str,x_fields:str="{}",headers:dict={"Accept":"application/json"}) -> dict:
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/mods/by_slug/"+slug,headers=headers_1)
    return response.json()
