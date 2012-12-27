$(document).ready(function() {
    var autoSetting;
    chrome.extension.sendMessage ({ method: "getLocalStorage", key: "auto"}, function (response) {
        autoSetting = response.data;

        if (autoSetting == "true" || autoSetting == "undefined") {
            injectOverlayElement();
            translate( reverseOverlay );
        }
    });
});
