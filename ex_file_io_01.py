# -------------------------------------------------------------
# 파일 입력과 출력 (I/O)
# 스트림 (stream) - 데이터의 흐름, 데이터의 이동 경로
#                 -종류 : 입력 스트림, 출력 스트림
# -------------------------------------------------------------
# with ~ as 구문
# - close 기능 자동 실행
# -------------------------------------------------------------

FILE_NAME='new_year.txt'

# -------------------------------------------------------------
# 파일 쓰기 mode= w : 덮어쓰기
#                a : 이어쓰기
#                x : 기존 파일 있으면 오류 발생
# -------------------------------------------------------------

# with open(FILE_NAME,mode='w',encoding='utf-8') as f:
#    f.write('새해 복 많이 받으세요~ 2023 : 토끼띠\n')
#    f.write('새해 복 많이 받으세요~ 2024 : 용띠\n')
#    f.write('새해 복 많이 받으세요~ 2025 : 뱀띠\n')
#    f.write('새해 복 많이 받으세요~ 2026 : 호랑이띠\n')

# -------------------------------------------------------------
# 파일 읽기 mode= r
# -------------------------------------------------------------

# with open(FILE_NAME,mode='r',encoding='utf-8') as f:
#     print(f.read())

# 파일 복사 함수 -----------------------------------------------
# 조건 : 파일명 끝 부분에 숫자 추가
# 예시 : data.txt -> data_1.txt , data_2.txt
# -------------------------------------------------------------

# 방법2
# with open(FILE_NAME,mode='r',encoding='utf-8') as c:
#     with open(FILE_NAME,mode='a',encoding='utf-8') as f:
#         f.write(c.read())

# 방법1
# def copyFile(filename):
#     # 파일명 만들기
#     _filename=filename.replace('.','_1.')
#     print(f'_filename : {_filename}')
#     # 파일 읽어서 새 파일에 쓰기
#     with open(filename, mode='r',encoding='utf-8')as f:
#         data=f.read()
#     with open(_filename, mode='w',encoding='utf-8')as f:
#         f.write(data)

# copyFile(FILE_NAME)

# 줄마다 숫자 넣는거
def copyFile(filename):
    _filename=filename.replace('.','_1.')
    with open(FILE_NAME,mode='r',encoding='utf-8') as f1:
        with open(FILE_NAME,mode='w',encoding='utf-8') as f2:
            lines=f1.readlines()
            for i in range(1,len(lines)):
                f2.write(f'[{i}]'+lines[i-1])

copyFile(FILE_NAME)