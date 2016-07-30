var $ = require ('jquery');
var moment = require('moment');

moment.locale('es');    // no funciona, a pesar que está tal cual lo pone la documentación:
                        //http://momentjs.com/docs/#/i18n/loading-into-nodejs/

// cambio de configuración del redondeo a segundos
moment.relativeTimeThreshold('s', 59);

//cambiar la forma en la que muestra los segundos (por defecto no indica el número de segundos)
moment.updateLocale('en', {
    relativeTime : {s: "%d seconds"}
});

comment_time = moment($('#1 time').attr("datetime"));

time = moment(comment_time).fromNow();

$("#fecha").append(time);



//ESTO ESTÁ A MEDIO HACER y además moments.js lo hace por nosotros
// now_time = moment();
// difference_time = now_time - comment_time;
// duration_time = moment.duration(difference_time);
// if (duration_time = moment.duration(7, "days")){
//     // console.log(moment(difference_time).format("DD/MM/YYYY"));
//     datetime_html = "Publicado el " + moment(comment_time).format("DD/MM/YYYY");
// } else if (duration_time > moment.duration(24, "hours")){
//     datetime_html = "Publicado el " + moment(difference_time).format("dddd");
// } else if (duration_time >=60){
//     datetime_html = "Publicado hace" + momento(difference_time).format('hh') + " horas";
// } else if (duration_time >=60){
//     datetime_html = "Publicado hace " + moment(comment_time).format("mm") + " minutos";
// } else if (duration_time <60){
//     datetime_html = "Publicado hace " + moment(comment_time).format("ss") + " segundos";
// }
