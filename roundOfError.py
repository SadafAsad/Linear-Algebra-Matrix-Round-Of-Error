def matrixInitializer(n, num, data):
    matrix = list()
    counter = 0
    for i in range(n):
        line_data = list()
        matrix.append(line_data)
        # if matrix b
        if num==3:
            line_data.append(data[counter])
            counter+=1
        else:
            for r in range(n):
                line_data.append(data[counter])
                counter+=1
    return matrix

def takingMatrixData():
    _input = input()
    samples = list()
    matrix_num = 1
    while _input!='o':
        _input_str = _input.split()
        _input_length = len(_input_str)
        # if matrix's dimension
        if _input_length==1:
            sample = list()
            samples.append(sample)
            n = int(_input_str[0])
        else:
            # if start of new sample
            if matrix_num==4:
                matrix_num = 1
            _input_list = list()
            i = 0
            while(i<_input_length):
                _input_list.append(float(_input_str[i]))
                i = i + 1
            # matrix initialize
            sample.append(matrixInitializer(n, matrix_num, _input_list))
            matrix_num+=1
        _input = input()
    return samples

def q1(samples):
    counter = 1
    for sample in samples:
        print("Sample " + str(counter) + ": " + str(sample))
        counter+=1
        
ans = takingMatrixData()
q1(ans)
