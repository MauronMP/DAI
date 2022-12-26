function detalle(i) {  // saca un modal con la información de cada coctel
    let html_str  = ''
    fetch('/api/recipes/'+i)
    .then(response => response.json())
    .then(filas => {
        
        // Muestro el nombre del cocktel i 
        html_str +="<h3 class='modal-title' id='modal_infoLabel'>" + filas.name + "</h3>"
        html_str +="<hr class='bg-secondary border-2 border-top borde-secondary'>"
        html_str +="<h5 class='my-3'> Ingredientes </h5>"
        html_str+= "<ul class='list-group'>"

        // Muestra fila a fila cada ingrediente del cocktel
        for (var key in filas.ingredients) {
            if (filas.ingredients.hasOwnProperty(key)) {
                html_str+="<p>"+key + ". " + filas.ingredients[key].name+"</p>"
            }
        }
        html_str += "</ul>"
        html_str +="<hr class='bg-secondary border-2 border-top border-secondary'>"

        // Muestro las instrucciones del cocktel i 
        html_str+='<h5> Elaboración: </h5>' + filas.instructions

        document.getElementById('recipe_data').innerHTML=html_str;
    })
}   