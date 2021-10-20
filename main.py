

import PyQt5,threading,time

class Main:
  def __init__(self):
    pass


def run():
    print([i for i in range(0,10)])
    #Alternative way
    for i in range(0,10):
        print(i) # print(f"{i}")
def main():
    run()

if __name__ == "__main__":
    main()
