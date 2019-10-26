def fetch_movies(movies, duration):
    if not movies or len(movies) < 2 or duration < 30:
        return []
    n = len(movies)
    i = 0
    j = n - 1
    result = []
    result_indexes = []
    max_duration = -1

    # movies.sort()
    # print(movies)
    # while i < j:
    #     sum_duration = movies[i] + movies[j]
    #     if sum_duration <= duration - 30:
    #         if sum_duration > max_duration:
    #             result = []
    #             result.append(movies[i])
    #             result.append(movies[j])
    #             max_duration = sum_duration
    #         i += 1
    #     else:
    #         j -= 1

    for i in range(len(movies)):
        for j in range(i + 1, len(movies)):
            sum_duration = movies[i] + movies[j]
            if sum_duration <= duration - 30:
                if sum_duration > max_duration:
                    result = []
                    result_indexes = []
                    result.append(movies[i])
                    result.append(movies[j])
                    result_indexes.append(i)
                    result_indexes.append(j)
                    max_duration = sum_duration
                    # print(result)

    if max_duration == -1:
        return []

    print(result_indexes)
    return result

print(fetch_movies([90, 85, 75, 60, 120, 150, 125], 250))
