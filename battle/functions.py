import csv


def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append(line.split(","))
    # Return list of tuples containing line numbers and lines where string is found

    return list_of_results


def create_data(file_name):
    file = open(file_name, "r")
    data = list(csv.reader(file))
    file.close()
    return data