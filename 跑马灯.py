import os
import time
def main():
    content = 'I LOVE YOU '
    while True:
        os.system('cls')#清理屏幕上的输出
        print(content)
        #休眠200ms
        time.sleep(0.2)
        content = content[1:]+content[0]
if __name__ == '__main__':
    main()
