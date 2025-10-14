# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Factorizacion LU

"""
AB = C   ---> A = LU
LUB = C   ---> UB = Z
LZ = C

U: La matriz original
L: La matriz identidad
C: Resultado de la matriz
Z: Vector Z1, Z2, Z3
B: Vector X, Y, Z.

- Hacemos Eliminacion Gaussiana a [UL]
- Hacemos LZ = C. Es decir que tendremos L triangular superior.
- Obtendremos entonces Z sustituyendo en la anterior.
- Ahora con los valores de Z hacemos UB = Z para obtener B.
"""

def create_matrix(columns, rows, value):
    new_list = []
    for row in range(columns):
        new_list.append([value]*rows)
    return new_list


def find_lu(l, u):
    for I in range(3):
        a = u[I][I]
        if a == 0:
            print("La matriz no tiene LU")
            break

        for J in range(I + 1, 3):
            b = u[J][I]
            c = -1 * b / a
            l[J][I] = -1 * c
            t = create_matrix(1, 3, 0)
            for k in range(3):
                t[0][k] = c * u[I][k]

            for k in range(3):
                u[J][k] += t[0][k]


def z_value(z, c, l):
    for row in range(3):
        z[row][0] = c[row][0]
        for column in range(3):
            if row == column:
                break
            z[row][0] -= l[row][column] * z[column][0]


def b_value(b, z, u):
    for i in range(2, -1, -1):
        b[i][0] = z[i][0]
        for j in range(2, -1, -1):
            if i == j:
                b[i][0] = b[i][0] / u[i][j]
                break

            b[i][0] -= u[i][j] * b[j][0]


def factorization_lu(u, c):
    z = create_matrix(3, 1, 0)
    b = create_matrix(3, 1, 0)
    list_l = create_matrix(3, 3, 0)
    list_l[0] = [1, 0, 0]
    list_l[1] = [0, 1, 0]
    list_l[2] = [0, 0, 1]
    find_lu(list_l, u)
    z_value(z, c, list_l)
    print("Resultado: ")
    b_value(b, z, u)
    print("Sencillas: ", b[0][0])
    print("Normales:  ", b[1][0])
    print("De lujo:   ", b[2][0])

"""
Ejemplo: 

    La empresa TEC construirá tres tipos de viviendas: 
    sencilla, normal y de lujo. En un mes se construyen 
    20 viviendas. En la zona norte se tienen 2 proyectos 
    para la construcción de tipo sencillas y uno para 
    viviendas normales, en total se construirán 27 casas 
    habitación. En la zona sur se tiene un proyecto para 
    la construcción de casas sencillas y tres proyectos 
    para la construcción de casas de lujo, en total 
    construirán 19 viviendas. ¿Cuántas viviendas de cada 
    tipo se construirán en el mes en dicha empresa?
    
    x: sencillas
    y: normales
    z: de lujo
"""
#  x + y +  z = 20
# 2x + y +  0 = 27
#  x + 0 + 3z = 19

U = create_matrix(3, 3, 0)
U[0] = [1,  1,  1]
U[1] = [2,  1,  0]
U[2] = [1,  0,  3]

C = create_matrix(3, 1, 0)
C[0] = [20]
C[1] = [27]
C[2] = [19]

factorization_lu(U, C)
