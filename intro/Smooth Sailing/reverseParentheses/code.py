def reverseParentheses(s):
    for haik in range(int(s.count('('))):
        a=s.rfind('(')
        b=s.find(')',a)
        c=s[b-1:a:-1]
        d=s[a:b+1]
        s=s.replace(d,c)
    return s
