
const recetas = []              // declaraciones   
let html_str  = ''              // de variables
let i         = 0               //
// fetch devuelve una promise
fetch('/api/recipes')           // GET por defecto,
.then(res => res.json())        // respuesta en json, otra promise
.then(filas => {                // arrow function
    filas.forEach(fila => {     // bucle ES6, arrow function
        i++
        recetas.push(fila)      // se guardan para después sacar cada una             
        // ES6 templates
        html_str += `
        <tr id="${fila._id}">
            <td class="numeroCocktel">${i}</td>
                <td>
                    <button onclick="detalle('${fila._id}')" 
                        type="button" class="btn btn-outline btn-sm"
                        data-bs-toggle="modal" data-bs-target="#modal_info" data-bs-dismiss="modal">
                        <div class="nombreCocktel">${fila.name}</div>
                    </button>
                </td>
            <td>
                <button onclick="editar('${fila._id}')" type="button" class="btn btn-warning btn-sm btn-sm mx-4" data-bs-toggle="modal" data-bs-target="#modal_edit" data-bs-dismiss="modal">Edit</button>
                <button onclick="borrar('${fila._id}')" type="button" class="btn btn-danger btn-sm btn-sm mx-4" data-bs-toggle="modal" data-bs-target="#modal_borrar" data-bs-dismiss="modal">Borrar</button>
            </td>
        </tr>`         // ES6 templates
    });
    document.getElementById('tbody').innerHTML=html_str  // se pone el html en su sitio
})