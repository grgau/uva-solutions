import math

epslon = 1e-7
p, q, r, s, t, u = 0, 0, 0, 0, 0, 0

def bisection():
  lo = 0
  hi = 1
  while(lo + epslon < hi):
    x = (lo+hi)/2;
    if f(lo) * f(x) <= 0:
      hi = x
    else:
      lo = x
  return (lo+hi)/2

def f(x):
  return p*math.exp(-x) + q*math.sin(x) + r*math.cos(x) + s*math.tan(x) + t*x*x + u

def main():
  global p, q, r, s, t, u
  while True:
    try:
      p, q, r, s, t, u = map(float, input().split())
      if f(0) * f(1) > 0:
        print("No solution")
      else:
        print("%.4f" % round(bisection(), 4))
    except EOFError:
      break
main()