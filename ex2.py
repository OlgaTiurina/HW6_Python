#Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#[12,'sadf',5643] ---> ['sadf'] ,[12,5643]

spis = [12, 'sadf', 5643]
f1 = filter(lambda x: type(x) is str, spis)
f2 = filter(lambda x: type(x) is int, spis)

print(list(f1), list(f2), sep=", ")
