import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kode_buku = None
        self.__judul = None
        self.__pengarang = None
        self.__penerbit = None
        self.__tahun = None
        self.__kategori = None
        self.__url = "http://localhost/appperpus/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_buku(self):
        return self.__kode_buku
        
    @kode_buku.setter
    def kode_buku(self, value):
        self.__kode_buku = value
    @property
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def pengarang(self):
        return self.__pengarang
        
    @pengarang.setter
    def pengarang(self, value):
        self.__pengarang = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    @property
    def tahun(self):
        return self.__tahun
        
    @tahun.setter
    def tahun(self, value):
        self.__tahun = value
    @property
    def kategori(self):
        return self.__kategori
        
    @kategori.setter
    def kategori(self, value):
        self.__kategori = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_buku(self, kode_buku):
        url = self.__url+"?kode_buku="+kode_buku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_buku']
            self.__kode_buku = item['kode_buku']
            self.__judul = item['judul']
            self.__pengarang = item['pengarang']
            self.__penerbit = item['penerbit']
            self.__tahun = item['tahun']
            self.__kategori = item['kategori']
        return data
    def simpan(self):
        payload = {
            "kode_buku":self.__kode_buku,
            "judul":self.__judul,
            "pengarang":self.__pengarang,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun,
            "kategori":self.__kategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_buku(self, kode_buku):
        url = self.__url+"?kode_buku="+kode_buku
        payload = {
            "kode_buku":self.__kode_buku,
            "judul":self.__judul,
            "pengarang":self.__pengarang,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun,
            "kategori":self.__kategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_buku(self,kode_buku):
        url = self.__url+"?kode_buku="+kode_buku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text