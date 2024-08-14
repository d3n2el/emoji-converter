import emoji
def main():
    em= input("Input:")
    y= emoji.emojize(em)
    print(y)
    print(type(em))

main()