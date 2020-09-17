#Created by Dawn
n,v=input().split(' ')
a=[]#Inventory list
b=[]#cost performance ratio list
m=[]#Value list
price=[]#Price list
v=int(v)
ans=0
for i in range(int(n)):
    num,p,c=input().split(' ')
    a.append(int(num))
    b.append(int(c)/int(p))
    m.append(int(c))
    price.append(int(p))
while 1:
    try:
        good=max(b)
        ind=b.index(good)
        if a[ind]*price[ind]>=v:

            num=v//price[ind]
            ans+=num*m[ind]
            v-=num*price[ind]
            a.remove(a[ind])
            b.remove(b[ind])
            m.remove(m[ind])
            price.remove(price[ind])  
            if v>=min(price):
                continue
            else:
                break
        else:
            ans+=m[ind]*a[ind]
            v=v-a[ind]*price[ind]
            a.remove(a[ind])
            b.remove(b[ind])
            m.remove(m[ind])
            price.remove(price[ind])    
    except ValueError:
        break
print(ans)
    
