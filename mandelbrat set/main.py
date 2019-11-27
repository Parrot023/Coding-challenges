from numpy import zeros
import cv2
import matplotlib.pyplot as plt


img = zeros([600,600,1])


width, height, channel = img.shape

def map(X, A, B, C, D):
    new_number = (X-A)/(B-A) * (D-C) + C
    return new_number

map(2, 0,10,0,5)

y_from = -3
y_to = 2
zoom = 0

print("{} out of {} pixels". format(0, width*height))

for x in range(width):
    for y in range(height):

        print("{} out of {} pixels". format(x * y, width*height))
        
        a = map(y, 0, width, -3, 2)
        b = map(x, 0, height, -2.5, 2.5)
        
        ca = a
        cb = b
        
        n = 0
        z = 0
        
        while n < 100:
            n += 1
            aa = a*a - b*b
            bb = 2 * a * b

            a = aa + ca
            b = bb + cb

            if ((a*a + b*b) > 16):
                break

        color = map(n ,0,100, 0,255)
        #print("n",color)

        if n == 100:
            color = 0

        img[x][y] = color




cv2.imwrite("mandelbrat set.png", img)
print("done")

            

