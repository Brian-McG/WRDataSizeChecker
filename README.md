# WRDataSizeChecker
A simple script for Webroot that checks and alerts when the monitored database files in WRData folder has exceeded the defined limit. If the limit is exceeded, a support ticket template is created which can then be copied as the body to a ticket.

## Download
Get the latest WRDataSizeChecker release from [here](https://github.com/Brian-McG/WRDataSizeChecker/releases/latest).

## Output and Configuration location
All output and configuration files reside in the ```.wrdatasizechecker``` folder which can be found in ```C:\Users\<USERNAME>``` on Windows 10 and ```C:\Documents and Settings\<USERNAME>``` on Windows XP.

## Configuration
*config.ini* can be found in the ```.wrdatasizechecker``` folder in the user directory. Modifying it allows the tool to automatically place your name and keycode into the support ticket template if required. It also allows configuration of the threshold required (in MB) to provide an alert and create the support ticket template.<br>
By default, the tool will run every day at 20:00, this can be modified in task scheduler if necessary.

## Output Examples
### Windows 10 alert
***Note:*** *The default alert threshold is 100MB not 5MB as in this example*<br>
![Example image of windows 10 alert](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/example_alert_windows10.jpg)

### Windows XP alert
***Note:*** *The default alert threshold is 100MB not 20MB as in this example*<br>
![Example image of windows XP alert](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/windows_xp_alert_example.jpg)

### Support ticket template
***Note:*** *This is with config.ini unmodified*<br>
![Example support ticket template created](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/example_submission_template.jpg)

## Building this project
### Requirements
  - Windows
  - Latest [Python 2.7](https://www.python.org/downloads/)
  - Latest [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/) (Download the latest version for Python 2.7 matching the corresponding architecture [***likely win32***])
