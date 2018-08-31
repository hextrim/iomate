$(document).ready(function(){
   var socket = io.connect('http://' + document.domain + ':' + location.port + '/livecdprogress');

   socket.on('build_hextrimos_iso_progressbar', function(msg) {
   $('#build-test.pie-chart-tiny').data('easyPieChart').update(msg.data);
//    $('#build-test').html('<h3 class="block-title">' + msg.data + '</h3>');
   });
   socket.on('convert_hextrimos_to_pxeboot_progressbar', function(msg) {
//    $('#convert-test').html('<h3 class="block-title">' + msg.data + '</h3>');
   $('#convert-test.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });

});

//$(document).ready(function(){
//   var socket = io.connect('http://' + document.domain + ':' + location.port + '/livecdprogress2');

//   socket.on('build_hextrimos_iso_progressbar', function(msg) {
//   $('#build-test.pie-chart-tiny').data('easyPieChart').update(msg.data);
//   $('#build-test').html('<h3 class="block-title">' + msg.data + '</h3>');
//   });
//  socket.on('convert_hextrimos_to_pxeboot_progressbar', function(msg) {
//   $('#convert-test').html('<h3 class="block-title">' + msg.data + '</h3>');
//   $('#convert-test.pie-chart-tiny').data('easyPieChart').update(msg.data);
//   });
//});

