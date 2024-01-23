import sympy
w = sympy.symbols('w')
Q_1,Q_2,Q_3 = sympy.symbols('Q_1:4')
w_0 = sympy.symbols('w_0')

Q_1 = 0.5
Q_2 = 1
Q_3 = 10
w_0 = 5

exp1 = sympy.sqrt(1/(1+Q_1**2*(w/w_0-w_0/w)**2))
exp2 = sympy.sqrt(1/(1+Q_2**2*(w/w_0-w_0/w)**2))
exp3 = sympy.sqrt(1/(1+Q_3**2*(w/w_0-w_0/w)**2))

sympy.plot((exp1,(w,0,30)),(exp2,(w,0,30)),(exp3,(w,0,30)))