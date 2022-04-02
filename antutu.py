import requests_html

ANTUTU_SCORE_SEL = '.item-antutu > a:nth-child(1) > span:nth-child(2)'
URL = 'https://www.kimovil.com/en/where-to-buy-samsung-galaxy-a71'

def get_mobile_url(mobile_model: str) -> str:
    # TODO: get this code real!
    return URL

def get_antutu(mobile_model: str,
        ses: requests_html.HTMLSession = requests_html.HTMLSession()) -> int:
    mobile_url = get_mobile_url(mobile_model)
    resp = ses.get(URL)
    antutu_score_str = resp.html.find(ANTUTU_SCORE_SEL, first=True).text
    antutu_score = int(antutu_score_str.replace('.',''))
    return antutu_score


ses = requests_html.HTMLSession()
antutu_score = get_antutu('Samsung Galaxy A71', ses=ses)

