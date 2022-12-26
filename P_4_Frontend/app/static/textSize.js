// Defino la variable localStorage del tamaño del texto
let tamanioTexto = localStorage.getItem("tamanioTexto");

// En caso de que no esté definido se establece una por defecto
if(tamanioTexto === null){
    txt = document.getElementById('tablaContenido');
    style = window.getComputedStyle(txt, null).getPropertyValue('font-size');
    currentSize = parseFloat(style);
    localStorage.setItem("tamanioTexto", currentSize);
} 
// En caso de estar ya incrementado el valor del texto se establece el que tenga asignado anteriormente
if(tamanioTexto != 16){
    txt = document.getElementById('tablaContenido');
    txt.style.fontSize = (localStorage.getItem("tamanioTexto")) + 'px';
}

// Aumento el tamaño del texto y guardo el valor en la variable del localStorage
function IncrementarTamanioTexto() {
    txt = document.getElementById('tablaContenido');
    style = window.getComputedStyle(txt, null).getPropertyValue('font-size');
    currentSize = parseFloat(style);
    txt.style.fontSize = (currentSize + 5) + 'px';
    localStorage.setItem("tamanioTexto", currentSize+5);
}

// Decremento el tamaño del texto y guardo el valor en la variable del localStorage
function DecrementarTamanioTexto() {
    txt = document.getElementById('tablaContenido');
    style = window.getComputedStyle(txt, null).getPropertyValue('font-size');
    currentSize = parseFloat(style);
    txt.style.fontSize = (currentSize - 5) + 'px';
    localStorage.setItem("tamanioTexto", currentSize-5);
}