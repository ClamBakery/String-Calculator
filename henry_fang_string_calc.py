# Henry Fang
# Python 3.7 Anaconda
import re


def add(numbers):
    """
    Takes a string of digit numbers in the form “//[delimiter(s)]\n[delimiter separated numbers]” and returns the sum of
    those numbers as a integer
    :param numbers: A string with a delimiter and a set of digits separated by the delimiter
    :return: An integer that is the sum of the numbers in the input or zero if the input is a empty string
    """
    # Check for empty string
    if numbers == "":
        return 0
    else:
        # Separate the delimiter from the digits to be summed
        delims, numbers_string = get_delimiter(numbers)

        # Split our string by the delimiters
        numbers_list = split_numbers(delims, numbers_string)

        # A list that will hold the non-negative numbers
        numbers_int = []
        # A list that stores any negatives we find
        negative_int = []
        # Check for negatives and values greater than 1000
        for num in numbers_list:
            if num < 0:
                negative_int.append(num)
            elif num > 1000:
                None
            else:
                numbers_int.append(num)

        # Throw exception when a negative value is found
        if len(negative_int) != 0:
            raise ValueError("Negatives not allowed. Negative values: " + "".join([str(number) + " " for number in
                                                                                   negative_int]))

        # Sum the list
        result = sum(numbers_int)

        return result


def get_delimiter(numbers):
    """
    Separate a string into it's delimiter(s) and the numbers separated by the delimiter then return them both
    :param numbers: A string with a delimiter and a set of digits separated by the delimiter(s)
    :return: A tuple where the first item is a list of delimiter(s) and the second is the string of numbers
    separated by the delimiter(s)
    """
    newline_index = numbers.find("\n")

    # Get the delimiter(s)
    delim_string = numbers[2:newline_index]
    delim_list = delim_string.split(",")

    # Get the numbers separated by the delimiter(s)
    numbers_string = numbers[newline_index:]

    return delim_list, numbers_string


def split_numbers(delimiters, num_string):
    """
    Split a string of numbers by some given delimiter(s) and return them as a list of integers
    :param delimiters: A list of delimiter(s)
    :param num_string: A string to be split into integers
    :return: A list of integers obtained by splitting a given string
    """
    # Build a regular expression from the list of delimiters
    delim_expression = ""
    for delim in delimiters:
        # Escape any special characters
        escaped_delim = re.escape(delim)
        delim_expression = delim_expression + escaped_delim + "|"

    # Remove last "|"
    delim_expression = delim_expression[:-1]

    # Split our number string into a list using regex
    numbers_list = re.split(delim_expression, num_string)

    # Strip each value and convert to integer
    numbers_list = [int(num.strip()) for num in numbers_list]

    return numbers_list


#####################################################
# Tests
#####################################################
tests_failed = 0

########################
# Simple delimiter tests
simple_inputs = ["//$\n1$2$5", "//*\n10*30*30\n*5", "//h\n12h\n3h5"]
simple_outputs = [8, 75, 20]

for s_i in range(len(simple_inputs)):
    s_result = add(simple_inputs[s_i])
    if s_result != simple_outputs[s_i]:
        print("Error, add() returned " + str(s_result) + " when " + str(simple_outputs[s_i]) + " was expected")
        tests_failed += 1

########################
# Negative number tests
negative_inputs = ["//$$$\n-1$$$2$$$5", "//$****\n-10$****30$****30", "//%%\n12%%3%%\n-5"]
negative_outputs = [8, 70, 20]

for n_i in range(len(negative_inputs)):
    try:
        n_result = add(negative_inputs[n_i])
    except ValueError:
        print("Successfully threw exception when given negative input(s)")

########################
# Greater than 1000 tests
greater_inputs = ["//$\n1001$2$5", "//$\n10$30000$30", "//%%\n1200\n%%3%%5"]
greater_outputs = [7, 40, 8]

for g_i in range(len(greater_inputs)):
    g_result = add(greater_inputs[g_i])
    if g_result != greater_outputs[g_i]:
        print("Error, when testing for greater length, add() returned " + str(g_result) + " when " +
              str(greater_outputs[g_i]) + " was expected")
        tests_failed += 1
        
########################
# Arbitrary length delimiter tests
arbitrary_inputs = ["//$$$\n1$$$2$$$5", "//$****\n10$****30$****30$****5", "//%%\n12%%3%%5\n"]
arbitrary_outputs = [8, 75, 20]

for a_i in range(len(arbitrary_inputs)):
    a_result = add(arbitrary_inputs[a_i])
    if a_result != arbitrary_outputs[a_i]:
        print("Error, when testing for arbitrary length delimiter, add() returned " + str(a_result) + " when " +
              str(arbitrary_outputs[a_i]) + " was expected")
        tests_failed += 1
        
########################
# Multiple delimiter tests
multiple_inputs = ["//$,*,%\n1$2*5%7", "//#,!\n10#30!30#5", "//@,%\n12%3\n@5"]
multiple_outputs = [15, 75, 20]

for m_i in range(len(multiple_inputs)):
    m_result = add(multiple_inputs[m_i])
    if m_result != multiple_outputs[m_i]:
        print("Error, when testing for multiple delimiters, add() returned " + str(m_result) + " when " +
              str(multiple_outputs[m_i]) + " was expected")
        tests_failed += 1
        
########################
# Multiple, arbitrary length delimiters
multi_arb_inputs = ["//$@@,*$@,%****\n1*$@2%****5$@@7", "//###!,!@!\n10###!30!@!\n30###!5",
                    "//@@@@,%%%%%%%\n12%%%%%%%3\n@@@@5"]
multi_arb_outputs = [15, 75, 20]

for ma_i in range(len(multi_arb_inputs)):
    ma_result = add(multi_arb_inputs[ma_i])
    if ma_result != multi_arb_outputs[ma_i]:
        print("Error, when testing for multiple arbitrary length delimiters, add() returned " + str(ma_result) +
              " when " + str(multi_arb_outputs[ma_i]) + " was expected")
        tests_failed += 1

########################
if tests_failed == 0:
    print("All tests passed")
else:
    print("\n" + str(tests_failed) + " out of " + str(len(simple_inputs) + len(negative_inputs) + len(greater_inputs) +
                                                      len(arbitrary_inputs) + len(multiple_inputs) +
                                                      len(multi_arb_inputs)) + " tests failed")
