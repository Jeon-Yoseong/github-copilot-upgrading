#!python
"""Distribute 설치 부트스트랩

setup.py에서 setuptools를 사용하려면 이 파일을 같은 디렉터리에 두고, 다음 코드를 추가하세요::

    from distribute_setup import use_setuptools
    use_setuptools()

특정 버전의 setuptools가 필요하거나, 다운로드 미러/디렉터리를 지정하려면 use_setuptools()에 옵션을 전달하세요.

이 파일은 스크립트로 실행해 setuptools를 설치/업그레이드할 수도 있습니다.
"""
import os
import sys
import time
import fnmatch
import tempfile
import tarfile
from distutils import log

try:
    from site import USER_SITE
except ImportError:
    USER_SITE = None

try:
    import subprocess
    def _python_cmd(*args):
        args = (sys.executable,) + args
        return subprocess.call(args) == 0
except ImportError:
    def _python_cmd(*args):
        args = (sys.executable,) + args
        if sys.platform == 'win32':
            def quote(arg):
                if ' ' in arg:
                    return '"%s"' % arg
                return arg
            args = [quote(arg) for arg in args]
        return os.spawnl(os.P_WAIT, sys.executable, *args) == 0

DEFAULT_VERSION = "0.6.10"
DEFAULT_URL = "http://pypi.python.org/packages/source/d/distribute/"
SETUPTOOLS_FAKED_VERSION = "0.6c11"

SETUPTOOLS_PKG_INFO = """\
Metadata-Version: 1.0
Name: setuptools
Version: %s
Summary: xxxx
Home-page: xxx
Author: xxx
Author-email: xxx
