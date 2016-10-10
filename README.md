# WRDataSizeChecker
A simple script that checks and alerts when the monitored database files in WRData folder has exceeded the defined limit. If the limit is exceeded, a support ticket template is created and saved in the ```.wrdatasizechecker``` folder in the user directory (```C:\Users\USER\.wrdatasizechecker``` on Windows 10) which can then be copied as the body to a ticket.

## Download
Get the latest WRDataSizeChecker release from [here](https://github.com/Brian-McG/WRDataSizeChecker/releases/latest).

## Configuration
config.ini can be found in the ```.wrdatasizechecker``` folder in the user directory. Modifying it allows the tool to automatically place your name and keycode into the support ticket template if required. It also allows configuration of the threshold required (in MB) to provide an alert and create the support ticket template.<br>
By default, the tool will run every day at 17:00, this can be modified in task scheduler if necessary.

## Output
Support ticket templates are created in the ```.wrdatasizechecker``` folder in the user directory if the limit has been exceeded.
### Windows alert
***Note:*** *The default alert threshold is 100MB not 5MB as in this example*<br>
![Example image of windows alert](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/example_alert_windows10.jpg)

### Support ticket template
***Note:*** *This is with config.ini unmodified*<br>
![Example support ticket template created](https://github.com/Brian-McG/WRDataSizeChecker/blob/master/examples/example_submission_template.jpg)

## Building
### Requirements
  - Windows
  - Latest [Python 2.7](https://www.python.org/downloads/)
  - Latest [pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/) (Download the latest version for Python 2.7 matching the corresponding architecture [***likely win32***])
