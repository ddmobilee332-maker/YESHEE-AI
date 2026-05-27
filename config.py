import threading

LOCK = threading.Lock()
KOPECHKA_KEY = 'api_key' # พิกัดดักเมลเดิม: https://www.kopechka.com/

VERSION_LIST = ['32.9.5', '32.7.5', '38.4.3', '38.4.2', '38.4.1', '38.7.1', '38.3.3', '40.8.3']

DOMAINS = [
    "api16-normal-alisg.tiktokv.com",
    "api16-normal-c-alisg.tiktokv.com",
    "api31-normal-alisg.tiktokv.com",
    "api16-normal-c-useast1a.tiktokv.com",
    "api22-normal-c-useast1a.tiktokv.com",
    "api16-normal-c-useast1a.musical.ly",
    "api19-normal-c-useast1a.musical.ly",
    "api.tiktokv.com"
]

COUNTRIES = ['au', 'kz', 'co']
