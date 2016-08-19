var $ = require ('jquery');


// TERCER INTENTO CON timeago
// var timeago = require('timeago');
// $.timeago.settings.refreshMillis = 1000;
// $.timeago.settings.strings.seconds = "%d seconds";

// (function ($) {
//   var originalVal = $.timeago.inWords;
//   $.timeago.inWords = function(distanceMillis) {
//     if (typeof distanceMillis != 'undefined') {
//         console.log("he sobreescrito la funcion inWords");
//
//         if (!this.settings.allowPast && ! this.settings.allowFuture) {
//             throw 'timeago allowPast and allowFuture settings can not both be set to false.';
//         }
//
//         var $l = this.settings.strings;
//         var prefix = $l.prefixAgo;
//         var suffix = $l.suffixAgo;
//         if (this.settings.allowFuture) {
//           if (distanceMillis < 0) {
//             prefix = $l.prefixFromNow;
//             suffix = $l.suffixFromNow;
//           }
//         }
//
//         if (!this.settings.allowPast && this.distanceMillis >= 0) {
//           return this.settings.strings.inPast;
//         }
//
//         var seconds = Math.abs(distanceMillis) / 1000;
//         var minutes = seconds / 60;
//         var hours = minutes / 60;
//         var days = hours / 24;
//         var years = days / 365;
//
//         function substitute(stringOrFunction, number) {
//           var string = $.isFunction(stringOrFunction) ? stringOrFunction(number, distanceMillis) : stringOrFunction;
//           var value = ($l.numbers && $l.numbers[number]) || number;
//           return string.replace(/%d/i, value);
//         }
//
//         var words = seconds < 60 && substitute($l.seconds, Math.round(seconds)) ||
//           seconds < 90 && substitute($l.minute, 1) ||
//           minutes < 45 && substitute($l.minutes, Math.round(minutes)) ||
//           minutes < 90 && substitute($l.hour, 1) ||
//           hours < 24 && substitute($l.hours, Math.round(hours)) ||
//           hours < 42 && substitute($l.day, 1) ||
//           days < 30 && substitute($l.days, Math.round(days)) ||
//           days < 45 && substitute($l.month, 1) ||
//           days < 365 && substitute($l.months, Math.round(days / 30)) ||
//           years < 1.5 && substitute($l.year, 1) ||
//           substitute($l.years, Math.round(years));
//
//         var separator = $l.wordSeparator || "";
//         if ($l.wordSeparator === undefined) { separator = " "; }
//         return $.trim([prefix, words, suffix].join(separator));
//
//
//
//     }
//     return originalVal.call(this, value);
//   };
// })($);
//
//
// $(document).ready(function() {
//  $("time.timeago").timeago();
// });




// SEGUNDO INTENTO
var moment = require('moment');
moment().format();

//moment.locale('cs'); //no funciona por un bug: http://momentjs.com/docs/#/use-it/browserify/
require('moment/locale/es');    // con esto si funciona

// cambio de configuración del redondeo a segundos
moment.relativeTimeThreshold('s', 59);

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
        elapsed_time = now_time.diff(comment_time, 'seconds');

        if (elapsed_time < 60){
            $(time).text(comment_time.fromNow());
            setTimeout(datetime, 1000);
        } else if (elapsed_time < (60*60)) {
            $(time).text(comment_time.fromNow());
            setTimeout(datetime, 60000);
        } else if (elapsed_time < (60*60*24)){
            $(time).text(comment_time.fromNow());
        } else if (elapsed_time < (60*60*24*7)) {
            var to_append = "el " + moment(comment_time).format('dddd');
            $(time).append(to_append);
        } else if (elapsed_time > (60*60*24*7)) {
            $(time).append(comment_time.format('LLL'));
            console.log(comment_time.format());
        }
    }
})();

//  PRIMER INTENTO
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
