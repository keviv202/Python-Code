def split_string(source,splitlist):
  output=[ ]
  isSplit=True
  for cha in source:
      if(cha in splitlist):
          isSplit=True
      else:
          if isSplit:
              output.append(cha)







source = "This is a test-of the,string separation-code!"
print (split_string(source,"!-"))
