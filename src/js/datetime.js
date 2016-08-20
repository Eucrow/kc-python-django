var $ = require ('jquery');

// SEGUNDO INTENTO
var moment = require('moment');
moment().format();

//moment.locale('cs'); //no funciona por un bug: http://momentjs.com/docs/#/use-it/browserify/
require('moment/locale/es');    // con esto si funciona

// Round relative time evaluation down
moment.relativeTimeRounding(Math.floor);

// cambio de configuración del redondeo a minutos
moment.relativeTimeThreshold('s', 60);
// cambio de configuración del redondeo a horas
moment.relativeTimeThreshold('m', 60);

//cambiar la forma en la que muestra los segundos (por defecto no indica el número de segundos)
moment.updateLocale('es', {
    relativeTime : {s: "%d segundos"}
});

(function datetime(){
    var times =  $(".container-article").find("time");
    for (var i=0; i<times.length; i++) {
        time = $(times[i]);
        refreshTime(time);
    }

    function refreshTime(time){
        comment_time = moment($(time).attr("datetime"), "YYYY-MM-DD HH:mm:ss");
        now_time = moment();
        elapsed_time = now_time.diff(comment_time, 'seconds'); // tiempo que hay
        // entre que se publica el artículo hasta el momento en que se refresca la pantalla

        // Función para actualizar y refrescar el tiempo transcurrido
        // Sólo vale para algunos casos... :(
        function updateAndRefresh(timeToRefresh){
            $(time).text(comment_time.fromNow());
            setTimeout(datetime, timeToRefresh);
        }

        // Según el tiempo que ha pasado desde la publicación
        if (elapsed_time < 60){ // menos de un minuto
            updateAndRefresh(1000); // refresca cada segundo
        } else if (elapsed_time < (60*60)) { // menos de una hora
            updateAndRefresh(60000); // refresca cada minuto
        } else if (elapsed_time < (60*60*24)){ // menos de un día
            // En el caso de las horas, mejor refrescar cuando ha pasado una hora desde
            // la publicación:
                minuto_pub =  moment(comment_time).minutes();
                minuto_act =  moment(now_time).minutes();
                timeToRefresh = 0;

                if (minuto_pub <= minuto_act) {
                    timeToRefresh = 60 - (minuto_act - minuto_pub);
                } else if (minuto_pub > minuto_act) {
                    timeToRefresh = minuto_pub - minuto_act;
                }

            updateAndRefresh( timeToRefresh*60*1000 );
        } else if (elapsed_time < (60*60*24*7)) { //menos de una semana
            var to_append = "el " + moment(comment_time).format('dddd');
            $(time).text(to_append);
            setTimeout(datetime, (24*60*60*1000)); // refresca cada día
        } else if (elapsed_time > (60*60*24*7)) { //mas de una semana
            $(time).text(comment_time.format('LLL'));
        }

    }
})();
