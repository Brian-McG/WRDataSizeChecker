# WRDataSizeChecker
A simple script that checks and alerts when the WRData folder has exceeded the defined limit. If the limit is exceeded, a support ticket template is created and saved in submissions folder which can then be copied as the body to a ticket.

## Requirements
  - Latest [Python 2.7](https://www.python.org/downloads/)
  - Latest [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/) (Download the latest version for Python 2.7 matching the corresponding architecture [***likely win32***])

## Configuration
Edit ***config.py*** with name and keycode before executing to have the script fill in those details automatically, else manually fill in the details when a ticket template is generated in the *submission* folder.
  
## Add to schedule
Execute the following in ***cmd*** (replacing with the relevant paths) to schedule this script to execute every day:<br>
```schtasks /create /tn "WRDataCheckerTask" /tr "PATH_TO_pythonw.exe PATH_TO_WRDataSizeChecker\main.py" /sc daily /st 17:00:00```

Typical PATH_TO_pythonw.exe: ```C:\Python27\pythonw.exe```<br>
 
