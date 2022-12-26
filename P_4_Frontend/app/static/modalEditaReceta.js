function editar_receta(id) {

    var nombre = document.getElementById('inputNombreCocktelEditar').value
    var ingredientes = document.getElementById('textareaIngredientesEditar').value
    var instrucciones = document.getElementById('textareaInstruccionesEditar').value

    //Eliminamos espacios, quitamos los guiones y los separamos por ',' elemento a elemento
    ingredientes = ingredientes.replace(/\r?\n|\r/g, " ");
    ingredientes = ingredientes.split('-').map(element => element.trim());
    ingredientes = ingredientes.slice(1);
    json_data = []

    // Guarda en un array el formato en json name : ingrediente para posteriormente insertarlo en el PUT
    for (var i = 0; i < ingredientes.length; i++) {
        nombre_ingrediente = { "name": ingredientes[i] };
        json_data.push(nombre_ingrediente)
    }

    (async () => {
        // Llamada por id con la opción PUT
        const rawResponse = await fetch("api/recipes/" + id, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            // Se le pasa los datos a actualizar introducidos en el formulario y se pasa a formato json
            body: JSON.stringify({ name: nombre, ingredients: json_data, instructions: instrucciones })
        });
        const content = await rawResponse.json();
        window.location.reload();
        console.log(content);
    })();
}