# Extremely fast by combining np.select and numexpr.evaluate (works with utf-8!)

### Here is a simple query:

[https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv](https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv)

```python
%timeit (df.PassengerId >800) | (df.PassengerId <60)
194 µs ± 586 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

**When you're working with pandas, speed matters!.**

### Well, there are 2 tricks to tremendously increase the speed of Pandas

**(Here are 2 examples: in case you have never heard about them)**

#### 1) np.select

```python
b=df.PassengerId.__array__()
%timeit np.select([b>800, b<60], [True,True], False)
21.5 µs ± 44.5 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

#### 2) numexpr.evaluate

```python
b=df.PassengerId.__array__()
%timeit [numexpr.evaluate('(b > 800)|(b < 60)')]
10.5 µs ± 25 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
```

#### Combining both

Well, why not combining those two?  numexpr.evaluate to do the queries, and np.select to filter the queries (True/False)

The problem is that numexpr has many limitations:

[https://numexpr.readthedocs.io/projects/NumExpr3/en/latest/user_guide.html#supported-operators](https://numexpr.readthedocs.io/projects/NumExpr3/en/latest/user_guide.html#supported-operators)

If you are working with numbers, you probably won't miss a lot, 

but with strings, it is different: numexpr nor supports the utf-8 format neither regex.

I am a German teacher and work most of the time with DataFrames containing strings (mainly bilingual dictionaries)

anywhere from 500 to 10000000 rows. Unfortunately, it is not that easy converting German words 

 to ASCII strings due to the special characters (ö, ä ...)

I found a way to simplify the conversion either way, without losing the special characters:

```python
df.Name.s_str().s_to_ascii()
df.Nameuni.s_str().s_to_utf8()
```

But converting them all the time back and forth (to use **Series.str [only UTF-8]**) doesn't make any sense, 

because we are loosing all the speed gained from numexpr.evaluate/np.select.

Unfortunately, **Series.str** doesn't accept binary data. 

But since I use all methods of the Series.str class frequently and 

I also want the benefits of numexpr.evaluate/np.select, I changed 

almost all methods of Series.str to make them work with binary data.

**Don’t be afraid**:

It won’t overwrite **Series.str**, it just adds **s_str**(parenthesis when you want to access the methods!)

Some of the adapted methods are faster, some are slower (still faster than converting)

and some are really slow, and should not be used (casefold/wrap/normalize)

and few of them are not working yet [(encode/decode) → adaption probably senseless].

And of course, the new insanely fast methods:

```python
s_uniascii_contains # only for strings, pass strings as utf-8
s_uniascii_equal # only for strings, pass strings as utf-8
d_floc # replacement for df.loc / combine it with numexpr.evaluate 
get_compiled_regex_from_wordlist  # instead of searching [Maria, Carlos, ...], use this function to generate a binary Trie regex
```

Scroll down to see the execution speed of every method compared to **Series.str**

## How to use

```python
from a_pandas_ex_fastloc import pd_add_fastloc,get_byte_regex,get_compiled_regex_from_wordlist,convert_utf8_to_ascii
pd_add_fastloc()
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
df['Nameuni'] = df.Name + 'ö' # get some utf-8 data with special characters
df['Nameuni2'] = df['Nameuni'].s_str().s_to_ascii()
dfbig = pd.concat([df.copy() for x in range(100)],ignore_index=True)
dfbigbig = pd.concat([df.copy() for x in range(1000)],ignore_index=True)
```

### # The highlights

#### s_uniascii_contains

```python
%timeit dfbigbig.loc[dfbigbig.Nameuni.str.contains('Harrisö')]
239 ms ± 1.62 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
%timeit dfbigbig.loc[dfbigbig.Nameuni2.s_str().s_uniascii_contains('Harrisö')]
14.7 ms ± 111 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

### s_uniascii_equal

```python
%timeit dfbigbig.loc[dfbigbig.Nameuni == 'Braund, Mr. Owen Harrisö']
29.3 ms ± 179 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
%timeit dfbigbig.loc[dfbigbig.Nameuni2.s_str().s_uniascii_equal('Braund, Mr. Owen Harrisö')]
3.89 ms ± 5.78 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

### s_to_utf8

```python
# Data can be converted easily to utf-8:
dfbigbig.loc[dfbigbig.Nameuni2.s_str().s_uniascii_contains('Harrisö')].Nameuni2.s_str().s_to_utf8()
Out[65]: 
0         Braund, Mr. Owen Harrisö
891       Braund, Mr. Owen Harrisö
1782      Braund, Mr. Owen Harrisö
2673      Braund, Mr. Owen Harrisö
3564      Braund, Mr. Owen Harrisö
                    ...           
Name: Nameuni2, Length: 1000, dtype: object
```

### d_floc

```python
# You can also use numbers, but you won't get a speedup for simple queries
%timeit -n 4 dfbigbig.d_floc([('(Age > 10)',True)]) 
%timeit -n 4 dfbigbig.loc[dfbigbig.Age > 10]
139 ms ± 562 µs per loop (mean ± std. dev. of 7 runs, 4 loops each)
140 ms ± 486 µs per loop (mean ± std. dev. of 7 runs, 4 loops each)
```

```python
# Once the query gets more sophisticated, things are different:
%timeit -n 4 dfbigbig.d_floc([('((Age*3221/3220 > (10*.432/.431)) & (PassengerId%10 ==0))',True)])
%timeit -n 4 dfbigbig.loc[(dfbigbig.Age*3221/3220 > 10*.432/.431) & (dfbigbig.PassengerId %10 ==0)]
23.4 ms ± 583 µs per loop (mean ± std. dev. of 7 runs, 4 loops each)
35.2 ms ± 342 µs per loop (mean ± std. dev. of 7 runs, 4 loops each)
```

```python
%timeit -n 4 dfbigbig.d_floc([('((Age*3221/3220 > (10*.432/.431)) & (PassengerId%10 ==0))',True),(f'contains(Nameuni2,{repr(convert_utf8_to_ascii("Harrisö"))})',True)], convertstr=False)
%timeit -n 4 dfbigbig.loc[((dfbigbig.Age*3221/3220 > 10*.432/.431) & (dfbigbig.PassengerId %10 ==0)) | dfbigbig.Nameuni.str.contains("Harrisö")]
39.8 ms ± 1.01 ms per loop (mean ± std. dev. of 7 runs, 4 loops each)
272 ms ± 1.12 ms per loop (mean ± std. dev. of 7 runs, 4 loops each)

# Different ways of doing the query, check out the numexpr documentation
%timeit -n 4 dfbigbig.d_floc([('((Age*3221/3220 > (10*.432/.431)) & (PassengerId%10 ==0))',True),(f'contains(Nameuni2,{repr(convert_utf8_to_ascii("Harrisö"))})',True)], convertstr=False)
%timeit -n 4 dfbigbig.d_floc([(f'((Age*3221/3220 > (10*.432/.431)) & (PassengerId%10 ==0)) | contains(Nameuni2,{repr(convert_utf8_to_ascii("Harrisö"))})',True)], convertstr=False)
```

```python
# How to negate results (operator ~)
%timeit -n 4 dfbigbig.d_floc([(f'((Age*3221/3220 > (10*.432/.431)) & (PassengerId%10 ==0)) | contains(Nameuni2,{repr(convert_utf8_to_ascii("Harrisö"))})',False)], convertstr=False, default=True)
%timeit -n 4 dfbigbig.loc[~(((dfbigbig.Age*3221/3220 > 10*.432/.431) & (dfbigbig.PassengerId %10 ==0)) | dfbigbig.Nameuni.str.contains("Harrisö"))]
194 ms ± 1.55 ms per loop (mean ± std. dev. of 7 runs, 4 loops each)
436 ms ± 3.34 ms per loop (mean ± std. dev. of 7 runs, 4 loops each)
```

```python
# without converting the Series with utf-8 strings to ASCII
queries=[('contains(Name, "Maria")',True)]
# convertstr=True -> Converts utf-8 to bytes, must be True if the column is not ASCII, and False if ASCII 
%timeit df.d_floc(queries, default=False, convertstr=True) 
%timeit df.loc[df.Name.str.contains('Maria')]

# Even though, the Series has been converted to bytes in every loop, fastloc is still much faster:
329 µs ± 4.25 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
491 µs ± 2.14 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# How to convert
df['Name2'] = df.Name.s_str().s_to_ascii()
# works also with special characters (ö, ï ...)
df['Nameuni2'] = df.Nameuni.s_str().s_to_ascii()
```

```python
# Faster when converted (convertstr=False)
queries=[('contains(Name2, "Maria")',True)]
%timeit df.d_floc(queries, default=False, convertstr=False) 
%timeit df.loc[df.Name.str.contains('Maria')]
270 µs ± 1.29 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
510 µs ± 1.15 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```python
# You can also use: 
%timeit df.loc[df.Name2.s_str().s_uniascii_contains('Maria')]

# The bigger the dataframe, the better:
dfbig['Nameuni2'] = dfbig.Nameuni.s_str().s_to_ascii()
dfbig['Name2'] = dfbig.Name.s_str().s_to_ascii()
queries=[('contains(Name2, "Maria")',True)]
%timeit dfbig.d_floc(queries, default=False, convertstr=False) 
%timeit dfbig.loc[dfbig.Name.str.contains('Maria')]
2.04 ms ± 206 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
25.6 ms ± 90.1 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)


dfbigbig['Nameuni2'] = dfbigbig.Nameuni.s_str().s_to_ascii()
dfbigbig['Name2'] = dfbigbig.Name.s_str().s_to_ascii()
queries=[('contains(Name2, "Maria")',True)]
%timeit dfbigbig.d_floc(queries, default=False, convertstr=False) 
%timeit dfbigbig.loc[dfbigbig.Name.str.contains('Maria')]
18.3 ms ± 347 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
251 ms ± 392 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

```python
# Converting the results to unicode:
dfbigbig.d_floc(queries, default=False, convertstr=False).Nameuni2 .s_str().s_to_utf8()
Out[42]: 
18        Vander Planke, Mrs. Julius (Emelia Maria Vande...
38                      Vander Planke, Miss. Augusta Mariaö
85        Backstrom, Mrs. Karl Alfred (Maria Mathilda Gu...
119                      Andersson, Miss. Ellis Anna Mariaö
307       Penasco y Castellana, Mrs. Victor de Satode (M...
                                ...                        
890535         Clarke, Mrs. Charles V (Ada Maria Winfield)ö
890687                    Caram, Mrs. Joseph (Maria Elias)ö
890690    Thayer, Mrs. John Borland (Marian Longstreth M...
890747              Panula, Mrs. Juha (Maria Emilia Ojala)ö
890925                        Heininen, Miss. Wendla Mariaö
Name: Nameuni2, Length: 12000, dtype: object
```

### convert_utf8_to_ascii

```python
# Searching for Unicode using numexpr directly
# Use this to convert the string to bin: {repr(convert_utf8_to_ascii("Harrisö"))}
queriesuni=[(f'contains(Nameuni2, {repr(convert_utf8_to_ascii("Harrisö"))})',True)]
%timeit df.d_floc(queriesuni, default=False, convertstr=False) 

293 µs ± 974 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


Out[11]: 
   PassengerId  ...                           Nameuni2
0            1  ...  b'Braund, Mr. Owen Harris\\u00f6'
[1 rows x 15 columns]

# Convert to utf-8
df.d_floc(queriesuni, default=False, convertstr=False).Nameuni2.s_str().s_to_utf8()
Out[17]: 
0    Braund, Mr. Owen Harrisö
Name: Nameuni2, dtype: object

#################################################################
%timeit df.loc[df.Nameuni.str.contains('Harrisö')]
514 µs ± 2.82 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
Out[13]: 
   PassengerId  ...                           Nameuni2
0            1  ...  b'Braund, Mr. Owen Harris\\u00f6'
[1 rows x 15 columns]
```

### get_byte_regex

```python
# Regex works too, but be careful with special characters

# Avoid this because you might get other results than you want:
comp0 = get_byte_regex('^.*?[öä]$')
print(comp0)
re.compile(b'^.*?[\\\\u00f6\\\\u00e4]$')

# Better
comp1=get_byte_regex('^.*?(?:(?:ö)|(?:ä))$')
print(comp1)
re.compile(b'^.*?(?:(?:\\\\u00f6)|(?:\\\\u00e4))$')

%timeit df.Nameuni2.s_str().findall(comp1)
%timeit df.Nameuni.str.findall('^.*?(?:(?:ö)|(?:ä))$')

# Not much faster, but at least a little
633 µs ± 1.35 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
641 µs ± 906 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

Out[21]: 
0                    [b'Braund, Mr. Owen Harris\\u00f6']
1      [b'Cumings, Mrs. John Bradley (Florence Briggs...
2                     [b'Heikkinen, Miss. Laina\\u00f6']
3      [b'Futrelle, Mrs. Jacques Heath (Lily May Peel...
4                   [b'Allen, Mr. William Henry\\u00f6']
                             ...                        
886                    [b'Montvila, Rev. Juozas\\u00f6']
887             [b'Graham, Miss. Margaret Edith\\u00f6']
888    [b'Johnston, Miss. Catherine Helen \\"Carrie\\...
889                    [b'Behr, Mr. Karl Howell\\u00f6']
890                      [b'Dooley, Mr. Patrick\\u00f6']
Name: Nameuni2, Length: 891, dtype: object

Out[22]: 
0                             [Braund, Mr. Owen Harrisö]
1      [Cumings, Mrs. John Bradley (Florence Briggs T...
2                              [Heikkinen, Miss. Lainaö]
3        [Futrelle, Mrs. Jacques Heath (Lily May Peel)ö]
4                            [Allen, Mr. William Henryö]
                             ...                        
886                             [Montvila, Rev. Juozasö]
887                      [Graham, Miss. Margaret Edithö]
888          [Johnston, Miss. Catherine Helen "Carrie"ö]
889                             [Behr, Mr. Karl Howellö]
890                               [Dooley, Mr. Patrickö]
Name: Nameuni, Length: 891, dtype: object


# With big DataFrames
%timeit dfbigbig.Nameuni2.s_str().findall(comp1)
%timeit dfbigbig.Nameuni.str.findall('^.*?(?:(?:ö)|(?:ä))$')
556 ms ± 2.61 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
571 ms ± 2.52 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#################################################################
# You can use all regex methods from a Series.str. 
# But usually no speedup when using regex (sometimes a little faster, sometimes a little slower)
regexpextractall='^.*?((?:ö)|(?:ä))$'
comp1=get_byte_regex(regexpextractall)
%timeit dfbig.Nameuni2.s_str().extractall(comp1)
%timeit dfbig.Nameuni.str.extractall(regexpextractall)
209 ms ± 2.65 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
206 ms ± 3.98 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

regexpextractall='^.*?((?:ö)|(?:ä))$'
comp1=get_byte_regex(regexpextractall)
%timeit dfbig.Nameuni2.s_str().replace(comp1, b'XX',regex=True)
%timeit dfbig.Nameuni.str.replace(regexpextractall, 'XX',regex=True)
69.9 ms ± 747 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
71.5 ms ± 293 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

#################################################################
```

### get_compiled_regex_from_wordlist

```python
# If you have a list of words, create a Trie regex:
# e.g. all names with starting with M
lotsofwords = ([o for o in set([re.sub(r'\W+','',x) for x in "\n".join(df.Name.unique().tolist()).split()]) if o.startswith('M')])
lotsofwordsre=get_compiled_regex_from_wordlist(
        wordlist=lotsofwords,
        boundary_right=True,
        boundary_left=True,
        capture=False,
        match_whole_line=False,
    flags=re.I
    )
%timeit df.loc[df.Name.apply(lambda x: True if [y for y in lotsofwords if y in x] else False)]
%timeit df.loc[df.Name2.s_str().contains(lotsofwordsre,regex=True)]
7.02 ms ± 47.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
914 µs ± 1.45 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
#################################################################
```

## Methods faster than Series.str

```python
# To avoid converting back and forth all the time (ascii - utf-8)
# I adapted most of the methods from the Series.str class 
# to work with bytes 
# Some methods are faster, some are slower and some are really slow 
# (casefold/wrap/normalize)
# But surely better than converting all the time 

# Lets create a copy of the DF
df5=dfbig.copy()
df5['Name1'] = df5.Nameuni2.copy() 
```

```python
#################################################################
print(df5.Name2.s_str().capitalize())
print(df5.Name1.s_str().capitalize())
print(df5.Name.str.capitalize())
%timeit -n 5 df5.Name2.s_str().capitalize()
%timeit -n 5 df5.Name1.s_str().capitalize()
%timeit -n 5 df5.Name.str.capitalize()
13.8 ms ± 313 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
13.9 ms ± 153 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
20.5 ms ± 169 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
# Not part of Series.str, but similar to Series.str.contains
print(df5.Name2.s_str().s_uniascii_equal('Svensson, Mr. Johan'))
print(df5.Name1.s_str().s_uniascii_equal('Svensson, Mr. Johan'))
print(df5.loc[df5.Name == 'Svensson, Mr. Johan'])
%timeit -n 5 df5.Name2.s_str().s_uniascii_equal('Svensson, Mr. Johan')
%timeit -n 5 df5.Name1.s_str().s_uniascii_equal('Svensson, Mr. Johan')
%timeit -n 5 df5.loc[df5.Name == ('Svensson, Mr. Johan')]
350 µs ± 126 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
317 µs ± 27.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
3.13 ms ± 34.7 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
# Not part of Series.str, but similar to Series.str.contains
print(df5.Name2.s_str().s_uniascii_contains('a'))
print(df5.Name1.s_str().s_uniascii_contains('a'))
print(df5.Name.str.contains('a'))
%timeit -n 5 df5.Name2.s_str().s_uniascii_contains('a')
%timeit -n 5 df5.Name1.s_str().s_uniascii_contains('a')
%timeit -n 5 df5.Name.str.contains('a')
1.12 ms ± 73.1 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
1.07 ms ± 16.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.6 ms ± 506 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().isalnum())
print(df5.Name1.s_str().isalnum())
print(df5.Name.str.isalnum())
%timeit -n 5 df5.Name2.s_str().isalnum()
%timeit -n 5 df5.Name1.s_str().isalnum()
%timeit -n 5 df5.Name.str.isalnum()
9.67 ms ± 125 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
9.44 ms ± 74.2 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
10 ms ± 122 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().isalpha())
print(df5.Name1.s_str().isalpha())
print(df5.Name.str.isalpha())
%timeit -n 5 df5.Name2.s_str().isalpha()
%timeit -n 5 df5.Name1.s_str().isalpha()
%timeit -n 5 df5.Name.str.isalpha()
9.74 ms ± 164 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
9.45 ms ± 91.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
9.77 ms ± 44.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().istitle())
print(df5.Name1.s_str().istitle())
print(df5.Name.str.istitle())
%timeit -n 5 df5.Name2.s_str().istitle()
%timeit -n 5 df5.Name1.s_str().istitle()
%timeit -n 5 df5.Name.str.istitle()
14 ms ± 563 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
13.8 ms ± 83.5 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.5 ms ± 188 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().partition())
print(df5.Name1.s_str().partition())
print(df5.Name.str.partition())
%timeit -n 5 df5.Name2.s_str().partition()
%timeit -n 5 df5.Name1.s_str().partition()
%timeit -n 5 df5.Name.str.partition()
86.8 ms ± 817 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
86.8 ms ± 297 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
89.5 ms ± 412 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().rpartition())
print(df5.Name1.s_str().rpartition())
print(df5.Name.str.rpartition())
%timeit -n 5 df5.Name2.s_str().rpartition()
%timeit -n 5 df5.Name1.s_str().rpartition()
%timeit -n 5 df5.Name.str.rpartition()
89.1 ms ± 773 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
90.2 ms ± 490 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
90.5 ms ± 383 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().repeat(100))
print(df5.Name1.s_str().repeat(100))
print(df5.Name.str.repeat(100))
%timeit -n 5 df5.Name2.s_str().repeat(100)
%timeit -n 5 df5.Name1.s_str().repeat(100)
%timeit -n 5 df5.Name.str.repeat(100)
75.7 ms ± 4.08 ms per loop (mean ± std. dev. of 7 runs, 5 loops each)
92.6 ms ± 5.07 ms per loop (mean ± std. dev. of 7 runs, 5 loops each)
113 ms ± 387 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().slice_replace(start=1, stop=10, repl=b'2'))
print(df5.Name1.s_str().slice_replace(start=1, stop=10, repl=b'2'))
print(df5.Name.str.slice_replace(start=1, stop=10, repl='2'))
%timeit -n 5 df5.Name2.s_str().slice_replace(start=1, stop=10, repl=b'2')
%timeit -n 5 df5.Name1.s_str().slice_replace(start=1, stop=10, repl=b'2')
%timeit -n 5 df5.Name.str.slice_replace(start=1, stop=10, repl='2')
30.8 ms ± 544 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
31 ms ± 285 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
44.5 ms ± 281 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().split())
print(df5.Name1.s_str().split())
print(df5.Name.str.split())
%timeit -n 5 df5.Name2.s_str().split()
%timeit -n 5 df5.Name1.s_str().split()
%timeit -n 5 df5.Name.str.split()
39.1 ms ± 558 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
39.8 ms ± 280 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
40.1 ms ± 244 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().swapcase())
print(df5.Name1.s_str().swapcase())
print(df5.Name.str.swapcase())
%timeit -n 5 df5.Name2.s_str().swapcase()
%timeit -n 5 df5.Name1.s_str().swapcase()
%timeit -n 5 df5.Name.str.swapcase()
17.7 ms ± 773 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
18.9 ms ± 334 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.2 ms ± 140 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().title())
print(df5.Name1.s_str().title())
print(df5.Name.str.title())
%timeit -n 5 df5.Name2.s_str().title()
%timeit -n 5 df5.Name1.s_str().title()
%timeit -n 5 df5.Name.str.title()
17.9 ms ± 475 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
19.6 ms ± 384 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.4 ms ± 162 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().strip(b'Svensson, Mr. Johan'))
print(df5.Name1.s_str().strip(b'Svensson, Mr. Johan'))
print(df5.Name.str.strip('Svensson, Mr. Johan'))
%timeit -n 5 df5.Name2.s_str().strip(b'Svensson, Mr. Johan')
%timeit -n 5 df5.Name1.s_str().strip(b'Svensson, Mr. Johan')
%timeit -n 5 df5.Name.str.strip('Svensson, Mr. Johan')
22.1 ms ± 595 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
19.3 ms ± 336 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
19.4 ms ± 156 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().translate(bytes.maketrans(b'\x47',b'X')))
print(df5.Name1.s_str().translate(bytes.maketrans(b'\x47',b'X')))
print(df5.Name.str.translate(str.maketrans('G','X')))
%timeit -n 5 df5.Name2.s_str().translate(bytes.maketrans(b'\x47',b'X'))
%timeit -n 5 df5.Name1.s_str().translate(bytes.maketrans(b'\x47',b'X'))
%timeit -n 5 df5.Name.str.translate(str.maketrans('G','X'))
20 ms ± 486 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
20.8 ms ± 183 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
86.3 ms ± 173 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().upper())
print(df5.Name1.s_str().upper())
print(df5.Name.str.upper())
%timeit -n 5 df5.Name2.s_str().upper()
%timeit -n 5 df5.Name1.s_str().upper()
%timeit -n 5 df5.Name.str.upper()
13.4 ms ± 324 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
13.7 ms ± 172 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
15.4 ms ± 180 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
#################################################################
#################################################################
```

## Methods slower than Series.str

```python
print(df5.Name2.s_str().replace(rb'a\w{3,7}',b'xxx',regex=True))
print(df5.Name1.s_str().replace(rb'a\w{3,7}',b'xxx',regex=True))
print(df5.Name.str.replace(r'a\w{3,7}','xxx',regex=True))
%timeit -n 5 df5.Name2.s_str().replace(rb'a\w{3,7}',b'xxx',regex=True)
%timeit -n 5 df5.Name1.s_str().replace(rb'a\w{3,7}',b'xxx',regex=True)
%timeit -n 5 df5.Name.str.replace(r'a\w{3,7}','xxx',regex=True)
63 ms ± 504 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
63.4 ms ± 325 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
60 ms ± 326 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().removeprefix(b'A'))
print(df5.Name1.s_str().removeprefix(b'A'))
print(df5.Name.str.removeprefix('A'))
%timeit -n 5 df5.Name2.s_str().removeprefix(b'A')
%timeit -n 5 df5.Name1.s_str().removeprefix(b'A')
%timeit -n 5 df5.Name.str.removeprefix('A')
23.3 ms ± 625 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
23 ms ± 185 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.4 ms ± 163 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().isupper())
print(df5.Name1.s_str().isupper())
print(df5.Name.str.isupper())
%timeit -n 5 df5.Name2.s_str().isupper()
%timeit -n 5 df5.Name1.s_str().isupper()
%timeit -n 5 df5.Name.str.isupper()
8.98 ms ± 197 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.57 ms ± 48.5 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.49 ms ± 53.9 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().isspace())
print(df5.Name1.s_str().isspace())
print(df5.Name.str.isspace())
%timeit -n 5 df5.Name2.s_str().isspace()
%timeit -n 5 df5.Name1.s_str().isspace()
%timeit -n 5 df5.Name.str.isspace()
8.82 ms ± 226 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.61 ms ± 122 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.29 ms ± 73.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().islower())
print(df5.Name1.s_str().islower())
print(df5.Name.str.islower())
%timeit -n 5 df5.Name2.s_str().islower()
%timeit -n 5 df5.Name1.s_str().islower()
%timeit -n 5 df5.Name.str.islower()
9 ms ± 269 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.59 ms ± 81.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.37 ms ± 129 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().slice(start=1, stop=10, step=2))
print(df5.Name1.s_str().slice(start=1, stop=10, step=2))
print(df5.Name.str.slice(start=1, stop=10, step=2))
%timeit -n 5 df5.Name2.s_str().slice(start=1, stop=10, step=2)
%timeit -n 5 df5.Name1.s_str().slice(start=1, stop=10, step=2)
%timeit -n 5 df5.Name.str.slice(start=1, stop=10, step=2)
18.9 ms ± 304 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
19.1 ms ± 235 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
15.5 ms ± 160 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().rfind(b'A'))
print(df5.Name1.s_str().rfind(b'A'))
print(df5.Name.str.rfind('A'))
%timeit -n 5 df5.Name2.s_str().rfind(b'A')
%timeit -n 5 df5.Name1.s_str().rfind(b'A')
%timeit -n 5 df5.Name.str.rfind('A')
41 ms ± 618 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
41.2 ms ± 301 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
35.2 ms ± 216 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().startswith(b'Svensson, Mr. Johan'))
print(df5.Name1.s_str().startswith(b'Svensson, Mr. Johan'))
print(df5.Name.str.startswith('Svensson, Mr. Johan'))
%timeit -n 5 df5.Name2.s_str().startswith(b'Svensson, Mr. Johan')
%timeit -n 5 df5.Name1.s_str().startswith(b'Svensson, Mr. Johan')
%timeit -n 5 df5.Name.str.startswith('Svensson, Mr. Johan')
24.2 ms ± 511 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.4 ms ± 327 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
18.6 ms ± 296 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().rjust(100))
print(df5.Name1.s_str().rjust(100))
print(df5.Name.str.rjust(100))
%timeit -n 5 df5.Name2.s_str().rjust(100)
%timeit -n 5 df5.Name1.s_str().rjust(100)
%timeit -n 5 df5.Name.str.rjust(100)
23.6 ms ± 513 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
23.6 ms ± 160 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
18.7 ms ± 129 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().isdigit())
print(df5.Name1.s_str().isdigit())
print(df5.Name.str.isdigit())
%timeit -n 5 df5.Name2.s_str().isdigit()
%timeit -n 5 df5.Name1.s_str().isdigit()
%timeit -n 5 df5.Name.str.isdigit()
8.81 ms ± 209 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.45 ms ± 94 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
8.34 ms ± 77.4 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().rstrip(b'A'))
print(df5.Name1.s_str().rstrip(b'A'))
print(df5.Name.str.rstrip('A'))
%timeit -n 5 df5.Name2.s_str().rstrip(b'A')
%timeit -n 5 df5.Name1.s_str().rstrip(b'A')
%timeit -n 5 df5.Name.str.rstrip('A')
17.5 ms ± 598 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.2 ms ± 208 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
11.9 ms ± 159 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().rsplit(b'A'))
print(df5.Name1.s_str().rsplit(b'A'))
print(df5.Name.str.rsplit('A'))
%timeit -n 5 df5.Name2.s_str().rsplit(b'A')
%timeit -n 5 df5.Name1.s_str().rsplit(b'A')
%timeit -n 5 df5.Name.str.rsplit('A')
29 ms ± 700 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
29.2 ms ± 338 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
22.9 ms ± 215 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().rstrip(b'A'))
print(df5.Name1.s_str().rstrip(b'A'))
print(df5.Name.str.rstrip('A'))
%timeit -n 5 df5.Name2.s_str().rstrip(b'A')
%timeit -n 5 df5.Name1.s_str().rstrip(b'A')
%timeit -n 5 df5.Name.str.rstrip('A')
17.3 ms ± 441 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.3 ms ± 217 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
12.1 ms ± 132 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().match(b'zz'))
print(df5.Name1.s_str().match(b'zz'))
print(df5.Name.str.match('zz'))
%timeit -n 5 df5.Name2.s_str().match(b'zz')
%timeit -n 5 df5.Name1.s_str().match(b'zz')
%timeit -n 5 df5.Name.str.match('zz')
33.6 ms ± 718 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
32.6 ms ± 187 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
26.9 ms ± 286 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().lstrip(b'zz'))
print(df5.Name1.s_str().lstrip(b'zz'))
print(df5.Name.str.lstrip('zz'))
%timeit -n 5 df5.Name2.s_str().lstrip(b'zz')
%timeit -n 5 df5.Name1.s_str().lstrip(b'zz')
%timeit -n 5 df5.Name.str.lstrip('zz')
17.5 ms ± 447 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17 ms ± 178 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
11.8 ms ± 98.1 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().lower())
print(df5.Name1.s_str().lower())
print(df5.Name.str.lower())
%timeit -n 5 df5.Name2.s_str().lower()
%timeit -n 5 df5.Name1.s_str().lower()
%timeit -n 5 df5.Name.str.lower()
13.5 ms ± 224 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
13.3 ms ± 168 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
11.9 ms ± 582 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().ljust(100))
print(df5.Name1.s_str().ljust(100))
print(df5.Name.str.ljust(100))
%timeit -n 5 df5.Name2.s_str().ljust(100)
%timeit -n 5 df5.Name1.s_str().ljust(100)
%timeit -n 5 df5.Name.str.ljust(100)
24.1 ms ± 540 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
23.8 ms ± 144 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
19.7 ms ± 146 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().removesuffix(b'A'))
print(df5.Name1.s_str().removesuffix(b'A'))
print(df5.Name.str.removesuffix('A'))
%timeit -n 5 df5.Name2.s_str().removesuffix(b'A')
%timeit -n 5 df5.Name1.s_str().removesuffix(b'A')
%timeit -n 5 df5.Name.str.removesuffix('A')
22.2 ms ± 672 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
22.2 ms ± 322 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
16.4 ms ± 86.2 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().len())
print(df5.Name1.s_str().len())
print(df5.Name.str.len())
%timeit -n 5 df5.Name2.s_str().len()
%timeit -n 5 df5.Name1.s_str().len()
%timeit -n 5 df5.Name.str.len()
24 ms ± 500 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
23.7 ms ± 275 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.8 ms ± 121 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().fullmatch(rb'(a\w{3})(\w+)'))
print(df5.Name1.s_str().fullmatch(rb'(a\w{3})(\w+)'))
print(df5.Name.str.fullmatch(r'(a\w{3})(\w+)'))
%timeit -n 5 df5.Name2.s_str().fullmatch(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name1.s_str().fullmatch(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name.str.fullmatch(r'(a\w{3})(\w+)')
29.3 ms ± 470 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
29.3 ms ± 330 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
23.9 ms ± 385 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().findall(rb'(a\w{3})(\w+)'))
print(df5.Name1.s_str().findall(rb'(a\w{3})(\w+)'))
print(df5.Name.str.findall(r'(a\w{3})(\w+)'))
%timeit -n 5 df5.Name2.s_str().findall(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name1.s_str().findall(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name.str.findall(r'(a\w{3})(\w+)')
42.8 ms ± 411 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
43.2 ms ± 506 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
39.5 ms ± 314 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().find(rb'(a\w{3})(\w+)'))
print(df5.Name1.s_str().find(rb'(a\w{3})(\w+)'))
print(df5.Name.str.find(r'(a\w{3})(\w+)'))
%timeit -n 5 df5.Name2.s_str().find(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name1.s_str().find(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name.str.find(r'(a\w{3})(\w+)')
40.5 ms ± 641 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
40.4 ms ± 175 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
34.5 ms ± 231 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().extractall(rb'(a\w{3})(\w+)'))
print(df5.Name1.s_str().extractall(rb'(a\w{3})(\w+)'))
print(df5.Name.str.extractall(r'(a\w{3})(\w+)'))
%timeit -n 5 df5.Name2.s_str().extractall(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name1.s_str().extractall(rb'(a\w{3})(\w+)')
%timeit -n 5 df5.Name.str.extractall(r'(a\w{3})(\w+)')
165 ms ± 439 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
167 ms ± 346 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
156 ms ± 308 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().extract(rb'(a\w{3})'))
print(df5.Name1.s_str().extract(rb'(a\w{3})'))
print(df5.Name.str.extract(r'(a\w{3})'))
%timeit -n 5 df5.Name2.s_str().extract(rb'(a\w{3})')
%timeit -n 5 df5.Name1.s_str().extract(rb'(a\w{3})')
%timeit -n 5 df5.Name.str.extract(r'(a\w{3})')
64.7 ms ± 699 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
63.7 ms ± 343 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
55.8 ms ± 352 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().endswith(b'a'))
print(df5.Name1.s_str().endswith(b'a'))
print(df5.Name.str.endswith('a'))
%timeit -n 5 df5.Name2.s_str().endswith(b'a')
%timeit -n 5 df5.Name1.s_str().endswith(b'a')
%timeit -n 5 df5.Name.str.endswith('a')
24.4 ms ± 800 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
23.9 ms ± 97.7 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
18.2 ms ± 160 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().count(re.compile(b'a+')))
print(df5.Name1.s_str().count(re.compile(b'a+')))
print(df5.Name.str.count(re.compile('a+')))
%timeit -n 5 df5.Name2.s_str().count(re.compile(b'a+'))
%timeit -n 5 df5.Name1.s_str().count(re.compile(b'a+'))
%timeit -n 5 df5.Name.str.count(re.compile('a+'))
88.5 ms ± 407 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
94.7 ms ± 280 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
83.4 ms ± 238 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().zfill(100))
print(df5.Name1.s_str().zfill(100))
print(df5.Name.str.zfill(100))
%timeit -n 5 df5.Name2.s_str().zfill(100)
%timeit -n 5 df5.Name1.s_str().zfill(100)
%timeit -n 5 df5.Name.str.zfill(100)
22.9 ms ± 369 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
22.5 ms ± 216 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.9 ms ± 80.3 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().contains(b'a'))
print(df5.Name1.s_str().contains(b'a'))
print(df5.Name.str.contains('a'))
%timeit -n 5 df5.Name2.s_str().contains(b'a')
%timeit -n 5 df5.Name1.s_str().contains(b'a')
%timeit -n 5 df5.Name.str.contains('a')
30.5 ms ± 551 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
30.5 ms ± 287 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.4 ms ± 249 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().pad(width=100, side='both', fillchar=b'-'))
print(df5.Name1.s_str().pad(width=100, side='both', fillchar=b'-'))
print(df5.Name.str.pad(width=100, side='both', fillchar='-'))
%timeit -n 5 df5.Name2.s_str().pad(width=100, side='both', fillchar=b'-')
%timeit -n 5 df5.Name1.s_str().pad(width=100, side='both', fillchar=b'-')
%timeit -n 5 df5.Name.str.pad(width=100, side='both', fillchar='-')
23.9 ms ± 579 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.2 ms ± 411 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
19.5 ms ± 77.7 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().center(width=5))
print(df5.Name1.s_str().center(width=5))
print(df5.Name.str.center(width=5))
%timeit -n 5 df5.Name2.s_str().center(width=5)
%timeit -n 5 df5.Name1.s_str().center(width=5)
%timeit -n 5 df5.Name.str.center(width=5)
17.7 ms ± 368 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
18 ms ± 327 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
12.5 ms ± 75.7 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
```

## Methods much slower than Series.str

```python
print(df5.Name2.s_str().cat())
print(df5.Name1.s_str().cat())
print(df5.Name.str.cat())
%timeit -n 5 df5.Name2.s_str().cat()
%timeit -n 5 df5.Name1.s_str().cat()
%timeit -n 5 df5.Name.str.cat()
14.1 ms ± 706 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
13.9 ms ± 877 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
3.74 ms ± 17.6 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().casefold())
print(df5.Name1.s_str().casefold())
print(df5.Name.str.casefold())
%timeit -n 5 df5.Name2.s_str().casefold()
%timeit -n 5 df5.Name1.s_str().casefold()
%timeit -n 5 df5.Name.str.casefold()
168 ms ± 556 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
200 ms ± 466 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
11.5 ms ± 115 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().join(b'zz'))
print(df5.Name1.s_str().join(b'zz'))
print(df5.Name.str.join('zz'))
%timeit -n 5 df5.Name2.s_str().join(b'zz')
%timeit -n 5 df5.Name1.s_str().join(b'zz')
%timeit -n 5 df5.Name.str.join('zz')
360 ms ± 2.22 ms per loop (mean ± std. dev. of 7 runs, 5 loops each)
366 ms ± 514 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
54 ms ± 271 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().normalize(form='NFC'))
print(df5.Name1.s_str().normalize(form='NFC'))
print(df5.Name.str.normalize(form='NFC'))
%timeit -n 5 df5.Name2.s_str().normalize(form='NFC')
%timeit -n 5 df5.Name1.s_str().normalize(form='NFC')
%timeit -n 5 df5.Name.str.normalize(form='NFC')
173 ms ± 892 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
189 ms ± 688 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
17.7 ms ± 127 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().wrap(10))
print(df5.Name1.s_str().wrap(10))
print(df5.Name.str.wrap(10))
%timeit -n 5 df5.Name2.s_str().wrap(10)
%timeit -n 5 df5.Name1.s_str().wrap(10)
%timeit -n 5 df5.Name.str.wrap(10)
1.48 s ± 67.7 ms per loop (mean ± std. dev. of 7 runs, 5 loops each)
1.55 s ± 25.5 ms per loop (mean ± std. dev. of 7 runs, 5 loops each)
899 ms ± 1.11 ms per loop (mean ± std. dev. of 7 runs, 5 loops each)
#################################################################
print(df5.Name2.s_str().get(1))
print(df5.Name1.s_str().get(1))
print(df5.Name.str.get(1))
%timeit -n 5 df5.Name2.s_str().get(1)
%timeit -n 5 df5.Name1.s_str().get(1)
%timeit -n 5 df5.Name.str.get(1)
45 ms ± 604 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
44.8 ms ± 294 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
24.5 ms ± 644 µs per loop (mean ± std. dev. of 7 runs, 5 loops each)
```
