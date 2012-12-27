
// listening to messages from the content script
chrome.extension.onMessage.addListener (function (request, sender, sendResponse) {

    if (request.method == "getLocalStorage") {
        sendResponse ({data: localStorage[request.key]});
    }
    else if (request.method == "getLanguage") {
        chrome.tabs.detectLanguage(null, function (language) {
            sendResponse ({ data: language });
        });
    }
    else { sendResponse( {} ); }

    return true;
});

// this is where it all starts, clicking the icon
// it sends a message 'ping' to the translate.js content script
chrome.browserAction.onClicked.addListener (function (tab) {
	chrome.tabs.getSelected (null, function(tab) {
	  chrome.tabs.sendMessage (tab.id, { method: "start" }, function (response) {} );
	});
});