from validator_collection import validators

def main():
    print(check_email(input('Email Address: ')))

def check_email(email):
    try:
        validators.email(email)
        return 'Valid'
    except:
        return 'Invalid'

if __name__ == '__main__':
    main()