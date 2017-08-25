'''
Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗103+2∗102+3∗101+4∗100
'''
def general_poly(L):
    def apply_to(x):
        poly_sum = 0
        for i in range(len(L)):
            poly_sum += L[i] * x**(len(L) - 1 - i)
        return poly_sum
    return apply_to
