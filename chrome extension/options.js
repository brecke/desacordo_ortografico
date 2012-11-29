$(document).ready(function() {
	
	jQuery(function($) {
    	$('#auto').prop('checked', function() {
    		var autoSetting = localStorage["auto"];
    		if(autoSetting == "false") {
    			return false;
    		} return true;
    	});
	});
});

$("#save_button").click(function() {
 	var autoSetting = $('#auto').is(':checked');  
 	localStorage["auto"] = autoSetting;
 	// console.log("Set to localStorage: " + localStorage["auto"]);
 	// console.log("Set to localStorage: " + localStorage.auto);
});