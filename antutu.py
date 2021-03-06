import requests_html
import K


def get_mobile_model_normalized(mobile_model: str) -> str:
     return mobile_model.lower().replace(' ','-')


def get_mobile_url(mobile_model: str) -> str:
    mobile_model_normalized = get_mobile_model_normalized(mobile_model)
    mobile_url = K.URL_TEMPLATE.format(mobile_model_normalized)
    return mobile_url


def get_antutu_score(resp_html: requests_html.HTML,
        antutu_score_sel: str = K.ANTUTU_SCORE_SEL ) -> int:
    antutu_score_text = resp_html.find(antutu_score_sel, first=True).text 
    antutu_score = antutu_score_text.replace('.', '')
    try:
        return int(antutu_score)
    except ValueError:
        return None


def get_antutu_version(resp_html: requests_html.HTML,
        antutu_version_sel: str = K.ANTUTU_VERSION_SEL ) -> str:
    antutu_version = resp_html.find(antutu_version_sel, first=True).text
    if not antutu_version:
        return None
    return antutu_version


def get_mobile_model_resp(mobile_model: str,
        ses: requests_html.HTMLSession = requests_html.HTMLSession(),
        ) -> requests_html.HTMLResponse:
    mobile_url = get_mobile_url(mobile_model)
    return ses.get(mobile_url)


def get_antutu(mobile_model: str,
        version_sel: str = K.ANTUTU_VERSION_SEL,
        score_sel: str = K.ANTUTU_SCORE_SEL,
        ses: requests_html.HTMLSession = requests_html.HTMLSession()) -> int:
    resp = get_mobile_model_resp(mobile_model)
    if resp.reason != 'OK':
        return None
    resp_html = resp.html
    version = get_antutu_version(resp_html, version_sel)
    score = get_antutu_score(resp_html, score_sel)
    antutu = { 'version': version, 'score': score}
    return antutu


if __name__ == '__main__':
    ses = requests_html.HTMLSession()
    sample_mobile_model = 'Samsung Galaxy A71' 
    antutu = get_antutu(sample_mobile_model)
