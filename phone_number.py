# 핸드폰 번호 가리기(programmers)
def solution(phone_number):
    # 슬라이싱 활용문제

    # 뒷 번호 4자리 제외하여 '*'로 가리고 뒷번호 4자리와 합치기
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
