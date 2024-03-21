def find_path_to_viewpoint(N):
    # Calculate the floor and room number for the given N
    floor, room_number = 1, 1
    while N > floor:
        N -= floor
        floor *= 2
        room_number *= 2
    
    path = []
    while floor > 0:
        # Append the current room to the path
        path.append(floor * 10**18 + room_number)
        
        # Move to the parent room in the above floor
        floor //= 2
        room_number = -(-room_number // 2)  # ceil division
        
    return path

# Test the function with the provided test cases
cnt = int(input())
test_cases = [int(input()) for _ in range(cnt)]
results = [find_path_to_viewpoint(tc) for tc in test_cases]
print(results)
