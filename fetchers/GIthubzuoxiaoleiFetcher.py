# encoding: utf-8

from .BaseFetcher import BaseFetcher
import requests
class GIthubzuoxiaoleiFetcher(BaseFetcher):
    """
    https://github.com/zuoxiaolei/proxys
    """

    def fetch(self):
        """
        执行一次爬取，返回一个数组，每个元素是(protocol, ip, port)，portocal是协议名称，http,https,socks5
        返回示例：
        72.206.181.97:64943
        72.221.232.152:4145
        """

        urls = {
            "http": "https://github.com/zuoxiaolei/proxys/raw/main/proxys/proxys.txt",
        }
        proxies = []

        for (protocol, url) in urls.items():
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36'
            }
            html = requests.get(url, headers=headers, timeout=10).text
            result = html.split('\n')
            for line in result:
                lines = line.split(":")
                if len(lines) == 2:
                    ip = lines[0].strip()
                    port = lines[1].strip()
                    proxies.append((protocol, ip, int(port)))

        return list(set(proxies))
