import os
import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=%s' % "GPX_Splitter",
    '--onefile',
    '--windowed',
    os.path.join('main.py'),
])