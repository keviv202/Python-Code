def version_number(s,s1):
    k=s.split('.')
    l=s1.split('.')

    if k[0]>l[0]:
        return s
    elif k[0]==l[0]:
        if k[1]>l[1]:
            return s
        elif l[1]>k[1]:
            return s1
        else:
            return 0
    elif l[0]>k[0]:
        return s1

print (version_number('11.11','11.11'))