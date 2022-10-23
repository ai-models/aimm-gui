@REM if exist ldm\Scripts\activate (
@REM   ldm\venv\Scripts\activate & pip3 install -r requirements.txt & pyinstaller.exe main.spec -y
@REM ) else (
@REM   python.exe -m venv ldm & ldm\Scripts\activate & pip3 install -r requirements.txt & pyinstaller.exe main.spec -y
@REM )

pipenv run pyinstaller main.spec -y