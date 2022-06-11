target_height = int(input())
current_height = target_height - 30
bad_tries = 0
is_fault_too_many_times = False
total_jumps = 0
while True:
    current_jump = int(input())
    total_jumps += 1
    if current_jump <= current_height:
        bad_tries += 1
        if bad_tries == 3:
            is_fault_too_many_times = True
            break
    else:
        if current_height >= target_height:
            break
        current_height += 5
        bad_tries = 0
if is_fault_too_many_times:
    print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")