d={'item': 'item1', 'amount': 400}
d1={'item': 'item2', 'amount': 300}
for key in d1:
    if key in d:
        d1[key] = d[key] + d1[key]
    else:
        pass
          
print(d1)