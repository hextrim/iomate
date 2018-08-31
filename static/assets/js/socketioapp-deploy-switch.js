// SW PROBE
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


// SW UPDATE PROGRESS BAR
$(document).ready(function(){
   var socket = io.connect('http://' + document.domain + ':' + location.port + '/swxprogress');

   socket.on('deploysw1-baseconfig-progress', function(msg) {
   $('#deploy-sw1-baseconfig.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });
   socket.on('deploysw1-portconfig-progress', function(msg) {
   $('#deploy-sw1-portconfig.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });
   socket.on('deploysw1-singleport-progress', function(msg) {
   $('#deploy-sw1-singleport.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });

   socket.on('deploysw2-baseconfig-progress', function(msg) {
   $('#deploy-sw2-baseconfig.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });
   socket.on('deploysw2-portconfig-progress', function(msg) {
   $('#deploy-sw2-portconfig.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });
   socket.on('deploysw1-singleport-progress', function(msg) {
   $('#deploy-sw2-singleport.pie-chart-tiny').data('easyPieChart').update(msg.data);
   });
});
