var background = (function() {

  //*cache DOM
  var $window = $(window);
  var $body = $('body');
  var $header = $('header');

  //*bind events
  $window.on('resize', _resizeBackground);


  _bgHeight();

  function _bgHeight() {
    var windowHt = $window.height();
    windowHt <= 1010 ? $header.height(windowHt) : $header.height(1010);
  }

  function _resizeBackground() {
    _bgHeight();
    $body.width($(window).width());
  }

})();