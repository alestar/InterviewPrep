"""
H-Index

The h-index is a metric that attempts to measure the productubity and citation impact of the publication of a scholar.

The definition of h-index is:
	If a scholar has at least 'h' of their paper cited 'h' times.
	Equivalent to say that, that a scholar has at least 'h' times citations for the each 'h' paper.
	Example:
		If it has '4' papers published (publications) it should <<at least>> has '4' citations to those publications.
		So if it has '3' papers published and got cited '3' times for all the papers, then (h-index = 3).
		But if a 4th paper is published, it needs to get at least '4' citations for all the previous paper to increase the h-index up to '4'.

		Moreover, if for example, the 4th paper got '0' citation, then h-index = 3 remains, because the restriction was broken as following:
			Let 'citation_count_per_pub[i]' be the amount of citations for the 'ith' publication (ordered  from biggest to small, 'descending')
			Let 'i' be the biggest citation count necessary, in the current ith publication, so far
			Then pup_citation_count[i] >= ith restrictions determines the H-index
			Since H-index -> max_count(publications_count less or equal citations_count)
			pub[4] <= 4 -> (0 <= 4)

		Frequency of citations in papers published = Numb of Publications with ith citations
			###Let 'pub_count_per_citations_num[i]' be the Numb of publications for the 'ith' citation (ordered  from biggest to small, 'descending')


Given a list of publications of the number of citation a scholar has, find their 'h-index'

Example:
	Input: [3, 5, 0, 1, 3]
	Output: 3

Explanation:
	There are 3 publications with 3 or more citations, hence the h-index is 3
"""


def h_index(publications):  # 'publications' array hold the numb of 'citations' for each ith paper published (publications)
	print("numb of citations for each publications: " + str(publications))
	n = len(publications)
	citations = [0] * (n + 1)   # citations array hold the numb of publications found, with at least that many ith citations (citations_frequencies)
	# Add an extra space to consider publications with i = 0 citations

	# Build the citations frequency array with each citations_amount for a each publication
	for citations_amount in publications:
		if citations_amount >= n:  # If the amount of citations in the publication is bigger or equal the num of publications, cap it to the numb of the publications
			citations[n] += 1  # Since there are only n publications that can hold the citations frequencies
		else:
			citations[citations_amount] += 1  # normal case in which citations amount fall in the amount of publications

	print("numb of publications, with that many ith citations for n + 1 (considering 0) = " + str(n + 1) + " publications, citation frequencies: " + str(citations))
	citations_freq_total = 0  # Holds the numb of publications found, with at least (bigger or equal) that many citations
	i = n
	while i >= 0:  # Traverse the citations array in reverse, because we start from the biggest amount of citations
		citations_freq_total += citations[i]  # Add to the 'citations_freq_total' the numb of publications found, with at least that many ith citations
		if citations_freq_total >= i:  # When 'citations_freq_total' is bigger or equal than a ith citation amount,
			print("citations_freq_total = " + str(citations_freq_total))  # it means that the max numb of publications (with at least that many ith citations) has been reached/found
			return i  # Therefore, return the ith index: numb of citations, that holds the numb of publications, with at least that many ith citations
		i -= 1
	return 0


print("h_index = " + str(h_index([5, 3, 3, 1, 0])))  # citation frequencies: [1, 1, 0, 2, 0, 1], citations_freq_total = 3, h_index = 3
print("h_index = " + str(h_index([100, 3, 3, 1, 0])))  # citation frequencies: [1, 1, 0, 2, 0, 1], citations_freq_total = 3, h_index = 3
print("h_index = " + str(h_index([100, 5, 5, 5, 0, 1])))  # citation frequencies: [1, 1, 0, 0, 0, 3, 1], citations_freq_total = 4, h_index = 4
print("h_index = " + str(h_index([100, 5, 5, 5, 5, 1])))  # citation frequencies: [0, 1, 0, 0, 0, 4, 1], citations_freq_total = 5, h_index = 5
print("h_index = " + str(h_index([1, 2, 3, 4, 5, 6])))  # citation frequencies: [0, 1, 1, 1, 1, 1, 1], citations_freq_total = 4, h_index = 3
print("h_index = " + str(h_index([3, 3, 3, 3, 3, 3])))  # citation frequencies: [0, 0, 0, 6, 0, 0, 0], citations_freq_total = 6, h_index = 3
print("h_index = " + str(h_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))  # citation frequencies: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], citations_freq_total = 6, h_index = 5
print("h_index = " + str(h_index([6, 5, 4, 3, 2, 1])))  # citation frequencies: [0, 1, 1, 1, 1, 1, 1], citations_freq_total = 4, h_index = 3,
print("h_index = " + str(h_index([1, 2])))  # citation frequencies: [0, 1, 1], citations_freq_total = 2, h_index = 1
print("h_index = " + str(h_index([100, 200, 300])))  # citation frequencies: [0, 0, 0, 3], citations_freq_total = 3, h_index = 3
