def file_read_from_head(fname, nlines):
    from intertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('test.txt',2)