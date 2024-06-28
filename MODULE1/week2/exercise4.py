def del_cost(target):
    return 1


def ins_cost(source):
    return 1


def sub_cost(target, source):
    if target == source:
        return 0
    else:
        return 1

def levenshtein_distance(source: str, target: str):
    M_rows = len(source) + 1
    N_columns = len(target) + 1
    matrix = [[0] * N_columns for _ in range(M_rows)]   

    for i in range(N_columns):
        matrix[0][i] = i
    for i in range(M_rows):
        matrix[i][0] = i


    for i in range(1,M_rows):
        for j in range(1,N_columns):
            matrix[i][j] = min(matrix[i-1][j] + del_cost(source[i-1]), 
                            matrix[i][j-1] + ins_cost(target[j-1]),
                            matrix[i-1][j-1] + sub_cost(source[i-1],target[j-1]))

    return matrix[M_rows-1][N_columns-1]
    

if __name__ == "__main__":
    print(levenshtein_distance("yu","you"))
    print(levenshtein_distance("kitten","sitting"))

