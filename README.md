# Header level 1
## header level 2
#### header level 4
-
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing.

This data was colected from [Kaggle](https://www.kaggle.com/datasets/mhadani/predictive-maintenance-aircraft-engine).
--
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing

* This is a star
* Another star

1. This is a number
2. another number

- This is dash
- another dash


The followig code does this....
``` python
def showTables():
    query = """SHOW TABLES;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df
```
The above code does this...

|Names|Designation|
|------|-----------|
|DevA | Developer |
|DevV | CTO |


![Image](https://lh7-us.googleusercontent.com/bQpKg-LfPjmUufGQhiZAZwfxEfPgeor8_cQWqEdOYoLq4MWwPpbPUhUVJujcLOSp-C1EUiveGwGtWjsxOU3yJ3niKcnDQkYZ-BMbHg37HewNUucMPKYnHDHrpDNXu_VWZ0gQDOUQU93TKhauhcamNXs)
