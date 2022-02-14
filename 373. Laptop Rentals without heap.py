def laptopRentals(times):
    start = sorted([x[0] for x in times])
    end = sorted([x[1] for x in times])

    i, j = 0, 0
    rental = 0
    while i < len(times):
        if start[i] >= end[j]:
            rental -= 1
            j += 1
        rental += 1
        i += 1
    return rental
