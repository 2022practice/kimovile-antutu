import requests_html

ANTUTU_SCORE_SEL = '.item-antutu > a:nth-child(1) > span:nth-child(2)'
URL = 'https://www.kimovil.com/en/where-to-buy-{}'

def get_mobile_url(mobile_model: str) -> str:
    mobile_model_normalized = mobile_model.lower().replace(' ','-')
    mobile_url = URL.format(mobile_model_normalized)
    return mobile_url

def get_antutu(mobile_model: str,
        ses: requests_html.HTMLSession = requests_html.HTMLSession()) -> int:
    mobile_url = get_mobile_url(mobile_model)
    resp = ses.get(mobile_url)
    antutu_score_str = resp.html.find(ANTUTU_SCORE_SEL, first=True).text
    try:
        antutu_score = int(antutu_score_str.replace('.',''))
    except ValueError:
        antutu_score = None
    return antutu_score


ses = requests_html.HTMLSession()
antutu_score = get_antutu('Samsung Galaxy A71', ses=ses)

