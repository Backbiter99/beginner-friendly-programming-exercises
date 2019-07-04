a = float(input('Enter the amount of money you have: '))
b = float(input('Enter the value of Bitcoin: '))
c = float(input('Enter the value of Ethereum: '))
d = float(input('Enter the value of Litecoin: '))

e = int( a / b )
f = int( a / c )
g = int( a / d )

print('With',a,'dollars you can buy:',e,'Bitcoins,',f,'Ethereum,',g,'Litecoin')