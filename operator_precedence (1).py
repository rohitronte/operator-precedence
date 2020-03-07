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
