class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #a = int(a, 2)
        #b = int(b, 2)
        #return bin(a + b)[2:]
        res = ""
        i_a, i_b = len(a) - 1, len(b) - 1
        carry = 0
        while i_a >= 0 or i_b >= 0 or carry:
            bit_a, bit_b = int(a[i_a]) if i_a>=0 else 0, int(b[i_b]) if i_b>=0 else 0
            digit = bit_a ^ bit_b ^ carry
        #    sum_w_carry = carry
        #    if i_a >=0:
        #        sum_w_carry += int(a[i_a])
        #    if i_b >= 0:
        #        sum_w_carry += int(b[i_b])

            #digit = (sum_w_carry) % 2
            res += f"{digit}"
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)
        #    carry = 1 if sum_w_carry > 1 else 0
            i_a -= 1
            i_b -= 1

        if carry != 0:
            res += "1"

        return res[::-1]
    
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))

        return res

    def hammingWeight(self, n: int) -> int:
        # First solution
        res = 0
        i = 0
        while n > 0:
            bit = (1 << i) & n # get value corresponding to i-th bit, for example for the number (11)_10 (11 base 10), the 3rd bit has value 8 (111 = 8 + 2 + 1)
            # if I want the bit value (0, 1) I do 1 & (n >> i)
            res += 1 if bit != 0 else 0
            n -= bit
            i += 1

        return res

        # Using % 2 to get last bit and moving 1 bit at a time
        res = 0
        while n > 0:
            print(n, n%2)
            res += n % 2
            n = n >> 1
        return res


        # Using n & (n-1) to eliminate iterations over the 0 bits, skiping fro set bit to set bit
        res = 0
        while n > 0:
            n = n & (n - 1)
            res += 1
        return res