var pageScrolling = (function() {

  //*cache DOM
  var $window = $(window);
  var $bodyHTML = $('body, html'); // Need both for scroll to top.
  var $toTop = $('#to-top'); // To-top button.
  var $post = $('.post');
  var $postSection = $('.post__section');
  var $headerScroll = $('.header__scroll'); // Sidebar scroll-to links.
  // Quicklinks.
  var $breakdownScroll = $('.post__quicklinks > .text-link');

  var numberOfSections = $postSection.length;
  var sectionOffsets = [];

  //*bind events
  // Check highlighted section in sidebar when scrolling or resizing window.
  $window.scroll(_checkScrollPosition);
  $window.on('resize', _checkScrollPosition);
  // Go to section when clicking quicklinks or sidebar section links.
  $headerScroll.on('click', _scrollToSection);
  $breakdownScroll.on('click', _scrollToSection);
  $toTop.on('click', _scrollToTop);


  function _getOffsets() {
    sectionOffsets = []; // Empty old offsets before pushing new values.

    $postSection.each(function() {
      // Reduce by 10 for browser differences. Needed for sidebar highlighting.
      sectionOffsets.push($(this).offset().top - 10);
    });
  }

  function _scrollToSection(e) {
    e.preventDefault();

    _getOffsets(); // Get (new) offsets for each section.

    // Get number of section to scroll to.
    var section = $(this).attr('class').split(' ')[1];
    // Subtract one to account for zero indexed sectionOffsets array.
    var scrollTo = sectionOffsets[section - 1];
    // Add 10 to adjust for difference in _getOffsets().
    $bodyHTML.animate({scrollTop: scrollTo + 10}, 200);
  }

  function _checkScrollPosition() {
    _getOffsets(); // Get (new) offsets for each section.

    var currentOffset = $(document).scrollTop(); // Current distance from top.

    if ( currentOffset > sectionOffsets[0] ){
      $toTop.show(); // Show to top button if past section one.

      var checkSection;

      for ( checkIndex = 0; checkIndex != numberOfSections; checkIndex++ ) {
        // Check sections until section is past current window location.
        if ( currentOffset >= sectionOffsets[checkIndex] ) {
          checkSection = checkIndex;
        }
        else {
          break; // Break loop if section is past current offset.
        };
      };

      var currentSection = checkSection;

      // Change highlighted section in sidebar to current section.
      $headerScroll.removeClass('current-section');
      $headerScroll.eq(currentSection).addClass('current-section');
    }
    else {
      $toTop.hide(); // Hide to top button.
      $headerScroll.removeClass('current-section'); // No sidebar highlighting.
    };
  }

  function _scrollToTop() {
    $(this).removeClass('hovered'); // Remove hover effect on click for touch.

    var postTop = $post.offset().top;
    $bodyHTML.animate({scrollTop: postTop}, 200);
  }

})();


var hoverEffects = (function() {

  //*cache DOM
  var $homeBtn = $('.header__home') // 3 Steps Taken button.
  var $socialBtn = $('.header__social-btn'); // Social media buttons.
  var $textLink = $('.text-link');
  var $toTop = $('#to-top') // To-top button.

  //*bind events
  $homeBtn.hover(_addEffect, _rmvEffect);
  $homeBtn.on('click', _rmvEffect);
  $socialBtn.hover(_addEffect, _rmvEffect);
  $socialBtn.on('click', _rmvEffect);
  $textLink.hover(_addEffect, _rmvEffect);
  $textLink.on('click', _rmvEffect);
  //Click rmv is executed in _scrollToTop in scrollHighlight
  $toTop.hover(_addEffect, _rmvEffect);


  function _addEffect() {
    $(this).addClass('hovered');
  }

  function _rmvEffect() {
    $(this).removeClass('hovered');
  }

})();