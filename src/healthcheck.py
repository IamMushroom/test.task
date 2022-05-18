import urllib.request
import vars
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(vars.log_dir),
        logging.StreamHandler(sys.stdout)
    ]
)


def url_ok(url):
    try:
        code = urllib.request.urlopen(url).code
        if code < 400:
            logging.info(code)
            status = True
        else:
            logging.error(code)
            status = False
    except:
        logging.critical('Service is not available')
        status = False
    return status


url = f'http://127.0.0.1:{vars.external_port}/'

if url_ok(url):
    sys.exit(0)
else:
    sys.exit(1)
