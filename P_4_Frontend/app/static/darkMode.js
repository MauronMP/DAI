
// Obtengo los elementos a cambiar con el modo oscuro y defino la variable darkMode
const toggleBtn = document.getElementById("toggle-btn");
const theme = document.getElementById("theme");
const nombreCockteles = document.getElementsByClassName('nombreCocktel');
const trTable = document.getElementById('trTable');
let darkMode = localStorage.getItem("dark-mode");

// En caso de no estar definino el modo oscuro se asume que está desactivado por defecto
if(darkMode === null){
    darkMode = localStorage.setItem("dark-mode", "disabled");
} 

// En caso de que ya estuviera activado en otra sesión se activa de nuevo al recargar la página
if (localStorage.getItem("dark-mode") === "enabled") {
    enableDarkMode();
} else {
    darkMode = localStorage.setItem("dark-mode", "disabled");
}

// Esta función establece los campos obtenidos previamente del html y le establece el css del modo oscuro
function enableDarkMode(){
    localStorage.setItem("dark-mode", "enabled");
    theme.classList.add("dark-mode-theme");
    for (const cocktel of nombreCockteles) {
        cocktel.classList.add('dark-mode-theme');
    }
    trTable.classList.add("dark-mode-theme");
};

// Esta función eliminar los atributos del modo oscuro y los deja por defecto tal y como estaban previamente
function disableDarkMode() {
    localStorage.setItem("dark-mode", "disabled");
    theme.classList.remove("dark-mode-theme");
    for (const cocktel of nombreCockteles) {
        cocktel.classList.remove('dark-mode-theme');
    }
    trTable.classList.remove("dark-mode-theme");
};

// Se ejecuta cuando el usuario presiona el boton del modo oscuro
function modoOscuro(){
    if (localStorage.getItem("dark-mode") === "disabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
};