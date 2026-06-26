def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = ['Paper A', 'Paper B', 'Paper C', 'Paper D']
result = find_paper(papers, 'Paper C')

if result:
    print("Paper found.")
else:
    print("Paper not found.")