import httpx

def get_files_by_filename(filename:str,x_fields:str="{}",headers:dict={"Accept":"application/json"}) -> dict:
    """
    通过文件名获取文件函数
    Args:
        filename(str): 文件名
        x_fields(str): 可选字段掩码
        headers(str): 请求头
    Returns:
        json_response(list): 一个字典，内容取决于x_fields值
    """
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/files/by_filename/"+filename,headers=headers_1)
    json_response=response.json()
    return json_response

def get_files_by_hash_sha256(shasum:str,x_fields:str="{}",headers:dict={"Accept":"application/json"}) -> dict:
    """
    通过哈希值（sha256算法）获取文件函数
    Args:
        shasum(str): 哈希值（sha256算法）
        x_fields(str): 可选字段掩码
        headers(str): 请求头
    Returns:
        json_response(list): 一个字典，内容取决于x_fields值
    """
    headers_1 = {
        "X-Fields": x_fields,
    }
    headers_1.update(headers)
    response=httpx.get("https://mcarchive.net/api/v1/files/by_hash/sha256/"+shasum,headers=headers_1)
    json_response=response.json()
    return json_response
