def dfs(party, parties, truth_known, visited):
    # If the party has already been visited, return
    if visited[party]:
        return
    visited[party] = True
    
    # Mark all attendees of the party as knowing the truth
    for attendee in parties[party]:
        truth_known.add(attendee)
    
    # Recursively visit all parties that the attendees have attended
    for i, other_party in enumerate(parties):
        if not visited[i] and any(attendee in truth_known for attendee in other_party):
            dfs(i, parties, truth_known, visited)

def count_valid_parties(N, M, known_truth, party_people):
    truth_known = set(known_truth)
    visited = [False] * M
    
    for i, party in enumerate(party_people):
        # Start DFS for parties that have attendees who know the truth
        if any(person in truth_known for person in party):
            dfs(i, party_people, truth_known, visited)
            
    # Count valid parties
    valid_parties_count = sum(1 for i, party in enumerate(party_people) if not any(person in truth_known for person in party))
    
    return valid_parties_count

# Sample input
N, M = map(int, input().split())
cnt = list(map(int, input().split()))
known_truth = [0]
if len(cnt) != 1:
    known_truth = cnt[1:]
party_people = [list(map(int, input().split()))[1:] for _ in range(M)]
print(count_valid_parties(N, M, known_truth, party_people))
