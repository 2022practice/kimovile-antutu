import requests_html
import K

def get_mobile_url(mobile_model: str) -> str:
    mobile_model_normalized = mobile_model.lower().replace(' ','-')
    mobile_url = K.URL_TEMPLATE.format(mobile_model_normalized)
    return mobile_url


def get_antutu_score(resp_html: requests_html.HTML,
        antutu_score_sel: str = K.ANTUTU_SCORE_SEL ) -> int:
    antutu_score_text = resp_html.find(antutu_score_sel, first=True).text
    antutu_score = antutu_score_text.replace('.', '')
    return int(antutu_score)


def get_antutu_version(resp_html: requests_html.HTML,
        antutu_version_sel: str = K.ANTUTU_VERSION_SEL ) -> str:
    return resp_html.find(antutu_version_sel, first=True).text


def get_antutu(mobile_model: str,
        version_sel: str = K.ANTUTU_VERSION_SEL,
        score_sel: str = K.ANTUTU_SCORE_SEL,
        ses: requests_html.HTMLSession = requests_html.HTMLSession()) -> int:
    mobile_url = get_mobile_url(mobile_model)
    resp_html = ses.get(mobile_url).html
    version = get_antutu_version(resp_html, version_sel)
    score = get_antutu_score(resp_html, score_sel)
    antutu = { 'version': version, 'score': score}
    return antutu


if __name__ == '__main__':
    ses = requests_html.HTMLSession()
    antutu = get_antutu('Samsung Galaxy A71')
