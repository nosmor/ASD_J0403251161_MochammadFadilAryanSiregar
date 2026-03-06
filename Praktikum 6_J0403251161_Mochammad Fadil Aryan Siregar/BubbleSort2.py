# --------------------------------------
# Nama : Mochammad Fadil Aryan Siregar
# Kelas : TPL A1
# NIM : J0403251161
# --------------------------------------

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            #agar descending, pembanding diubah menjadi < agar ditukar dengan yang paling kecil dan diurutkan
            if alist[i]<alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
