$(document).ready(function() {

	jQuery(function($) {
    	$('#auto').prop('checked', function() {
    		var autoSetting = localStorage["auto"];
            return autoSetting == "true";
    	});
	});
});

$("#save_button").click(function() {
 	var autoSetting = $('#auto').is(':checked');
 	localStorage["auto"] = autoSetting;
});