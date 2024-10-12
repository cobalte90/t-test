import random
import numpy as np
from matplotlib import pyplot as plt

n = int(input( 'Введите желаемый размер выборки: ' ))
rng = np.random.default_rng()

s_1 = rng.normal(size=n)
s_2 = rng.normal(size=n)

sample_1 = [ float(np.round(x,5)) for x in s_1 ]
sample_2 = [ float(np.round(x,5)) for x in s_2 ]


mean_1 = round(sum(sample_1)/len(sample_1), 5)
mean_2 = round(sum(sample_2)/len(sample_2),5)
std_1, std_2 = 0, 0
print('Среднее значение первой выборки :', round(mean_1, 3), '\nСреднее значение второй выборки: ', round(mean_2, 3))

sm = 0
for el in sample_1:
    sm+=(el-mean_1)**2
std_1 = (abs(sm/(len(sample_1)-1)))**0.5
sm = 0
for el in sample_2:
    sm+=(el-mean_2)**2
std_2 = (abs(sm/(len(sample_2)-1)))**0.5

print('Стандартное отклонение первой выборки :', round(std_1, 3), '\nСтандартное отклонение второй выборки: ', round(std_2, 3))

m_1 = (std_1)**2/len(sample_1)
m_2 = (std_2)**2/len(sample_2)

t = abs(mean_1-mean_2) / ( (m_1 + m_2)**0.5 )
t = round(t, 5)
df = len(sample_1)+len(sample_2)-2

plt.hist(sample_1, bins=50, alpha=0.7)
plt.hist(sample_2, bins=50, alpha=0.7)


print('Значение t-критерия: ', t, '\nЧисло степеней свободы:', df)
print('Вы можете рассчитать p-value, введя данные значения здесь: https://pvaluecalculator.io или https://www.socscistatistics.com/pvalues/tdistribution.aspx')
plt.show()
