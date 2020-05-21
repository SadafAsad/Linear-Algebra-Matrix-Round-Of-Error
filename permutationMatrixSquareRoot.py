import itertools

def zeroMatrix(n):
    matrix = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

def decomposition(n, data_str):
    cycles_list = list()
    for r in range(n):
        cycle = list()
        x = int(data_str[r])
        if x!=-1:
            data_str[r] = -1
            cycle.append(x)
            while x!=r:
                tmp = int(data_str[x])
                data_str[x] = -1
                x = tmp
                cycle.append(x)
            cycles_list.append(cycle)
    return cycles_list

    # for cycle in cycles_list:
    #     cycle.sort()

    # cycles_list.sort()
    # new_cycles_list = list(cycles_list for cycles_list,_ in itertools.groupby(cycles_list))
    # return new_cycles_list

def readDataFromFile(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()
    sample_counter = int(file_lines[0])
    samples = list()
    for i in range(sample_counter):
        index = (2*(i+1))-1
        n = int(file_lines[index])
        one_s = file_lines[index+1].split()
        cycle_list = decomposition(n, one_s)
        samples.append(cycle_list)
    return samples

def hasSqr(cycle_list):
    odd_num = 0
    even_num = 0
    for cycle in cycle_list:
        if len(cycle)%2==0:
            even_num+=1
        else:
            odd_num+=1

    return 0

samples = readDataFromFile("data.in")
print(samples[0])
print(samples[1])
print(samples[2])
print(samples[3])
print(samples[4])
print(samples[5])
print(samples[6])
print(samples[7])
print(samples[8])
# counter = 1
# for sample in samples:
#     if not hasSqr(sample):
#         print("Sample " + str(counter) + " impossible")
#     counter+=1