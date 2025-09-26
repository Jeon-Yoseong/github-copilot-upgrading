# upgraded 폴더 파일 구조 설명

이 폴더는 legacy 폴더의 모든 파일과 디렉터리 구조를 그대로 복사한 업그레이드 작업 공간입니다.

## 주요 파일 및 디렉터리

- MANIFEST.in: 패키징에 포함할 파일 목록을 지정합니다.
- README.rst: 프로젝트 및 guachi 라이브러리 설명서입니다.
- distribute_setup.py: setuptools 설치를 위한 부트스트랩 스크립트입니다.
- setup.py: guachi 패키지의 설치 및 메타데이터를 정의합니다.
- docs/: 문서 관련 파일 및 빌드 결과가 들어가는 디렉터리입니다.
- guachi/: 핵심 라이브러리 코드가 들어있는 디렉터리입니다.
  - __init__.py: guachi 패키지 초기화 파일
  - config.py: 설정 관련 코드
  - database.py: 데이터베이스 관련 코드
  - tests/: 테스트 코드 디렉터리
    - test_configmapper.py, test_configurations.py, test_database.py, test_integration.py: 각각의 테스트 스크립트
- guachi.egg-info/: 패키지 정보 및 메타데이터가 저장되는 디렉터리입니다.
  - PKG-INFO, SOURCES.txt, dependency_links.txt, top_level.txt: 패키지 정보 파일

이 구조는 레거시 프로젝트를 최신 Python 환경으로 업그레이드하는 실습 및 테스트를 위한 기반이 됩니다.
