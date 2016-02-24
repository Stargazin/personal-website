var highlightSocialBtns = (function() {

  //*cache DOM
  var $socialBtn = $('.header__social'); // Social media buttons.

  //*bind events
  $socialBtn.hover(_addEffect, _rmvEffect);
  $socialBtn.on('click', _rmvEffect); // Remove effect on touch for mobile.


  function _addEffect() {
    $(this).addClass('hovered');
  }

  function _rmvEffect() {
    $(this).removeClass('hovered');
  }

})();


var filterPosts = (function() {

  //*cache DOM
  var $headerFilter = $('.header__filter__link'); // Filter buttons.
  var $listing = $('.listing'); // Contains all posts.
  var $listingHeader = $('.listing__header'); // Blog welcome message.
  var $listingPost = $('.listing__post'); // Individual posts.

  var currentCategory = 'all';

  //*bind events
  $headerFilter.on('click', _filterListing);


  function _filterListing(e) {
    e.preventDefault();

    // Remove class from every button then add to selected button.
    $headerFilter.removeClass('current-category');
    $(this).addClass('current-category');

    // Assign selected category (all, life, music, or web).
    var filterCategory = $(this).attr('class').split(' ')[1];

    // Change the color of welcome message underline based on category.
    $listingHeader.removeClass(currentCategory);
    currentCategory = filterCategory;
    $listingHeader.addClass(currentCategory);

    // Hide all posts first (for quick flash effect).
    $listingPost.hide();

    // Show all posts if 'all' is selected.
    if ( filterCategory == 'all' ) {
      $listingPost.show();
    }
    // Else show only the selected category's posts.
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