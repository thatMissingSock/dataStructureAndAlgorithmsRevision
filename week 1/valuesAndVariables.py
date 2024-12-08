"""This isn't really coding as it is a good example of showing you what get's interned and what doesn't. This 'page'
mainly deals with integers and floats."""



x = 2
y = x
z = "3"
w = 2 + 1

a = "hi"
b = a + a
c = b

p = 2
q = "2"
r = 2.0
s = "2.0"

a = -2
b = -1
c = 0
d = 1
e = 2

# ↑ Code goes here
# Please do not modify the following code.
# It shows information about
# everything defined above.

from collections import defaultdict

def aliases():
  addr2vars = defaultdict(lambda : [])
  for varname in globals():
    if varname[:2] != "__" and varname not in {"defaultdict", "aliases"}:
      addr2vars[eval(f"id({varname})")].append(varname)

  print("Aliases:")
  for address in addr2vars:
    vars = ", ". join(addr2vars[address])
    val = eval(addr2vars[address][0])
    if isinstance(val, str):
      val = "'" + val + "'"
    print(vars, "\tAddress ", address, ", Value ", val, sep="")

aliases()