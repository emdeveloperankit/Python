# logical operators = evaluate  multiple conditions (or, and , not)
# or  = at least one condition must be true
# and = both conditions must be true
# not = inverts the condition (not false, not true)

temp=34
planning=False

if temp >30 or temp <0 or planning:
    print("The outdoor event is cancelled ")
else:
    print("The outdooe event is still scheduled")
