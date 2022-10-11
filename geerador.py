import  os
from pickle import TRUE
from random import  random  


Nombres = ["Hugo" , "Martín" , "Lucas" , "Mateo" , "Leo" , "Daniel" , "Alejandro" , "Pablo" , "Manuel" , "Álvaro" , "Adrián" , "David" , "Mario" , "Enzo" , "Diego" , "Marcos" , "Izan" , "Javier" , "Marco" , "Álex" , "Bruno" , "Oliver" , "Miguel" , "Thiago" , "Antonio" , "Marc" , "Carlos" , "Ángel" , "Juan" , "Gonzalo" , "Gael" , "Sergio" , "Nicolás" , "Dylan" , "Gabriel" , "Jorge" , "José" , "Adam" , "Liam" , "Eric" , "Samuel" , "Darío" , "Héctor" , "Luca" , "Iker" , "Amir" , "Rodrigo" , "Saúl" , "Víctor" , "Francisco" , "Iván" , "Jesús" , "Jaime" , "Aarón" , "Rubén" , "Ian" , "Guillermo" , "Erik" , "Mohamed" , "Julen" , "Luis" , "Pau" , "Unai" , "Rafael" , "Joel" , "Alberto" , "Pedro" , "Raúl" , "Aitor" , "Santiago" , "Rayan" , "Pol" , "Nil" , "Noah" , "Jan" , "Asier" , "Fernando" , "Alonso" , "Matías" , "Biel" , "Andrés" , "Axel" , "Ismael" , "Martí" , "Arnau" , "Imran" , "Luka" , "Ignacio" , "Aleix" , "Alan" , "Elías" , "Omar" , "Isaac" , "Youssef" , "Jon" , "Teo" , "Mauro" , "Óscar" , "Cristian" , "Leonardo" , "Abel" , "Adrián" , "Alejandro" , "Ángel" , "Carlos" , "César" , "Bruno" , "Daniel" , "Darío" , "David" , "Diego" , "Emilio" , "Fabián" , "Felipe" , "Gabriel" , "Héctor" , "Hugo" , "Jacobo" , "Jaime" , "Joaquín" , "Juan" , "Leonardo" , "Leo" , "Lucas" , "Marcos" , "Martín" , "Mateo" , "Matías" , "Miguel" , "Nicolás" , "Pablo" , "Raúl" , "Samuel" , "Santiago" , "Sebastián" , "Tomás" , "Tristán" , "Joan" , "Andrés" , "Ricardo" , "Manuel" , "Ezequiel" , "Francisco" , "Elías" , "Blas" , "Alfonso" , "Ulises" , "Gerardo" , "Alfredo" , "Álvaro" , "Amadeo" , "Amancio" , "Antonio" , "Baltasar" , "Beltrán" , "Benito" , "Rufino" , "Boris" , "Camilo" , "Ciro" , "Conrado" , "Donato" , "Florentino" , "Saturnino" , "Segundo" , "Anastasio" , "Cipriano" , "Teófilo" , "Casimiro" , "Bonifacio" , "Victorino" , "Eleuterio" , "Urbano" , "Severino" , "Inocencio" , "Primitivo" , "Bautista" , "Agapito" , "Benedicto" , "Enrique" , "Eugenio" , "Estanislao" , "Fausto" , "Faustino" , "Felipe" , "Félix" , "Fermín" , "Francisco" , "Gaspar" , "Genaro" , "Hilario" , "Hugo" , "Ignacio" , "Ireneo" , "Ismael" , "Joaquín" , "José" , "Juan" , "Julián" , "Justo" , "Leopoldo" , "León" , "Lisandro" , "Lorenzo" , "Lucas" , "Manuel" , "Mateo" , "Pedro" , "Pío" , "Romeo" , "Roque" , "Rufino" , "Santiago" , "Salvador" , "Simón" , "Valentín" , "Valentino" , "Vicente" , "Víctor" , "Abundio" , "Ambrosio" , "Aniceto" , "Anselmo" , "Apolonio" , "Aquilino" , "Arsenio" , "Atanasio" , "Atilano" , "Avelino" , "Bartolo" , "Basilio" , "Baudilio" , "Benigno" , "Buenaventura" , "Calixto" , "Celedonio" , "Cirilo" , "Clemente" , "Conrado" , "Crisóstomo" , "Crispín" , "Críspulo" , "Dionisio" , "Eliodoro" , "Eliseo" , "Emerico" , "Emeterio" , "Epifanio" , "Eufrasio" , "Eulogio" , "Feliciano" , "Florencio" , "Froilán" , "Fructuoso" , "Frutos" , "Gregorio" , "Gumersindo" , "Hermenegildo" , "Herminio" , "Higinio" , "Hipólito" , "Indalecio" , "Isidoro" , "Laureano" , "Leandro" , "Leocadio" , "Leovigildo" , "Lope" , "Macario" , "Melitón" , "Nemesio" , "Nicanor" , "Niceto" , "Nicomedes" , "Odón" , "Orencio" , "Pantaleón" , "Patricio" , "Perfecto" , "Petronilo" , "Policarpo" , "Polonio" , "Prudencio" , "Regino" , "Remigio" , "Rómulo" , "Ruperto" , "Sandalio" , "Serapio" , "Servando" , "Silvestre" , "Sinforoso" , "Sofronio" , "Telesforo" , "Tiburcio" , "Toribio" , "Ulpiano" , "Valeriano" , "Venancio" , "Victoriano" , "Zoilo" , "Abdón" , "Abilio" , "Acacio" , "Adalberto" , "Adolfo" , "Afrodisio" , "Ágabo" , "Albino" , "Alcibíades" , "Amalio" , "Amasvindo" , "Amelio" , "Amonario" , "Antelmo" , "Antíoco" , "Antenor" , "Argimiro"  ];
Apellidos = ["Hernandez " , "Garcia " , "Martinez " , "Lopez " , "Gonzalez " , "Perez " , "Rodriguez " , "Sanchez " , "Ramirez " , "Cruz " , "Flores " , "Gomez " , "Morales " , "Vazquez " , "Reyes " , "Jimenez " , "Torres " , "Diaz " , "Gutierrez " , "Ruiz " , "Mendoza " , "Aguilar " , "Ortiz " , "Moreno " , "Castillo " , "Romero " , "Alvarez " , "Mendez " , "Chavez " , "Rivera " , "Juarez " , "Ramos " , "Dominguez " , "Herrera " , "Medina " , "Castro " , "Vargas " , "Guzman " , "Velazquez " , "Rojas " , "De la cruz " , "Contreras " , "Salazar " , "Luna " , "Ortega " , "Santiago " , "Guerrero " , "Estrada " , "Bautista " , "Cortes " , "Soto " , "Alvarado " , "Espinoza " , "Lara " , "Avila " , "Rios " , "Cervantes " , "Silva " , "Delgado " , "Vega " , "Marquez " , "Sandoval " , "Carrillo " , "Fernandez " , "Leon " , "Mejia " , "Solis " , "Rosas " , "Ibarra " , "Valdez " , "Nuez " , "Campos " , "Santos " , "Camacho " , "Navarro " , "Maldonado " , "Rosales " , "Acosta " , "Pea " , "Miranda " , "Cabrera " , "Trejo " , "Valencia " , "Nava " , "Pacheco " , "Robles " , "Molina " , "Fuentes " , "Rangel " , "Huerta " , "Meza " , "Padilla " , "Espinosa " , "Aguirre " , "Salas " , "Cardenas " , "Orozco " , "Valenzuela " , "Ayala " , "Zuñiga " , "Ochoa " , "Mora " , "Serrano " , "Salinas " , "Tapia " , "Olvera " , "Duran " , "Suarez " , "Macias " , "Zamora " , "Arellano " , "Calderon " , "Barrera " , "Villegas " , "Zavala " , "Gallegos " , "Lozano " , "Beltran " , "Velasco " , "Figueroa " , "Franco " , "Galvan " , "Montes " , "Sosa " , "Villanueva " , "Arias " , "Andrade " , "Antonio " , "Marin " , "Vasquez " , "Esquivel " , "Ponce " , "Corona " , "Garza " , "Alonso " , "Palacios " , "Trujillo " , "Bernal " , "Pineda " , "Rocha " , "Cortez " , "Rubio " , "Escobar " , "Galindo " , "Villa " , "De jesus " , "Cano " , "Benitez " , "Cuevas " , "Bravo " , "Mata " , "Osorio " , "Carmona " , "Montoya " , "Enriquez " , "Rivas " , "Parra " , "Cisneros " , "Resendiz " , "Cordova " , "De la rosa " , "Tellez " , "Vera " , "Tovar " , "Zarate " , "Leyva " , "Quintero " , "Quiroz " , "Salgado " , "Becerra " , "Arroyo " , "Peralta " , "Esparza " , "Avalos " , "Roman " , "Barajas " , "Felix " , "Guevara " , "Murillo " , "Olivares " , "De leon " , "Castellanos " , "Villarreal " , "Lugo " , "Montiel " , "Angeles " , "Villalobos " , "Segura " , "Saucedo " , "Gallardo " , "Chan " , "Reyna " , "Mercado " , "Davila " , "Navarrete " , "Paredes " , "Guerra " , "Guillen " , "Leal " , "Monroy " , "Del angel " , "Zapata " , "Santana " , "Nieto " , "Islas " , "Uribe " , "Escobedo " , "Pia " , "Granados " , "Solano " , "Caballero " , "Zepeda " , "Arriaga " , "Barron " , "Barrios " , "Galicia " , "Ojeda " , "Gil " , "Acevedo " , "Alfaro " , "Godinez " , "Mondragon " , "Medrano " , "Duarte " , "Ventura " , "Balderas " , "Rico " , "Aguilera " , "Coronado " , "Arredondo " , "Francisco " , "Escamilla " , "Palma " , "Amador " , "Blanco " , "Najera " , "Bonilla " , "Pech " , "Gamez " , "Ocampo " , "Carbajal " , "Valdes " , "Carrasco " , "Romo " , "Melendez " , "Escalante " , "Hurtado " , "Sierra " , "May " , "Barragan " , "Armenta " , "Carranza " , "Alarcon " , "Vidal " , "De los santos " , "Correa " , "Arreola " , "Baez " , "Carrera " , "Gaytan " , "Alcantara " , "Quezada " , "Anaya " , "Colin " , "Toledo " , "Arenas " , "Renteria " , "Jaramillo " , "Santillan " , "Valle " , "Varela " , "Venegas " , "Rendon " , "Soriano " , "Lira " , "Aranda " , "Zaragoza " , "Aviles " , "Cordero " , "Moran " , "Valadez " , "Quintana " , "Arteaga " , "Hidalgo " , "De la torre " , "Salvador " , "Galvez " , "Gamboa " , "Sotelo " , "Aquino " , "Becerril " , "Baltazar " , "Altamirano " , "Cazares " , "Montalvo " , "Covarrubias " , "Aparicio " , "Canul " , "Martin " , "Paz "  ]; 
Ciudades = ["Tokio" , "Nueva York" , "Los Ángeles" , "Londres" , "Seúl" , "París" , "Osaka" , "Chicago" , "Shanghái" , "Berlín" , "Moscú" , "Washington D.C." , "Beijing" , "Ciudad de México" , "São Paulo" , "Dallas" , "Shenzhen" , "Cantón" , "Toronto" , "Frankfurt" , "Tianjin" , "Houston" , "Mumbai" , "Roma" , "Filadelfia" , "Yakarta" , "Hamburgo" , "San Francisco" , "Singapur" , "Hong Kong" , "Boston" , "Nagoya" , "Ámsterdam" , "Estambul" , "Taipéi" , "Chonging" , "Madrid" , "Atlanta" , "Birmingham" , "Dongguan" , "Milán" , "Busan" , "Bangkok" , "Seattle" , "Buenos Aires" , "Bruselas" , "Nankin" , "Sídney" , "Wuhan" , "Múnich" , "Miami" , "Hangzhou" , "Río de Janeiro" , "Kioto" , "Minneapolis" , "Dubái" , "Shenyang" , "Riad" , "Detroit" , "Montreal" , "Chengdu" , "Ginebra" , "Fukuoka" , "Colonia" , "Nueva Delhi" , "Viena" , "Estocolmo" , "Oslo" , "Lisboa" , "Dublín" , "Glasgow" , "Bogotá" , "Melbourne" , "San Petersburgo" , "Marsella" , "Phoenix" , "Harbin" , "Róterdam" , "Manila" , "Santiago" , "Johannesburgo" , "Barcelona" , "Baltimore" , "Stuttgart" , "Abu Dabi" , "Tel Aviv" , "Zúrich" , "Hefei" , "Sapporo" , "Vancouver" , "Calcuta" , "Brisbane" , "Monterrey" , "Yeda" , "Brasilia" , "El Cairo" , "Nápoles" , "Varsovia" , "Lima" , "Lagos" , "Denver" , "Lyon" , "Incheon" , "Dusseldorf" , "Copenhague" , "Praga" , "Liverpool" , "Amberes" , "Valencia" , "Hiroshima" , "Atenas" , "San José" , "Guadalajara" , "La Haya" , "Novosibirsk" , "Bonn" , "Portland" , "Jerusalén" , "Ankara" , "Kuala Lumpur" , "Doha" , "Riverside" , "Jinan" , "Ciudad del Cabo" , "Perth" , "Daegu" , "Sendai" , "Austin" , "Toulouse" , "Ahmedabad" , "San Luis" , "Basilea" , "Sevilla" , "Qingdao" , "Xi'an" , "Pittsburgh" , "Budapest" , "Venecia" , "San Diego" , "Kuwait" , "Nanchang" , "Dalian" , "Helsinki" , "Berna" , "Nairobi" , "Taiyuan" , "Haifa" , "Bangalore" , "Bristol" , "Ho Chi Minh" , "Essen" , "Shantou" , "Kunming" , "Daejeon" , "Kaohsiung" , "Sacramento" , "Utrecht" , "Gotemburgo" , "Belo Horizonte" , "Ekaterimburgo" , "Shizuoka" , "Zibo" , "Zhengzhou" , "Lausana" , "Zaragoza" , "Charlotte" , "Orlando" , "Cleveland" , "Bremen" , "Puebla" , "Huizhou" , "Niza" , "Fortaleza" , "Ottawa" , "Casablanca" , "Gante" , "Indianápolis" , "Cincinnati" , "Izmir" , "Chennai" , "Fuzhou" , "Shijiazhuang" , "Changsha" , "Saitama" , "Dresde" , "Curitiba" , "Ulsan" , "Málaga" , "Turín" , "Columbus" , "Calgary" , "Kansas" , "Quebec" , "Mánchester" , "Hyderabad" , "Auckland" , "Bilbao" , "San Antonio" , "Córdoba" , "Foshan" , "Wuxi" , "Sanya" , "Niigata" , "Leipzig" , "Eindhoven" , "Nantes" , "Nizhni Nóvgorod" , "Salvador" , "Graz" , "Cracovia" , "Suzhou" , "Nashville" , "Las Vegas" , "Surabaya" , "Tijuana" , "Zhongshan" , "Zhuhai" , "Palermo" , "Macao" , "Sheffield" , "Oporto" , "León" , "Murcia" , "Génova" , "Estrasburgo" , "Teherán" , "Karachi" , "Virginia Beach" , "Milwaukee" , "Providence" , "Kitakyushu" , "Almaty" , "Porto Alegre" , "Adelaida" , "Changchun" , "Ningbo" , "Xiamen" , "Nueva Orleans" , "Salt Lake City" , "Recife" , "Montpellier" , "Surat" , "Medan" , "Taichung" , "Santiago de Querétaro" , "Lodz" , "Búfalo" , "Richmond" , "Oklahoma City" , "Guiyang" , "Taizhou" , "Yantai" , "Kumamoto" , "Leeds" , "Hanói" , "Burdeos" , "Bridgeport" , "Rochester" , "Memphis" , "Lieja" , "Durban" , "Linz" , "Wenzhou" , "Urumqi" , "Edimburgo" , "Raleigh" , "Jacksonville" , "Bursa" , "Pretoria" , "Leicester" , "Jaipur" , "Daca" , "Medellín" , "Bucarest" , "Louisville" , "Honolulu" , "Tangshan" , "Luoyang" , "Alejandría" , "Bolonia" , "Albany" , "Birmingham" , "Florencia" , "Nantong" , "Tampa" , "Luxemburgo" , "Haikou" , "Edmonton" , "Huzhou" , "Omaha" , "Tulsa" , "Lille" , "Changzhou" , "Akron" , "Dayton" , "El Paso" , "Argel" , "Adis Abeba" , "Winnipeg" ];
Colores = ["Negro", "azul", "marrón", "gris", "verde", "naranja", "rosa", "púrpura", "rojo", "blanco" , "amarillo"] 
tipo = ["loca","Estatal","Nacional","Internacional"]
pos = ["delantero" , "postero" , "defensa" ,  "medio" ]

class Random:
    def __init__(self) -> None:
        self.getRandom()
        self.getName()
        self.getSurName() 
        self.getArray()
        self.getAllName()
        self.getCity()
        self.getTel()
        self.getYear()
        self.getDay()
        self.getMonth()
        self.getFecha()
        self.getColor()
        self.getTipo()
        self.getPos()

    def   getName(self) -> str:
        return Nombres[self.getRandom(max = len(Nombres))] 

    def getSurName(self) -> str:
        return  Apellidos[self.getRandom(max = len(Apellidos))]  

    def getRandom(self,min = 0 , max = 10) -> int:
        try:
            if min > max : 
                return "Error min = {} > max = {}".format(min,max)     
            num = int(random() * max) 
            return num        
        except:

            return "Error min = {} > max = {}".format(min,max)
        

    def getAllName(self) ->str :
        return self.getName() + " " + self.getSurName() + " " + self.getSurName()  

    def getCity(self) -> str :
        return Ciudades[self.getRandom(max = len(Ciudades))]

    def  getTel(self,lada = "452") ->str :
        for i in range(0,7):
            lada += str(self.getRandom(max = 10)) ;
        return lada 
    def getYear(self,min = 2000 , max =2022) -> str:
            cant  = 2
            years = [] 
            while  cant > len(years) :
                year = self.getRandom(min,max)
                if not(year in  years):
                    if year >= min  and  year <= max :
                        years.append(year)
            return  years[self.getRandom(max = len(years ))]


    def getDay(self,min =  1  , max =31) -> str:
            cant  = 2
            days = [] 
            while  cant > len(days) :
                day = self.getRandom(min,max)
                if not(day  in  days ):
                    if day >= min  and  day <= max :
                        days.append(day)
            return  days[self.getRandom(max = len(days))]


    def getMonth(self,min =  1  , max =12) -> str:
            cant  = 2
            months = [] 
            while  cant > len(months) :
                month = self.getRandom(min,max)
                if not(month  in  months ):
                    if month >= min  and  month <= max :
                        months.append(month)
            return  months[self.getRandom(max = len(months))]


    def  getFecha(self,min = 2000 , max = 2022 , formato = "{y}/{m}/{d}") -> str :
            cant  = 2
            Fechas = [] 
            while  cant > len(Fechas) :
                year = self.getYear();
                month = self.getMonth()  
                day  = self.getDay(max=21)  if  month ==  2  else  self.getDay();
                Fecha  = formato.format(y = str(year) , m = (str( month) if month >= 10 else "0" + str(month) ) ,  d =  (str( day) if day >= 10 else "0" + str(day) )   )
                if not(Fecha in  Fechas ):
                    if year >= min  and  year <= max :
                        Fechas.append(Fecha)
            return  Fechas[self.getRandom(max = len(Fechas))]
        
    def  getArray(self,size = 10 ,max = 10 ,unique = True ) :
        n = [] 
        while len(n) < size :
            num  = self.getRandom(max = max )
            if  unique :
                if not(num  in n):
                    n.append(num)     
            else :
                n.append(num)
            
        return n ; 

    def getColor(self) -> str :
        return  Colores[self.getRandom(max  = len(Colores))]

    def getTipo(self) -> str :
        return  tipo[self.getRandom(max = len(tipo))]

    def getPos(self) -> str :
        return  pos[self.getRandom(max = len(pos))]



             



def  _main() -> None:
     # n  nombres 
     r = Random() 
     n =  5 
     for  i  in  range(0,n):
        Nombre =  r.getAllName()
        print(f"{Nombre}") 
    
    
    
    




if __name__ == "__main__" :
    _main()


