// Easy Challenge: L’armée de Daenerys : https://tainix.fr/challenge/L-armee-de-Daenerys

let armee = 5844;
let armee_after = 0;
let need = "";
var mon_armee_nombre = []
let nombre_dragon = 0
let nombre_immacules = 0
let nombre_dotrakis = 0
var mon_armee_nombre = 
        {
            dragon:{nombre:3,degats:1000},
            immacules:{nombre:200,degats:15},
            dotrakis:{nombre:5000,degats:1}
        }
let tiers_fight = armee/3
armee = armee - tiers_fight
while (tiers_fight > mon_armee_nombre["dragon"]["degats"]){
    if (tiers_fight > mon_armee_nombre["dragon"]["degats"]){
        nombre_dragon++;
        tiers_fight = tiers_fight - mon_armee_nombre["dragon"]["degats"];
    }
    else{
        break
    }
}
armee = armee + tiers_fight;
need = ""+nombre_dragon + "_";
let moitie_restante = armee / 2;
armee = armee - moitie_restante
while (moitie_restante > mon_armee_nombre["immacules"]["degats"]){
    if (moitie_restante > mon_armee_nombre["immacules"]["degats"]){
        nombre_immacules++;
        moitie_restante = moitie_restante - mon_armee_nombre["immacules"]["degats"];
    }
    else{
        break
    }
}
armee = armee + moitie_restante;
need = need+""+nombre_immacules + "_" + armee ;
console.log(armee);
