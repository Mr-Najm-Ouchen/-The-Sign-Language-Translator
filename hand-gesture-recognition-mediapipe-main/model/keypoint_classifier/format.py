import csv
from io import StringIO

raw_data = """"""

# Convert raw data to a file-like object
file_like_object = StringIO(raw_data)


rows = []
reader = csv.reader(file_like_object)

for row in reader:
    if row[0] == '3':
        row[0] = '25'
    rows.append(row)

output_file_like_object = StringIO()
writer = csv.writer(output_file_like_object)
writer.writerows(rows)

modified_csv_data = output_file_like_object.getvalue()

print(modified_csv_data)
