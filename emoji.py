import emoji
print(emoji.__version__)
def main():
    em= input("Input:")
    y= emoji.emojize(em, language= "alias")
    print(y)

main()