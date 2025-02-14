from django.db import models
import pandas as pd

csvRead = pd.read_csv('blog/Company_data_base.csv', encoding='latin-1',  skipinitialspace=True)
# header = next(reader)
print(csvRead)

# Create your models here.
class Target_Finder_Input(models.Model):
    alliances = models.BooleanField(max_length=500)
    #alternativeEngines = models.BooleanField(max_length=500)
    #capacityIncrease = models.BooleanField(max_length=500)
    #companyLaunch = models.BooleanField(max_length=500)
    #corporateFinance = models.BooleanField(max_length=500)
    #corporateMA = models.BooleanField(max_length=500)
    #humanResource = models.BooleanField(max_length=500)
    #presicionTechnology = models.BooleanField(max_length=500)
    #innovation = models.BooleanField(max_length=500)
    #productLaunches = models.BooleanField(max_length=500)
    #productUpgrades = models.BooleanField(max_length=500)
    #reporting = models.BooleanField(max_length=500)
    #strategy = models.BooleanField(max_length=500)



COLOR_CHOICES = [
    ('type','---type in a Country name---'),
    ('Argentina','Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia','Australia'),
    ('Austria','Austria'),
    ('Azerbaijan','Azerbaijan'),
    ('Bangladesh', 'Bangladesh'),
    ('Belarus','Belarus'),
    ('Belgium','Belgium'),
    ('Bolivia','Bolivia'),
    ('Brazil','Brazil'),
    ('Bulgaria','Bulgaria'),
    ('Burundi','Burundi'),
    ('Canada','Canada'),
    ('Chile','Chile'),
    ('China','China'),
    ('Czech Republic','Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Egypt','Egypt'),
    ('Estonia','Estonia'),
    ('Ethiopia','Ethiopia'),
    ('Finland', 'Finland'),
    ('France','France'),
    ('Germany','Germany'),
    ('Ghana','Ghana'),
    ('Iceland','Iceland'),
    ('India','India'),
    ('India','India'),
    ('Iran','Iran'),
    ('Hungary','Hungary'),
    ('Ireland','Ireland'),
    ('Israel','Israel'),
    ('Italy','Italy'),
    ('Japan','Japan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya','Kenya'),
    ('Latvia','Latvia'),
    ('Libya','Libya'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg','Luxembourg'),
    ('Mexico','Mexico'),
    ('Morocco','Morocco'),
    ('Netherlands','Netherlands'),
    ('New Zealand','New Zealand'),
    ('Nigeria','Nigeria'),
    ('Norway','Norway'),
    ('Peru','Peru'),
    ('Poland','Poland'),
    ('Portugal','Portugal'),
    ('Romania', 'Romania'),
    ('Russia','Russia'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Serbia','Serbia'),
    ('Singapore', 'Singapore'),
    ('Slovakia','Slovakia'),
    ('Slovenia','Slovenia'),
    ('South Africa','South Africa'),
    ('South Korea','South Korea'),
    ('Spain','Spain'),
    ('Sudan','Sudan'),
    ('Sweden','Sweden'),
    ('Switzerland','Switzerland'),
    ('Tanzania','Tanzania'),
    ('Thailand','Thailand'),
    ('Turkey','Turkey'),
    ('Turkmenistan','Turkmenistan'),
    ('Ukraine','Ukraine'),
    ('United Arab Emirates','United Arab Emirates'),
    ('United Kingdom','United Kingdom'),
    ('United States','United States'),
    ('Uruguay','Uruguay'),
    ('Uzbekistan','Uzbekistan'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe','Zimbabwe'),

]


Company_Chioces = [
    ('type a company name','---type a company name---'),
    ('365FarmNet(Claas)','365FarmNet(Claas)'),
    ('Aachen University of Applied Sciences','Aachen University of Applied Sciences'),
    ('AB VOLVO','AB VOLVO'),
    ('Abemec BV','Abemec BV'),
    ('Abundant Robotics','Abundant Robotics'),
    ('AC Damate','AC Damate'),
    ('Accenture plc','Accenture plc'),
    ('Adama Agricultural Solutions','Adama Agricultural Solutions'),
    ('Advanced Farm Technologies','Advanced Farm Technologies'),
    ('Ag Growth International Inc (AGI)','Ag Growth International Inc (AGI)'),
    ('Ag Leader Technology','Ag Leader Technology'),
    ('AGC Bor Glassworks','AGC Bor Glassworks'),
    ('AGCO Corporation','AGCO Corporation'),
    ('AGCO-RM','AGCO-RM'),
    ('AGI EMEA Srl (Ag Growth International)','AGI EMEA Srl (Ag Growth International)'),
    ('Agintegrated','Agintegrated'),
    ('Agjunction','Agjunction'),
    ('Agrar-Markt DEPPE GmbH','Agrar-Markt DEPPE GmbH'),
    ('AGRAVIS Fläming-Mittelelbe GmbH','AGRAVIS Fläming-Mittelelbe GmbH'),
    ('Agravis Ost','Agravis Ost'),
    ('AGRAVIS Raiffeisen AG','AGRAVIS Raiffeisen AG'),
    ('AgreenCulture','AgreenCulture'),
    ('Agri CS a.s.','Agri CS a.s.'),
    ('Agrian','Agrian'),
    ('AgriArgo Ibérica','AgriArgo Ibérica'),
    ('Agri-Epi Centre','Agri-Epi Centre'),
    ('Agrifac (Exel Industries)','Agrifac (Exel Industries)'),
    ('Agrifac Machinery B.V.','Agrifac Machinery B.V.'),
    ('Agrimulsa','Agrimulsa'),
    ('Agrisem International S.A.S.','Agrisem International S.A.S.'),
    ('Agrointelli','Agrointelli'),
    ('Agrotec a.s. (Agrotec Group)','Agrotec a.s. (Agrotec Group)'),
    ('Agrotec Magyarország','Agrotec Magyarország'),
    ('AgroVision','AgroVision'),
    ('AgroVista Holding','AgroVista Holding'),
    ('Agsolco Ukraine','Agsolco Ukraine'),
    ('AgXtend (CNHI)','AgXtend (CNHI)'),
    ('Ahern Deutschland GmbH','Ahern Deutschland GmbH'),
    ('Ahern International','Ahern International'),
    ('A-K Maskiner','A-K Maskiner'),
    ('Alamo Group','Alamo Group'),
    ('Alan Snow Agricultural Engineers','Alan Snow Agricultural Engineers'),
    ('Alpego SpA','Alpego SpA'),
    ('Alphabet Inc','Alphabet Inc'),
    ('Amazone','Amazone'),
    ('AMAZONEN-Werke H. Dreyer GmbH & Co. KG','AMAZONEN-Werke H. Dreyer GmbH & Co. KG'),
    ('American Society of Agricultural and Biological Engineers','American Society of Agricultural and Biological Engineers'),
    ('Amkodor','Amkodor'),
    ('Antonio Carraro S.p.A.','Antonio Carraro S.p.A.'),
    ('Apache Sprayers','Apache Sprayers'),
    ('APV','APV'),
    ('54','Arag Srl'),
    ('Arbo Spol s.r.o.','Arbo Spol s.r.o.'),
    ('Arbos (Lovol)','Arbos (Lovol)'),
    ('Argo Tractors SpA','Argo Tractors SpA'),
    ('Arla Foods','Arla Foods'),
    ('Asa-Lift','Asa-Lift'),
    ('ATOS SE','ATOS SE'),
    ('ATR Landhandel','ATR Landhandel'),
    ('August Bruns Landmaschinen GmbH','August Bruns Landmaschinen GmbH'),
    ('AVR','AVR'),
    ('Axiál Kft','Axiál Kft'),
    ('Bakker Ulrum BV','Bakker Ulrum BV'),
    ('Baltic Agro AS','Baltic Agro AS'),
    ('BARCLAYS PLC','BARCLAYS PLC'),
    ('Barto AG','Barto AG'),
    ('BAYER AG','BAYER AG'),
    ('BayWa AG','BayWa AG'),
    ('Bednar FMT sro','Bednar FMT sro'),
    ('Bednar UK','Bednar UK'),
    ('Belagrospetsmash','Belagrospetsmash'),
    ('Bell Equipment','Bell Equipment'),
    ('Ben Burgess','Ben Burgess'),
    ('Ben-Gurion University of the Negev','Ben-Gurion University of the Negev'),
    ('Bernard Krone Holding GmbH & Co.KG','Bernard Krone Holding GmbH & Co.KG'),
    ('Berthoud (Exel Industries)','Berthoud (Exel Industries)'),
    ('Birž? žemtiekimas','Birž? žemtiekimas'),
    ('Blue River Technology (Deere & Co.)','Blue River Technology (Deere & Co.)'),
    ('BMW AG','BMW AG'),
    ('Bobruiskagromash Holding','Bobruiskagromash Holding'),
    ('Bosch','Bosch'),
    ('Bosch Rexroth','Bosch Rexroth'),
    ('Boston Dynamics','Boston Dynamics'),
    ('BR Industrier AS','BR Industrier AS'),
    ('Bryanskselmash','Bryanskselmash'),
    ('Bucher Industries AG','Bucher Industries AG'),
    ('Bucher Municipal','Bucher Municipal'),
    ('Bushel Plus','Bushel Plus'),
    ('Camso','Camso'),
    ('Carraro International SE','Carraro International SE'),
    ('Carraro SpA','Carraro SpA'),
    ('Carraro Tractors (Carraro Group)','Carraro Tractors (Carraro Group)'),
    ('CARRS BILLINGTON AGRICULTURAL','CARRS BILLINGTON AGRICULTURAL'),
    ('Case Construction (CNHI)','Case Construction (CNHI)'),
    ('Case IH (CNHI)','Case IH (CNHI)'),
    ('Caterpillar','Caterpillar'),
    ('Caussade Semences','Caussade Semences'),
    ('Challenger (AGCO)','Challenger (AGCO)'),
    ('Chandlers Farm Equipment','Chandlers Farm Equipment'),
    ('Cherkizovo Group','Cherkizovo Group'),
    ('Chinese Academy of Sciences','Chinese Academy of Sciences'),
    ('Claas','Claas'),
    ('CNH Industrial Capital','CNH Industrial Capital'),
    ('CNH Industrial Finance Europe S.A.','CNH Industrial Finance Europe S.A.'),
    ('CNH INDUSTRIAL N.V.','CNH INDUSTRIAL N.V.'),
    ('CNH Industrial Polska','CNH Industrial Polska'),
    ('Cofabel','Cofabel'),
    ('COFCO International','COFCO International'),
    ('Cognitive Pilot','Cognitive Pilot'),
    ('Colven Brasil','Colven Brasil'),
    ('Commoditrader','Commoditrader'),
    ('Commonwealth Scientific and Industrial Research Organisation (CSIRO)','Commonwealth Scientific and Industrial Research Organisation (CSIRO)'),
    ('COMPANIE GÉNÉRALE DES ÉTABLISSEMENTS MICHELIN SCA','COMPANIE GÉNÉRALE DES ÉTABLISSEMENTS MICHELIN SCA'),
    ('Concern Tractor Plants (CTP)','Concern Tractor Plants (CTP)'),
    ('CONTINENTAL AG','CONTINENTAL AG'),
    ('Continental Farmers Group','Continental Farmers Group'),
    ('Cornell University','Cornell University'),
    ('Cornthwaite Group','Cornthwaite Group'),
    ('Corteva Agriscience','Corteva Agriscience'),
    ('Court of Modena','Court of Modena'),
    ('CREA Victoria Group','CREA Victoria Group'),
    ('Cropio','Cropio'),
    ('CropX','CropX'),
    ('Cummins Inc','Cummins Inc'),
    ('Cygnet Holding','Cygnet Holding'),
    ('Dana Incorporated','Dana Incorporated'),
    ('Danish Agro','Danish Agro'),
    ('Danish Agro Machinery Holding A/S','Danish Agro Machinery Holding A/S'),
    ('Danish Technological Institute','Danish Technological Institute'),
    ('Dansk Landbrugs Grovvareselskab (DLG A.m.b.A.)','Dansk Landbrugs Grovvareselskab (DLG A.m.b.A.)'),
    ('DASSAULT SYSTÈMES S.A.','DASSAULT SYSTÈMES S.A.'),
    ('Datalogisk','Datalogisk'),
    ('De Lage Landen International B.V. (DLL Group)','De Lage Landen International B.V. (DLL Group)'),
    ('Decisive Farming Corp.','Decisive Farming Corp.'),
    ('Deere & Company','Deere & Company'),
    ('Delair','Delair'),
    ('Denizbank','Denizbank'),
    ('DEUTSCHE GESELLSCHAFT FÜR INTERNATIONALE ZUSAMMENARBEIT (GIZ) GMBH','DEUTSCHE GESELLSCHAFT FÜR INTERNATIONALE ZUSAMMENARBEIT (GIZ) GMBH'),
    ('DEUTSCHE TELEKOM AG','DEUTSCHE TELEKOM AG'),
    ('Deutscher Bundestag','Deutscher Bundestag'),
    ('Deutsches Zentrum für Luft- und Raumfahrt (DLR)','Deutsches Zentrum für Luft- und Raumfahrt (DLR)'),
    ('DEUTZ AG','DEUTZ AG'),
    ('Deutz-Fahr (SDF Group)','Deutz-Fahr (SDF Group)'),
    ('Deutz-Fahr Austria Landmaschinen GmbH','Deutz-Fahr Austria Landmaschinen GmbH'),
    ('Dewulf','Dewulf'),
    ('Dieci','Dieci'),
    ('Dixie Chopper','Dixie Chopper'),
    ('DJI','DJI'),
    ('DLF','DLF'),
    ('Dongfeng Motor Group','Dongfeng Motor Group'),
    ('Doosan Bobcat','Doosan Bobcat'),
    ('Drone Ag','Drone Ag'),
    ('DroneDeploy','DroneDeploy'),
    ('Dutch Power Company','Dutch Power Company'),
    ('Ecobotix','Ecobotix'),
    ('Ecole polytechnique fédérale de Lausanne (EPFL)','Ecole polytechnique fédérale de Lausanne (EPFL)'),
    ('eFarm GmbH & Co. KG (e-farm.com','eFarm GmbH & Co. KG (e-farm.com)'),
    ('eFarmer B.V.','eFarmer B.V.'),
    ('Eikmaskin AS','Eikmaskin AS'),
    ('Einböck','Einböck'),
    ('Ekoniva Group','Ekoniva Group'),
    ('Ekosem-Agrar','Ekosem-Agrar'),
    ('Ekotechnika AG','Ekotechnika AG'),
    ('Elmec','Elmec'),
    ('Energifabriken','Energifabriken'),
    ('Epicenter K','Epicenter K'),
    ('Equipment Technologies (Exel Industries)','Equipment Technologies (Exel Industries)'),
    ('Escorts Kubota India Private Limited','Escorts Kubota India Private Limited'),
    ('Escorts Limited','Escorts Limited'),
    ('ETH Zurich','ETH Zurich'),
    ('Euralis Semences','Euralis Semences'),
    ('Eurasia Group Kazakhstan','Eurasia Group Kazakhstan'),
    ('European Bank for Reconstruction and Development (EBRD)','European Bank for Reconstruction and Development (EBRD)'),
    ('Evrard (Exel Industries)','Evrard (Exel Industries)'),
    ('Exel Industries','Exel Industries'),
    ('EXXACT Robotics','EXXACT Robotics'),
    ('Faresin Industries','Faresin Industries'),
    ('Farm King','Farm King'),
    ('Farmdroid','Farmdroid'),
    ('Farmers Edge','Farmers Edge'),
    ('Farmertronics','Farmertronics'),
    ('Farmet','Farmet'),
    ('Farming Agrícola','Farming Agrícola'),
    ('Farmstore','Farmstore'),
    ('FarmX','FarmX'),
    ('Farol','Farol'),
    ('FaunaPhotonics','FaunaPhotonics'),
    ('Faurecia S.A.','Faurecia S.A.'),
    ('FederUnacoma (Italian Agricultural Machinery Manufacturers Federation)','FederUnacoma (Italian Agricultural Machinery Manufacturers Federation)'),
    ('Feerum','Feerum'),
    ('Fella (AGCO)','Fella (AGCO)'),
    ('Felleskjøpet Agri','Felleskjøpet Agri'),
    ('Fenaco','Fenaco'),
    ('Fendt (AGCO)','Fendt (AGCO)'),
    ('Ferrari Trattori','Ferrari Trattori'),
    ('FieldSense','FieldSense'),
    ('Fliegl','Fliegl'),
    ('Fliegl Agrartechnik GmbH','Fliegl Agrartechnik GmbH'),
    ('FMR Maskiner','FMR Maskiner'),
    ('FPT Industrial (CNHI)','FPT Industrial (CNHI)'),
    ('Frans Vervaet B.V.','Frans Vervaet B.V.'),
    ('Fraunhofer Center X-ray Technology EZRT','Fraunhofer Center X-ray Technology EZRT'),
    ('Fritzmeier Umwelttechnik GmbH & Co. KG','Fritzmeier Umwelttechnik GmbH & Co. KG'),
    ('Garant-Kotte','Garant-Kotte'),
    ('Garford Farm Machinery Ltd','Garford Farm Machinery Ltd'),
    ('Gartenland GmbH','Gartenland GmbH'),
    ('Gazprombank Leasing','Gazprombank Leasing'),
    ('GEA GROUP AG','GEA GROUP AG'),
    ('geo-konzept GmbH','geo-konzept GmbH'),
    ('German Association of Machinery Manufacturers (VDMA)','German Association of Machinery Manufacturers (VDMA)'),
    ('Getreide AG','Getreide AG'),
    ('Glencore Agriculture','Glencore Agriculture'),
    ('Goldoni (Lovol)','Goldoni (Lovol)'),
    ('Gomselmash','Gomselmash'),
    ('Goodvalley','Goodvalley'),
    ('Google LLC','Google LLC'),
    ('Government of Austria','Government of Austria'),
    ('Government of Belarus','Government of Belarus'),
    ('Government of German state of Baden-Württemberg','Government of German state of Baden-Württemberg'),
    ('Government of Hungary','Government of Hungary'),
    ('Government of Italy','Government of Italy'),
    ('Government of Japan','Government of Japan'),
    ('Government of Kazakhstan','Government of Kazakhstan'),
    ('Government of North Kazakhstan Region','Government of North Kazakhstan Region'),
    ('Government of Orenburg Region in Russia','Government of Orenburg Region in Russia'),
    ('Government of Romania','Government of Romania'),
    ('Government of Rostov Region in Russia','Government of Rostov Region in Russia'),
    ('Government of Russia','Government of Russia'),
    ('Government of South Korea','Government of South Korea'),
    ('Government of the United States','Government of the United States'),
    ('Government of Turkmenistan','Government of Turkmenistan'),
    ('Government of Ukraine','Government of Ukraine'),
    ('Government of Uzbekistan','Government of Uzbekistan'),
    ('Government of Voronezh Region in Russia','Government of Voronezh Region in Russia'),
    ('Government of Zimbabwe','Government of Zimbabwe'),
    ('Grasdorf','Grasdorf'),
    ('Great Plains (Kubota)','Great Plains (Kubota)'),
    ('Grégoire (SDF Group)','Grégoire (SDF Group)'),
    ('Grégoire-Besson S.A.S.','Grégoire-Besson S.A.S.'),
    ('Grimme','Grimme'),
    ('Grimme Landmaschinenfabrik GmbH & Co. KG','Grimme Landmaschinenfabrik GmbH & Co. KG'),
    ('Grimme Skandinavien A/S','Grimme Skandinavien A/S'),
    ('Grimme UK Ltd','Grimme UK Ltd'),
    ('Group Schumacher','Group Schumacher'),
    ('Groupe Latitude GPS3','Groupe Latitude GPS'),
    ('GSI Group LLC','GSI Group LLC'),
    ('GVS Agrar AG','GVS Agrar AG'),
    ('Hamblys','Hamblys'),
    ('Hankkija Oy','Hankkija Oy'),
    ('Hardi (Exel Industries)','Hardi (Exel Industries)'),
    ('Helms TMT Centret A/S','Helms TMT Centret A/S'),
    ('Herborg Maskinforretning','Herborg Maskinforretning'),
    ('He-VA','He-VA'),
    ('Hissink & Zonen','Hissink & Zonen'),
    ('Hogervorst Sprayer Solutions','Hogervorst Sprayer Solutions'),
    ('Holde Agri Invest','Holde Agri Invest'),
    ('Holmer','Holmer'),
    ('Holmer Maschinenbau GmbH','Holmer Maschinenbau GmbH'),
    ('Honey Bee Manufacturing','Honey Bee Manufacturing'),
    ('Horsch Maschinen GmbH','Horsch Maschinen GmbH'),
    ('HRN Tractors','HRN Tractors'),
    ('Hummingbird Technologies','Hummingbird Technologies'),
    ('Hürlimann (SDF Group)','Hürlimann (SDF Group)'),
    ('IBM Corporation','IBM Corporation'),
    ('Indian Agricultural Research Institute','Indian Agricultural Research Institute'),
    ('Indigo Agriculture','Indigo Agriculture'),
    ('Innovative Vehicle Institute','Innovative Vehicle Institute'),
    ('Interagri Bulgaria','Interagri Bulgaria'),
    ('International Tractors Ltd (ITL)','International Tractors Ltd (ITL)'),
    ('Iowa State University','Iowa State University'),
    ('Ipso SRL','Ipso SRL'),
    ('Iveco (CNHI)','Iveco (CNHI)'),
    ('Iveco Bus (CNHI)','Iveco Bus (CNHI)'),
    ('J Hundahl','J Hundahl'),
    ('J. Stehouwer Mechanisatie BV','J. Stehouwer Mechanisatie BV'),
    ('J.C.  Bamford Excavators Ltd. (JCB)','J.C.  Bamford Excavators Ltd. (JCB)'),
    ('Jacto','Jacto'),
    ('JCB','JCB'),
    ('Jean Heybroek','Jean Heybroek'),
    ('JJ Dabekausen BV','JJ Dabekausen BV'),
    ('John Deere (Deere & Co.)','John Deere (Deere & Co.)'),
    ('John Deere Ibérica','John Deere Ibérica'),
    ('John Deere Polska','John Deere Polska'),
    ('John Deere Russia','John Deere Russia'),
    ('Johnston Tractors','Johnston Tractors'),
    ('Joseph Vögele AG','Joseph Vögele AG'),
    ('JPMorgan Chase & Co.','JPMorgan Chase & Co.'),
    ('Jungheinrich AG','Jungheinrich AG'),
    ('Junkkari','Junkkari'),
    ('Kamps de Wild BV','Kamps de Wild BV'),
    ('Karlsruhe Institute of Technology (KIT)','Karlsruhe Institute of Technology (KIT)'),
    ('Kaweco','Kaweco'),
    ('KazAgroFinance','KazAgroFinance'),
    ('Kazrost Engineering','Kazrost Engineering'),
    ('KBBG (Kubota Bulgaria)','KBBG (Kubota Bulgaria)'),
    ('Kernel (kernel.ua)','Kernel (kernel.ua)'),
    ('Kharkiv Tractor Plant (HTZ ??? KhTZ)','Kharkiv Tractor Plant (HTZ ??? KhTZ)'),
    ('King Agro (Deere & Co.)','King Agro (Deere & Co.)'),
    ('Kinze Manufacturing','Kinze Manufacturing'),
    ('Kioti Tractors','Kioti Tractors'),
    ('Kirov Plant (Kirovets)','Kirov Plant (Kirovets)'),
    ('KITE Zrt','KITE Zrt'),
    ('Kleemann','Kleemann'),
    ('KMZ Industries','KMZ Industries'),
    ('KÖCKERLING GmbH & Co. KG','KÖCKERLING GmbH & Co. KG'),
    ('Komatsu','Komatsu'),
    ('Kongskilde (CNHI)','Kongskilde (CNHI)'),
    ('Kotte GmbH & Co. KG','Kotte GmbH & Co. KG'),
    ('Kotte Landtechnik GmbH & Co. KG','Kotte Landtechnik GmbH & Co. KG'),
    ('Kragmann A/S','Kragmann A/S'),
    ('Kramer (Wacker Neuson)','Kramer (Wacker Neuson)'),
    ('Kramer-Werke GmbH','Kramer-Werke GmbH'),
    ('Kramp Groep','Kramp Groep'),
    ('Krampe Fahrzeugbau GmbH','Krampe Fahrzeugbau GmbH'),
    ('Krone','Krone'),
    ('Krone Commercial Vehicle Group','Krone Commercial Vehicle Group'),
    ('Krone UK','Krone UK'),
    ('Kubota','Kubota'),
    ('Kubota (Deutschland) GmbH','Kubota (Deutschland) GmbH'),
    ('Kubota (U.K.) Ltd','Kubota (U.K.) Ltd'),
    ('Kubota Agricultural Machinery India Pvt. Ltd.','Kubota Agricultural Machinery India Pvt. Ltd.'),
    ('Kubota Corporation','Kubota Corporation'),
    ('Kubota España SA','Kubota España SA'),
    ('Kubota Holdings Europe B.V.','Kubota Holdings Europe B.V.'),
    ('Kubota Tractor Corporation','Kubota Tractor Corporation'),
    ('Kuhn (Bucher)','Kuhn (Bucher)'),
    ('Kuhn Farm Machinery (UK) Ltd','Kuhn Farm Machinery (UK) Ltd'),
    ('Kuhn Group','Kuhn Group'),
    ('Kusto Agro Farming (????? ???? ???????)','Kusto Agro Farming (????? ???? ???????)'),
    ('Kverneland (Kubota)','Kverneland (Kubota)'),
    ('Kverneland Group','Kverneland Group'),
    ('Kverneland Group CIS','Kverneland Group CIS'),
    ('Lagerhaus Technik-Center (LTC)','Lagerhaus Technik-Center (LTC)'),
    ('Lamborghini Trattori (SDF Group)','Lamborghini Trattori (SDF Group)'),
    ('Landini (Argo)','Landini (Argo)'),
    ('Lantbrukarnas Riksförbund (LRF)','Lantbrukarnas Riksförbund (LRF)'),
    ('Lantmännen','Lantmännen'),
    ('Lantmännen Maskin','Lantmännen Maskin'),
    ('Laser Zentrum Hannover e.V.','Laser Zentrum Hannover e.V.'),
    ('Lely','Lely'),
    ('Lemken','Lemken'),
    ('LEMKEN GmbH & Co. KG','LEMKEN GmbH & Co. KG'),
    ('Liebherr','Liebherr'),
    ('Lindner Traktoren','Lindner Traktoren'),
    ('Lindsay Corporation','Lindsay Corporation'),
    ('Lister Wilder Ltd','Lister Wilder Ltd'),
    ('Louis Dreyfus','Louis Dreyfus'),
    ('Lovol','Lovol'),
    ('LS Tractors','LS Tractors'),
    ('Magni Telescopic Handlers SRL','Magni Telescopic Handlers SRL'),
    ('Mahindra & Mahindra Limited (M&M)','Mahindra & Mahindra Limited (M&M)'),
    ('Malkom','Malkom'),
    ('Manitou (Manitou Group)','Manitou (Manitou Group)'),
    ('Manitou BF S.A. (Manitou Group)','Manitou BF S.A. (Manitou Group)'),
    ('Manna Irrigation Intelligence','Manna Irrigation Intelligence'),
    ('Marathon Group','Marathon Group'),
    ('Mark Weatherhead Ltd.','Mark Weatherhead Ltd.'),
    ('Maschinenfabrik Bernard Krone GmbH & Co. KG','Maschinenfabrik Bernard Krone GmbH & Co. KG'),
    ('Maschio Gaspardo','Maschio Gaspardo'),
    ('Maskinhandler Indkøbsringen (MI)','Maskinhandler Indkøbsringen (MI)'),
    ('Maskinpartner A/S','Maskinpartner A/S'),
    ('Massachusetts Institute of Technology (MIT)','Massachusetts Institute of Technology (MIT)'),
    ('Massey Ferguson (AGCO)','Massey Ferguson (AGCO)'),
    ('MAZ (Minsk Automobile Plant)','MAZ (Minsk Automobile Plant)'),
    ('Mazzotti (Deere & Co.)','Mazzotti (Deere & Co.)'),
    ('McCormick (Argo)','McCormick (Argo)'),
    ('Mckinsey & Company','Mckinsey & Company'),
    ('Mechan Groep','Mechan Groep'),
    ('Mechanisatiebedrijf GroeNoord','Mechanisatiebedrijf GroeNoord'),
    ('Mercedes-Benz (Daimler)','Mercedes-Benz (Daimler)'),
    ('Merit Functional Foods','Merit Functional Foods'),
    ('Merlo','Merlo'),
    ('Merlo S.p.A. (Merlo Group)','Merlo S.p.A. (Merlo Group)'),
    ('MHP SE','MHP SE'),
    ('Microsoft Corporation','Microsoft Corporation'),
    ('MIG Agricultural Co. Ltd.','MIG Agricultural Co. Ltd.'),
    ('Ministry for Economic Cooperation and Development@Government of Germany','Ministry for Economic Cooperation and Development@Government of Germany'),
    ('Ministry of Agriculture Fisheries and Food@Government of Spain','Ministry of Agriculture Fisheries and Food@Government of Spain'),
    ('Ministry of Agriculture@Government of Italy','Ministry of Agriculture@Government of Italy'),
    ('Ministry of Agriculture@Government of Russia','Ministry of Agriculture@Government of Russia'),
    ('Ministry of Economic Development@Government of Italy','Ministry of Economic Development@Government of Italy'),
    ('Ministry of Environment and Food@Government of Denmark','Ministry of Environment and Food@Government of Denmark'),
    ('Ministry of Industry and Trade@Government of Russia','Ministry of Industry and Trade@Government of Russia'),
    ('Minsk Tractor Works (MTZ Belarus)','Minsk Tractor Works (MTZ Belarus)'),
    ('Miratorg Holding (previously Agri-Business Holding)','Miratorg Holding (previously Agri-Business Holding)'),
    ('Mirogroup Resources','Mirogroup Resources'),
    ('Mironovsky Hleboproduct (MHP Group)','Mironovsky Hleboproduct (MHP Group)'),
    ('Mitsubishi Mahindra Agricultural Machinery Co. Ltd.','Mitsubishi Mahindra Agricultural Machinery Co. Ltd.'),
    ('Monarch Tractor','Monarch Tractor'),
    ('Monash University','Monash University'),
    ('Monsanto','Monsanto'),
    ('Morbark LLC','Morbark LLC'),
    ('Motrac Industries','Motrac Industries'),
    ('MTT Tractors BV','MTT Tractors BV'),
    ('Mutares SE & Co','Mutares SE & Co'),
    ('Müthing GmbH & Co.','Müthing GmbH & Co.'),
    ('NAIO Technologies','NAIO Technologies'),
    ('National Science Foundation','National Science Foundation'),
    ('National University of Singapore','National University of Singapore'),
    ('Nellemann Machinery','Nellemann Machinery'),
    ('NEOLINE SAS','NEOLINE SAS'),
    ('Netafim','Netafim'),
    ('Netherton Tractors Ltd','Netherton Tractors Ltd'),
    ('New Holland (CNHI)','New Holland (CNHI)'),
    ('New Holland Construction (CNHI)','New Holland Construction (CNHI)'),
    ('New Leader Manufacturing','New Leader Manufacturing'),
    ('NewTec Ost Vertriebsgesellschaft GmbH','NewTec Ost Vertriebsgesellschaft GmbH'),
    ('NewTec Vertriebsgesellschaft für Agrartechnik GmbH','NewTec Vertriebsgesellschaft für Agrartechnik GmbH'),
    ('Next2Sun','Next2Sun'),
    ('Nhr Agropartners SRL','Nhr Agropartners SRL'),
    ('Nibulon','Nibulon'),
    ('Nikola Corporation','Nikola Corporation'),
    ('Northwestern University','Northwestern University'),
    ('Norwegian Agro Machinery','Norwegian Agro Machinery'),
    ('Novariant','Novariant'),
    ('Novatel','Novatel'),
    ('Nutrien Ltd.','Nutrien Ltd.'),
    ('Nvidia','Nvidia'),
    ('Orthman','Orthman'),
    ('OSRAM LICHT AG','OSRAM LICHT AG'),
    ('Östra Sönnarslövs Traktorservice AB','Östra Sönnarslövs Traktorservice AB'),
    ('Ovostar Union','Ovostar Union'),
    ('P Tuckwell Ltd','P Tuckwell Ltd'),
    ('Panasonic','Panasonic'),
    ('Parrot SA','Parrot SA'),
    ('Pasquali','Pasquali'),
    ('Pegas-Agro','Pegas-Agro'),
    ('Perkins','Perkins'),
    ('Pessl Instruments','Pessl Instruments'),
    ('Pichon (Samson)','Pichon (Samson)'),
    ('PiX4D','PiX4D'),
    ('PLA S.A.','PLA S.A.'),
    ('Ploeger','Ploeger'),
    ('PM-Pro','PM-Pro'),
    ('Politecnico di Torino','Politecnico di Torino'),
    ('Pöttinger','Pöttinger'),
    ('Pöttinger UK','Pöttinger UK'),
    ('Precision Decisions','Precision Decisions'),
    ('Precision Planting LLC','Precision Planting LLC'),
    ('Proagrica','Proagrica'),
    ('Pronar','Pronar'),
    ('Protein Industries Canada','Protein Industries Canada'),
    ('PV Dobson','PV Dobson'),
    ('Quivogne','Quivogne'),
    ('Rabobank','Rabobank'),
    ('Rabobank Groep N.V.','Rabobank Groep N.V.'),
    ('Radicle Growth','Radicle Growth'),
    ('Raiffeisen Bank Aval','Raiffeisen Bank Aval'),
    ('Raiffeisen Waren GmbH','Raiffeisen Waren GmbH'),
    ('Raiffeisen Waren-Zentrale Rhein-Main eG','Raiffeisen Waren-Zentrale Rhein-Main eG'),
    ('Rauch','Rauch'),
    ('RAUCH Landmaschinenfabrik GmbH','RAUCH Landmaschinenfabrik GmbH'),
    ('Raven Industries','Raven Industries'),
    ('RDO Equipment Co.','RDO Equipment Co.'),
    ('Reesink Agri','Reesink Agri'),
    ('Reform-Werke Bauer & Co GmbH','Reform-Werke Bauer & Co GmbH'),
    ('501','Regional Government of Andalusia'),
    ('Reime Landteknikk','Reime Landteknikk'),
    ('Rigitrac-Traktorbau AG','Rigitrac-Traktorbau AG'),
    ('Ripon Farm Services','Ripon Farm Services'),
    ('Ristone Holding','Ristone Holding'),
    ('Rivulis Irrigation','Rivulis Irrigation'),
    ('Robert Bosch GmbH','Robert Bosch GmbH'),
    ('Robert Schuster Fahrzeuge und Landmaschinen GmbH','Robert Schuster Fahrzeuge und Landmaschinen GmbH'),
    ('RootWave','RootWave'),
    ('Ros Agro PLC','Ros Agro PLC'),
    ('Rosagroleasing','Rosagroleasing'),
    ('Rosspetsmash','Rosspetsmash'),
    ('Rostok Holding','Rostok Holding'),
    ('Rostselmash','Rostselmash'),
    ('Rothamsted Research','Rothamsted Research'),
    ('Royal Reesink BV','Royal Reesink BV'),
    ('Royal Traktor Zrt','Royal Traktor Zrt'),
    ('RSM Agrartechnik GmbH','RSM Agrartechnik GmbH'),
    ('Rusagro Group','Rusagro Group'),
    ('Rusmolco','Rusmolco'),
    ('Russell Group','Russell Group'),
    ('Russian Academy of Sciences','Russian Academy of Sciences'),
    ('Russian Agricultural Bank (Rosselkhozbank)','Russian Agricultural Bank (Rosselkhozbank)'),
    ('Russian State Agrarian University - Moscow Timiryazev Agricultural Academy','Russian State Agrarian University - Moscow Timiryazev Agricultural Academy'),
    ('RWA Raiffeisen Ware Austria AG','RWA Raiffeisen Ware Austria AG'),
    ('RWZ Rhein-Main eG','RWZ Rhein-Main eG'),
    ('Salford Group','Salford Group'),
    ('Samasz','Samasz'),
    ('Same (SDF Group)','Same (SDF Group)'),
    ('Same Deutz-Fahr Deutschland GmbH','Same Deutz-Fahr Deutschland GmbH'),
    ('Sampo-Rosenlew Oy','Sampo-Rosenlew Oy'),
    ('Samson','Samson'),
    ('Samson Agro A/S','Samson Agro A/S'),
    ('Sanko Holding','Sanko Holding'),
    ('SANY','SANY'),
    ('SAP SE','SAP SE'),
    ('Saudi Agricultural and Livestock Investment Company (SALIC)','Saudi Agricultural and Livestock Investment Company (SALIC)'),
    ('Savings Bank of Russian Federation (Sberbank)','Savings Bank of Russian Federation (Sberbank)'),
    ('Schäffer Maschinenfabrik GmbH','Schäffer Maschinenfabrik GmbH'),
    ('Schuler Manufacturing','Schuler Manufacturing'),
    ('Schwarzmayr Landtechnik','Schwarzmayr Landtechnik'),
    ('SD Kjærsgaard','SD Kjærsgaard'),
    ('SDF Group','SDF Group'),
    ('Sea Specialized Port Nika-Tera','Sea Specialized Port Nika-Tera'),
    ('Securities and Exchange Commission@Government of the United States','Securities and Exchange Commission@Government of the United States'),
    ('Seges','Seges'),
    ('Semler Agro Holding A/S','Semler Agro Holding A/S'),
    ('Sensor-Technik Wiedemann GmbH (STW)','Sensor-Technik Wiedemann GmbH (STW)'),
    ('Serco Landtechnik AG','Serco Landtechnik AG'),
    ('Sharmans','Sharmans'),
    ('SIA Baltic Agro Machinery','SIA Baltic Agro Machinery'),
    ('SIP','SIP'),
    ('Skolkovo Foundation','Skolkovo Foundation'),
    ('Small Robot Company','Small Robot Company'),
    ('Smart Guided Systems (Smart Path Systems)','Smart Guided Systems (Smart Path Systems)'),
    ('Snorkel','Snorkel'),
    ('Sogaz','Sogaz'),
    ('Solectrac','Solectrac'),
    ('Solideal','Solideal'),
    ('Solis (ITL)','Solis (ITL)'),
    ('South Dakota State University','South Dakota State University'),
    ('Spearhead Machinery Ltd','Spearhead Machinery Ltd'),
    ('Stanford University','Stanford University'),
    ('Stara','Stara'),
    ('Stecomat SARL','Stecomat SARL'),
    ('Steketee','Steketee'),
    ('STEYR Traktoren (CNHI)','STEYR Traktoren (CNHI)'),
    ('Stichting De Hoeksche Waard op de Kaart','Stichting De Hoeksche Waard op de Kaart'),
    ('Stihl','Stihl'),
    ('Strom Praha','Strom Praha'),
    ('Strube D&S GmbH','Strube D&S GmbH'),
    ('Stücker Landtechnik','Stücker Landtechnik'),
    ('Sukup Manufacturing Co','Sukup Manufacturing Co'),
    ('Sulky-Burel','Sulky-Burel'),
    ('SwarmFarm Robotics','SwarmFarm Robotics'),
    ('Swecon','Swecon'),
    ('Swedish Agro Machinery','Swedish Agro Machinery'),
    ('Swiss Federal Office of Agriculture','Swiss Federal Office of Agriculture'),
    ('SYDBANK A/S','SYDBANK A/S'),
    ('Symbio - a Faurecia Michelin Hydrogen Company','Symbio - a Faurecia Michelin Hydrogen Company'),
    ('Syngenta Group Co Ltd','Syngenta Group Co Ltd'),
    ('T&G Global Limited','T&G Global Limited'),
    ('Tanco','Tanco'),
    ('Taranis','Taranis'),
    ('TARMAKBIR','TARMAKBIR'),
    ('TBS Maskinpower','TBS Maskinpower'),
    ('Team 3 Services','Team 3 Services'),
    ('Technische Universiteit Delft','Technische Universiteit Delft'),
    ('Technotorg','Technotorg'),
    ('Tecnoma (Exel Industries)','Tecnoma (Exel Industries)'),
    ('Tehnos','Tehnos'),
    ('TELEFONAKTIEBOLAGET L.M. ERICSSON','TELEFONAKTIEBOLAGET L.M. ERICSSON'),
    ('TELUS Ventures','TELUS Ventures'),
    ('Temasek Holdings','Temasek Holdings'),
    ('Terramera Inc','Terramera Inc'),
    ('TerrAvion','TerrAvion'),
    ('The Boeing Company','The Boeing Company'),
    ('The State Bank for Foreign Economic Affairs of Turkmenistan','The State Bank for Foreign Economic Affairs of Turkmenistan'),
    ('Thrive AgTech','Thrive AgTech'),
    ('Thurlow Nunn Standen','Thurlow Nunn Standen'),
    ('Titan Machinery Germany','Titan Machinery Germany'),
    ('Titan Machinery Inc.','Titan Machinery Inc.'),
    ('Titan Machinery Romania SRL','Titan Machinery Romania SRL'),
    ('Titan Machinery Ukraine','Titan Machinery Ukraine'),
    ('tks Agri','tks Agri'),
    ('Tong Yang Moolsan Co. (TYM)','Tong Yang Moolsan Co. (TYM)'),
    ('Topcon','Topcon'),
    ('Toshiba Corporation','Toshiba Corporation'),
    ('Toyota Motor Corporation','Toyota Motor Corporation'),
    ('Tractors and Farm Equipment Limited (TAFE)','Tractors and Farm Equipment Limited (TAFE)'),
    ('Tramontini','Tramontini'),
    ('Trimble Inc','Trimble Inc'),
    ('Tümosan Motor Traktör','Tümosan Motor Traktör'),
    ('U.S Agency for International Development','U.S Agency for International Development'),
    ('U.S. Federal Communications Commission (FCC)','U.S. Federal Communications Commission (FCC)'),
    ('Unia','Unia'),
    ('Union of Industrialists and Entrepreneurs of Turkmenistan','Union of Industrialists and Entrepreneurs of Turkmenistan'),
    ('United Nations','United Nations'),
    ('Universitat Politècnica de València (UPV)','Universitat Politècnica de València (UPV)'),
    ('University of Bologna','University of Bologna'),
    ('University of Bonn','University of Bonn'),
    ('University of California San Diego','University of California San Diego'),
    ('University of Cambridge','University of Cambridge'),
    ('University of Copenhagen','University of Copenhagen'),
    ('University of Córdoba','University of Córdoba'),
    ('University of Hohenheim','University of Hohenheim'),
    ('University of Illinois at Urbana-Champaign','University of Illinois at Urbana-Champaign'),
    ('University of Lincoln','University of Lincoln'),
    ('University of Maryland','University of Maryland'),
    ('University of Melbourne','University of Melbourne'),
    ('University of Saskatchewan','University of Saskatchewan'),
    ('University of Sydney','University of Sydney'),
    ('University of Western Australia','University of Western Australia'),
    ('University of Zurich','University of Zurich'),
    ('Unser Lagerhaus Warenhandels-Gesellschaft GmbH','Unser Lagerhaus Warenhandels-Gesellschaft GmbH'),
    ('URSUS S.A.','URSUS S.A.'),
    ('Väderstad','Väderstad'),
    ('Väderstad AB','Väderstad AB'),
    ('Väderstad Components AB (Väderstad)','Väderstad Components AB (Väderstad)'),
    ('Vaderstad Industries Inc. (Seed Hawk Inc.','Vaderstad Industries Inc. (Seed Hawk Inc.'),
    ('Vaderstad Kft','Vaderstad Kft'),
    ('Valpadana (Argo)','Valpadana (Argo)'),
    ('Valtra (AGCO)','Valtra (AGCO)'),
    ('Vanderfield','Vanderfield'),
    ('Vermeer Corporation','Vermeer Corporation'),
    ('Versatile (Rostselmash)','Versatile (Rostselmash)'),
    ('Versatile Ukraine','Versatile Ukraine'),
    ('Vicon (Kubota)','Vicon (Kubota)'),
    ('VisioGreen','VisioGreen'),
    ('Vitesco Technologies','Vitesco Technologies'),
    ('Vodafone Spain','Vodafone Spain'),
    ('Vodafone Turkey','Vodafone Turkey'),
    ('Vogelsang GmbH & Co KG','Vogelsang GmbH & Co KG'),
    ('Voronezhselmash','Voronezhselmash'),
    ('Vredo','Vredo'),
    ('VTB Group','VTB Group'),
    ('WABCO Holdings Inc.','WABCO Holdings Inc.'),
    ('Wacker Neuson SE','Wacker Neuson SE'),
    ('Wageningen Universiteit en Researchcentrum','Wageningen Universiteit en Researchcentrum'),
    ('Weidemann (Wacker Neuson)','Weidemann (Wacker Neuson)'),
    ('Wirtgen Group (Deere & Co.)','Wirtgen Group (Deere & Co.)'),
    ('xarvio (BASF Digital Farming GmbH)','xarvio (BASF Digital Farming GmbH)'),
    ('Xtreme Manufacturing','Xtreme Manufacturing'),
    ('Yanmar','Yanmar'),
    ('YANMAR HOLDINGS CO LTD','YANMAR HOLDINGS CO LTD'),
    ('Yanmar Turkey Makine A.?.','Yanmar Turkey Makine A.?.'),
    ('YARA INTERNATIONAL ASA','YARA INTERNATIONAL ASA'),
    ('YTO Group Corporation','YTO Group Corporation'),
    ('ZAO Agrocomplex','ZAO Agrocomplex'),
    ('Zasso Group AG','Zasso Group AG'),
    ('Zetor Tractors a.s.','Zetor Tractors a.s.'),
    ('ZF Friedrichshafen AG','ZF Friedrichshafen AG'),
    ('ZG Raiffeisen eG','ZG Raiffeisen eG'),
    ('Zoetis Inc.','Zoetis Inc.'),
    ('Zoomlion Heavy Machinery','Zoomlion Heavy Machinery'),
    ('Zuidberg','Zuidberg'),
    ('ZWL Holding GmbH','ZWL Holding GmbH'),
]



class MyModel(models.Model):
   Countries = models.CharField( max_length=300, choices=COLOR_CHOICES, default='--type in a Country name --')
   Companies = models.CharField( max_length=300, choices=Company_Chioces, default='--type in a Company name --')



class Manors(models.Model):
  #field declarations

  def get_fields(self):
    return [(score_data.Company_name, score_data.Number_of_signals)]
