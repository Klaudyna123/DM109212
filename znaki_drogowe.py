import pandas

dane = pandas.read_csv("sign_names.csv")
dane2=pandas.read_pickle("train.p")
dane3=pandas.read_pickle("test.p")

print(dane)
print(dane2)
print(dane3)