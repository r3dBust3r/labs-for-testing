from cryptography.fernet import Fernet



def decrypt(key, data):
    if not isinstance(key, bytes):
        key = key.encode()

    if not isinstance(data, bytes):
        data = data.encode()

    fernet = Fernet(key)
    dec_data = fernet.decrypt(data)
    
    return dec_data.decode()


def main():
    key = 'KOjE9QtNlJpeWetkMZPZHDnZbNcfndlmNTncxwLNksg='
    data = 'gAAAAABnr3inYJH2nS-_qIQpCXx7p9xkO8K43zEkbZumrf14zc407mEtwx1gKNuk_XSGMoUggUcLFkdLBI4-8zeCecJKOH1PUVcwcw2GYwz8llePf7UcD9U='

    cipher = decrypt(key, data)

    print(cipher)


if __name__ == '__main__':
    main()