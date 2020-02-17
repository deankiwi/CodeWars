def hourglassSum(arr):

    hourGlasslst = []
    
    for i in range(4):
        for j in range(4):
            #breakpoint()
            glass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            hourGlasslst.append(glass)

    return(max(hourGlasslst))





matrix = [
[1, 1, 1, 0, 0, 0],
[0,1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0 ,0],
[0, 0, 0, 0, 0 ,0],
[0, 0, 0, 0, 0 ,0]]

print(hourglassSum(matrix))
