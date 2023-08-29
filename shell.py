import requests


def main():
    print(requests.get('https://ip.useragentinfo.com/json').text)


if __name__ == '__main__':
    main()
