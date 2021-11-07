output_a = 52.0
print(output_a)
output_a = "{:g}".format(output_a)
print(output_a)

output_b = "{:g}".format(52.0)
output_c = "{:g}".format(52.00)
print(output_b)
print(output_c)

# 실험
output_a = "{:g}".format(0.0)
output_b = "{:g}".format(50.0)
output_c = "{:g}".format(0.04)
output_d = "{:g}".format(0.20)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

print("# .0 or 0. 형태")
output_f = "{:g}".format(.0)
output_g = "{:g}".format(.50)
output_h = "{:g}".format(53.)
print(output_f)
print(output_g)
print(output_h)

print("# 연산 적용 확인")
a = .5
b = .4
print( a + b )
