import Lab2

def test_min_max_Req1():

    input_arr = [1, 2, 3]
    expected = (1, 3)
    result = Lab2.find_min_max(input_arr)
    assert (result == expected)


def test_calc_average_Req2():
    input_arr = [1, 2, 3]
    expected = 2
    result = Lab2.calc_average(input_arr)
    assert (result == expected)

def test_calc_median_temperature_Req3():
    input_arr = [1, 2, 3, 4, 5]
    expected = 3
    result = Lab2.calc_median_temperature(input_arr)

    assert (result == expected)