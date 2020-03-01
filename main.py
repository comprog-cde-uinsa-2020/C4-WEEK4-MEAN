import mean

if __name__ == "__main__":

    listnama = ["Sarah","Budi","Atika","Andre","Sinaga"]
    listnilai1 = [90,75,66,69,90]
    listnilai2 = [78,70,66,69,90]
    listnilai3 = [80,80,90,80,79]

    listSiswa =[]
        
for i in range(5):
    listSiswa.append(mean.Siswa(listnama[i], listnilai1[i], listnilai2[i], listnilai3[i]))
    
for siswa in listSiswa:
    siswa.tampilkan_profil()
    siswa.tampilkan_rata()
