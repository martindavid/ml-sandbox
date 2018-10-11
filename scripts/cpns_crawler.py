from typing import List, Dict
import requests
from http import HTTPStatus
import json
import uuid
from time import sleep


def crawl_cpns_website():
    """
    
    """
    job_post_list = []

    try:
        for i in range(85000, 135000, 100):
            payload = construct_request_payload(i, 100)
            response = create_request_to_website(payload)

            if response is not None and response.get('data', None) is not None:
                data = response.get('data')
                job_post_list = job_post_list + data
                print(
                    f"Success fetch {len(data)} data, total list {len(job_post_list)}")

            if len(job_post_list) % 30000 == 0:
                dump_to_json_file(job_post_list)
                job_post_list = []

            if len(job_post_list) % 5000 == 0:
                sleep(180)

        dump_to_json_file(job_post_list)
        print(f'Success fetch total {len(job_post_list)} job post from the website')
    except Exception as e:
        print(e)


def dump_to_json_file(list_of_job_post: List[Dict]) -> None:
    try:
        with open(f'result-{uuid.uuid4()}.json', 'w') as f:
            json.dump(list_of_job_post, f)
    except Exception as e:
        print(e)


def create_request_to_website(payload: str):
    url = "https://sscn.bkn.go.id/lowongan/spf"


    headers = {
        'Cookie': "f5_cspm=1234; BIGipServerpool_sscn=184771594.47873.0000; _ga=GA1.3.802880963.1538780153; _gid=GA1.3.1659337965.1538780153",
        'Origin': "https://sscn.bkn.go.id",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Referer': "https://sscn.bkn.go.id/lowongan",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive",
        'Cache-Control': "no-cache",
        'Postman-Token': "03e10029-f3df-4c73-8ea5-29cac73a2bea"
        }

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)

    if response.status_code == HTTPStatus.OK:
        return response.json()
    
    return None

def construct_request_payload(record_start_num: int, length: int) -> str:
    return f"draw=1&columns%5B0%5D%5Bdata%5D=ROWNUM&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=PENDIDIKAN_NM&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=JAB_NM&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=INS_NM&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=JENIS_FORMASI_NM&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=LOKASI_NM&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=JUM_PERJAB&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=JUM_PENDAFTAR&columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=LINK_WEB_INS_DAFTAR&columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start={record_start_num}&length={length}&search%5Bvalue%5D=&search%5Bregex%5D=false&jenisFormasi=&pendidikanFormasi=&instansiFormasi=&jabatanFormasi=&lokasiFormasi="    


if __name__=='__main__':
    crawl_cpns_website()
