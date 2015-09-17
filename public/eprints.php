<?php 
ini_set('display_errors',1);
ini_set('display_startup_errors',1);
error_reporting(-1); 

header('Access-Control-Allow-Origin: https://medlib.mef.hr');  //I have also tried the * wildcard and get the same response
    //header("Access-Control-Allow-Credentials: true");
    header('Access-Control-Allow-Methods: GET, PUT, POST, DELETE, OPTIONS');
    header('Access-Control-Max-Age: 1000');
    header('Access-Control-Allow-Headers: Content-Type, Content-Range, Content-Disposition, Content-Description, Origin, X-Requested-With, Accept, x-prototype-version');
	//header('Content-type: application/xml');
		if (isset($_POST['q'])) {
			$string = $_POST['q'];
		}
		else if (isset($_GET['q'])) {
			$string = $_GET['q'];
		}
		else exit('ERROR');

        /*if(isset($_SERVER['HTTP_ORIGIN'])){
	        $http_origin = $_SERVER['HTTP_ORIGIN'];

	        if ($http_origin == "http://fulir.irb.hr" || $http_origin == "https://medlib.mef.hr")
	        {  
	        	header("Access-Control-Allow-Origin: $http_origin");
	        }
        }*/

        $start = microtime();
        
        
        require_once('config.php');
        $db = new PDO('mysql:host='.host.';dbname='.dbname.';charset='.charset, user, pass);
        $db->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING );
        $stmt = $db->prepare("SELECT * FROM MERGED WHERE reference LIKE CONCAT('%', :string1, '%') OR acronym LIKE CONCAT('%', :string2, '%') OR title LIKE CONCAT('%', :string3, '%') LIMIT 25");
		$stmt->bindParam(':string1', $string, PDO::PARAM_INT);
		$stmt->bindParam(':string2', $string, PDO::PARAM_INT);
		$stmt->bindParam(':string3', $string, PDO::PARAM_INT);
		$stmt->execute();
		//print_r($stmt->errorInfo());
		$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
            /*$ress = DB::table('MERGED')->where("reference", "LIKE", "%$string%")
            ->orWhere("acronym", "LIKE", "%$string%")
            ->orWhere("title", "LIKE", "%$string%")->take(15)->get();*/

        $end = microtime() - $start;
        //echo $end;
        


        echo "<ul>";
        foreach ($rows as $key) {
            echo "<li>".$key['title'] ."-". $key['acronym']. "(". $key['reference'].")</br><small>".$key['leader']."</small><ul><li id=\"for:value:relative:_title\">".$key['title']."-". $key['acronym']."</li><li id=\"for:value:relative:_leader\">".$key['leader']."</li><li id=\"for:value:relative:_code\">".$key['reference']."</li><li id=\"for:value:relative:_type\">".$key['fs']."</li></ul></li>";
        }
        echo "</ul>";

        /*echo "<pre>";
        print_r($ress);
        echo "</pre>";*/

    
 ?>