def calculate_bmi(height, weight):
    print ("Height is " + str(height))
    print ("Weight is " + str(weight))

    bmi = weight/(height*height)
    print (str(bmi))


calculate_bmi(height = 1.73, weight = 57)
