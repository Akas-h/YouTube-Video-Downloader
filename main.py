import sys
def main():
    if len(sys.argv)<2:
        print("url required")
        return
    url=sys.argv[1]
    print(url)




main()
