import requests
import sys

def main():
    p = price()

    quiery(p)

def price():
    try:
        f = float(sys.argv[1])
    except ValueError:
        sys.exit('Not a number')
    except IndexError:
        sys.exit('No argument')

    return f


def quiery(f):
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        n = r['bpi']['USD']['rate'].replace(',', '')
        print(f'${float(n) * f:,.4f}')
    except requests.RequestException:
        sys.exit('Request Exception')

if __name__ == '__main__':
    main()