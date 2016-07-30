var $ = require ('jquery');
var apiClient = require('./api-client.js');

module.exports = {
    load: function(){
        apiClient.list(function(response){
            $(".list-comments").html(''); //vaciamos el html
            for (var i in response) {
                var commentToGet = response[i];

                var comment_id = commentToGet.id || "";
                var name = commentToGet.name || "";
                var surname = commentToGet.surname || "";
                var email = commentToGet.email || "";
                var comment_text = commentToGet.comment || "";

                var html = '<article class="comment" comment-id="'+ comment_id +'">';
                html += '<div>' + name + '</div>';
                html += '<div>' + surname + '</div>';
                html += '<div>' + email + '</div>';
                html += '<div>' + comment_text + '</div>';
                html += '</article>';
                $('.list-comments').append(html);
            }
        },
        function(response){
            console.error("ERROR", response);
        })
    }
}
