import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__kode_anggota = None
        self.__nim = None
        self.__nama_anggota = None
        self.__jk = None
        self.__prodi = None
        self.__alamat = None
        self.__url = "http://localhost/appperpus/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_anggota(self):
        return self.__kode_anggota
        
    @kode_anggota.setter
    def kode_anggota(self, value):
        self.__kode_anggota = value
    @property
    def nim(self):
        return self.__nim
        
    @nim.setter
    def nim(self, value):
        self.__nim = value
    @property
    def nama_anggota(self):
        return self.__nama_anggota
        
    @nama_anggota.setter
    def nama_anggota(self, value):
        self.__nama_anggota = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nim(self, nim):
        url = self.__url+"?nim="+nim
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_anggota']
            self.__kode_anggota = item['kode_anggota']
            self.__nim = item['nim']
            self.__nama_anggota = item['nama_anggota']
            self.__jk = item['jk']
            self.__prodi = item['prodi']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nim":self.__nim,
            "nama_anggota":self.__nama_anggota,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nim(self, nim):
        url = self.__url+"?nim="+nim
        payload = {
            "kode_anggota":self.__kode_anggota,
            "nim":self.__nim,
            "nama_anggota":self.__nama_anggota,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nim(self,nim):
        url = self.__url+"?nim="+nim
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text