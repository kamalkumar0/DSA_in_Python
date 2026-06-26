def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return papers.index(paper)  # Return the index of the found paper
    return False

papers = ['Paper A', 'Paper B', 'Paper C', 'Paper D']
result = find_paper(papers, 'Paper C')

if result:
    print("Paper found at index:", result)
else:
    print("Paper not found.")