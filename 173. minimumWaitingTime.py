def minimumWaitingTime(queries):
    queries.sort()
	out = 0
	for i in range(len(queries)):
		out += sum(queries[:i])
	return out
