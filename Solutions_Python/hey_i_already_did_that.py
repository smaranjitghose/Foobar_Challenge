def decimalToBase(dn, db):
    digits = []
    while dn > 0:
        digits.insert(0, str(dn % db))
        dn = dn / db
    return ''.join(digits)


def baseToDecimal(bn, cb):
  n = 0
  for d in str(bn):
    n = cb * n + int(d)
  return n


def getSubtract(x, y, b):
  if b == 10:
    return int(x) - int(y)

  dx = baseToDecimal(x, b)
  dy = baseToDecimal(y, b)
  dz = dx-dy
  return decimalToBase(dz, b)


def solution(n, b):
    arr = []
    while True:
        x = "".join(sorted(str(n), reverse=True))
        y = "".join(sorted(str(n)))
        z = getSubtract(x, y, b)

        zl = len(str(z))
        xl = len(str(x))

        if (zl) != xl:
            z = z * pow(10, (xl-zl))

        for index, item in enumerate(arr):
          if item == z:
            return index + 1
            break
        arr = [z] + arr
        n = z
