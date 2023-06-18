import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("790x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NIM:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_ANGGOTA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=0, column=1, padx=5, pady=5)
        # Textbox
        self.txtNim = Entry(mainFrame) 
        self.txtNim.grid(row=1, column=1, padx=5, pady=5)
        self.txtNim.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_anggota = Entry(mainFrame) 
        self.txtNama_anggota.grid(row=2, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk = StringVar()
        Cbo_jk = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk) 
        Cbo_jk.grid(row=3, column=1, padx=5, pady=5)
        # Adding jk combobox drop down list
        Cbo_jk['values'] = ('Laki-laki','Perempuan')
        Cbo_jk.current()
        # Textbox
        self.txtProdi = Entry(mainFrame) 
        self.txtProdi.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_anggota','kode_anggota','nim','nama_anggota','jk','prodi','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_anggota', text='ID_ANGGOTA')
        self.tree.column('id_anggota', width="20")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('nim', text='NIM')
        self.tree.column('nim', width="100")
        self.tree.heading('nama_anggota', text='NAMA_ANGGOTA')
        self.tree.column('nama_anggota', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="90")
        self.tree.heading('prodi', text='PRODI')
        self.tree.column('prodi', width="60")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="200")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtNim.delete(0,END)
        self.txtNim.insert(END,"")
        self.txtNama_anggota.delete(0,END)
        self.txtNama_anggota.insert(END,"")
        self.txtJk.set("")
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_anggota"],d["kode_anggota"],d["nim"],d["nama_anggota"],d["jk"],d["prodi"],d["alamat"]))
    def onCari(self, event=None):
        nim = self.txtNim.get()
        obj = Anggota()
        a = obj.get_by_nim(nim)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nim = self.txtNim.get()
        obj = Anggota()
        res = obj.get_by_nim(nim)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txtNim.delete(0,END)
        self.txtNim.insert(END,obj.nim)
        self.txtNama_anggota.delete(0,END)
        self.txtNama_anggota.insert(END,obj.nama_anggota)
        self.txtJk.set(obj.jk)
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,obj.prodi)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_anggota = self.txtKode_anggota.get()
        nim = self.txtNim.get()
        nama_anggota = self.txtNama_anggota.get()
        jk = self.txtJk.get()
        prodi = self.txtProdi.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        obj.nim = nim
        obj.nama_anggota = nama_anggota
        obj.jk = jk
        obj.prodi = prodi
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nim(nim)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nim = self.txtNim.get()
        obj = Anggota()
        obj.nim = nim
        if(self.ditemukan==True):
            res = obj.delete_by_nim(nim)
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
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()