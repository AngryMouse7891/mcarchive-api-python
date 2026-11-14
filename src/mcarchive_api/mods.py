import httpx
from urllib.parse import urlencode

def build_query(params: dict) -> str:
    return "?" + urlencode(params)

def get_mods(keyword:str="",game_version:str="",author:str="",x_fields:str="{slug,name}",headers:dict={"Accept":"application/json"}) -> list:
    """
    获取模组函数
    Args:
        keyword(str): 关键词
        game_version(str): Minecraft游戏版本
        author(str): 作者
        x_fields(str): 可选字段掩码
        headers(str): 请求头
    Returns:
        json_response(list): 一个列表，返回匹配MC游戏版本、作者、关键词的所有模组，内容取决于x_fields值
    """
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
    json_response=response.json()
    return json_response

def get_mods_by_slug(slug:str,x_fields:str="{}",headers:dict={"Accept":"application/json"}) -> dict:
    """
    根据获取模组函数
    Args:
        slug(str): 必填项，模组ID
        x_fields(str): 可选字段掩码
        headers(str): 请求头
    Returns:
        json_response(list): 一个列表，返回匹配项目ID的模组，内容取决于x_fields值
    """
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/mods/by_slug/"+slug,headers=headers_1)
    json_response=response.json()
    return json_response
