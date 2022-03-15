def selection_sort_asc(a):
	n = len(a)
	for i in range(n):
		mini = i
		for j in range(i + 1, n):
			if a[j] < a[mini]:
				mini = j
		a[i], a[mini] = a[mini], a[i]


a = [10, 9, 8, 7, 6]
selection_sort_asc(a)
print(a)
