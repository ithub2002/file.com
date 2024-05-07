from scipy.stats import f_oneway

p1 = [89,89,88,78,79]
p2 = [93,92,94,89,88]
p3 = [89,88,89,93,90]
p4 = [81,78,81,92,82]

a = f_oneway(p1, p2, p3, p4)
print("Statistics =", a.statistic)
print("Pvalue =", a.pvalue)
