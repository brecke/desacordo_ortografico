chrome.extension.onRequest.addListener(
	function(request, sender, sendResponse) {
  		if (request.method == "getLocalStorage")
    		sendResponse({data: localStorage[request.key]});
  		else
    		sendResponse({});
	});

chrome.browserAction.onClicked.addListener(
	function(tab) {
		//console.log(contentWindow.document.body);
		// translate();

		chrome.tabs.getSelected(null, function(tab) {
		  chrome.tabs.sendMessage(tab.id, {greeting: "hello"}, function(response) {
		    console.log(response.farewell);
		  });
		});
	});