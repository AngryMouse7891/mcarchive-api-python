import httpx

def get_authors(x_fields:str="{id,name}",headers:dict={"Accept":"application/json"}) -> list:
    """
    获取作者函数
    Args:
        x_fields(str): 可选字段掩码
        headers(str): 请求头
    Returns:
        json_response(list): 一个列表，返回作者ID、名字等内容，内容取决于x_fields值
    """
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/authors",headers=headers_1)
    json_response=response.json()
    return json_response

def get_game_versions(x_fields:str="{id,name}",headers:dict={"Accept":"application/json"}) -> list:
    """
    获取Minecraft游戏版本函数
    Args:
        x_fields(str): 可选字段掩码
        headers(str): 请求头
    Returns:
        json_response(list): 一个列表，返回所有Minecraft版本（MCArchive仅限1.16.3-），内容取决于x_fields值
    """
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/game_versions",headers=headers_1)
    json_response=response.json()
    return json_response
