def add_nums(*args): # * with args can carry n numbers of arguments
    total = 0
    for a in args:
        total += a
    print(total)

add_nums(6)
add_nums(32)
add_nums(3, 36)
add_nums(4, 6, 8, 12, 346346)
