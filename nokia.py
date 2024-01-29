import hashlib
import base64

def gen(username, productID, key):
    md = hashlib.sha1()
    msg = str(username + productID + key).encode("utf-8")
    md.update(msg)
    digest = md.digest()
    return base64.b64encode(digest).decode("utf-8")

def main():
    prod = input("Product ID -> ")
    key = input("Secret Key -> ")
    uname = input("Username -> ")
    print(f"Serial Number -> {gen(uname, prod, key)}")

if __name__ == '__main__':
    main()