import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("930x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NOBUKTI:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_BUKU1:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_BUKU2:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL_PINJAM:').grid(row=0, column=3,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL_HRSKEMBALI:').grid(row=1, column=3,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL_DIKEMBALIKAN:').grid(row=2, column=3,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNobukti = Entry(mainFrame) 
        self.txtNobukti.grid(row=0, column=1, padx=5, pady=5)
        self.txtNobukti.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_buku1 = Entry(mainFrame) 
        self.txtKode_buku1.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKode_buku2 = Entry(mainFrame) 
        self.txtKode_buku2.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtTgl_pinjam = Entry(mainFrame) 
        self.txtTgl_pinjam.grid(row=0, column=4, padx=5, pady=5)
        # Textbox
        self.txtTgl_hrskembali = Entry(mainFrame) 
        self.txtTgl_hrskembali.grid(row=1, column=4, padx=5, pady=5)
        # Textbox
        self.txtTgl_dikembalikan = Entry(mainFrame) 
        self.txtTgl_dikembalikan.grid(row=2, column=4, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=5, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=5, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=5, padx=5, pady=5)
        # define columns
        columns = ('id_peminjaman','nobukti','kode_anggota','nama','kode_buku1','kode_buku2','tgl_pinjam','tgl_hrskembali','tgl_dikembalikan')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_peminjaman', text='ID_PEMINJAMAN')
        self.tree.column('id_peminjaman', width="20")
        self.tree.heading('nobukti', text='NOBUKTI')
        self.tree.column('nobukti', width="80")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="110")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('kode_buku1', text='KODE_BUKU1')
        self.tree.column('kode_buku1', width="80")
        self.tree.heading('kode_buku2', text='KODE_BUKU2')
        self.tree.column('kode_buku2', width="80")
        self.tree.heading('tgl_pinjam', text='TGL_PINJAM')
        self.tree.column('tgl_pinjam', width="120")
        self.tree.heading('tgl_hrskembali', text='TGL_HRSKEMBALI')
        self.tree.column('tgl_hrskembali', width="120")
        self.tree.heading('tgl_dikembalikan', text='TGL_DIKEMBALIKAN')
        self.tree.column('tgl_dikembalikan', width="150")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNobukti.delete(0,END)
        self.txtNobukti.insert(END,"")
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtKode_buku1.delete(0,END)
        self.txtKode_buku1.insert(END,"")
        self.txtKode_buku2.delete(0,END)
        self.txtKode_buku2.insert(END,"")
        self.txtTgl_pinjam.delete(0,END)
        self.txtTgl_pinjam.insert(END,"")
        self.txtTgl_hrskembali.delete(0,END)
        self.txtTgl_hrskembali.insert(END,"")
        self.txtTgl_dikembalikan.delete(0,END)
        self.txtTgl_dikembalikan.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_peminjaman"],d["nobukti"],d["kode_anggota"],d["nama"],d["kode_buku1"],d["kode_buku2"],d["tgl_pinjam"],d["tgl_hrskembali"],d["tgl_dikembalikan"]))
    def onCari(self, event=None):
        nobukti = self.txtNobukti.get()
        obj = Peminjaman()
        a = obj.get_by_nobukti(nobukti)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nobukti = self.txtNobukti.get()
        obj = Peminjaman()
        res = obj.get_by_nobukti(nobukti)
        self.txtNobukti.delete(0,END)
        self.txtNobukti.insert(END,obj.nobukti)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtKode_buku1.delete(0,END)
        self.txtKode_buku1.insert(END,obj.kode_buku1)
        self.txtKode_buku2.delete(0,END)
        self.txtKode_buku2.insert(END,obj.kode_buku2)
        self.txtTgl_pinjam.delete(0,END)
        self.txtTgl_pinjam.insert(END,obj.tgl_pinjam)
        self.txtTgl_hrskembali.delete(0,END)
        self.txtTgl_hrskembali.insert(END,obj.tgl_hrskembali)
        self.txtTgl_dikembalikan.delete(0,END)
        self.txtTgl_dikembalikan.insert(END,obj.tgl_dikembalikan)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nobukti = self.txtNobukti.get()
        kode_anggota = self.txtKode_anggota.get()
        nama = self.txtNama.get()
        kode_buku1 = self.txtKode_buku1.get()
        kode_buku2 = self.txtKode_buku2.get()
        tgl_pinjam = self.txtTgl_pinjam.get()
        tgl_hrskembali = self.txtTgl_hrskembali.get()
        tgl_dikembalikan = self.txtTgl_dikembalikan.get()
        # create new Object
        obj = Peminjaman()
        obj.nobukti = nobukti
        obj.kode_anggota = kode_anggota
        obj.nama = nama
        obj.kode_buku1 = kode_buku1
        obj.kode_buku2 = kode_buku2
        obj.tgl_pinjam = tgl_pinjam
        obj.tgl_hrskembali = tgl_hrskembali
        obj.tgl_dikembalikan = tgl_dikembalikan
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nobukti(nobukti)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nobukti = self.txtNobukti.get()
        obj = Peminjaman()
        obj.nobukti = nobukti
        if(self.ditemukan==True):
            res = obj.delete_by_nobukti(nobukti)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()