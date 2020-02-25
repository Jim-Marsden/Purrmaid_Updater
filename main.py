import urllib.request
import os
import json

json_address = ('https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118983&authkey=AAwfa8P4ZYZ0hG0', "version_info.json")

urls = {
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118950&authkey=AOXCsz7S9kOh0fU' : "Purrmaid.exe",
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118944&authkey=AKuQOGhxUEc_Cdg': 'bz2.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118951&authkey=ANMZAuK-PvGw_mY': 'freetype.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118947&authkey=AI6zKht8UpErUWs': 'libpng16.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118949&authkey=APm_6IC53on83lY': 'sfml-graphics-2.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118945&authkey=AMTKIa1FzG5n4IU': 'sfml-system-2.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118946&authkey=AH1G8wHGX6VoyvI': 'sfml-window-2.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118952&authkey=AJMSGHCQUdOQr9U': 'tgui.dll',
    'https://onedrive.live.com/download?cid=B5984EFBEBCB7914&resid=B5984EFBEBCB7914%21118948&authkey=AGyq2Ac8MHWWOkI': 'zlib1.dll',
    'https://raw.githubusercontent.com/Jim-Marsden/Purrmaid/master/Swifty_Sprite_Sheet3.png' :'Swifty_Sprite_Sheet3.png',
    'https://raw.githubusercontent.com/Jim-Marsden/Purrmaid/master/xubuntu_bg_aluminium.jpg':  'xubuntu_bg_aluminium.jpg',
    'https://raw.githubusercontent.com/Jim-Marsden/Purrmaid/master/TileSet.png': 'TileSet.png',
    'https://raw.githubusercontent.com/Jim-Marsden/Purrmaid/master/swifty3.png': 'swifty3.png',
}

local_json_settings = json.load(open('version_info.json', 'r'))



urllib.request.urlretrieve(json_address[0], F'host.{json_address[1]}')
host_json_settings = json.load(open('host.version_info.json', 'r'))

os.system('mkdir purrmaid')
for url, name in urls.items():
    if local_json_settings[name] == 0 or host_json_settings[name] > local_json_settings[name]:
        print(F'{name} has started downloading', end='...')
        urllib.request.urlretrieve(url, f'purrmaid/{name}')
        print(F'{name} has completed.')
        local_json_settings[name] = host_json_settings[name]

