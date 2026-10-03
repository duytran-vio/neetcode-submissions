class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patScore = defaultdict(int)
        webByUser = defaultdict(list)

        for i in range(len(username)):
            webByUser[username[i]].append((website[i], timestamp[i]))

        for user, webs in webByUser.items():
            webs.sort(key = lambda web: web[1])
            webSet = set()
            # pattern = [webs[0][0],webs[1][0],webs[2][0]]
            for i in range(len(webs)):
                for j in range(i + 1, len(webs)):
                    for k in range(j + 1, len(webs)):
                        webSet.add((webs[i][0], webs[j][0], webs[k][0]))
            
            for patTuple in webSet:
                patScore[patTuple] += 1

        maxPat = tuple()
        max_score = 0
        for patTuple in patScore:     
            if patScore[patTuple] > max_score or (patScore[patTuple] == max_score and patTuple < maxPat):
                    maxPat = patTuple
                    max_score = patScore[patTuple]
        return list(maxPat)
