# WRDataSizeChecker
A simple script that checks and alerts when the WRData folder has exceeded the defined limit

## Requirements
  - Python 2.7 (virtual environment suggested: [link](http://stackoverflow.com/a/23842752))
  - [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)

## Configuration
Edit ```config.py``` with name and keycode before executing
  
## Add to schedule
```schtasks /create /tn "WRDataCheck2" /tr "<path to pythonw.exe> <path to WRDataSizeChecker>\main.py" /sc daily /st 17:00:00```
 
