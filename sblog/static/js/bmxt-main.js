$(document).ready(function(){
	$("#divHead li").mouseover(function(){
		$(this).addClass("liHandOn");
		});
	$("#divHead li").mouseout(function(){
		$(this).removeClass("liHandOn");
		});
})