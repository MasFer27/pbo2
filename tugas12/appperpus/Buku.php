<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kode_buku = "";
    public $judul = "";
    public $pengarang = "";
    public $penerbit = "";
    public $tahun = "";
    public $kategori = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kode_buku(int $kode_buku)
    {
        $query = "SELECT * FROM $this->table WHERE kode_buku = $kode_buku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kode_buku`,`judul`,`pengarang`,`penerbit`,`tahun`,`kategori`) VALUES ('$this->kode_buku','$this->judul','$this->pengarang','$this->penerbit','$this->tahun','$this->kategori')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kode_buku = '$this->kode_buku', judul = '$this->judul', pengarang = '$this->pengarang', penerbit = '$this->penerbit', tahun = '$this->tahun', kategori = '$this->kategori' 
        WHERE id_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kode_buku($kode_buku): int
    {
        $query = "UPDATE $this->table SET kode_buku = '$this->kode_buku', judul = '$this->judul', pengarang = '$this->pengarang', penerbit = '$this->penerbit', tahun = '$this->tahun', kategori = '$this->kategori' 
        WHERE kode_buku = $kode_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_buku = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kode_buku($kode_buku): int
    {
        $query = "DELETE FROM $this->table WHERE kode_buku = $kode_buku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>