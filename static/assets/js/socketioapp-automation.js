$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/swxprobe');

    socket.on('sw1usbsignal', function(msg) {
    $('#sw1probe').html('<h3 class="block-title">' + msg.data + '</h3>');
    });
    socket.on('sw2usbsignal', function(msg) {
    $('#sw2probe').html('<h3 class="block-title">' + msg.data + '</h3>');
    });
    socket.on('sw1portsignal', function(msg) {
    $('#sw1probe').html('<h3 class="block-title">' + msg.data + '</h3>');
    });
    socket.on('sw2portsignal', function(msg) {
    $('#sw2probe').html('<h3 class="block-title">' + msg.data + '</h3>');
    });
});



//$(document).ready(function(){
 //   var socket = io.connect('http://' + document.domain + ':' + location.port + '/sw1probe');
//
 //   socket.on('sw1signal', function(msg) {
  //  $('#sw1probe').replaceWith('<h3 class="block-title">' + msg.data + '</h3>');
   // });
  //  socket.on('sw2signal', function(msg) {
  //  $('#sw2probe').replaceWith('<h3 class="block-title">' + msg.data + '</h3>');
  //  });
//});

//$(document).ready(function(){
//    var socket = io.connect('http://' + document.domain + ':' + location.port + '/sw2probe');
//
//   socket.on('sw2signal', function(msg) {
//  $('#sw2probe').replaceWith('<h3 class="block-title">' + msg.data + '</h3>');
//    });
//});

//$(document).ready(function(){
//   var socket = io.connect('http://' + document.domain + ':' + location.port + '/swxprogress');
//
//   socket.on('sw1progressbar', function(msg) {
//   $('.pie-chart-tiny').data('easyPieChart').update(msg.data);
//  });
//
//});

