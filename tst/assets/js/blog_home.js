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

var filters = (function() {

  //*cache DOM
  var $headerFilter = $('.header__filter__link');
  var $listing = $('.listing');
  var $listingHeader = $('.listing__header');
  var $listingPost = $('.listing__post');

  var currentCategory = 'all';

  //*bind events
  $headerFilter.on('click', _filterListing);

  function _filterListing(e) {
    e.preventDefault();

    $headerFilter.removeClass('current-category');
    $(this).addClass('current-category');

    var filterCategory = $(this).attr('class').split(' ')[1];

    $listingHeader.removeClass(currentCategory);
    currentCategory = filterCategory;
    $listingHeader.addClass(currentCategory);

    $listingPost.hide();
    if ( filterCategory == 'all' ) {
      $listingPost.show();
    }
    else {
      $listingPost.each(function() {
        var postCategory = $(this).attr('class').split(' ')[1];
        if ( postCategory == filterCategory ) {
          $(this).show();
        };
      });
    };
  }

})();