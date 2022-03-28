function toggle(carta){
    carta = '#' + carta
    if (document.querySelector(carta).style.display == "block"){
        document.querySelector(carta).style.display = "none";
    }
    else{
        document.querySelector(carta).style.display = "block";
    }
}