n=int(input())
def latex(n):
    def findloc(index,s):
        for i in range(index,len(s)):
            if s[i]=="{":
                j=1
                flag=True
                while s[i+j]!="}":
                    if s[i+j] not in [str(r) for r in range(10)]:
                        flag=False
                        break
                    j=j+1
                if flag:
                    return [i,s[i+1:i+j]]
                    
        return None
    if n==1:
        return 1
    elif n==2:
        return "1+\\frac{2}{3}"
    else:
        s=latex(n-1)
        index=0
        while findloc(index,s) is not None:
            f=findloc(index,s)
            index=f[0]+len(f[1])+1
            first=int(f[1])*2
            second=first+1
            s=s[0:index]+"+\\frac{"+str(first)+"}{"+str(second)+"}"+s[index:]
            index=index+10+len(str(first))+len(str(second))
        return s
            
            
    
        
print(latex(n))