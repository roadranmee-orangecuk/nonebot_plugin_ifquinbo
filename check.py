import requests
from lxml import etree
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def cc() -> str:
    url = 'https://vapi.cc.163.com/video_play_url/361433'
    res_status = requests.get(url=url, headers=headers, timeout=3)
    res_status.encoding = 'utf-8'
    json_status = res_status.text
    dict_status = json.loads(json_status)
    print(dict_status)
    try:
        if dict_status['data'] == 'no live':
            return '没勃，摸了'
    except KeyError:
        url = 'https://cc.163.com/361433/'
        res_title = requests.get(url=url, headers=headers, timeout=3)
        res_title.encoding = 'utf-8'
        html = res_title.text
        hparser = etree.HTMLParser()
        tree = etree.HTML(html, hparser)
        title = tree.xpath(
            '//div[@class="js-onlive-title-normal nick onlive-setting-name"]/text()')[0]
        return '勃了勃了，'+title.replace('【Quin】', '')


if __name__ == '__main__':
    cc()
