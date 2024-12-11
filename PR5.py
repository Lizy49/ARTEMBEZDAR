def RootsCount(A, B, C):
    
    discr = B**2 - 4 * A * C
    
    
    if discr > 0:
        return 2  
    elif discr == 0:
        return 1  
    else:
        return 0  



coefficients = [(1, -3, 2), (1, 2, 1), (1, 0, 1)]

for A, B, C in coefficients:
    root_count = RootsCount(A, B, C)
    print(f'Для уравнения {A}x^2 + {B}x + {C} количество корней: {root_count}')
