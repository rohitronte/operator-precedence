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
    
    exp=line[i].split('->')
    #print exp[0],exp[1]
    if exp[0]>='A' and exp[0]<='Z' and len(exp[0])==1:
          print ("valid rhs production")

    else: 
          print ("invalid rhs production")
          flag=0
    txt=exp[1].split('%')
    
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

      if  exp[1][i]=='<' and exp[1][i+1] =='<' or exp[1][i]=='>' and exp[1][i+1] =='>':
        count-=1



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
            x=x-1
          if exp[1][k]=='>' and exp[1][k+1]=='>':
            arr[0][x]='>>'
            k=k+1
            x=x-1
          if exp[1][k]!='>' and exp[1][k]!='<':
            arr[0][x]=exp[1][k]

            
          x=x+1
    

      for m in range (0,len(arr)):
        arr[m][0]=arr[0][m];
      arr[m][0]='$'
      arr[0][x]='$'
    
    


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



import sys
import shlex
import csv
#Write a program which will provide an implementation of operator precedance parser. Read an operator grammar and precedance table from input file/files (file for grammar, file for precedence). Read an input sentence and show the step by step parsing of that given sentence.

def issodd(x):
  if(x%2==0):
    return 0
  else:
    return 1
def main():
  
  input_string = "i+i-i"
  input_ind = list(shlex.shlex(input_string))
  input_ind.append('$')
  
  master = {}
  master_list = []
  new_list = []
  non_terminals = []
  grammar = open('grammar.txt', 'r')
  
  for row2 in grammar:
    
    if '->' in row2:
    
      if len(new_list) == 0:
        start_state = row2[0]
        non_terminals.append(row2[0])
        new_list = []
        new_list.append(row2.rstrip('\n'))
      else:
        master_list.append(new_list)
        del new_list
        new_list = []
        new_list.append(row2.rstrip('\n'))
        non_terminals.append(row2[0])
        
    
    elif '%' in row2:
      new_list.append(row2.rstrip('\n'))
    print(row2)
  
  master_list.append(new_list)
  
  
  for x in range(len(master_list)):
    for y in range(len(master_list[x])):
      master_list[x][y] = [s.replace('%', '') for s in master_list[x][y]]
      master_list[x][y] = ''.join(master_list[x][y])
      print(master_list[x][y])
      master[master_list[x][y]] = non_terminals[x] 

  for key, value in master.items():
    if '->' in key:
      length = len(key)
      for i in range(length):
        if key[i] == '-' and key[i + 1] == ">":
          index =  i+2
          break
      var_key = key
      new_key = key[index:]
  
  print(var_key,new_key)
  var = master[var_key]
  del master[var_key]
  master[new_key] = var 
  
  order_table = []
  with open('order.csv', 'r') as file2:
    order = csv.reader(file2)
    for row in order:
      order_table.append(row)
  
  operators = order_table[0]
  print (order_table)

  stack = []

  stack.append('$') 
  
  
  print ("Stack", "\t\t\t\t", "Input", "\t\t\t\t", "Precedence relation", "\t\t", "Action")
  
  vlaag = 1
  arr1=[]
  while vlaag :
    if input_ind[0] == '$' and len(stack)==2: 
      vlaag = 0

    length = len(input_ind)

    buffer_inp = input_ind[0] 
    temp1 = operators.index(str(buffer_inp))
    s=1
    s+=s
    print ("stack",stack, stack[-1])
    print(len(stack))
    
    if stack[-1] in non_terminals:
      buffer_stack = stack[-2]
    else:
      buffer_stack = stack[-1]
    
    temp2 = operators.index(str(buffer_stack))
    #print buffer_inp, buffer_stack
          
    precedence = order_table[temp2][temp1]
      
    if precedence == '<':
      action = 'shift'
    elif precedence == '>':
      action = 'reduce'
        
    print (stack, "\t\t", input_ind, "\t\t", precedence, "\t\t", action, "\n")
    
    if action == 'shift':
      stack.append(buffer_inp)
      input_ind.remove(buffer_inp)
      if(stack[-1:] not in operators):
                #print(stack[-1:])
                                temp=''.join(stack[1:])
                                arr1.append(temp)
    elif action == 'reduce':
      for key, value in master.items():
        var1 = ''.join(stack[-1:])
        var2 = ''.join(stack[-3:])
        #print(master.items())
        #print(var1,var2)
        if str(key) == str(buffer_stack):
          stack[-1] = value
          break
        elif key == var1 or stack[-3:]==list(var1):
          stack[-3:] = value
          break
        elif key == var2:
          stack[-3:] = value  
      if(stack[-1:] not in operators):
  
                                temp=''.join(stack[1:])
                                arr1.append(temp) 
    del buffer_inp, temp1, buffer_stack, temp2, precedence
    
    if vlaag == 0:
      print ("Accepted!!")
  
  temp=""
  l=0
  print(arr1)
  print(input_string)
  for i in range(len(arr1)):
    if (len(arr1[i])==3 or len(arr1[i])==5 or len(arr1[i])==7 or len(arr1[i])==9):
      if arr1[i][2]=='i':
        temp=(arr1[i])+input_string[l+3:]
      elif arr1[i][2]=='E':
        temp=(arr1[i])+input_string[l+3:]
        l+=2

      print(temp)


  print('E')  


  return 2
  
if __name__ == "__main__":
  sys.exit(main())


    










	
