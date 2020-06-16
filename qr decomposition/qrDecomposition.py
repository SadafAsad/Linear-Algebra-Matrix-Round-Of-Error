import math

def readDataFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()

    sample_counter = int(file_lines[0])
    samples = list()

    n = int(file_lines[1])
    m = int(file_lines[2])
    index = 3
    i_sample = 0
    while(True):
        sample = list()

        # initializing a
        a = list()
        j_index = 0
        # add m empty columns
        for j_index in range(m):
            a.append(list())

        # filling a
        j_index = 0
        element_counter = 0
        for element_counter in range(n*m):
            if j_index==m:
                j_index = 0
            a[j_index].append(float(file_lines[index]))
            index+=1
            j_index+=1
        sample.append(a)

        # initializing and filling y
        y = list()
        i_index = 0
        for i_index in range(n):
            y.append(float(file_lines[index]))
            index+=1
        sample.append(y)

        # adding first sample :[a,y]
        samples.append(sample)
        i_sample+=1

        # end of file
        if i_sample==sample_counter:
            break

        n = int(file_lines[index])
        m = int(file_lines[index+1])
        index = index+2

    return samples

def columnNorm(cl):
    summ = 0
    for i in cl:
        summ = summ + (i**2)
    return math.sqrt(summ)

def columnDotProduct(cl1, cl2):
    ans = 0
    count = len(cl1)
    for i in range(count):
        ans = ans+(cl1[i]*cl2[i])
    return ans

def columnMultiply(cl1, scalar):
    cl1_multiplied = list()
    for i in cl1:
        cl1_multiplied.append(i*scalar)
    return cl1_multiplied

def columnMinus(cl1, cl2):
    cl3 = list()
    count = len(cl1)
    for i in range(count):
        cl3.append(cl1[i]-cl2[i])
    return cl3

def calculateU(cl, e):
    return columnMultiply(columnDotProduct(cl, e), e)

def calculateE(u):
    return columnMultiply(u, 1/columnNorm(u))

def QMatrix(a):
    a_len = len(a)
    a_index = 0
    
    e_matrix = list()
    for a_index in range(a_len):
        # u_n calculating
        e_index = 0
        k = a_index
        a_n = a[a_index]
        u = a_n
        while k!=0:
            u = columnMinus( u , columnMultiply( e_matrix[e_index] , columnDotProduct(a_n,e_matrix[e_index]) ) )
            e_index+=1
            k-=1
        
        # e_n filling
        e_matrix.append(calculateE(u))
    
    return e_matrix
        
def RMatrix(a, e):
    a_len = len(a)
    r = list()
    # initializing with zero
    for i in range(a_len):
        r_row = list()
        for j in range(a_len):
            r_row.append(0)
        r.append(r_row)
    
    count = 0
    cycle = 0
    for i in range(a_len):
        while count!=a_len:
            r[i][count] = columnDotProduct(a[count], e[i])
            count+=1
        cycle+=1
        count = cycle

    return r

print(RMatrix([[1,1,0], [1,0,1], [0,1,1]], QMatrix([[1,1,0], [1,0,1], [0,1,1]])))
