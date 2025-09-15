import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

series = pd.Series(data)

print("=========Series 1============")
print(series.head(5))

print("\n=========Series Type============")
print(type(series))

series2 = pd.Series(data, index=[
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"])

print("\n=========Series 2============")
print(series2.tail(7))

data2 = {'a': 10, 'b': 20, 'c': 30}

series3 = pd.Series(data2)

print("\n=========Series 3============")
print(series3.head())


bucket_list = ["Red", "Yellow", "Blue", "Black", "Gray", "Purple", "Gold"]

series4 = pd.Series(bucket_list, index=["A", "B", "C", "D", "E", "F", "G"])
print("\n=========Ex 1============")
print(series4.head(2))

bio_data = {'Name': "Oluwaseyi Egunjobi", "Sex": "M", "Phone": "07034490363"}

series5 = pd.Series(bio_data)
print("\n=========Ex 2============")
print(series5)

data = {
    'Name': ['Chris', 'Ayo', 'Chisom'],
    'Age': [26, 24, 22],
    'Home_Town': ['Benin', 'Ibadan', 'Enugu']
}


df = pd.DataFrame(data)
print("\n=========DataFrame============")
print(df.head())

