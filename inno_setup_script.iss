; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E82C3168-7C9A-4EE5-84D3-6782AC4BFA19}
AppName=WRDataSizeChecker
AppVerName=WRDataSizeChecker
AppPublisherURL=https://github.com/Brian-McG/WRDataSizeChecker
AppSupportURL=https://github.com/Brian-McG/WRDataSizeChecker
AppUpdatesURL=https://github.com/Brian-McG/WRDataSizeChecker
DefaultDirName={pf}\WRDataSizeChecker
DefaultGroupName=WRDataSizeChecker
DisableProgramGroupPage=yes
OutputBaseFilename=WRDataSizeCheckerSetup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\WRDataSizeChecker.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\default_config.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\Microsoft.VC90.CRT.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\msvcm90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\msvcp90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\msvcr90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\python.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\python27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\pywintypes27.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\win32api.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\win32gui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\WRDataSizeChecker.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\bmcge\Documents\WRDataSizeChecker\dist\WRDataSizeChecker\Include\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\WRDataSizeChecker"; Filename: "{app}\WRDataSizeChecker.exe"

[Run]
Filename: "schtasks.exe"; Parameters: "/create /tn WRDataCheckerTask /tr ""\""{app}\WRDataSizeChecker.exe""\"" /sc daily /st 17:00:00"
Filename: "{app}\WRDataSizeChecker.exe"; Flags: shellexec

[UninstallRun]
Filename: "schtasks.exe"; Parameters: "/Delete /TN WRDataCheckerTask /F"

