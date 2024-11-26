"""
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where
edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

"""
def findChampions(n,edges):
    incoming =  [True] * n
    for src,dest in edges:
        incoming[dest] = False

    champion = -1
    championCount = 0

    for team in range(n):
        if  incoming[team]:
            champion = team
            championCount += 1

    if championCount > 1:
        return -1

    return champion


n = 3
edges = [[2, 0], [2, 1]]
print(findChampions(n,edges))