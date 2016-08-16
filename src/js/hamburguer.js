var $ =require('jquery');

//adaptado de: https://codepen.io/g13nn/pen/eHGEF

$( ".cross" ).hide();

// $( ".menu" ).hide();

$( ".hamburger" ).click(function() {
    $( ".menu" ).slideToggle( "150", function() {
        $( ".hamburger" ).hide();
        $( ".cross" ).show();
        });
});

$( ".cross" ).click(function() {
    $( ".menu" ).slideToggle( "250", function() {
        $( ".cross" ).hide();
        $( ".hamburger" ).show();
    });
});

//esto parece una chapucilla:
// $( window ).resize(function() {
//     if ($("window").width>736){
//         $( ".menu" ).show();
//     }
//
// });
