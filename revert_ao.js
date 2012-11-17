
$(document).ready(function() {

    var autoSetting;
    chrome.extension.sendRequest({ 
        method: "getLocalStorage", key: "auto"},
        function(response) {

            // alert(response.data);
            autoSetting = response.data;
            // console.log("local storage response: " + autoSetting);

            if(autoSetting == "true") {
                translate();
            } else if (autoSetting == "false") {
                
            }
        });
});






