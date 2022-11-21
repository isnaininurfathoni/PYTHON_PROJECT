#code by_isnaininurfathoni
#NIM 210104009
def password():
	print("=====CREATE PASSWORD=====")
	input_password=input("masukan password :")
	panjang_chr=len(input_password)
	if panjang_chr <12:
		print("Error,minimal password 12 karakter")
	elif panjang_chr >=12:
		if input_password[0]!="@":
 			print ('password invalid')
 			password ()
		elif input_password[0]=="@":
						print("password diterima\nPassword anda :",input_password)
password ()