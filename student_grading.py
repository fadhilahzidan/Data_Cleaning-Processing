# Membuat Function Cleaning NIM
while True:
    def cleaning_nim(file_location):
        file = open(file_location)
        next(file) # Melewati 1 Baris agar header tidak terhitung
        data = []
        rm = ['TT','T']
        data_new= []
        h = []
        for nama in file:
            kolom = nama.split(',') #
            # Menukar Nilai dengan NIM Jika Tidak sesuai dengan tempatnya
            if len(kolom[0]) < 7:
                if len(kolom[1]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[1]
                    kolom[1] = temp
                elif len(kolom[2]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[2]
                    kolom[2] = temp
                elif len(kolom[3]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[3]
                    kolom[3] = temp
                elif len(kolom[4]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[4]
                    kolom[4] = temp
                elif len(kolom[5]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[5]
                    kolom[5] = temp
                elif len(kolom[6]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[6]
                    kolom[6] = temp
            elif len(kolom[0])>7:
                pass
            else:
                continue
            b = len(kolom)-1
            if b > 6:
                kolom[b] = kolom[b].rstrip()
                if kolom[b] == '':
                    del kolom[b]
            else:
                kolom[6] = kolom[6].rstrip()
            data.append(list(kolom))

        for i in range(len(data)):
            for j in range(len(data[i])):
                for x in data[i][j]:
                    if x in rm:
                        h.append(i)
        for i in range(len(data)):
            if i in h:
                continue
            else:
                data_new.append(data[i])

        file.close()
        return data_new

    # Membuat Function Double Cleaning NIM
    def cleaning_double(lst):
        temp_lst = []
        rmv = []
        new_lst = []
        for i in range(len(lst)):
            temp_lst.append(lst[i][0])
        for k in range(len(lst)):
            for j in range(k+1,len(lst)):
                if temp_lst[k] == temp_lst[j]:
                    rmv.append(k)
        for i in range(len(lst)):
            if i in rmv :
                continue
            else:
                new_lst.append(lst[i])
        return new_lst

    # Membuat Function untuk cek Nilai/NIM yang tidak sesuai ( ada huruf )
    def cleaning_nilai_huruf(lst):
        abjad = {'e':'3', 's':'5', 't':'7','b':'8'}
        for k in range(len(lst)):
            for b in range(len(lst[0])):
                for c in lst[k][b]:
                    for key,value in abjad.items():
                        if c.lower() in key:
                            lst[k][b] = lst[k][b].replace(c,value)  
        return lst              

    #  Membuat Function Mengubah Tipe data Tugas1 - UAS menjadi int
    def cleaning_tipe(lst):
        for k in range(len(lst)):
            for b in range(1,len(lst[k])):
                if lst[k][b] is not str:
                    lst[k][b] = int(lst[k][b])
        return lst

    # Membuat Function Jika ada nilai 0 / None akan di ubah menjadi 50
    def cleaning_baris(lst):
        for k in range(len(lst)):
            for b in range(1,7):
                if lst[k][b] == 0 or lst[k][b] == None or lst[k][b] == '0':
                    lst[k][b] = 50
        return lst

    # Membuat Function untuk Cek Anomali Data Nilai > 100 | Nilai < 0 di ubah dengan 80 dan 20
    def cleaning_anomali(lst):
        for k in range(len(lst)):
            for b in range(1,7):
                if lst[k][b] > 100:
                    lst[k][b] = 80
                elif lst[k][b] < 0:
                    lst[k][b] = 20
        return lst

    # Membuat Function Untuk mengecek apakah panjang dari NIM sudah sesuai jika belum disesuaikan
    def cleaning_pnjgnim(lst):
        for k in range(len(lst)):
            pjg = len(lst[k][0]) 
            if pjg < 10:
                while pjg < 10:
                    lst[k][0] += '0'
                    pjg +=1

            elif pjg > 10:
                while pjg > 10:
                    lst[k][0] = lst[k][0][:-1]
                    pjg -= 1
        return lst

    # Membuat Function Untuk Menyesuaikan jika ada baris yang melebihi seharusnya
    def cleaning_lebihkolom(lst):   
        for k in range(len(lst)):
            pnjg = len(lst[k])-1
            if pnjg > 6:
                if lst[k][pnjg] % 2 ==0:
                    lst[k][5] = lst[k][pnjg]
                    lst[k].remove(lst[k][pnjg])
                else:
                    lst[k][6] = lst[k][pnjg]
                    lst[k].remove(lst[k][pnjg])
        return lst

    # Membuat Function Untuk Menghitung Mean
    def mean(data): #Masukanya harus dengan kutip 2 ('NamaKolom')
        jmlh = 0
        mean = 0
        for k in range(1,len(lst)):
            jmlh += lst[k][data]
        mean = jmlh // len(lst)
        return mean

    # Membuat Function Untuk Menghitung Median
    def median(data):
        new_lst =[]
        for k in range(1,len(lst)):
            new_lst.append(lst[k][data])
        if len(new_lst) % 2 == 0:
            q1 = new_lst[len(new_lst) // 2]
            q2 = new_lst[len(new_lst) // 2 - 1]
            median = (q1 + q2) / 2
        else:
            median = new_lst[len(new_lst) // 2]
        return median

    # Membuat Function Untuk Menghitung Standart Deviasi
    def standart_deviasi(data):
        new_lst = []
        x = 0
        for k in range(1,len(lst)):
            new_lst.append(lst[k][data])
        for j in new_lst:
            x += (j-mean(data))**2
        varian = x / len(new_lst)
        standar_deviasi = varian**0.5
        return standar_deviasi


    # Menjawab Pertanyaan
    def nilai_uts_tinggi(lst):
        def element(elem):
            return elem[5]
        tinggi = sorted(lst, key=element,reverse=True)
        return tinggi[0][0]

    def nilai_uas_terendah(lst):
        def element(elem):
            return elem[6]
        tinggi = sorted(lst, key=element)
        return tinggi[0][0]
    
    def qui1_di_atas_rata2(lst):
        quiz1_atas_mean = []
        for i in range(len(lst)):
            if lst[i][3] > mean(3):
                quiz1_atas_mean.append(lst[i][0])
        return quiz1_atas_mean
    
    def tugas2_di_atas_rata2(lst):
        tugas2_atas_mean = []
        for i in range(len(lst)):
            if lst[i][2] > mean(2):
                tugas2_atas_mean.append(lst[i][0])
        return tugas2_atas_mean
    
    def quiz2_di_bawah_median(lst):
        quiz2_bawah_median = []
        for i in range(len(lst)):
            if lst[i][4] < median(4):
                quiz2_bawah_median.append(lst[i][0])
        return quiz2_bawah_median

    def tugas1_di_bawah_median(lst):
        tugas1_bawah_median = []
        for i in range(len(lst)):
            if lst[i][1] < median(1):
                tugas1_bawah_median.append(lst[i][0])
        return tugas1_bawah_median

    def lst_nilai_akhir(lst):
        lst_rata_rata= []
        def element(elem):
            return elem[1]
        for i in range(len(lst)):
            jmlh = 0
            for j in range(1,len(lst[i])):
                jmlh+= lst[i][j]
            meann = jmlh / len(lst[i])
            c = [lst[i][0],meann]
            lst_rata_rata.append(c)
        return sorted(lst_rata_rata,key=element)

    def pencilan(lst):
        pecilan_bawah = []
        pecilan_atas = []
        kurang_mean = []
        jmlh = 0
        if len(lst) % 2 == 0:
            q2 = 2 * (len(lst)+1)/4 
            q1 = 1 * (len(lst)+1)/4 
            q3 = 3 * (len(lst)+1)/4
            q2 = lst[int(q2)][1]+lst[int(q2+1)][1] / 2
            q3 = lst[int(q3)][1]+lst[int(q3+1)][1] / 2
            q1 = lst[int(q1)][1]+lst[int(q1+1)][1] / 2
        else:
            q2 = lst[len(lst) // 2][1]
            q1 = lst[(len(lst) // 2) // 2][1]
            q3 = lst[(len(lst) // 2) + ((len(lst) // 2) // 2)][1]
        l = 1.5*(q3-q1)
        pd_dalam = q1 - l
        pd_luar = q3 + l
        for i in range(len(lst)):
            jmlh += lst[i][1]
        mean_seluruh = jmlh / len(lst)

        for i in range(len(lst)):
            if lst[i][1]<mean_seluruh:
                kurang_mean.append(lst[i][0])
        for i in range(len(lst)):
            if lst[i][1] < pd_dalam:
                pecilan_bawah.append(lst[i][0])
            elif lst[i][1] > pd_luar:
                pecilan_atas.append(lst[i][0])
        return kurang_mean,pecilan_bawah,pecilan_atas


    # Tampilan file .csv        
    masukan = input('\n\nMasukan Lokasi File Dataset (.csv) yang digunakan : \nContoh : C:\\Users\\Documents\\dataset3.csv \n\nLokasi File :\n')
    f = open('dataset_fixed.csv','w')
    lst = cleaning_nim(masukan)
    lst = cleaning_double(lst)
    lst = cleaning_nilai_huruf(lst)
    lst = cleaning_tipe(lst)
    lst = cleaning_baris(lst)
    lst = cleaning_anomali(lst)
    lst = cleaning_pnjgnim(lst)
    lst = cleaning_lebihkolom(lst)
    nilai_tinggi_uts = nilai_uts_tinggi(lst)
    nilai_rendah_uas = nilai_uas_terendah(lst)
    quiz1_atas_mean = qui1_di_atas_rata2(lst)
    tugas2_atas_mean = tugas2_di_atas_rata2(lst)
    quiz2_bawah_median = quiz2_di_bawah_median(lst)
    tugas1_bawah_median = tugas1_di_bawah_median(lst)
    rata_kslrh_sort = lst_nilai_akhir(lst)
    kurang_mean,pecilan_bawah,pecilan_atas = pencilan(rata_kslrh_sort)
    header = ['NIM','TUGAS1','TUGAS2','QUIZ1','QUIZ2','UTS','UAS']
    lst.insert(0,header)
    
    for k in lst:
        string = ','.join(map(str,k))
        f.write(string+'\n')
    f.close

    f = open('hasil','w')
    f.write('HASIL :\n')
    mean1 = mean(1)
    mean2 = mean(2)
    mean3 = mean(3)
    mean4 = mean(4)
    mean5 = mean(5)
    mean6 = mean(6)
    median1 = median(1)
    median2 = median(2)
    median3 = median(3)
    median4 = median(4)
    median5 = median(5)
    median6 = median(6)
    std1 = standart_deviasi(1)
    std2 = standart_deviasi(2)
    std3 = standart_deviasi(3)
    std4 = standart_deviasi(4)
    std5 = standart_deviasi(5)
    std6 = standart_deviasi(6)
    f.write(f'Mean, Median, Standart Deviasi untuk Tugas 1 : {mean1}, {median1}, {std1:.2f}\n')
    f.write(f'Mean, Median, Standart Deviasi untuk Tugas 2 : {mean2}, {median2}, {std2:.2f}\n')
    f.write(f'Mean, Median, Standart Deviasi untuk Quiz 1  : {mean3}, {median3}, {std3:.2f}\n')
    f.write(f'Mean, Median, Standart Deviasi untuk Quiz 2  : {mean4}, {median4}, {std4:.2f}\n')
    f.write(f'Mean, Median, Standart Deviasi untuk UTS     : {mean5}, {median5}, {std5:.2f}\n')
    f.write(f'Mean, Median, Standart Deviasi untuk UAS     : {mean6}, {median6}, {std6:.2f}\n\n')
    f.write(f'Nilai Tertinggi UTS Dengan NIM      : {nilai_tinggi_uts}\n')
    f.write(f'Nilai Terendah UAS Dengan NIM       : {nilai_rendah_uas}\n')
    f.write('\nNilai Quiz 1 Di Atas Rata-rata Dengan NIM :\n')
    for j,i in enumerate(quiz1_atas_mean):
        f.write(f'{j+1}\t{i}\n')
    f.write('\nNilai Tugas 2 di atas Rata-rata Dengan NIM :\n')
    for j,i in enumerate(tugas2_atas_mean):
        f.write(f'{j+1}\t{i}\n')
    f.write('\nNilai Quiz 2 di bawah Median Dengan NIM :\n')
    for j,i in enumerate(quiz2_bawah_median):
        f.write(f'{j+1}\t{i}\n')
    f.write('\nNilai Tugas 1 di bawah median Dengan NIM :\n')
    for j,i in enumerate(tugas1_bawah_median):
        f.write(f'{j+1}\t{i}\n')
    f.write('\nNilai Keseluruhan (pencilan bawah) Dengan NIM :\n')
    for j,i in enumerate(pecilan_bawah):
        f.write(f'{j+1}\t{i}\n')
    f.write('\nNilai Keseluruhan (pencilan atas) Dengan NIM :\n')
    for j,i in enumerate(pecilan_atas):
        f.write(f'{j+1}\t{i}\n')
    f.write(f'\nNilai Keseluruhan di bawah mean Dengan NIM  :\n')
    for j,i in enumerate(kurang_mean):
        f.write(f'{j+1}\t{i}\n')
    f.close()

    if input("\nProgram dijalankan ulang? (Y/N) : ").strip().lower() != 'y':
        break
