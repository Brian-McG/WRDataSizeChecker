# -*- mode: python -*-

block_cipher = None


a = Analysis(['WRDataSizeChecker.py'],
             pathex=['C:\\Users\\bmcge\\Documents\\WRDataSizeChecker'],
             binaries=None,
             datas=[("default_config.ini", "."), ("README.md", "."), ("python.ico", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='WRDataSizeChecker',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='python.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='WRDataSizeChecker', icon='python.ico')
