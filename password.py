#code by_isnaininurfathoni
#NIM 210104009

def password():
	input_password=str(input("masukan password :"))
	list_pass=[]
	list_pass.append(input_password)
	chr=len(input_password)
	if chr <12:
		print("Error,minimal password 12 karakter")
	elif chr >=12:
		#first_char=list_pass
		if list_pass[0]!="@":
 			print ('password invalid')
 			password ()
		elif list_pass[0]=="@":
			 print("password diterima")
						
password ()