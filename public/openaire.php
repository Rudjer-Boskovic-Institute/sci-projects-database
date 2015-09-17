<?php 


    $db = new PDO('mysql:host=localhost;dbname=projekti;charset=utf8', 'projekti', 'ooPoo4ie');
    $db->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING );
    $stmt = $db->prepare('SELECT MZOS.Broj_projekta as PROJECT_IDENTIFIER, MZOS.Naziv_projekta_EN as PROJECT_TITLE, 
                                      "Ministry of Science Education and Sport, MSES" as FUNDER_NAME, MZOS.Godina_pocetka as START_DATE, 
                                       MZOS.Godina_zavrsetka as END_DATE, USTANOVE.naziv_ust_EN as ORGANIZAITON_INVOLVED 
                                       FROM MZOS 
                                       JOIN USTANOVE ON MZOS.Sifra_ustanove = USTANOVE.irl');
    $stmt->execute();
    $mzos = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $stmt = $db->prepare('SELECT CONCAT(CASE HRZZ.programme WHEN "Istraživački projekti" THEN "IP"
                                        WHEN "Uspostavni istraživački projekti" THEN "UIP"
                                        WHEN "Partnerstvo u istraživanjima" THEN "PUI"
                                        END,"-",HRZZ.call,"-",HRZZ.id) as PROJECT_IDENTIFIER, HRZZ_EN.title as PROJECT_TITLE, "Croatian Science Foundation, CSF" as FUNDER_NAME, 
                                        STR_TO_DATE(SUBSTRING_INDEX(HRZZ.duration, "-", 1), "%d.%m.%Y") as START_DATE, 
                                        STR_TO_DATE(SUBSTRING_INDEX(HRZZ.duration, "-", -1), "%d.%m.%Y") as END_DATE, HRZZ.institution as ORGANIZATION_INVOLVED 
                                        FROM HRZZ_EN
                                        JOIN HRZZ_EN ON HRZZ.id = HRZZ_EN.id');
    $stmt->execute();
    $hrzz = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $projekti = array_merge($mzos, $hrzz);
    $output = "PROJECT_IDENTIFIER\tPROJECT_TITLE\tFUNDER_NAME\tSTART_DATE\tEND_DATE\tORGANIZATION_INVOLVED\n";
    foreach ($projekti as $projekt) {
        $output.=  implode("\t", (array)$projekt)."\n";
    }

    echo $output;
 ?>        
        