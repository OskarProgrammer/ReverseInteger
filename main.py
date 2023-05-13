class Solution:
    def reverse(self, x: int) -> int:
        
        x = str(x)
        x = list(x)
        if x[0]=="-":
            x = x[1::]
            x.reverse()
            x = "".join(x)
            y = "-"+x
            y = int(y)
            if y < -2**31:
                return 0
            return y
        else:
            x.reverse()
            x = "".join(x)
            x = int(x)
            if x > 2**31-1:
                return 0
            return x