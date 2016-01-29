var scrollHighlight = (function() {

  //*cache DOM
  var $document = $(document);
  var $window = $(window);
  var $bodyHTML = $('body, html');
  var $toTop = $('#to-top');
  var $postSection = $('.post__section');
  var $sideScrollContainer = $('.side__scroll-container');
  var $sideScroll = $('.side__scroll');

  var numOfSections = $postSection.length;
  var sectionOffsets = [];

  //*bind events
  $window.scroll(_checkScrollPosition);
  $window.on('resize', _checkScrollPosition);
  $toTop.on('click', _scrollToTop);
  // $sideScroll.hover(_selectSideNav, _unselectSideNav);
  // $sideScroll.on('click', _unselectSideNav);

  function _getOffsets() {
    $postSection.each(function() {
      //Reduce offsets by 10 to adjust for errors in currentOffset
      sectionOffsets.push( $(this).offset().top-10 );
    });
  }

  function _checkScrollPosition() {
    var currentOffset = $(document).scrollTop();
    _getOffsets();

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

      $sideScroll.removeClass('current-section');
      $sideScroll.eq(currentSection).addClass('current-section');
    }
    else {
      $toTop.hide();
      $sideScroll.removeClass('current-section');
    };
  }

  function _scrollToTop() {
    $bodyHTML.animate({scrollTop: 0}, 250);
  }

  // function _selectSideNav() {
  //   $(this).parent().addClass('side__scroll--selected');
  // }

  // function _unselectSideNav() {
  //   $(this).parent().removeClass('side__scroll--selected');
  // }

})();


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