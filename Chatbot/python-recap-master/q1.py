'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

user_input = input('문자를 입력하세요: ')
# str = str.split(" ")
# 아래에 코드를 작성해 주세요.
print("첫번째 문자는 : ",user_input[0]," 마지막 문자는 : ",user_input[-1])
print("첫번째 문자는 : {} 마지막 문자는 : {}".format(user_input[0],user_input[-1]))