function guardar() {
 
    let i = document.getElementById("imagen-receta").value;
    let n = document.getElementById("nombre-receta").value;
    let d= document.getElementById("descripcion-receta").value;
 
    let receta = {
        imagen: i,
        nombre: n,
        descripcion: d
    };

    let url = "http://localhost:5000/recetas";
    var options = {
        body: JSON.stringify(receta),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    };
    
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
 
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}

