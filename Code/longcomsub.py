#!/usr/bin/env python3

# Δημιουργούμε μια συνάρτηση η οποία δέχεται σαν είσοδο δύο συμβολοσειρές και επιστρέφει την μέγιστη κοινή υποακολουθία τους.
def lcs_weighted(S1, S2, d, r , e):
	m = len(S1) # Αποθηκεύουμε το μήκος της S1
	n = len(S2) # Το ίδιο για την S2
	
	L = [[0 for x in range(n+1)] for x in range(m+1)] # Ετοιμάζουμε έναν πίνακα n*m που θα χρησιμοποιήσουμε ως πίνακα Δυναμικού προγραμματισμού
	
	# Υπολογίζουμε το κάθε D(i,j)
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = (i+j)*d
			else:
				L[i][j] = min((L[i-1][j] + d), (L[i][j-1] + d), (L[i-1][j-1] + t(S1, S2, i, j, e, r)))
				
				
	#print (L)
				
	i = m
	j = n
	position=0
	max_position=0
	length=0
	max_length=0
	
	while i > 0 or j > 0:
		
		left=L[i][j-1]
		up=L[i-1][j]
		diag=L[i-1][j-1]
		direction = get_minvalue([left,up,diag])
		
		print("current cell:", L[i][j],'\n'+"max_length:", max_length,'\n'+"max_position:", max_position, '\n'+"direction:", direction,'\n'+"LCS: " + S1[max_position:max_position+max_length],'\n')
		
		match direction:
			case 0:
				if length>max_length:
						max_length=length
						length=0
						max_position=position
				j-=1
				
			case 1:
				if length>max_length:
						max_length=length
						length=0
						max_position=position
				i-=1
				
			case 2:
				if S1[i-1]==S2[j-1]:
					length+=1
					position=i-1
				elif length>max_length:
					max_length=length
					length=0
					max_position=position
					
				i=i-1
				j=j-1
				
	if length>max_length:
		max_length=length
		max_position=position
		
		
	# Printing the sub sequences
	print("S1 : " + S1 + "\nS2 : " + S2)
	print("LCS: " + S1[max_position:max_position+max_length])
	
	
	
def t(S1, S2, i, j, e, r):
	
	if S1[i-1] == S2[j-1]:
		return e
	else:
		return r
	
	
def get_minvalue(inputlist): #Επιστρέφει το index της ελλάχιστης τιμής μέσα σε μια λίστα
	
	#get the minimum value in the list
	min_value = min(inputlist)
	
	#return the index of minimum value 
	min_index=inputlist.index(min_value)
	return min_index 



S1 ="kalimera"
S2 ="oli mera kai oli nixta"

#Βάρος Ένθεσης / Διαγραφής (gap)
d=1 

#Βάρος Αντικατάστασης (missmatch)
r=2

#Βάρος Ταιριάσματος (match)
e=0

#Βρες την μέγιστη κοινή υποακολουθία των S1, S2.
lcs_weighted(S1, S2, d, r, e)
