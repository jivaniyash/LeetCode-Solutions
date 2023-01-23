class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        s = '0'
        m = max(len_a,len_b)
        if len_a == len_b:
            pass
        elif len_a > len_b:
            b = s*(len_a-len_b) + b
        elif len_a < len_b:
            a = s*(len_b-len_a) + a
        f =''
        c = '0'
        x = ['011','110','101']
        y = ['001','100','010']
        for i in range(-1,-m-1,-1):
            if c + a[i] + b[i] in x:
                f = '0' + f
                c = '1'
            elif  c + a[i] + b[i] in y:
                f = '1' + f
                c = '0'
            elif c + a[i] + b[i] == '111':
                f = '1' + f
                c = '1'
            else:
                f = '0' + f
                # c = '0'
        return c + f if c == '1' else f
            

        # c = 0
        # len_a = len(a)
        # for i in range(len_a):
        #     c += int(a[i])* 2**(len_a)
        # c1 = 0
        # len_b = len(b)
        # for i in range(len_b):
        #     c1 += int(b[i])* 2**(len_b)
        # return c+c1