import cv2

imageA_input_path = 'card1.png'
imageA = cv2.imread(imageA_input_path)
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

steps = 2
a = len(grayA)-steps + 1
b = len(grayA[0]) - steps + 1
grayA_Avg = (a, b)

for x in range(len(grayA)):
    for y in range(len(grayA[0])):
        grayA_Avg[len(grayA)][len(grayA[0])] = grayA[x:x+steps, y:y+steps].mean()
