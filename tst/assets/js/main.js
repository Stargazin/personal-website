var background = (function() {

  //*cache DOM
  var $window = $(window);
  var $body = $('body');
  var $header = $('header');

  //*bind events
  $window.on('resize', _resizeBackground);


  _bgHeight();

  function _bgHeight() {
    $header.height($window.height());
  }

  function _resizeBackground() {
    _bgHeight();
    $body.width($(window).width());
  }

})();