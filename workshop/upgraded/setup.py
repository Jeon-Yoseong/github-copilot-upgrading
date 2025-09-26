import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup

tests_require = ['pytest']

setup(
    name = "guachi",
    version = "0.0.6",
    packages = ['guachi'],
    include_package_data=True,
    package_data = {
        '': ['distribute_setup.py'],
        },

    # 메타데이터
    author = "Alfredo Deza",
    author_email = "alfredodeza [at] gmail [dot] com",
    description = "전역, 영구 설정을 딕셔너리로 관리",
    long_description = """\
프로젝트가 커지면 전역적으로 접근 가능한 설정 관리자가 필요해집니다.

설정을 딕셔너리로 매핑하는 것은 매우 유용하지만, 메모리 문제를 일으킬 수 있습니다.

**Guachi**는 값을 디스크에 영구적으로 저장할 뿐만 아니라, INI 스타일 키를 딕셔너리 키로 매핑하고, 일부 값이 누락된 경우 기본값을 채워줍니다.

**guachi**가 값을 어떻게 저장하는지 몰라도, 일반 딕셔너리처럼 사용하면 됩니다!

사용자 상호작용
------------------
예를 들어 Twitter 애플리케이션에서 ``ini`` 파일을 사용하는 경우를 가정해봅시다.
다음은 샘플 INI 파일입니다::

    [DEFAULT]

    app.twitter.username = alfredodeza
    app.update.frequency = 60
    app.load.startup = False

username, frequency, startup 옵션이 있습니다.

다음과 같이 사용할 수 있습니다::

    ini_file = ``/Users/alfredo/.twwiter.ini``
    conf = ConfigMapper(config_db_path)
    conf.set_config(ini_file)

이제 **guachi**가 설정 파일을 파싱하고 값을 저장했습니다.

키를 호출해 값을 조회할 수 있습니다::

    >>> db_conf = conf.stored_config()
    >>> db_conf['frequency']
    60

"""
)