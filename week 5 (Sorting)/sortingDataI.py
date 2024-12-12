def show(list):
  print("\n".join(map(str, list)))
  print()

table = [
  [500, "John", "Smith",
      50, 45, 70],
  [321, "Arnold", "Black",
      55, 80, 60],
  [112, "Adam", "Smith",
      80, 40, 20],
  [440, "Jack", "Black",
      60, 40, 50]
]
print("Original table:")
show(table)

# Example: Sort by first name, in reverse order
print("Example: Sort by first name, in reverse order:")
def fname(record):
  return record[1]
by_fnamerev = sorted(table, key = fname, reverse = True)
show(by_fnamerev)

def lastName(table):
    return table[2]

print("Sort by last name:")
# As above
by_lname = sorted(table, key = lastName)
show(by_lname)

print("Sort by student id:")
# Do you need to use a key?
studentID = lambda table: table[0]
by_id = sorted(table, key = studentID)
show(by_id)

# Sort by first name in reverse alphabetical order, and then by last name in reverse order
print("Sort by first name in reverse, then by last name:")
# Can you use the previous variables?
by_fnamerev_lname = sorted(table, key = lambda x: x[2])
by_fnamerev_lname = sorted(by_fnamerev_lname, key = lambda x: x[1], reverse=True)
show(by_fnamerev_lname)

# Sort by score on first test, then by score on second test, then by score on third test
print("Sort by each score in turn:")
by_scores = sorted(table, key= lambda x : (x[5], x[4], x[3]))
show(by_scores)

print("Sort by total score:")
def totalScore(x):
    return (x[3] + x[4] + x[5])
by_totalscore = sorted(table, key=totalScore, reverse=True)
show(by_totalscore)

print("Sort by first name and then by total score:")
by_fname_totalscore = sorted(table, key=totalScore, reverse=True)
by_fname_totalscore = sorted(by_fname_totalscore, key=lambda x: x[1])
show(by_fname_totalscore)