import re
import pick
import argparse
import requests
import traceback
import webbrowser


def decode(code: str) -> str:
    result = ''
    i = len(code) / 0x2 - 0x5
    while i >= 0x0:
        result += code[int(i)]
        i = i - 0x2
    i = len(code) / 0x2 + 0x4
    while i < len(code):
        result += code[int(i)]
        i = i + 0x2
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()
    html = requests.get(args.url).text
    links = re.findall(r'>Link (.*):<.*\n?<a href="(.*)" target=', html)
    assert len(links) > 1, 'not found download link'
    _, index = pick.pick(list(map(lambda x:x[0], links)))
    html = requests.get(links[index][1]).text
    codes = re.findall(r'Goroi_n_Create_Button\("(.*)"\);', html)
    assert len(codes) == 1, 'not found download code'
    download_url = 'http://bluemediafiles.com/get-url.php?url={}'.format(decode(codes[0]))
    print(download_url)
    webbrowser.open(download_url)

if __name__ == '__main__':
    try:
        main()
    except AssertionError as e:
        print(e)
    except:
        traceback.print_exc()
        exit(1)
    exit(0)