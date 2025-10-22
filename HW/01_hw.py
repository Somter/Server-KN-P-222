start = int(input("Введіть першу межу: "))
end = int(input("Введіть другу межу: "))
step = int(input("Введіть крок: "))

if step == 0:
    print("Крок не може бути нулем!")
else:
    if start <= end:
        for i in range(start, end + 1, step):
            print(i, end=" ")
    else:
        for i in range(start, end - 1, -abs(step)):
            print(i, end=" ")
