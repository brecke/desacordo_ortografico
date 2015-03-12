function isCapitalized(string) {
    first = string[0];
    rest  = string.slice(1);
    return first==first.toUpperCase() && rest==rest.toLowerCase();
}

function capitalize(string) {
    return string[0].toUpperCase() + string.slice(1).toLowerCase();
}

function isLowerCase(string) {
    return string == string.toLowerCase();
}

function isUpperCase(string) {
    return string == string.toUpperCase();
}

// go through the DOM recursively
function getTextNodesIn(node, includeWhitespaceNodes) {
    var textNodes = [], whitespace = /^\s*$/;

    function getTextNodes(node) {

        if (node.nodeType == 3) {
            if (includeWhitespaceNodes || (!whitespace.test(node.textContent))) { // nodeValue
              textNodes.push(node);
            }

        // recursively get the text nodes from other node types:
        // TYPE 1: ELEMENT_NODE
        // exception for <script>
        // exception for <style>
        // exception for <em>
        // exception for <i>
        // exception for <b>
        // exception for <strong>
        } else if (node.nodeType == 1
          && node.nodeName.toLowerCase() != "script"
          && node.nodeName.toLowerCase() != 'style'
          // && node.nodeName.toLowerCase() != 'strong'
          // && node.nodeName.toLowerCase() != 'em'
          && node.nodeName.toLowerCase() != 'i'
          // && node.nodeName.toLowerCase() != 'b'
          ) {

          for (var i = 0, len = node.childNodes.length; i < len; ++i) {
              getTextNodes(node.childNodes[i]);
          }
        }
    }

    getTextNodes(node);
    return textNodes;
}

function translate(createOverlay, removeOverlay) {

  createOverlay();

  var textNodes = getTextNodesIn(document.body, false);

  for(var i = 0; i < textNodes.length; i++) {

    text = $.trim(textNodes[i].textContent);

    // replace via regex
    text = text.replace(':', ' ');
    text = text.replace('...', ' ');
    text = text.replace('.', ' ');
    text = text.replace('?', ' ');
    // text = text.replace('\'', '');
    text = text.replace('_', ' ');
    text = text.replace('@', ' ');

    text = text.replace('”', ' ');
    text = text.replace('“', ' ');
    text = text.replace('‘', ' ');
    text = text.replace('’', ' ');

    text = text.replace(';', ' ');
    text = text.replace('(', ' ');
    text = text.replace(')', ' ');
    text = text.replace('«', ' ');
    text = text.replace('»', ' ');

    text = text.replace(',', ' ');
    text = text.replace('!', ' ');

    text = $.trim(text);
    tokens = text.split(/[\s,]+/);

    for (var j = 0; j < tokens.length; j++) {
      word = tokens[j];
      replaceWord = mappings[ word.toLowerCase() ];

       if (replaceWord) {
           if (isCapitalized(word)) {
               textNodes[i].textContent = textNodes[i].textContent.replace(word, capitalize( replaceWord ));
           } else if (isUpperCase(word)) {
               textNodes[i].textContent = textNodes[i].textContent.replace(word, replaceWord.toUpperCase());
           } else {
               textNodes[i].textContent = textNodes[i].textContent.replace(word, replaceWord);
           };
       };
    }
  }
    // callback for removing the overlay
    removeOverlay();
}

// clicking on the chrome extension icon
chrome.extension.onMessage.addListener( function(request, sender, sendResponse) {

    // start translation
    if (request.method == "start") {
        // ask the background script for the selected tab language
        chrome.extension.sendMessage( { method: "getLanguage" }, function (response) {
            if (response) {
                language = response.data;
                if(language == "pt-PT" || language == "pt") {
                    translate (injectOverlayElement, reverseOverlay);
                }
            }
        });
    };
});