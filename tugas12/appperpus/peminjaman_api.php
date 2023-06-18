<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$nobukti=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nobukti'])){
            $nobukti = $_GET['nobukti'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($nobukti>0){
            $result = $peminjaman->get_by_nobukti($nobukti);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->nobukti = $_POST['nobukti'];
        $peminjaman->kode_anggota = $_POST['kode_anggota'];
        $peminjaman->nama = $_POST['nama'];
        $peminjaman->kode_buku1 = $_POST['kode_buku1'];
        $peminjaman->kode_buku2 = $_POST['kode_buku2'];
        $peminjaman->tgl_pinjam = $_POST['tgl_pinjam'];
        $peminjaman->tgl_hrskembali = $_POST['tgl_hrskembali'];
        $peminjaman->tgl_dikembalikan = $_POST['tgl_dikembalikan'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nobukti'])){
            $nobukti = $_GET['nobukti'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->nobukti = $_PUT['nobukti'];
        $peminjaman->kode_anggota = $_PUT['kode_anggota'];
        $peminjaman->nama = $_PUT['nama'];
        $peminjaman->kode_buku1 = $_PUT['kode_buku1'];
        $peminjaman->kode_buku2 = $_PUT['kode_buku2'];
        $peminjaman->tgl_pinjam = $_PUT['tgl_pinjam'];
        $peminjaman->tgl_hrskembali = $_PUT['tgl_hrskembali'];
        $peminjaman->tgl_dikembalikan = $_PUT['tgl_dikembalikan'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($nobukti<>""){
            $peminjaman->update_by_nobukti($nobukti);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nobukti'])){
            $nobukti = $_GET['nobukti'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($nobukti>0){
            $peminjaman->delete_by_nobukti($nobukti);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>