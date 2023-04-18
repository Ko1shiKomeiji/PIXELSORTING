import cv2
import os


def BW(low, high):
    img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
    height = int(img.shape[0])
    length = img.shape[1]
    line = []
    low_border = low
    up_border = high
    data = []
    strg = ''

    for row in range(0, height):
        for column in range(0, length):
            if (img[row, column] > low_border) and (img[row, column] < up_border):
                line.append(255)
            else:
                line.append(0)
        for column in range(0, length):
            img[row, column] = line[column]
        for i in range(0, len(line) - 1):
            if line[i] != line[i + 1]:
                strg += f"{line[i]}1"
            else:
                strg += f"{line[i]}"
        strg += f"{line[len(line) - 1]}"
        data.append(strg)
        line.clear()
        strg = ''
        #print(f"{round((row / height) * 100, 2)}%")

    cv2.imwrite("BW.jpg", img)
    return data


if __name__ == "__main__":
    BW(100, 200)