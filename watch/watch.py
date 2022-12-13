import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matcher = re.search(r'src=.+', s)
        if 'youtube' in matcher.group(0):
            list = matcher.group(0).replace('src=', '').split(' ')
            url = list[0].split('/')
            link = url[2].strip('www.').replace('be.com', '.be')
            urlend = url[4].strip('<>"')
            if 's' not in url[0]:
                https = url[0].replace(':', 's:').strip('"')
                return f'{https}//{link}/{urlend}'
        else:
            return None
    except:
        return None

    return f'{url[0]}//{link}/{urlend}'.strip('"')


if __name__ == "__main__":
    main()