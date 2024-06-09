#!/usr/bin/python3

def main():
    filterlist = list("abcdefghijklmnopqrstuvwxyz")
    text = input(">>> ")

    for banned in filterlist:
        if banned in text.lower():
            print("no letters allowed!!!!!!!!!")
            main()

    try:
        eval(text)
    except Exception as e:
        print(e)

    main()


if __name__ == "__main__":
    main()
