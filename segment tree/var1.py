n = int(input(''))
rectangles = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input('').split())
    rectangles.append(((x1, y1), (x2, y2)))

m = int(input(''))
points = []
for i in range(m):
    x, y = map(int, input('').split())
    points.append((x, y))

for point in points:
    count = 0
    for rectangle in rectangles:
        if rectangle[0][0] <= point[0] < rectangle[1][0] and rectangle[1][1] > point[1] >= rectangle[0][1]:
            count += 1
    print(count, end=" ")
