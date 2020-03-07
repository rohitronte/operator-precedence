def prec(x):
  if x=='id':
    return 0
  if x=='!':
    return 1
  if x=='~':
    return 2
  if x=='*':
    return 3
  if x=='/':
    return 4
  if x=='+':
    return 5
  if x=='-':
    return 6
  if x=='<<':
    return 7
  if x=='>>':
    return 8
  if x=='&':
    return 9
  if x=='|':
    return 10
  if x=='&&':
    return 11  
  if x=='||':
    return 12
  if x=='$':
    return 13


#opening file
ff= open("input.txt", "r")
#reading line
line = ff.readlines()
#total number of lines
count_lines=len(line)

print ((count_lines))
flag=1
#check operator grammar
operator=['+','-','*','/','&','|','~','>','<','!','&&','||']
for i in range (0,count_lines):
    print (line[i])
    exp=line[i].split('->')
    #print exp[0],exp[1]
    if exp[0]>='A' and exp[0]<='Z' and len(exp[0])==1:
          print ("valid rhs production")

    else: 
          print ("invalid rhs production")
          flag=0
    txt=exp[1].split('%')
    print(txt)
    for i in range (0,len(txt)):
          print (txt[i])
    for i in range (0,len(txt)):
          if '$' in txt[i]:
                 print ("invalid null in production",i+1)
                 flag=0
    for i in range (0,len(txt)):
          for j in range (1,len(txt[i])):
                 if txt[i][j-1]>='A' and txt[i][j-1]<='Z' and txt[i][j]>='A' and txt[i][j]<='Z' :
                      print ("no two consecutive terminals allowed in production",i+1)
                      flag=0
    for i in range (0,len(txt)):
          if len(txt[i])==2:
                 if txt[i][0] not in operator:
                      print ("invalid production(1)",i+1)
                      flag=0
          if len(txt[i])==3:
                 if txt[i][len(txt[i])-2] not in operator:
                      if 'id' not in txt[i]:
                           print ("invalid production(2)",i+1)
                           flag=0
          if len(txt[i])==4:
                 if txt[i][len(txt[i])-2] not in operator and txt[i][len(txt[i])-3] not in operator:
                      print ("invalid production(3)",i+1)
                      flag=0
  
    
    count=0;
    for i in range(0,len(exp[1])):
      if exp[1][i] in operator or exp[1][i]=='i' or exp[1][i]=='d':
        count+=1


    print(count)
    rows,cols=(count+1,count+1) 

    x=1
    
    arr=[[0 for i in range(cols)] for j in range (rows)]
    if flag==1:
      for k in range (0,len(exp[1])):
        if exp[1][k]=='i' and exp[1][k+1]=='d': 
          arr[0][x]='id'
          x=x+1
        if exp[1][k] in operator:
          if exp[1][k]=='<' and exp[1][k+1]=='<':
            arr[0][x]='<<'
            k=k+1
          if exp[1][k]=='>' and exp[1][k+1]=='>':
            arr[0][x]='>>'
            k=k+2
          else:
            arr[0][x]=exp[1][k]
          x=x+1
    

      for m in range (0,len(arr)):
        arr[m][0]=arr[0][m];
    arr[m][0]='$'
    arr[0][x]='$'
  
    print(arr)
    for i in range(1,len(arr)):
      for j in range(1,len(arr)):
        if arr[0][i]=='id' or arr[0][i]=='$':
          if arr[0][i]==arr[j][0]:
            arr[i][j]='--'
          elif(arr[0][i]=='$'):
            arr[i][j]='<'
          elif(arr[0][i]=='id'):
            arr[i][j]='>'
        elif arr[i][0]==arr[0][j]:
          arr[i][j]='>'
        elif prec(arr[i][0])>prec(arr[0][j]):
          arr[i][j]='<'
        elif prec(arr[i][0])<prec(arr[0][j]):
          arr[i][j]='>'
        elif prec(arr[0][j])>prec(arr[0][j]):
          arr[i][j]='<'
        elif prec(arr[i][0])<prec(arr[0][j]):
          arr[i][j]='>'
        

    for i in range(len(arr)):
      for j in range(len(arr[i])):
        print(arr[i][j],"  ", end=' ' )
      print('\n')



    