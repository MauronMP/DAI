function eliminar_receta(id){
    // Peticion get por id del cocktel a eliminar con la condición DELETE
    fetch("api/recipes/"+id,
    {
        method: "DELETE",
    })
    // En caso de ser buena la petición y correcta la orden, se busca el elemento y elimina de la tabla
    .then(response => {
        const element = document.getElementById(id);
        element.remove();
    })
    .catch(error => console.log(error))
}