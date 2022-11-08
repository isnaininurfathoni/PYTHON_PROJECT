import socket
import struct
import ipaddress

#code menu dan input pilihan 
def menu():
   print('*************************************************')
   print('CALCULATOR IP ADDRESS')
   print('*************************************************')
   print('Silahkan Pilih :')
   print('1.Menentukan Class IP ADDRESS')
   print('2.Menghitung Subnet mask')
   print('3.Konversi IP ADDRESS ke Biner')
   print('*************************************************')


print(menu())
pilih=int(input('Silahkan masukan pilihan anda |1|2|3| :'))
if pilih==1:
    x=int(input('Masukan Oktet pertama pada IP ADDRESS :'))
    if(x in range(0,127)):
      print('IP tersebut masuk dalam kelas A')
    elif(x in range(128,191)):
      print('IP tersebut masuk dalam kelas B')
    elif(x in range(192,223)):
      print('IP tersebut masuk dalam kelas C')
    elif(x in range(224,240)):
      print('IP tersebut masuk dalam kelas D')
    else:
       print('IP tersebut masuk dalan kelas E')



elif pilih==2:
    x=input(str('Masukan IP : '))

    z=ipaddress.IPv4Network(x)

    print('netmask:'+ str(z.netmask))
    print('network address :'+ str(z.network_address))

elif pilih==3:
    ip=input('Masukan IP:')
    dec_to_bin = lambda ip4: bin(struct.unpack('!I', socket.inet_pton(socket.AF_INET, ip4))[0])
    print ('Biner dari IP anda adalah :',dec_to_bin(ip))
elif pilih==4:
  print('menu tidak tersedia')
print(pilih)



b=input('Apakah anda ingin kembali ke menu awal? [Y/n]?')

if b=='Y':
  print(menu())

elif b=='n':
  print('')