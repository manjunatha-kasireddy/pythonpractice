  import pandas as pd
  mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
  }
  myvar = pd.DataFrame(mydataset)
  print(myvar)

  a = [1, 7, 2]
  myvar = pd.Series(a)
  print(myvar)
  print(myvar[0])

  myvar = pd.Series(a, index = ["x", "y", "z"])
  print(myvar)
  print(myvar["y"])

  b = {"day1": 0, "day2": 3, "day3": 2}
  c = pd.Series(b)
  print(c)

  c = pd.Series(b, index = ["day1", "day2"])
  print(c)

  d = {
    "amount": [20, 38, 30, 58, 54, 41],
    "due": [50, 40, 45, 85, 41, 48]
  }
  e = pd.DataFrame(d)
  print(e)

  print(e.loc[0])
  print(e.loc[0:3])

  pd.options.display.max_rows = 5
  f = pd.read_csv('data.csv')

  print(f.to_string())