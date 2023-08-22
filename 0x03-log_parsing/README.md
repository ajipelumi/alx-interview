## Log Parsing

### Description
This is a script that reads `stdin` line by line and computes metrics.

### Example
```bash
./0-generator.py | ./0-stats.py 

```

### Files
[0-generator.py](0-generator.py)
[0-stats.py](0-stats.py)

### Explanation
* [0-generator.py](0-generator.py) - This script generates random logs.
* [0-stats.py](0-stats.py) - This script reads `stdin` line by line and computes metrics:
  * `stdin` format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  * After every 10 lines and/or a keyboard interruption (`CTRL + C`), prints these statistics from the beginning:
    * Total file size: `File size: <total size>`
    * where `<total size>` is the sum of all previous `<file size>` (see format above)
    * Number of lines by status code:
      * possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
      * if a status code doesn’t appear, don’t print anything for this status code
      * format: `<status code>: <number>`
      * status codes should be printed in ascending order

First, we import the `sys` module to read from `stdin` and iterate over it line by line.

We then get `file_size` and `status_code` from each line. We then increment the `file_size` and `status_code` in the `status_codes` dictionary.

We then print the `file_size` and `status_codes` dictionary after every 10 lines and/or a keyboard interruption.