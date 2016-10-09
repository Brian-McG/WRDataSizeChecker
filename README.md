# WRDataSizeChecker
A simple script that checks and alerts when the monitored database folders in WRData folder has exceeded the defined limit. If the limit is exceeded, a support ticket template is created and saved in the *submissions* folder which can then be copied as the body to a ticket.

## Requirements
  - Windows
  - Latest [Python 2.7](https://www.python.org/downloads/)
  - Latest [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/) (Download the latest version for Python 2.7 matching the corresponding architecture [***likely win32***])

## Download
Get the latest WRDataSizeChecker code from [here](https://github.com/Brian-McG/WRDataSizeChecker/archive/master.zip) and unzip it in the desired location

## Configuration
Edit ***config.py*** in a text editor and modify the name and keycode before executing to have the script fill in those details automatically, else manually fill in the details when a ticket template is generated in the *submission* folder.
  
## Add to schedule
Execute the following in ***cmd*** (replacing with the relevant paths) to schedule this script to execute every day:<br>
```schtasks /create /tn "WRDataCheckerTask" /tr "PATH_TO_pythonw.exe PATH_TO_WRDataSizeChecker\main.py" /sc daily /st 17:00:00```

Typical PATH_TO_pythonw.exe: ```C:\Python27\pythonw.exe```<br>
***cmd*** can be accessed by going to start and typing it.

## Example output
### Windows alert
***Note:*** *The default alert threshold is 100MB not 5MB as in this example*<br>
![Example image of windows alert](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/example_alert_windows10.jpg)

### Support ticket template
***Note:*** *This is with config.py unmodified*<br>
![Example support ticket template created](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/example_submission_template.jpg)



 
