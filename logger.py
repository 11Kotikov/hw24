def log_data_file_add (data):
    with open ('log.json', 'a') as log_writing:
        log_writing.write(data)
def log_data_file_open ():
    with open ('log.json', 'a') as log_reading:
        print (*log_reading.readlines)