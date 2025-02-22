from interface import Interface

if __name__ == '__main__':
    interface = Interface()
    while True:
        truefalse = interface.run()
        if not truefalse:
            print("Closing program.....")
            break
