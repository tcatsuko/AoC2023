raw_input = []
f = open("aoc01.txt","rt")
for line in f:
    raw_input += [line[:-1]]
f.close()
total_sum = 0
for line in raw_input:
    num_list = [x for x in line if x.isdigit()]
    calibration_number = int(num_list[0] + num_list[-1])
    total_sum += calibration_number

print("part 1: calibration sum is " + str(total_sum))
total_sum = 0
digit_strings = ["one","two","three","four","five","six","seven","eight","nine"]
digit_mapping = {"one":"1","two":"2", "three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
digits = ["1","2","3","4","5","6","7","8","9"]
for line in raw_input:
    first_digit_index = len(line)
    last_digit_index = -1
    first_digit = ""
    last_digit = ""
    for digit in digit_strings:
        digit_index = line.find(digit)
        if digit_index > -1 and digit_index < first_digit_index:
            first_digit_index = digit_index
            first_digit = digit_mapping[digit]
        digit_index = line.rfind(digit)
        if digit_index > last_digit_index:
            last_digit_index = digit_index
            last_digit = digit_mapping[digit]
    for digit in digits:
        digit_index = line.find(digit)
        if digit_index > -1 and digit_index < first_digit_index:
            first_digit_index = digit_index
            first_digit = digit
        digit_index = line.rfind(digit)
        if digit_index > last_digit_index:
            last_digit_index = digit_index
            last_digit = digit
    calibration = first_digit + last_digit
    total_sum += int(first_digit + last_digit)
print("part 2: calibration value is " + str(total_sum))