#1. Biggie size
def biggie_size(list):
    new_list = []
    for i in range(len(list)):
        if list[i] > 0:
            new_list.append("big")
        else:
            new_list.append(list[i])
    return new_list
print(biggie_size([-1, 3, 5, -5]))

#2. Count Positives
def count_positives(list):
    sum = 0
    for i in range(len(list)):
        if list[i] > 0:
            sum += 1
        list[len(list) - 1] = sum
    return list
print(count_positives([-1,1,1,1]))

#3. sum total
def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sum_total([1,2,3,4]))

#4. Average
def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum / len(list)
print(average([1,2,3,4]))

#5 Length
def length(list):
    return len(list)
print(length([37,2,1,-9]))

#6. Minimum
def minimum(list):
    min = list[0]
    for i in range(len(list)):
        if len(list) == 0:
            return "False"
        elif list[i] < min:
            min = list[i]
    return min
print(minimum([37,2,1,-9]))

#7 Maximum
def maximum(list):
    max = list[0]
    for i in range(len(list)):
        if len(list) == 0:
            return "False"
        elif list[i] > max:
            max = list[i]
    return max
print(maximum([37,2,1,-9]))

#8. Ultimate Analysis
def ultimate_analysis(list):
    max = list[0]
    min = list[0]
    sum = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
        sum += list[i]
    avg = sum / len(list)
    dic = {"sumTotal:" + str(sum), "average:" + str(avg), "minimum:" + str(min), "maximum:" + str(max), "length:" + str(len(list))}
    return dic
print(ultimate_analysis([37,2,1,-9]))

#9. Reverse list
def reverse_list(list):
    reversed = []
    for i in range(len(list) - 1, -1, -1):
        reversed.append(list[i])
    return reversed
print(reverse_list([37,2,1,-9]))