// Starter Challenge : Utilisation d’une fonction : https://tainix.fr/challenge/Utilisation-d-une-fonction



function find_modulo_3(values){
    
    let resultat = [];
    
    for(const value of values) {
        if(value%3==0){
            resultat.push(value)
        }
    }
    console.log(resultat.join("-"));
}

const values = [85, 54, 79, 78, 94, 69, 94, 91, 53, 26, 72, 72, 19, 33, 58, 60, 93, 96, 44, 47, 28, 16, 23, 31, 50, 60, 86];
find_modulo_3(values)