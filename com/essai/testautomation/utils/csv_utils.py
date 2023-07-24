import csv


def read_csv(file_name: str, skip_header: bool, delimiter: str):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)

        if skip_header:
            return list(reader)[1:]
        else:
            return list(reader)
