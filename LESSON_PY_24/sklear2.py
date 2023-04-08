#https://www.youtube.com/watch?v=fit-ZAWexZ0&list=PLrCZzMib1e9p6lpNv-yt6uvHGyBxQncEh&index=9

from sklearn.preprocessing import Normalizer

# данные о людях (рост, зарплата, вес)
data = [[178, 500000, 58], 
[130, 5000, 110], 
[190, 100000000, 90]] 

scaler = Normalizer().fit(data)
normalized_data = scaler.transform(data)

print('После нормализации:')
print(normalized_data[:3]) # теперь нет гигантской разницы в значениях признаков


