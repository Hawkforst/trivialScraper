import requests
import time
import random
import gdown

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)
    time.sleep(random.randrange(1,2)
    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


f = open('text.txt')
long_string = f.readlines()
interesting_strings = []

for item in long_string:
    if 'drive.google' in item:
        interesting_strings.append(item)

print(interesting_strings)
interesting_strings = interesting_strings[0]
interesting_strings = interesting_strings.split('https://web.archive.org/web/20161219093036/')
links = []

for item in interesting_strings:
    if 'drive.google' in item:
        idx = item.find('"')
        links.append(item[:idx])

cntr = 1
for link in links:
    print(link)
    fname = './data/History_' + str(cntr) + '.pdf'
    file_id = link.split('/')[-2]
    print('id:', file_id)
    destination = fname
    url = 'https://drive.google.com/uc?id=' + file_id
    gdown.download(url, fname, quiet=False)
    print('Getting file #', str(cntr))
    cntr += 1
    # dont get caught!
    time.sleep(random.randrange(2,4) + random.random())
