[Setup]
AppName=ChatGPT
AppVersion=1.0
DefaultDirName={pf}\ChatGPT-CLI

[Files]
Source: "dist\chatgpt.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commonprograms}\ChatGPT-CLI"; Filename: "{app}\chatgpt.exe"

[Run]
Filename: "cmd.exe"; Parameters: "/c setx path ""%path%;{app}"""; Flags: runhidden
