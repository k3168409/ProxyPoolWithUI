# encoding: utf-8

from collections import namedtuple

Fetcher = namedtuple('Fetcher', ['name', 'fetcher'])

from .GIthubShiftyTRFetcher import GIthubShiftyTRFetcher
from .GIthubcaliphdevFetcher import GIthubcaliphdevFetcher
from .GIthubHyperBeatsFetcher import GIthubHyperBeatsFetcher
from .GIthubiptotalFetcher import GIthubiptotalFetcher
from .GIthubmertguvencliFetcher import GIthubmertguvencliFetcher
from .GIthubmmpx12Fetcher import GIthubmmpx12Fetcher
from .GIthubofficialputuidFetcher import GIthubofficialputuidFetcher
from .GIthubproxy4parsingFetcher import GIthubproxy4parsingFetcher
from .GIthubprxchkFetcher import GIthubprxchkFetcher
from .GIthubroosterkidFetcher import GIthubroosterkidFetcher
from .GIthubShiftyTRFetcher import GIthubShiftyTRFetcher
from .GIthubtahaluindoFetcher import GIthubtahaluindoFetcher
from .GIthubTheSpeedXFetcher import GIthubTheSpeedXFetcher
from .GIthubyemixzyFetcher import GIthubyemixzyFetcher
from .GIthubZaeem20Fetcher import GIthubZaeem20Fetcher
from .GIthubzuoxiaoleiFetcher import GIthubzuoxiaoleiFetcher

fetchers = [
    Fetcher(name='GIthubShiftyTRFetcher', fetcher=GIthubShiftyTRFetcher),
    Fetcher(name='GIthubcaliphdevFetcher', fetcher=GIthubcaliphdevFetcher),
    Fetcher(name='GIthubHyperBeatsFetcher', fetcher=GIthubHyperBeatsFetcher),
    Fetcher(name='GIthubiptotalFetcher', fetcher=GIthubiptotalFetcher),
    Fetcher(name='GIthubmertguvencliFetcher', fetcher=GIthubmertguvencliFetcher),
    Fetcher(name='GIthubmmpx12Fetcher', fetcher=GIthubmmpx12Fetcher),
    Fetcher(name='GIthubofficialputuidFetcher', fetcher=GIthubofficialputuidFetcher),
    Fetcher(name='GIthubproxy4parsingFetcher', fetcher=GIthubproxy4parsingFetcher),
    Fetcher(name='GIthubprxchkFetcher', fetcher=GIthubprxchkFetcher),
    Fetcher(name='GIthubroosterkidFetcher', fetcher=GIthubroosterkidFetcher),
    Fetcher(name='GIthubShiftyTRFetcher', fetcher=GIthubShiftyTRFetcher),
    Fetcher(name='GIthubtahaluindoFetcher', fetcher=GIthubtahaluindoFetcher),
    Fetcher(name='GIthubTheSpeedXFetcher', fetcher=GIthubTheSpeedXFetcher),
    Fetcher(name='GIthubyemixzyFetcher', fetcher=GIthubyemixzyFetcher),
    Fetcher(name='GIthubZaeem20Fetcher', fetcher=GIthubZaeem20Fetcher),
    Fetcher(name='GIthubzuoxiaoleiFetcher', fetcher=GIthubzuoxiaoleiFetcher),
]
