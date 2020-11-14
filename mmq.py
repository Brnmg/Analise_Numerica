x = [ 1 , 1.1 , 1.3 , 1.5 , 1.9 , 2.1 ]
y = [ 1.84 , 1.96 , 2.21 , 2.45 , 2.94 , 3.18]

#x = [4 , 4.2, 4.5, 4.7 ,5.1 , 5.5 , 5.9, 6.3 , 6.8 ,7.1]
#y = [102.56 , 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

somaX = 0
somaY = 0
somaX2 = 0
somaXY = 0

for i in range(len(x)):
  somaX += x[i]
print("Somatória de x =", somaX)

for i in range(len(x)):
  somaY += y[i]
print("Somatória de y =", somaY)

for i in range(len(x)):
  somaX2 += ( x[i] * x[i] )
print("Somatória de x² =", somaX2)

for i in range(len(x)):
  somaXY += (x[i]*y[i])
print("Somatória de x * y =", somaXY)

print("Valor de M =", len(x))

a0 = ((somaX2 * somaY) - (somaXY * somaX)) / ((len(x) * (somaX2)) - (somaX * somaX))
print("A0 = ",a0)

a1 = ((len(x) * somaXY) - (somaX * somaY) ) / ((len(x) * somaX2) - (somaX * somaX))
print("A1 = ",a1)

print("A equação da reta é: ", "%.4f" % a1, "x +", "%.4f" % a0)