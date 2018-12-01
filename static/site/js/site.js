(function(){
  
  $(window).scroll(function () {
      console.log(5+6);
      var top = $(document).scrollTop();
      $('.slider').css({
        'background-position': '0px -'+(top/3).toFixed(2)+'px'
      });
      if(top > 30)
      $('.navbar').addClass('navbar-fixed-top');
    else
      $('.navbar').removeClass('navbar-fixed-top');
        
  }).trigger('scroll');
})();



/*----------------------------------------------------*/
/*	Flexslider
/*----------------------------------------------------*/




