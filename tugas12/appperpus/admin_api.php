<?php
require_once 'database.php';
require_once 'Admin.php';
$db = new MySQLDatabase();
$admin = new Admin($db);
$id=0;
$username=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['username'])){
            $username = $_GET['username'];
        }
        if($id>0){    
            $result = $admin->get_by_id($id);
        }elseif($username>0){
            $result = $admin->get_by_username($username);
        } else {
            $result = $admin->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new admin
        $admin->username = $_POST['username'];
        $admin->passwd = $_POST['passwd'];
               
        $v = $admin->login($admin->username,$admin->passwd);      
        
        if($v!=null){
            $data['status']='success';
            $data['message']=$v;
        } else {
            $data['status']='failed';
            $data['message']='Login is not valid';
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
        if(isset($_GET['username'])){
            $username = $_GET['username'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $admin->username = $_PUT['username'];
        $admin->passwd = $_PUT['passwd'];
        $admin->rolename = $_PUT['rolename'];
        if($id>0){    
            $admin->update($id);
        }elseif($username<>""){
            $admin->update_by_username($username);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Admin updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Admin update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['username'])){
            $username = $_GET['username'];
        }
        if($id>0){    
            $admin->delete($id);
        }elseif($username>0){
            $admin->delete_by_username($username);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Admin deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Admin delete failed.';
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