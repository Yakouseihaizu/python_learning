# def isDinct(num):
#     string = str(num)
#     if len(string) == 1:
#         return True
#     elif len(string) == 2:
#         if string[1] == string[0]:
#             return False
#         else:
#             return True
#     else:
#         if string[1] == string[0]:
#             return False
#         elif string[1] == string[2]:
#             return False
#         elif string[2] == string[0]:
#             return False
#         else:
#             return True
# re = 0
# for i in range(1,1000):
#     if isDinct(i) and (i%2 == 0):
#         re +=1

# print(re)

# import sympy
# t = sympy.symbols('t')

# Us = 1
# U0 = 0.5
# tau = 1
# uc = Us*(1-sympy.exp(-t/tau))+U0*sympy.exp(-t/tau)

# sympy.plot((uc,(t,0,5)),(U0,(t,-1,0)))
