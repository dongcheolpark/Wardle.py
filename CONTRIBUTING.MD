# CONTRIBUTING.MD

### 프로젝트 설정
먼저 프로젝트 디렉토리를 만들어 주시고 프로젝트를 fork 해주신 다음
```shell
$ git init
$ git remote add upstream https://github.com/dongcheolpark/Wordle.py.git
$ git remote add origin https://github.com/{your-personal-repo}/Wordle.py.git
```
필요하시다면 가상환경 설정해주신 후
```shell
$ python -m unittest discover -s tests -p 'Test*.py'
```
를 실행해주시면 테스트 코드 실행할 수 있습니다.

### 기여 방법
먼저 issue를 작성 또는 작성된 issue에서 해야 할 일을 확인 후 브랜치 새로 생성해서 PR 오픈 해 주시면 됩니다.
PR 오픈시에는 PR과 관련된 issue 연결해 주셔야 합니다. 