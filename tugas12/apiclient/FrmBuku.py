import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("740x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_BUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDUL:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENGARANG:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENERBIT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KATEGORI:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_buku = Entry(mainFrame) 
        self.txtKode_buku.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_buku.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJudul = Entry(mainFrame) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPengarang = Entry(mainFrame) 
        self.txtPengarang.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenerbit = Entry(mainFrame) 
        self.txtPenerbit.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtTahun = Entry(mainFrame) 
        self.txtTahun.grid(row=4, column=1, padx=5, pady=5)
        # Combo Box
        self.txtKategori = StringVar()
        Cbo_kategori = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtKategori) 
        Cbo_kategori.grid(row=5, column=1, padx=5, pady=5)
        # Adding kategori combobox drop down list
        Cbo_kategori['values'] = ('Umum','Filsafat dan Psikologi','Agama','Sosial','Bahasa','Sains dan Matematika','Teknologi','Seni dan Rekreasi','Sejarah dan Geografi')
        Cbo_kategori.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_buku','kode_buku','judul','pengarang','penerbit','tahun','kategori')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_buku', text='ID_BUKU')
        self.tree.column('id_buku', width="20")
        self.tree.heading('kode_buku', text='KODE_BUKU')
        self.tree.column('kode_buku', width="80")
        self.tree.heading('judul', text='JUDUL')
        self.tree.column('judul', width="200")
        self.tree.heading('pengarang', text='PENGARANG')
        self.tree.column('pengarang', width="100")
        self.tree.heading('penerbit', text='PENERBIT')
        self.tree.column('penerbit', width="100")
        self.tree.heading('tahun', text='TAHUN')
        self.tree.column('tahun', width="60")
        self.tree.heading('kategori', text='KATEGORI')
        self.tree.column('kategori', width="150")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPengarang.delete(0,END)
        self.txtPengarang.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,"")
        self.txtKategori.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_buku"],d["kode_buku"],d["judul"],d["pengarang"],d["penerbit"],d["tahun"],d["kategori"]))
    def onCari(self, event=None):
        kode_buku = self.txtKode_buku.get()
        obj = Buku()
        a = obj.get_by_kode_buku(kode_buku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_buku = self.txtKode_buku.get()
        obj = Buku()
        res = obj.get_by_kode_buku(kode_buku)
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,obj.kode_buku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.judul)
        self.txtPengarang.delete(0,END)
        self.txtPengarang.insert(END,obj.pengarang)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.penerbit)
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,obj.tahun)
        self.txtKategori.set(obj.kategori)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_buku = self.txtKode_buku.get()
        judul = self.txtJudul.get()
        pengarang = self.txtPengarang.get()
        penerbit = self.txtPenerbit.get()
        tahun = self.txtTahun.get()
        kategori = self.txtKategori.get()
        # create new Object
        obj = Buku()
        obj.kode_buku = kode_buku
        obj.judul = judul
        obj.pengarang = pengarang
        obj.penerbit = penerbit
        obj.tahun = tahun
        obj.kategori = kategori
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_buku(kode_buku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_buku = self.txtKode_buku.get()
        obj = Buku()
        obj.kode_buku = kode_buku
        if(self.ditemukan==True):
            res = obj.delete_by_kode_buku(kode_buku)
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
    aplikasi = FrmBuku(root2, "Aplikasi Data Buku")
    root2.mainloop()