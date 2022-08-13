# whatools
![whatools](https://github.com/lcasan/whatools/blob/main/src/img/screen.png)

This aplication allows the user to access a whole set of feactures that **[WhatsApp](https://web.whatsapp.com)** does not allow by default

## Feactures
- **Send message to multiples groups and users**
  - **send only text**
  - **send only imagen**
  - **send imagen commented with text**
- **Clean chat of groups or users selected**
- **Add tags to groups or user**  

## Compilation
1. Activate virtual enviroment
#### **Windows:**
~~~
env/Scripts/activate
~~~
#### **Linux:**
~~~
source env/bin/activate
~~~

#### **Run:**
~~~ 
pyinstaller run.spec
~~~

#### **.spec file:**
~~~
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
	('env/Lib/site-packages/sv_ttk', 'sv_ttk'),
	('src/img', 'src/img'),
	('src/drives/firefox', 'src/drives'),
	('src/database/model.db', 'src/database')
]

a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
)
~~~

## Author
This program was developed by Luis Miguel Casañ González <<lcasan120100@gmail.com>>
