#Time O(n^2) for loop and max, Space: O(n)
def tournamentWinner(competitions, results):
    # Write your code here.
    out = {}
    output = ""
    for i in range(len(competitions)):
        if results[i] == 1:
            if competitions[i][0] not in out:
                out[competitions[i][0]] = 3
            else:
                out[competitions[i][0]] += 3
        else:
            if competitions[i][1] not in out:
                out[competitions[i][1]] = 3
            else:
                out[competitions[i][1]] += 3
                    
    return max(out, key=out.get)

matches = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results = [0, 0, 1]
print(tournamentWinner(matches, results))

#============
#Time O(n) , Space O(k)
def tournamentWinner(competitions, results):
    # Write your code here.
    current_best_team = ""
    out = {current_best_team:0}

    for i in range(len(competitions)):
        winning_team = ''
        if results[i] == 1:
            if competitions[i][0] not in out:
                out[competitions[i][0]] = 3
            else:
                out[competitions[i][0]] += 3
            winning_team = competitions[i][0]	
        else:
            if competitions[i][1] not in out:
                out[competitions[i][1]] = 3
            else:
                out[competitions[i][1]] += 3
            winning_team = competitions[i][1]
        if out[winning_team] > out[current_best_team]:
            current_best_team = winning_team
            
    return current_best_team


matches = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results = [0, 0, 1]
print(tournamentWinner(matches, results))