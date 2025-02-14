from cryptography.fernet import Fernet



def encrypt(key, data):
    if not isinstance(key, bytes):
        key = key.encode()

    if not isinstance(data, bytes):
        data = data.encode()

    fernet = Fernet(key)
    enc_data = fernet.encrypt(data)
    
    return enc_data


def main():
    key = 'KOjE9QtNlJpeWetkMZPZHDnZbNcfndlmNTncxwLNksg='
    data = 'H3llo P3Nt3st3r!!'

    cipher = encrypt(key, data)

    print(cipher)


if __name__ == '__main__':
    main()