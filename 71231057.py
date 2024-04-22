#!/usr/bin/env python
# coding: utf-8

# In[8]:


def bandingkan_file(file1, file2):

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()


    for i, (line1, line2) in enumerate(zip(lines1, lines2)):
        if line1 != line2:
            print(f"Perbedaan pada baris {i+1}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}\n")

    if len(lines1) != len(lines2):
        if len(lines1) > len(lines2):
            print("File 1 memiliki lebih banyak baris")
        else:
            print("File 2 memiliki lebih banyak baris")

file1 = 'file1.txt'
file2 = 'file2.txt'
bandingkan_file(file1, file2)


# In[ ]:


def baca_soal(file):
    soal = []
    with open(file, 'r') as f:
        for line in f:
            pertanyaan, jawaban = line.strip().split("||")
            soal.append((pertanyaan.strip(), jawaban.strip()))
    return soal

def main():
    file_soal = "soal.txt"
    soal = baca_soal(file_soal)

    print(f"Nama file: {file_soal}")
    for pertanyaan, jawaban in soal:
        print(pertanyaan)
        jawab = input("Jawab: ").strip().lower()
        if jawab == jawaban.lower():
            print("Jawaban benar!\n")
        else:
            print("Jawaban salah!\n")

if __name__ == "__main__":
    main()


# In[ ]:




