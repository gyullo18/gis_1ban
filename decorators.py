
#
# def decorator(func): #받는 인자 - 함수 = 이름이 달라져도 됨
#     def decorated(input_text): #새로운 함수 선언 -- hello_world 인자를 그대로 받아옴
#         print('함수 시작') #함수의 시작과 끝을 꾸며주는거1
#         func(input_text)
#         print('함수 끝')  # 2
#     #꾸며진 함수의 리턴
#     return  decorated
#
# #적용하고자 하는 함수 위에다 @deco -- 함수내용을 바꾸지 않고도 가능 + 중복을 최소화 할 수 있다.
# @decorator
# def hello_world(input_text): #간단한 문자열을 받겠다
#     print(input_text)
# hello_world('Hello World')#받는 인자로 헬로 월드
#
#
# def Decorator(func):
#     def Decorated(a, b):
#         if a >= 0 and b >= 0:
#             return func(a, b)
#         else :
#             raise ValueError('다 양수여야함')
#     return Decorated
# @Decorator
# def tri(a, b):
#     return 1/2*a*b
#
# def sqr(a, b):
#     return a*b
# tri(2,4)
# sqr(2,4)
#
# class User():
#     def __init__(self, auth):
#         self.is_authenticated =auth
# user = User(auth=False) #함수를 실행시키면 permission error가 뜸
#
# r_area = tri(user, 10,10)
# print(r_area)
#     def login_required(func):
#         def decorated(user, a, b):
#             if user.is_authenticated:
#                 return func(user, a, b)
#             else :
#
#





