
'''
break - breaking / stopping / terminating the loop immediately
control jumps out of the loop

continue - skip an iteration and jump to next iteration

applicable for both the loops - for as well as while

'''
counter = 1
total = 0
while counter <= 10:
    if counter == 5:
        print("Cannot continue further")
        counter += 1
        continue
    print("Counter Value :: " , counter)
    total = total + counter
    # counter = counter + 1
    counter += 1

print("Counter value to terminate the loop ", counter)
print("Total ", total)