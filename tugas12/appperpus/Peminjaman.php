<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $nobukti = "";
    public $kode_anggota = "";
    public $nama = "";
    public $kode_buku1 = "";
    public $kode_buku2 = "";
    public $tgl_pinjam = "";
    public $tgl_hrskembali = "";
    public $tgl_dikembalikan = "";
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
    public function get_by_nobukti(int $nobukti)
    {
        $query = "SELECT * FROM $this->table WHERE nobukti = $nobukti";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nobukti`,`kode_anggota`,`nama`,`kode_buku1`,`kode_buku2`,`tgl_pinjam`,`tgl_hrskembali`,`tgl_dikembalikan`) VALUES ('$this->nobukti','$this->kode_anggota','$this->nama','$this->kode_buku1','$this->kode_buku2','$this->tgl_pinjam','$this->tgl_hrskembali','$this->tgl_dikembalikan')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nobukti = '$this->nobukti', kode_anggota = '$this->kode_anggota', nama = '$this->nama', kode_buku1 = '$this->kode_buku1', kode_buku2 = '$this->kode_buku2', tgl_pinjam = '$this->tgl_pinjam', tgl_hrskembali = '$this->tgl_hrskembali', tgl_dikembalikan = '$this->tgl_dikembalikan' 
        WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nobukti($nobukti): int
    {
        $query = "UPDATE $this->table SET nobukti = '$this->nobukti', kode_anggota = '$this->kode_anggota', nama = '$this->nama', kode_buku1 = '$this->kode_buku1', kode_buku2 = '$this->kode_buku2', tgl_pinjam = '$this->tgl_pinjam', tgl_hrskembali = '$this->tgl_hrskembali', tgl_dikembalikan = '$this->tgl_dikembalikan' 
        WHERE nobukti = $nobukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id_peminjaman = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nobukti($nobukti): int
    {
        $query = "DELETE FROM $this->table WHERE nobukti = $nobukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>