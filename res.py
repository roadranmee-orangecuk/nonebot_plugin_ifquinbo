import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def res_get_try(url: str, proxies: dict, timeout: tuple[int, int] | int, max_try: int) -> requests.Response | None:
    i_try = 0
    while i_try < max_try:
        try:
            res = requests.get(url=url, headers=headers, proxies=proxies, timeout=timeout)
            return res
        except requests.exceptions.RequestException:
            i_try += 1
    return None


def get_html_tree(html: str) -> None:
    tree = etree.HTML(text=html, parser=etree.HTMLParser())
    return tree


def tree_xpath_parse(html: str, xpath_: str) -> list:
    tree = get_html_tree(html=html)
    datas = tree.xpath(xpath_)
    return datas
