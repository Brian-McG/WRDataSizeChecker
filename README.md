# WRDataSizeChecker
A simple script that checks and alerts when the WRData folder has exceeded the defined limit. A support ticket templete is completed and saved in submissions folder which can then be copied as the body to a ticket.

## Requirements
  - Python 2.7
  - [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)

## Configuration
Edit ```config.py``` with name and keycode before executing to have the script fill in those details automatically, else manually fill in the details in the generated ticket template.
  
## Add to schedule
```schtasks /create /tn "WRDataCheckerTask" /tr "<path to pythonw.exe> <path to WRDataSizeChecker>\main.py" /sc daily /st 17:00:00```
 
