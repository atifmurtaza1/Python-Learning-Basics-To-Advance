def all_sum(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    return total


result = all_sum(1,2,3)

print(result)