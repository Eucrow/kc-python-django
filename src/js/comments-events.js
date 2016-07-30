var $ = require ('jquery');

var commentsList = require('./comments-list.js');

module.exports = {
    load: function(){
        $(document).ready(function() {
            $(window).scroll(function() {
                if ($('body').height() <= ($(window).height() + $(window).scrollTop())) {
                    if (!$.trim($(".list-comments").html())){ //$.trim elimina caracteres en blanco y saltos de línea
                        // cargamos la lista de comentarios
                        commentsList.load();
                    }
                }
            });
        });
    }
}
