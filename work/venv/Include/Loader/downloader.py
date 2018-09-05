import requests


class Downloader:
    def __init__(self):
        pass
    def __call__(self, url):
        try:
            response = requests.get(url)
        except Exception:
            return {'url': url, 'code': '808','html': ""}
        # return {'html': response.text, 'code': response.status_code}
        return {'url': url, 'code': response.status_code,'html': response.text}