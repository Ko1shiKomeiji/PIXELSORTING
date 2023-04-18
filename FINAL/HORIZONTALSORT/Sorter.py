import random
import BWMaker
import cv2


def main():
    for k in range(0, 10):
        data = BWMaker.BW(100 + k * random.randrange(1, 5), 200 - k * random.randrange(1, 5))
        img = cv2.imread('1.jpg')
        length = img.shape[1]
        line_s = []
        linel = []
        row = 0

        for line in data:
            sort = line.split('1')
            line_len = 0
            for part in sort:
                if '0' in part:
                    for i in range(line_len, line_len + len(part)):
                        linel.append(img[row, i])
                    line_len += len(part)
                else:
                    for i in range(line_len, line_len + (len(part) // 3)):
                        line_s.append(img[row, i])
                    line_len += len(part) // 3
                linel.sort(key= lambda x: x[random.randrange(0,3)])
                line_s += linel
                linel.clear()
            for column in range(0, length):
                img[row, column] = line_s[column - 1]
            line_s.clear()
            row += 1

        cv2.imwrite(f"TESTDEMO\{k}f.jpg", img)
        cv2.imwrite(f"TESTDEMO\{25 - k}f.jpg", img)
        print(f"file #{k} has created!")


main()


