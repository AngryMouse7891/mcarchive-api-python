import httpx

def get_files_by_filename(filename:str,x_fields:str="{}",headers:dict={"Accept":"application/json"}) -> dict:
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/files/by_filename/"+filename,headers=headers_1)
    return response.json()

def get_files_by_hash_sha256(shasum:str,x_fields:str="{}",headers:dict={"Accept":"application/json"}) -> dict:
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/files/by_hash/sha256/"+shasum,headers=headers_1)
    return response.json()
