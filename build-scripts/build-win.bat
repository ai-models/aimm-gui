if exist ldm\Scripts\activate (
  ldm\venv\Scripts\activate & pip3 install -r requirements.txt & pyinstaller.exe main.spec -y
) else (
  python.exe -m venv ldm & ldm\Scripts\activate & pip3 install -r requirements.txt & pyinstaller.exe main.spec -y
)