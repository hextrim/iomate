$(document).ready(function(){
   var socket = io.connect('http://' + document.domain + ':' + location.port + '/swxprogress');

   socket.on('sw1progressbar', function(msg) {
   $('.pie-chart-tiny').data('easyPieChart').update(msg.data);
  });

});
