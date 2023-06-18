import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__nobukti = None
        self.__kode_anggota = None
        self.__nama = None
        self.__kode_buku1 = None
        self.__kode_buku2 = None
        self.__tgl_pinjam = None
        self.__tgl_hrskembali = None
        self.__tgl_dikembalikan = None
        self.__url = "http://localhost/appperpus/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nobukti(self):
        return self.__nobukti
        
    @nobukti.setter
    def nobukti(self, value):
        self.__nobukti = value
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def kode_buku1(self):
        return self.__kode_buku1
        
    @kode_buku1.setter
    def kode_buku1(self, value):
        self.__kode_buku1 = value
    @property
    def kode_buku2(self):
        return self.__kode_buku2
        
    @kode_buku2.setter
    def kode_buku2(self, value):
        self.__kode_buku2 = value
    @property
    def tgl_pinjam(self):
        return self.__tgl_pinjam
        
    @tgl_pinjam.setter
    def tgl_pinjam(self, value):
        self.__tgl_pinjam = value
    @property
    def tgl_hrskembali(self):
        return self.__tgl_hrskembali
        
    @tgl_hrskembali.setter
    def tgl_hrskembali(self, value):
        self.__tgl_hrskembali = value
    @property
    def tgl_dikembalikan(self):
        return self.__tgl_dikembalikan
        
    @tgl_dikembalikan.setter
    def tgl_dikembalikan(self, value):
        self.__tgl_dikembalikan = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nobukti(self, nobukti):
        url = self.__url+"?nobukti="+nobukti
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_peminjaman']
            self.__nobukti = item['nobukti']
            self.__kode_anggota = item['kode_anggota']
            self.__nama = item['nama']
            self.__kode_buku1 = item['kode_buku1']
            self.__kode_buku2 = item['kode_buku2']
            self.__tgl_pinjam = item['tgl_pinjam']
            self.__tgl_hrskembali = item['tgl_hrskembali']
            self.__tgl_dikembalikan = item['tgl_dikembalikan']
        return data
    def simpan(self):
        payload = {
            "nobukti":self.__nobukti,
            "kode_anggota":self.__kode_anggota,
            "nama":self.__nama,
            "kode_buku1":self.__kode_buku1,
            "kode_buku2":self.__kode_buku2,
            "tgl_pinjam":self.__tgl_pinjam,
            "tgl_hrskembali":self.__tgl_hrskembali,
            "tgl_dikembalikan":self.__tgl_dikembalikan
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nobukti(self, nobukti):
        url = self.__url+"?nobukti="+nobukti
        payload = {
            "nobukti":self.__nobukti,
            "kode_anggota":self.__kode_anggota,
            "nama":self.__nama,
            "kode_buku1":self.__kode_buku1,
            "kode_buku2":self.__kode_buku2,
            "tgl_pinjam":self.__tgl_pinjam,
            "tgl_hrskembali":self.__tgl_hrskembali,
            "tgl_dikembalikan":self.__tgl_dikembalikan
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nobukti(self,nobukti):
        url = self.__url+"?nobukti="+nobukti
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text