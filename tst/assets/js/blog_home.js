var highlightSocialBtns = (function() {

  //*cache DOM
  var $headerSocial = $('.header__social');

  //*bind events
  $headerSocial.hover(_showSocial, _hideSocial);
  $headerSocial.on('click', _hideSocial);

  function _showSocial() {
    $(this).addClass('social-show');
  }

  function _hideSocial() {
    $(this).removeClass('social-show');
  }

})();