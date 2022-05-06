import sys
import hashlib

def main():
    if len(sys.argv) == 1:
        print("Provide the challenge code as parameter:")
        print("python3 netg.py 784019874562340ghjsfdk")
        exit(1)

    resp = sys.argv[1]
    print("Possible keys:")
    print(hashlib.md5(f"{resp}NetGuard3".encode("utf-8")).hexdigest())
    print(hashlib.md5(f"{resp}NetGuard2".encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
