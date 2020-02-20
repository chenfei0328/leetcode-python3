class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        b = b[2:]

        while len(b) < 32:
            b = '0' + b

        n = b[::-1]
        n = int(n, base=2)
        return n