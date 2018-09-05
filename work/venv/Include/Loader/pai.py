import threading
from downloader import Downloader
import time

def main(max_threads=10):
    # alexa = AlexaCallback()
    downloader = Downloader()
    # urls = alexa()
    urls = ['http://www.baidu.com'] * 100
    thrads =[]

    def down():
        while urls:
            time.sleep(1)
            if len(urls) > 0:
                dict_url = downloader(urls.pop())
            else:
                break

    while urls:
        if len(thrads) < max_threads:
            t = threading.Thread(target=down)
            t.start()
            thrads.append(t)

if __name__ == '__main__':
    main()

