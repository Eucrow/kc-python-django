var gulp        = require('gulp');
var browserSync = require('browser-sync').create();


//definimos tarea por defecto
gulp.task("default", function(){

    //iniciamos browserSync
    browserSync.init({
        server: "./",//levanta el servidor web en la carpeta actual
        //proxy: "127.0.0.1:8000",    // actúa como proxy enviado las peticiones a
                                    //sparrest que está en el puerto 8000
        //browser: "chrome"
    });

    // observa cambio en archivos HTML y recarga el navegador
    gulp.watch("*.html").on("change", browserSync.reload);
});
