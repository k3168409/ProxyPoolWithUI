# encoding: utf-8

import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from fetchers.GIthubofficialputuidFetcher import GIthubofficialputuidFetcher

def run():
    fetcher = GIthubofficialputuidFetcher()
    print(fetcher.fetch())

if __name__ == '__main__':
    run()
