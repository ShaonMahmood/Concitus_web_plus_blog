(function ($) {
	$(document).ready(function () {


		/*
		* 01. Change "_scrollFixPos" variable if navigation menu changed/homepage changed
		* 02. Animate to a section is depending on navigation menu's height. So, change the value here : "scrollTop: target.offset().top - 50" (replace 50)
		* 03. In about section, each about div's height is same
		* 04. Form validation is done by jquery and need to change the value "if ($('i.fa.fa-check').size() >= 2)" for valid inputs if input fields increased or decreased
		* 05. Submitting form is nothing (just showing and alert box)
		* */

		//fixing navbar at top when it reaches top
		var _scrollFixPos = $('#home').height() - 5;
		$(window).scroll(function () {
			var _navbar = $('#navbar');
			var _about = $('#about');
			if ($(window).scrollTop() >= _scrollFixPos)
			{
				_navbar.addClass('fixed-navbar');
				_about.css('margin-top', '50px');
			}
			else
			{
				_navbar.removeClass('fixed-navbar');
				_about.css('margin-top', '0');
			}
		});


		//animate when scroll to another section
		$('.navbar-nav a').click(AnimateScroll);
		$('.go-about').click(AnimateScroll);

        function AnimateScroll ()
        {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top-50	//(-0) because navbar height 50px
                    }, 1000);
                    return false;
                }
            }
        }

		//setting '.team-img' height according to team's img
		function TeamParent_SetHeight()
		{
			$('.each-team').height($('.team-img img').height());
		}
		TeamParent_SetHeight();


		//same height in about section
		var _aboutSectionHeight = 0;
		var _eachAbout = $('.each-about');
		SameHeight ();
		function SameHeight () {
			_eachAbout.each(function () {
				var _this = $(this);
				if (_aboutSectionHeight < _this.outerHeight())   _aboutSectionHeight = _this.outerHeight();   //find bigger height
			});
			_eachAbout.css('height',_aboutSectionHeight);
		}

		//height functionality will be called upon device width change
		$(window).resize(function() {
			TeamParent_SetHeight();
			SameHeight ();
		});



		//form validation
		var emailReg = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;

		var errClass = "has-warning";
		var errIcon = "fa-times";
		var successClass = "has-success";
		var successIcon = "fa-check";

		$('#input_email').keyup(function ()
		{
			var formParent = $(this).closest('.form-group');

			if (!emailReg.test( $(this).val() )) InputError (formParent);
			else InputSuccess(formParent);
		});

		$('#input_name').keyup(function ()
		{
			var formParent = $(this).closest('.form-group');

			if ($(this).val().length < 2) InputError (formParent);
			else InputSuccess(formParent);
		});

		function InputSuccess (param1)
		{
			param1.removeClass(errClass).addClass(successClass);
			param1.find('i.fa').removeClass(errIcon).addClass(successIcon);
		}

		function InputError (param2)
		{
			param2.removeClass(successClass).addClass(errClass);
			param2.find('i.fa').removeClass(successIcon).addClass(errIcon);
		}
	});
})(jQuery);
