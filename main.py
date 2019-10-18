nama = 'Siti Estiya Pujiningtiyas'
program = 'Hukum Newton 1'

print(f'Program{program} oleh {nama}')

def hitung_HK1_Newton(massa, percepatan) :
    HK1_Newton = massa * percepatan
    print(f'massa = {massa/1}kg mengalami sebuah percepatan = {percepatan/1} m/s**')
    print(f'Sehingga HK1_Newton = {HK1_Newton} N')
    return HK1_Newton

#massa
#percepatan
HK1_Newton = hitung_HK1_Newton(5, 0)
HK1_Newton = hitung_HK1_Newton(50, 0)

keterangan = 'HK 1 Newton menjelaskan tentang kelembaman benda ditandai dengaan tidak adanya perpindahan selama gaya yang diberikan = 0'

print(f'keterangan{keterangan}')

program = 'Hukum Newton 2'

print(f'program{program}')

def hitung_HK2_Newton(massa, percepatan) :
    HK2_Newton = massa * percepatan
    print(f'massa = {massa/1}kg mengalami sebuah percepatan = {percepatan/1} m/s**')
    print(f'Sehingga HK2_Newton = {HK2_Newton} N')
    return HK2_Newton

#massa
#percepatan
HK2_Newton = hitung_HK2_Newton(5, 3)
HK2_Newton = hitung_HK2_Newton(50, 2)

keterangan = "Hukum 2 Newton menjelaskan bahwa apabila sebuah benda bermassa dikenai sebuah Gaya sebesar N maka akan mengalami sebuah percepatan dimana percepatannya tidak sama dengan 0"

print(f'keterangan{keterangan}')

program = 'Hukum 3 Newton'

print(f'program{program}')

def hitung_HK3_Newton(Gaya1, Gaya2) :
    HK3_Newton = Gaya1
    HK3_Newton = -Gaya2
    print(f'Gaya1 = {Gaya1/1}N akan mengalami sebuah gaya yang berlawanan arah  = {-Gaya2/1}N')
    print(f'Sehingga HK3_Newton = {HK3_Newton} N')
    return HK3_Newton

#aksi
#reaksi
HK3_Newton = hitung_HK3_Newton(5, 5)
HK3_Newton = hitung_HK3_Newton(15, 15)

keterangan = 'Hukum 3 Newton menjelaskan tentang sebuah aksi = -reaksi, sehingga apabila sebuah benda bermassa m mengalami sebuah Gaya maka benda tersebut juga akan mengalami akan mengalami reaksi Gaya sebelumnya yang ditandai dengan tanda (-) sebagai tanda berlawanan'

print(f'keterangan{keterangan}')
