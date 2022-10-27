import statistics as stats

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    a = get_user_input()
    print("The results from get_user_input:", a)
    find_min_max(a)
    print("The results from calc_average:", calc_average(a))
    print ("Temperature arranged in ascending order:", sort_temperature(a))
    print ("The median result is: ", calc_median_temperature(a))

def display_main_menu():
    print("Enter some numbers separated by commas(e.g 5,67,32)")

def get_user_input():
    input_string = input()
    user_list = input_string.split()
    for i in range(len(user_list)):
        # convert each item to int type
        user_list[i] = float(user_list[i])
    return user_list

def calc_average(a):
    return sum(a)/len(a)


def find_min_max(a):
    minimum = min(a)
    maximum = max(a)
    print("The minimum is",minimum)
    print("The maximum is",maximum)
    return minimum, maximum

def sort_temperature(a):
    return sorted(a, reverse=False)

def calc_median_temperature(a):
    return stats.median(a)

if __name__ == "__main__":
    main()

