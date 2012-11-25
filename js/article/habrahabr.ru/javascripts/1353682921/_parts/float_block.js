/**
 * В этом файле описан функционал, который реализует плавающий баннер в правой части сайта :)
 */
 
$(document).ready(function(){

	if( $('.similar_questions').size() ) {
		show_float_block('.similar_questions')
	}else if( $('.daily_best_posts').size() ) {
		show_float_block('.daily_best_posts')
	}
	
	
		
})

function show_float_block(selector){


	if( $(window).width() < 1024 || $(window).height() < 500 || screen.width < 1024) {  return; }
	
	var float_block = $(selector)
	var flowt_block_width = float_block.width()
	
	var sidebar = $('.sidebar_right')
	if(! sidebar.size()) return ;
	
	var last_sidebar_item = sidebar.children(':last-child')
	if(! last_sidebar_item.size() ) return ;
	

	
	var show_float_block = false
	
	$(window).bind('scroll resize', function () { 
		
	var last_sidebar_item_bottom = last_sidebar_item.offset().top + last_sidebar_item.outerHeight()		

		if(! float_block.size()) return ;
		
	if( $(window).width() < 1024 || $(window).height() < 500 || screen.width < 1024) {  return; }
		
		if( this.pageYOffset > last_sidebar_item_bottom) {
			var sidebar_position = sidebar.offset().top 
			if(show_float_block == false){
				float_block.addClass('float_block').animate({ opacity: 0 }, 0, function() {
					float_block.animate({ opacity: 1 }, 500).css('width', flowt_block_width+'px')
				})
			}
			show_float_block = true
		}else{
			if(show_float_block == true){
			 	float_block.removeClass('float_block').css('width', 'auto')
			}
			show_float_block = false
		}
		if( (float_block.outerHeight() + this.pageYOffset) > $('#footer').offset().top - 150  ){
			if(show_float_block == true){
			  float_block.removeClass('float_block').css('width', 'auto')
			}
			show_float_block = false
		}
	})
}