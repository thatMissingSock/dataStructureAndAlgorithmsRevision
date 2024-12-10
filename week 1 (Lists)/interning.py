"""This isn't coding per se but explains how interning works, this means that it usually deals with string literals
and functions rather than basic integers and floats."""
# a = "hello"
# b = "hel" + "lo"
# c = b
# #
# a = "hello"
# if len(a) < 9:
#   b = "hello"
# c = b
#
# g = "hello"
# h = "hel"
# i = "lo"
# j = h + i
#
# k = "hello"
# def greet():
#   return "hello"
# l = greet()
#
# m = 2
# n = 1 + 1
# o = 1 + 2
# p = 3
#
# p = 0
# q = 0 + 0
# r = 0.0
# s = 1 // 2
#
# t = 2
# u = 1
# v = u + u
#
# t = 2000
# u = 1000
# v = u + u
#
# a = "2"
# b = 2
# c = int("2")
# d = str(2)

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