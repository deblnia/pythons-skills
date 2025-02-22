
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    import csv
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records