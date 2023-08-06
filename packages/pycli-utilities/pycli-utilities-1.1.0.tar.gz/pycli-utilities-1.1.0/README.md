# PyCLI Utilities <br/>[![Upload Python Package](https://github.com/itsthevp/pycli-utilities/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/itsthevp/pycli-utilities/actions/workflows/python-publish.yml)
- As name suggests, CLI Utilities is the python package containing various CLI utilities to perform various operations on different types on files.

- Every utility has its own sets of configuration options which you can explore by specifying -h or --help after utility's command. 

- This repository is open for everyone. Please feel free to suggest / add more CLI tools to this repository.

# Available Utilities

#### CSV Validator
---
```console
$ csv-validate file [options]
```

This utility is designed to validate CSV file by validating that each row of the CSV file has same number of columns. 


#### CSV NULL Cleaner
---
```console
$ csv-remove-nulls file [options]
```

This utility is designed to remove NULL characters (ascii code: 0) from the CSV file.
This utility basically does the two things:

- Replaces the NULL's with empty string
- Removes the empty or only separator contained rows (if any)


#### CSV Column Remover
---
```console
$ csv-remove-column file column_number [options]
```

This utility is designed to remove specific column from the CSV file.


#### CSV Column Shifter
---
```console
$ csv-shift-column file from_location to_location [options]
```

This utility is designed to shift particular column within the CSV file.


#### CSV Splitter
---
```console
$ csv-split file number_of_records [options]
```

This utility is designed to split the large CSV file into multiple CSV files by number of records.


#### CSV Column Merger
---
```console
$ csv-merge-columns file [options]
```

This utility is designed to merge two or more columns of a CSV file.


#### NDJSON Validator
---
```console
$ ndjson-validate file [options]
```

This utility is designed to validate the NDJSON file.


#### NDJSON Key Remover
---
```console
$ ndjson-remove-key file keyName [options]
```

This utility is designed to remove a particular key (if exists) from all the records of a NDJSON file.


#### NDJSON Key Merger
---
```console
$ ndjson-merge-keys file --keys key1 key2 ... [options]
```

This utility is designed to merge multiple keys of every record of a NDJSON file.