import os
import platform
import shutil
import stat
import sys
from urllib.parse import urlparse

import requests
import tqdm

BIN_PATH = os.path.join(os.path.dirname(__file__), 'bin')

FFMPEG_BINARIES = {
    "Linux": {"ffmpeg": "ffmpeg-linux64-v4.1", "ffprobe": "ffprobe-linux64-v4.1"},
    "Darwin": {"ffmpeg": "ffmpeg-osx64-v4.1", "ffprobe": "ffprobe-osx64-v4.1"},
    "Windows": {"ffmpeg": "ffmpeg-win64-v4.1.exe", "ffprobe": "ffprobe-win64-v4.1.exe"}
}


def get_ffmpeg_exe(ffmpeg: bool = True, ffprobe: bool = False):
    localvars = locals().copy()
    exes = [exe for exe in ['ffmpeg', 'ffprobe'] if localvars[exe]]
    for exe in exes:
        if shutil.which(exe):
            continue
        _os = platform.system()
        if not os.path.exists(BIN_PATH):
            os.mkdir(BIN_PATH)
        url = "https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/" + FFMPEG_BINARIES[_os][exe]
        filename = os.path.join(
            BIN_PATH, f"{exe}.exe" if _os == "Windows" else exe
        )
        print(
            f"{exe} was not found! downloading from imageio/imageio-binaries repository."
        )
        try:
            download_file(url, filename)
        except Exception as f:
            shutil.rmtree(BIN_PATH)
            sys.exit(str(f))
        st = os.stat(filename)
        os.chmod(filename, st.st_mode | stat.S_IEXEC)


def download_file(url, filename=None):
    if not filename:
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

    r = requests.get(url, stream=True)
    try:
        file_size = int(r.headers['Content-Length'])
    except KeyError:
        file_size = 1000
    chunk_size = 1024
    num_bars = int(file_size / chunk_size)

    with open(filename, 'wb') as fp:
        for chunk in tqdm.tqdm(
                r.iter_content(chunk_size=chunk_size)
                , total=num_bars
                , unit='KB'
                , desc=filename
                , leave=True
        ):
            fp.write(chunk)
