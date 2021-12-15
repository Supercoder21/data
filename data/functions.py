def mean(x):
    add = 0
    n = len(x)
    for i in x:
        add = add + i
    mean = add/n
    return mean
def median(x):
    num = len(x)
    sort = x.sort()
    if num%2 == 0:
        median1 = x[(num//2)-1]
        median = (median1 + x[(median1+1)-1])/2
        return median
    else:
        median = x[((num//2)+1)-1]
        return median
def sd(x):
    add = 0
    add2 = 0
    n = len(x)
    for i in x:
        add = add + i
    mean = add/n
    for i in range(n):
        x[i] = x[i]-mean
        x[i] = x[i]*x[i]
    for i in x:
        add2 = add2 + i
    variance = add2/n
    sd = variance**0.5
    return sd
def range(x):
    mx = max(x)
    mn = min(x)
    range = mx-mn
    return range
