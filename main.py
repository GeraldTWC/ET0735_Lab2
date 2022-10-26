def calculate_bmi(height, weight):
    print("Height is " + str(height))
    print("Weight is " + str(weight))

    bmi = weight/(height*height)
    print(str(bmi))

    if bmi < 18.5:
        print("Under weight")
    elif 18.5 <= bmi <= 25:
        print("Normal weight")
    else:
        print("Over weight")

calculate_bmi(1.73,57)

