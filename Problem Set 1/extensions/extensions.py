def main():
    e = input('File Name: ').casefold().strip()
    print(analyze(e))

def analyze(e):
    if f'{e}'.endswith('.gif'):
        return 'image/gif'
    if f'{e}'.endswith('.jpg') or f'{e}'.endswith('.jpeg'):
        return 'image/jpeg'
    if f'{e}'.endswith('.png'):
        return 'image/png'
    if f'{e}'.endswith('.txt'):
        return 'text/plain'
    if f'{e}'.endswith('.pdf'):
        return 'application/pdf'
    if f'{e}'.endswith('.zip'):
        return 'application/zip'
    if f'{e}'.endswith('.bin'):
        return 'application/octet-stream'
    else:
        return 'application/octet-stream'


main()