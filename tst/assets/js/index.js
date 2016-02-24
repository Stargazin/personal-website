var headerBackground = (function() {

  //*cache DOM
  var $window = $(window);
  var $body = $('body');
  var $header = $('header');

  //*bind events
  $window.on('resize', _resizeBackground);


  _bgHeight(); // Run on load to set height of picture to window height.

  function _bgHeight() {
    var windowHt = $window.height();
    // Prevent header from being set too large (picture not large enough).
    windowHt <= 1010 ? $header.height(windowHt) : $header.height(1010);
  }

  function _resizeBackground() {
    _bgHeight();
    $body.width($(window).width()); // Set body width equal to width of window.
  }

})();