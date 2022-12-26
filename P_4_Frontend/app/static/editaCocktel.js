function editar(id){
    html_str=''
    fetch('/api/recipes/'+id)
    .then(response => response.json())
    .then(filas => {
        // Voy guardando los ingredientes en una cadena de texto para luego segmentarla por cada uno
        for (var key in filas.ingredients) {
            if (filas.ingredients.hasOwnProperty(key)) {
                html_str+="- " +filas.ingredients[key].name + "\n"
            }
        }
        // Va almacenando los valores de los distintos elementos html
        var res = document.querySelectorAll("#inputNombreCocktelEditar, #textareaIngredientesEditar, #textareaInstruccionesEditar, #boton_editar_receta");
        for (var i = 0; i < res.length; i++) {
            switch (i) {
                case 0:
                    res[i].value = filas.name;
                    break;
                case 1:
                    res[i].value = html_str;
                    break;
                case 2:
                    res[i].value = filas.instructions;
                    break;
                case 3:
                    res[i].value = filas._id;
                    break;
                default:
                    console.log(`Error`);
            }
        }
    })
}