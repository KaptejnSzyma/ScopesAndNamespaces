def spam1():

    def spam2():

        def spam3():
            z = " even more spam"
            return z

        y = " more spam"
        y += spam3()
        return y

    x = "spam"
    x += spam2()
    return x


print(spam1())