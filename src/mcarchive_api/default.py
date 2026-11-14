import httpx

def get_authors(x_fields:str="{id,name}",headers:dict={"Accept":"application/json"}) -> list:
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/authors",headers=headers_1)
    return response.json()

def get_game_versions(x_fields:str="{id,name}",headers:dict={"Accept":"application/json"}) -> list:
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/game_versions",headers=headers_1)
    return response.json()
