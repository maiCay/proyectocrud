var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args);
document.getElementById("id-receta").value = decodeURIComponent(parts[0][1])
document.getElementById("imagen-receta").value = decodeURIComponent(parts[1][1])
document.getElementById("nombre-receta").value = decodeURIComponent(parts[2][1])
document.getElementById("descripcion-receta").value = decodeURIComponent(parts[3][1])
 
function modificar() {
    let id = document.getElementById("id-receta").value
    let i = document.getElementById("imagen-receta").value
    let n = document.getElementById("nombre-receta").value
    let d = document.getElementById("descripcion-receta").value
    let receta = {
        imagen: i,
        nombre: n,
        descripcion: d
    }

    let url = "http://localhost:5000/recetas/"+id;
    var options = {
        body: JSON.stringify(receta),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
