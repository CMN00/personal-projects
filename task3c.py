holder = ['jack', 'jill', 'jon', 'bill', 'nathan', 'felix']
balances = [100,200,300,250,500,600]
pairs = list(zip(holder,balances))
pairs.sort(key=lambda x: x[1], reverse=True)
            
pairs = pairs[:3]
print('the top 3 account hodlers are:', pairs)



