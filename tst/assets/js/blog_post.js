var scrollHighlight = (function() {

  //*cache DOM
  var $document = $(document);
  var $window = $(window);
  var $bodyHTML = $('body, html');
  var $toTop = $('#to-top');
  var $post = $('.post');
  var $postSection = $('.post__section');
  var $headerScroll = $('.header__scroll');
  var $breakdownScroll = $('.post__breakdown__short > .text-link');

  var numOfSections = $postSection.length;
  var sectionOffsets = [];

  //*bind events
  $window.scroll(_checkScrollPosition);
  $window.on('resize', _checkScrollPosition);
  $headerScroll.on('click', _scrollToSection);
  $breakdownScroll.on('click', _scrollToSection);
  $toTop.on('click', _scrollToTop);

  function _getOffsets() {
    sectionOffsets = [];
    $postSection.each(function() {
      //Reduce offsets by 10 to adjust for errors in currentOffset
      sectionOffsets.push($(this).offset().top-10);
    });
  }

  function _scrollToSection(e) {
    e.preventDefault();
    _getOffsets();

    var section = $(this).attr('class').split(' ')[1]-1;
    var scrollTo = sectionOffsets[section];
    $bodyHTML.animate({scrollTop: scrollTo+10}, 250);
  }

  function _checkScrollPosition() {
    _getOffsets();
    var currentOffset = $(document).scrollTop();

    var currentSection = 0;
    if ( currentOffset > sectionOffsets[0] ){
      $toTop.show();

      var checkIndex = 0;
      while (checkIndex != numOfSections) {
        if ( currentOffset >= sectionOffsets[checkIndex]) {
          currentSection = checkIndex;
          checkIndex++;
        }
        else {
          break;
        };
      }

      $headerScroll.removeClass('current-section');
      $headerScroll.eq(currentSection).addClass('current-section');
    }
    else {
      $toTop.hide();
      $headerScroll.removeClass('current-section');
    };
  }

  function _scrollToTop() {
    var postTop = $post.offset().top;
    $bodyHTML.animate({scrollTop: postTop}, 250);
  }

})();


var highlight = (function() {

  //*cache DOM
  var $headerSocial = $('.header__social');
  var $textLink = $('.text-link');

  //*bind events
  $headerSocial.hover(_showSocial, _hideSocial);
  $headerSocial.on('click', _hideSocial);
  $textLink.hover(_darkenLink, _lightenLink);
  $textLink.on('click', _lightenLink);

  function _showSocial() {
    $(this).addClass('social-show');
  }

  function _hideSocial() {
    $(this).removeClass('social-show');
  }

  function _darkenLink() {
    $(this).addClass('link-dark');
  }

  function _lightenLink() {
    $(this).removeClass('link-dark');
  }

})();