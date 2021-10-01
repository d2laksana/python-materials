# Control Flow
Pada kehidupan nyata terkadang kita perlu membuat keputusan dan apa yang harus dilakukan berdasarkan keputusan tersebut. Atau kita melakukan pekerjaan yang sama dan berulang.

Hal serupa juga ada dalam pemrograman, dimana kita perlu membuat keputusan atau mengulang pekerjaan yang sama. Istilah tersebut yaitu **pemilihan/percabangan (_selection_)** dan **pengulangan (_looping_)**.

<div align="center">
    <img src="../../images/control_flow.png" alt="Control FLow" />
</div>

## Pemilihan (Selection)
Adakalanya sebuah aksi dikerjakan jika memenuhi persyaratan (kondisi) tertentu. 

Misalkan saat di persimpangan jalan terdapat traffic light. Jika lampu berwarna merah, maka kendaraan harus berhenti. Langkah ini dapat kita tulis dalam instruksi berikut:

> Jika lampu traffic light berwarna merah, maka kendaraan berhenti.

Bentuk instruksi seperti di atas dinamakan **percabangan**, dan dalam bentuk algoritma dapat ditulis sebagai berikut:
```
1. MULAI
2. Deklarasikan variabel lampu = "merah"
3. JIKA lampu = "merah", MAKA
        Cetak "Kendaraan berhenti"
4. SELESAI
```

#### Contoh 1. Algoritma menentukan bilangan ganap/ganjil
```
Langkah 1 - MULAI
Langkah 2 - Deklarasikan variabel bilangan n
Langkah 3 - Tentukan nilai n
Langkah 4 - JIKA n habis dibagi 2, MAKA
                Cetak "Genap"
Langkah 5 - JIKA TIDAK, MAKA
                Cetak "Ganjil"
Langkah 6 - SELESAI
```