# APNIC-IPs
A bunch of file including asia-pacific ips and a simple ip grabber.

Only use it for study or scientific researches!

# How-to
You can grab a specific country's whole ip into a format like `192.168.1.0/24` with:  
```
python getips.py CN
```
and a whole asia-pacific's ip use `all`:  
```
python getips.py all
```

This will generates two file including an unformatted apnic file `delegated-apnic-latest` and result file `ipfinal.txt`

# P.S.
The output file can directly put into [zmap](https://github.com/zmap/zmap)

Some output examples can be found in this repository.