# Pandas DataFrame Operations 8 times faster (or even more)

DataFrame.query has never worked for me. On my PC, it has been extremely slow when using small DataFrames, and only a little bit, if at all, faster when using huge DataFrames. 

DataFrame.query uses pd.eval, and pd.eval uses numexpr. The weird thing is that numexpr is insanely fast when it is used against a DataFrame, but nor pd.eval neither DataFrame.query aren’t. First I thought there was a problem with my Pandas/environment configuration, but then I read on the[ Pandas page](https://pandas.pydata.org/docs/user_guide/indexing.html#performance-of-query):

_You will only see the performance benefits of using the numexpr engine with DataFrame.query() if your frame has more than approximately 200,000 rows._

Well, **a_pandas_ex_numexpr** adds different methods to the DataFrame/Series classes, and will get tremendous speed-ups **(up to 8 times faster in my tests)** even for small DataFrames. All tests were done using: [https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv](https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv)

**Let the numbers speak for themselves**

## How to import / use a_pandas_ex_numexpr

```python
from a_pandas_ex_numexpr import pd_add_numexpr
pd_add_numexpr()
import pandas as pd
dafra = "https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv"
df = pd.read_csv(dafra)



df
Out[3]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[891 rows x 12 columns]
```

## Speed test - a_pandas_ex_numexpr

```python
# Code explanation at the end of the page
wholedict = {'c': df.Pclass}
%timeit df['Survived'].ne_query('b * 99.5 / 000.1 + 42123.323211 / 1335523.42232 * c', return_np=True, local_dict=wholedict)
30.8 µs ± 229 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'].ne_query('b * 99.5 / 000.1 + 42123.323211 / 1335523.42232 * c', return_np=False, local_dict=wholedict)
70.1 µs ± 2.44 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'] * 99.5 / 000.1 + 42123.323211 / 1335523.42232 * df['Pclass']
262 µs ± 4.25 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
%timeit pd.eval("df.Survived * 99.5 / 000.1 + 42123.323211 / 1335523.42232 * df.Pclass") #used by df.query
1.37 ms ± 45.4 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


df['Survived'].ne_query('b * 99.5 / 000.1 + 42123.323211 / 1335523.42232 * c', return_np=False, local_dict=wholedict)
Out[33]: 
0        0.094622
1      995.031541
2      995.094622
3      995.031541
4        0.094622
          ...    
886      0.063081
887    995.031541
888      0.094622
889    995.031541
890      0.094622
Length: 891, dtype: float64


df['Survived'] * 99.5 / 000.1 + 42123.323211 / 1335523.42232 * df['Pclass']
Out[34]: 
0        0.094622
1      995.031541
2      995.094622
3      995.031541
4        0.094622
          ...    
886      0.063081
887    995.031541
888      0.094622
889    995.031541
890      0.094622
Length: 891, dtype: float64
```

```python
wholedict = {'c': df.Pclass}
%timeit df['Survived'].ne_query('b * 99.5 * c', return_np=True, local_dict=wholedict)
27 µs ± 245 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'].ne_query('b * 99.5 * c', return_np=False, local_dict=wholedict)
65.7 µs ± 1.65 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'] * 99.5 * df['Pclass']
140 µs ± 5.46 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit pd.eval("df.Survived * 99.5 * df.Pclass")
916 µs ± 7.1 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
wholedict = {'c': df.Pclass}
%timeit df['Survived'].ne_query('b / c', return_np=True, local_dict=wholedict)
26.5 µs ± 200 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'].ne_query('b / c', return_np=False, local_dict=wholedict) # returns a Series
60.3 µs ± 336 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'] / df['Pclass']
68.2 µs ± 599 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit pd.eval("df.Survived / df.Pclass")
929 µs ± 31.7 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

## All functions/methods

## Speed of some “ready to use methods” for Series

```python
%timeit df.loc[df.PassengerId.ne_less_than(100)]
142 µs ± 412 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId <100]
212 µs ± 897 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
%timeit df.loc[df.Survived.ne_not_equal(0)]
157 µs ± 390 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.Survived!=0]
229 µs ± 1.46 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
%timeit df.loc[df.PassengerId.ne_greater_than(100)]
174 µs ± 375 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId>100]
248 µs ± 2.26 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
%timeit df.loc[df.PassengerId.ne_equal(1)]
138 µs ± 626 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId == 1]
209 µs ± 1.04 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
%timeit df.loc[df.Cabin.ne_search_for_string_contains('C1')]
329 µs ± 1.18 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
%timeit df.loc[df.Cabin.str.contains('C1',na=False)]
403 µs ± 924 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
%timeit df.loc[df.PassengerId.ne_greater_than_or_equal_to(100)]
175 µs ± 832 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId>=100]
251 µs ± 2.77 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
%timeit df.loc[df.PassengerId.ne_less_than_or_equal_to(100)]
145 µs ± 1.82 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId <=100]
212 µs ± 1.63 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
##############################################################
```

## Overview - all methods for DataFrames/Series

```python
# Always use 'b' as the variable for the Series/DataFrame
df.ne_search_in_all_columns('b == 1')
array([  0,   1,   2,   3,   8,   9,  10,  11,  15,  17,  19,  21,  22,
        23,  25,  28,  31,  32,  36,  39,  43,  44,  47,  52,  53,  55,
        56,  58,  61,  65,  66,  68,  74,  78,  79,  81,  82,  84,  85,
        88,  97,  98, 106, 107, 109, 123, 125, 127, 128, 133, 136, 141,
       142, 146, 151, 156, 161, 165, 166, 172, 183, 184, 186, 187, 190,
       192, 193, 194, 195, 198 ...]
```

```python
    # Returns duplicated index if the value is found in
    # several columns. Exceptions will be ignored
    # the dtype argument is useful when searching for
    # strings -> dtype='S' (ascii only)
    df.ne_search_in_all_columns('b == "1"', dtype='S')

array([  0,   1,   2,   3,   8,   9,  10,  11,  15,  17,  19,  21,  22,
        23,  25,  28,  31,  32,  36,  39,  43,  44,  47,  52,  53,  55,
        56,  58,  61,  65,  66,  68,  74,  78,  79,  81,  82,  84,  85,
        88,  97,  98, 106, 107, 109, ...]
```

```python
    # Converts all columns to  dtype='S' before searching
    # Might not work with special characters
    # UnicodeEncodeError: 'ascii' codec can't encode character '\xe4' in position 0:
    df.ne_search_string_allhits_contains('C1')
Out[6]: 
     PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
3              4         1       1  ...   53.1000  C123         S
11            12         1       1  ...   26.5500  C103         S
110          111         0       1  ...   52.0000  C110         S
137          138         0       1  ...   53.1000  C123         S
268          269         1       1  ...  153.4625  C125         S
273          274         0       1  ...   29.7000  C118         C
298          299         1       1  ...   30.5000  C106         S
331          332         0       1  ...   28.5000  C124         S
351          352         0       1  ...   35.0000  C128         S
449          450         1       1  ...   30.5000  C104         S
452          453         0       1  ...   27.7500  C111         C
571          572         1       1  ...   51.4792  C101         S
609          610         1       1  ...  153.4625  C125         S
669          670         1       1  ...   52.0000  C126         S
711          712         0       1  ...   26.5500  C124         S
712          713         1       1  ...   52.0000  C126         S
889          890         1       1  ...   30.0000  C148         C
[17 rows x 12 columns]
```


```python
# Series doesn't return duplicated results
df.Cabin.ne_search_string_allhits_contains('C1')
Out[9]: 
3      C123
11     C103
110    C110
137    C123
268    C125
273    C118
298    C106
331    C124
351    C128
449    C104
452    C111
571    C101
609    C125
669    C126
711    C124
712    C126
889    C148
Name: Cabin, dtype: object

%timeit df.Cabin.ne_search_string_allhits_contains('C1')
274 µs ± 2.74 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

%timeit df.Cabin.loc[df.Cabin.str.contains('C1', na=False)]
351 µs ± 1.16 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# All rows where the string/substring C1 is found.
# Numbers are converted to string (ascii)
df.ne_search_string_dataframe_contains('C1')
Out[13]: 
     PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
3              4         1       1  ...   53.1000  C123         S
11            12         1       1  ...   26.5500  C103         S
110          111         0       1  ...   52.0000  C110         S
137          138         0       1  ...   53.1000  C123         S
268          269         1       1  ...  153.4625  C125         S
273          274         0       1  ...   29.7000  C118         C
298          299         1       1  ...   30.5000  C106         S
331          332         0       1  ...   28.5000  C124         S
351          352         0       1  ...   35.0000  C128         S
449          450         1       1  ...   30.5000  C104         S
452          453         0       1  ...   27.7500  C111         C
571          572         1       1  ...   51.4792  C101         S
609          610         1       1  ...  153.4625  C125         S
669          670         1       1  ...   52.0000  C126         S
711          712         0       1  ...   26.5500  C124         S
712          713         1       1  ...   52.0000  C126         S
889          890         1       1  ...   30.0000  C148         C
[17 rows x 12 columns]


df.ne_search_string_dataframe_contains('610')
Out[14]: 
     PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
194          195         1       1  ...   27.7208    B4         C
609          610         1       1  ...  153.4625  C125         S
[2 rows x 12 columns]
```

```python
# Converts all columns to ascii and searches in each column
# For each presence in a column, you  get a duplicate of the index
df.ne_search_string_dataframe_allhits_equal('1')
df.ne_search_string_dataframe_allhits_equal('1')
Out[15]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
1              2         1       1  ...  71.2833   C85         C
1              2         1       1  ...  71.2833   C85         C
..           ...       ...     ...  ...      ...   ...       ...
887          888         1       1  ...  30.0000   B42         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
889          890         1       1  ...  30.0000  C148         C
[886 rows x 12 columns]
```

```python
# All equal strings in a Series
df.Embarked.ne_search_string_dataframe_allhits_equal('S')
 Out[16]: 
0      S
2      S
3      S
4      S
6      S
      ..
883    S
884    S
886    S
887    S
888    S
Name: Embarked, Length: 644, dtype: object

%timeit df.Embarked.ne_search_string_dataframe_allhits_equal('S')
160 µs ± 2.14 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.Embarked.loc[df.Embarked=='S']
178 µs ± 3.04 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

```python
# Converts the whole df to ascii and checks where the
# the value is present. Exceptions are ignored
df.ne_search_string_dataframe_equal('C123')
Out[20]: 
     PassengerId  Survived  Pclass  ...  Fare Cabin  Embarked
3              4         1       1  ...  53.1  C123         S
137          138         0       1  ...  53.1  C123         S
[2 rows x 12 columns]
```

```python
# Might not be efficient (The only method that was slower during testing)!  
%timeit df.Cabin.loc[df.Cabin.ne_search_for_string_series_equal('C123')]
252 µs ± 1.02 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
%timeit df.Cabin.loc[df.Cabin=='C123']
158 µs ± 1.28 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

Out[21]: 
     PassengerId  Survived  Pclass  ...  Fare Cabin  Embarked
3              4         1       1  ...  53.1  C123         S
137          138         0       1  ...  53.1  C123         S
[2 rows x 12 columns]
```

```python
# Returns bool values
df.loc[df.ne_search_for_string_contains('C1')]
Out[7]: 
array([[False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False, False, False],
       ...,
       [False, False, False, ..., False, False, False],
       [False, False, False, ..., False,  True, False],
       [False, False, False, ..., False, False, False]])
```

```python
# returns Bool
df.loc[df.Cabin.ne_search_for_string_contains('C1')]

Out[14]: 
     PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
3              4         1       1  ...   53.1000  C123         S
11            12         1       1  ...   26.5500  C103         S
110          111         0       1  ...   52.0000  C110         S
137          138         0       1  ...   53.1000  C123         S
268          269         1       1  ...  153.4625  C125         S
273          274         0       1  ...   29.7000  C118         C
298          299         1       1  ...   30.5000  C106         S
331          332         0       1  ...   28.5000  C124         S
351          352         0       1  ...   35.0000  C128         S
449          450         1       1  ...   30.5000  C104         S
452          453         0       1  ...   27.7500  C111         C
571          572         1       1  ...   51.4792  C101         S
609          610         1       1  ...  153.4625  C125         S
669          670         1       1  ...   52.0000  C126         S
711          712         0       1  ...   26.5500  C124         S
712          713         1       1  ...   52.0000  C126         S
889          890         1       1  ...   30.0000  C148         C
[17 rows x 12 columns]


%timeit df.loc[df.Cabin.ne_search_for_string_contains('C1')]
329 µs ± 1.18 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
%timeit df.loc[df.Cabin.str.contains('C1',na=False)]
403 µs ± 924 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# Returns the index of all rows where the value was found.
# Exceptions (e.g. wrong datatype etc.) are ignored.
# duplicates (more positive results in one row) are not deleted
df.ne_equal_df_ind(1)
array([  0,   1,   2,   3,   8,   9,  10,  11,  15,  17,  19,  21,  22,
        23,  25,  28,  31,  32,  36,  39,  43,  44,  47,  52,  53,  55,
        56,  58,  61,  65,  66,  68,  74,  78,  79,  81,  82,  84,  85,
        88,  97,  98, 106, 107, 109, 123...]
```

```python
# You can pass dtype='S' to convert the values to string 
# (or other formats) before performing the search.
# df.ne_equal_df_ind(b'1', 'S')
# If you use 'S', you have to pass a binary value
df.ne_equal_df_ind(b'1', 'S')
Out[16]: 
array([  0,   1,   2,   3,   8,   9,  10,  11,  15,  17,  19,  21,  22,
        23,  25,  28,  31,  32,  36,  39,  43,  44,  47,  52,  53,  55,
        56,  58,  61,  65,  66,  68,  74,...]
```

```python
# same as DataFrame.ne_equal_df_ind
# but deletes all duplicates
df.ne_equal_df_ind_no_dup(b'1', 'S')
array([  0,   1,   2,   3,   6,   7,   8,   9,  10,  11,  13,  15,  16,
        17,  18,  19,  21,  22,  23,  24,  25,  27,  28,  30,  31,  32,
        34,  35,  36,  39,  40,  41,  43,  44
```

```python
# Same as DataFrame.ne_equal_df_ind,
# but returns the DataFrame (df.loc[])
df.ne_equal_df_dup(b'1', 'S')
Out[18]: 
     PassengerId  Survived  Pclass  ...      Fare Cabin  Embarked
0              1         0       3  ...    7.2500   NaN         S
1              2         1       1  ...   71.2833   C85         C
2              3         1       3  ...    7.9250   NaN         S
3              4         1       1  ...   53.1000  C123         S
8              9         1       3  ...   11.1333   NaN         S
..           ...       ...     ...  ...       ...   ...       ...
856          857         1       1  ...  164.8667   NaN         S
869          870         1       3  ...   11.1333   NaN         S
871          872         1       1  ...   52.5542   D35         S
879          880         1       1  ...   83.1583   C50         C
880          881         1       2  ...   26.0000   NaN         S
[886 rows x 12 columns]
```

```python
# Same as DataFrame.ne_equal_df_ind_no_dup
# but returns the DataFrame (df.loc)
df.ne_equal_df_no_dup(b'1', 'S')
Out[19]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
6              7         0       1  ...  51.8625   E46         S
..           ...       ...     ...  ...      ...   ...       ...
879          880         1       1  ...  83.1583   C50         C
880          881         1       2  ...  26.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
[524 rows x 12 columns]
```

```python
# Returns bool
array([ True, False, False, False, False, False, False, False, False,
       False, False, False, ...]
df.loc[df.PassengerId.ne_equal(1)]
%timeit df.loc[df.PassengerId.ne_equal(1)]
138 µs ± 626 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId == 1]
209 µs ± 1.04 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# Every time the condition is False, the index is
# added to the return value.
# Example:
# A row has 6 columns. 2 of them have the value 1.
# That means the index of the row will be added 4 times
# to the final result
df.loc[df.ne_not_equal_df_ind(1)]
array([  1,   2,   3, ..., 888, 889, 890], dtype=int64)

df.loc[df.ne_not_equal_df_ind(1)]
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
5              6         0       3  ...   8.4583   NaN         Q
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[5344 rows x 12 columns]
```

```python
# Same as DataFrame.ne_not_equal_df_ind
# but drops all duplicates

df.ne_not_equal_df_ind_no_dup(0)
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16,...]

df.loc[df.ne_not_equal_df_ind_no_dup(0)]
Out[26]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[891 rows x 12 columns]
```

```python
# same as DataFrame.ne_not_equal_df_ind
# but returns the DataFrame (df.loc)
df.ne_not_equal_df_dup(0)
Out[28]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[4387 rows x 12 columns]
```

```python
# same as DataFrame.ne_not_equal_df_no_dup
# but returns the DataFrame (df.loc)
df.ne_not_equal_df_no_dup(0)
Out[29]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[891 rows x 12 columns]
```

```python
returns Bool
df.Survived.ne_not_equal(0)
array([False,  True,  True,  True, False, False, False, False,  True,
        True,  True,  True, False, False, False,  True, False,  True,
       False,  True ...]

df.loc[df.Survived.ne_not_equal(0)]
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
8              9         1       3  ...  11.1333   NaN         S
9             10         1       2  ...  30.0708   NaN         C
..           ...       ...     ...  ...      ...   ...       ...
875          876         1       3  ...   7.2250   NaN         C
879          880         1       1  ...  83.1583   C50         C
880          881         1       2  ...  26.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
889          890         1       1  ...  30.0000  C148         C
[342 rows x 12 columns]

%timeit df.loc[df.Survived.ne_not_equal(0)]
157 µs ± 390 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.Survived!=0]
229 µs ± 1.46 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# returns index, duplicates are possible
# if the condition is valid for more than one
# column. Exceptions (e.g. wrong dtype) are ignored
df.ne_greater_than_df_ind(100)
array([100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
       113, 114, 115...]
```

```python
# Same as DataFrame.ne_greater_than_df_ind
# but gets rid off all duplicates
df.ne_greater_than_df_ind_no_dup(0)
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16...]
```

```python
# Same as DataFrame.ne_greater_than_df_ind
# but returns the DataFrame (df.loc)
df.ne_greater_than_df_dup(0)
Out[22]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[4210 rows x 12 columns]
```

```python
# same as DataFrame.ne_greater_than_df_ind_no_dup
# but returns the DataFrame (df.loc)
df.ne_greater_than_df_no_dup(600)
Out[24]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
600          601         1       2  ...  27.0000   NaN         S
601          602         0       3  ...   7.8958   NaN         S
602          603         0       1  ...  42.4000   NaN         S
603          604         0       3  ...   8.0500   NaN         S
604          605         1       1  ...  26.5500   NaN         C
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[291 rows x 12 columns]
```

```python
# Returns bool
df.PassengerId.ne_greater_than(5)
Out[26]: 
array([False, False, False, False, False,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True...]

df.loc[df.PassengerId.ne_greater_than(100)]
%timeit df.loc[df.PassengerId.ne_greater_than(100)]
174 µs ± 375 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId>100]
248 µs ± 2.26 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# returns index, duplicates are possible
# if the condition is valid for more than one
# column. Exceptions (e.g. wrong dtype) are ignored

df.ne_less_than_df_ind(10)
array([  0,   1,   2, ..., 881, 884, 890], dtype=int64)
```

```python
# Same as DataFrame.ne_less_than_df_ind
# but without duplicates
df.ne_less_than_df_ind_no_dup(100)
Out[28]: 
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16,  17,  18,  19,  20,  21,...]
```

```python
# Same as DataFrame.ne_less_than_df_ind,
# but returns DataFrame (df.loc)
df.ne_less_than_df_dup(1)
Out[29]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
4              5         0       3  ...   8.0500   NaN         S
5              6         0       3  ...   8.4583   NaN         Q
6              7         0       1  ...  51.8625   E46         S
7              8         0       3  ...  21.0750   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
674          675         0       2  ...   0.0000   NaN         S
732          733         0       2  ...   0.0000   NaN         S
806          807         0       1  ...   0.0000   A36         S
815          816         0       1  ...   0.0000  B102         S
822          823         0       1  ...   0.0000   NaN         S
[1857 rows x 12 columns]
```

```python
# Same as DataFrame.ne_less_than_df_ind_no_dup
# but returns DataFrame (df.loc)
df.ne_less_than_df_no_dup(1)
Out[30]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[834 rows x 12 columns]
```

```python
# returns bool
# df.PassengerId.ne_less_than(100)
df.PassengerId.ne_less_than(100)
Out[31]: 
array([ True,  True,  True,  True,  True,  True...]
%timeit df.loc[df.PassengerId.ne_less_than(100)]
142 µs ± 412 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId <100]
212 µs ± 897 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# returns index, duplicates are possible
# if the condition is valid for more than one
# column. Exceptions (e.g. wrong dtype) are ignored
df.ne_greater_than_or_equal_to_df_ind(100)
Out[35]: 
array([ 99, 100, 101, 102, 103, 104, ...]
```

```python
# Same as DataFrame.ne_greater_than_or_equal_to_df_ind ,
# but without duplicates
# df.ne_greater_than_or_equal_to_df_ind_no_dup(100)
df.ne_greater_than_or_equal_to_df_ind_no_dup(100)
Out[36]: 
array([ 27,  31,  88,  99, 100, 101, 102,...] 
```

```python
# Same as DataFrame.ne_greater_than_or_equal_to_df_ind,
# but returns DataFrame (df.loc)
df.ne_greater_than_or_equal_to_df_dup(100)
Out[37]: 
     PassengerId  Survived  Pclass  ...      Fare            Cabin  Embarked
99           100         0       2  ...   26.0000              NaN         S
100          101         0       3  ...    7.8958              NaN         S
101          102         0       3  ...    7.8958              NaN         S
102          103         0       1  ...   77.2875              D26         S
103          104         0       3  ...    8.6542              NaN         S
..           ...       ...     ...  ...       ...              ...       ...
742          743         1       1  ...  262.3750  B57 B59 B63 B66         C
763          764         1       1  ...  120.0000          B96 B98         S
779          780         1       1  ...  211.3375               B3         S
802          803         1       1  ...  120.0000          B96 B98         S
856          857         1       1  ...  164.8667              NaN         S
[845 rows x 12 columns]
```

```python
# Same as DataFrame.ne_greater_than_or_equal_to_df_ind,
# but returns DataFrame (df.loc)
df.ne_greater_than_or_equal_to_df_no_dup(100)
Out[38]: 
     PassengerId  Survived  Pclass  ...      Fare        Cabin  Embarked
27            28         0       1  ...  263.0000  C23 C25 C27         S
31            32         1       1  ...  146.5208          B78         C
88            89         1       1  ...  263.0000  C23 C25 C27         S
99           100         0       2  ...   26.0000          NaN         S
100          101         0       3  ...    7.8958          NaN         S
..           ...       ...     ...  ...       ...          ...       ...
886          887         0       2  ...   13.0000          NaN         S
887          888         1       1  ...   30.0000          B42         S
888          889         0       3  ...   23.4500          NaN         S
889          890         1       1  ...   30.0000         C148         C
890          891         0       3  ...    7.7500          NaN         Q
[795 rows x 12 columns]
```

```python
# returns bool
df.PassengerId.ne_greater_than_or_equal_to(100)
Out[39]: 
array([False, False, False, False, False...])
df.PassengerId.ne_greater_than_or_equal_to(100)
%timeit df.loc[df.PassengerId.ne_greater_than_or_equal_to(100)]
175 µs ± 832 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId>=100]
251 µs ± 2.77 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# returns index, duplicates are possible
# if the condition is valid for more than one
# column. Exceptions (e.g. wrong dtype) are ignored
df.ne_less_than_or_equal_to_df_ind(100)
Out[40]: array([  0,   1,   2, ..., 888, 889, 890], dtype=int64)
```

```python
# Same as DataFrame.ne_less_than_or_equal_to_df_ind ,
# but without duplicates
df.ne_less_than_or_equal_to_df_ind_no_dup(100)
Out[41]: 
array([  0,   1,   2,   3,   4,   5,   6,   7,   8, ...])
```

```python
# Same as DataFrame.ne_less_than_or_equal_to_df_ind,
# but returns DataFrame (df.loc)
df.ne_less_than_or_equal_to_df_dup(100)
Out[42]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[5216 rows x 12 columns]
```

```python
# Same as DataFrame.ne_less_than_or_equal_to_df_ind,
# but returns DataFrame (df.loc)
df.ne_less_than_or_equal_to_df_no_dup(0)
Out[53]: 
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q
[829 rows x 12 columns]
```

```python
# returns bool
df.PassengerId.ne_less_than_or_equal_to(100)
Out[55]: 
array([ True,  True,  True,  True, ....]

%timeit df.loc[df.PassengerId.ne_less_than_or_equal_to(100)]
145 µs ± 1.82 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df.PassengerId <=100]
212 µs ± 1.63 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# Combining conditions
%timeit df.loc[df.PassengerId.ne_greater_than(100) & df.Cabin.ne_search_for_string_series_contains('C1')]
360 µs ± 2.56 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
%timeit df.loc[(df.PassengerId>100) & df.Cabin.str.contains('C1',na=False)]
552 µs ± 3.49 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# you can pass your own queries
# If you want to compare the DataFrame/Series to another array
# the variable 'b' represents the DataFrame/Series 
# That means: don't use it for something else
wholedict = {'c': np.array([1])}
df[['Survived','Pclass']].ne_query('b == c',local_dict=wholedict)
Out[14]: 
array([[False, False],
       [ True,  True],
       [ True, False],
       ...,
       [False, False],
       [ True,  True],
       [False, False]])


# You can use any NumExpr operator/function
# https://numexpr.readthedocs.io/projects/NumExpr3/en/latest/user_guide.html
# And get a tremendous speedup (even with small DataFrames)
%timeit df['Survived'] + df.Pclass
68.6 µs ± 167 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'] * df.Pclass
69 µs ± 260 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'] == df.Pclass
72.3 µs ± 817 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

# You have to pass the Series/Arrays that you are using in the expression as a dict (local_dict)
wholedict = {'c': df.Pclass}
%timeit df['Survived'].ne_query('b + c',local_dict=wholedict)
25.2 µs ± 130 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'].ne_query('b * c',local_dict=wholedict)
25.3 µs ± 177 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df['Survived'].ne_query('b == c',local_dict=wholedict)
25.2 µs ± 197 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

# Exceptions are not ignored
# If you want to compare the DataFrame with a scalar:
df[['Survived','Pclass']].ne_query('b == 1')

# works also for Series
wholedict = {'c': np.array([1])}
df['Survived'].ne_query('b == c',local_dict=wholedict)

# scalar
df['Pclass'].ne_query('b == 1')

%timeit df.loc[df['Pclass'].ne_query('b == 1')]
155 µs ± 530 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
%timeit df.loc[df['Pclass'] == 1]
220 µs ± 3.96 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```
