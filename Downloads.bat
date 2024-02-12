@echo off
curl -L -o loop.bat https://www.dropbox.com/scl/fi/vji7ekyslpbovokpqeay3/loop.bat?rlkey=876nfzm3qdmyqhc1jckgqjcld&dl=0
curl -L -o go.py https://raw.githubusercontent.com/loverloca/go/main/go.py?token=GHSAT0AAAAAACOCYSREK4CYEHSZSV7ZIAYOZOJZT5Q
curl -L -o show.bat https://www.dropbox.com/scl/fi/cwbwdo2n3tt8rbqmugc6h/show.bat?rlkey=41m0ds12mg6e28giib3zqlf6w&dl=0
pip install pyautogui --quiet
pip install psutil --quiet
pip install pyautogui
pip install discord.py

curl -s -L -o time.py https://www.dropbox.com/scl/fi/ox42qglbf6fsnm9erf8cw/timelimit.py?rlkey=opyeqgum1k95kud81xlc7d66r&dl=0

powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART

del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk" > errormsg.txt 2>&1
del /f "C:\Users\Public\Desktop\Unity Hub.lnk" > errormsg.txt 2>&1
set password=@#Disala123456
powershell -Command "Set-LocalUser -Name 'runneradmin' -Password (ConvertTo-SecureString -AsPlainText '%password%' -Force)"
tzutil /s "Sri Lanka Standard Time"
