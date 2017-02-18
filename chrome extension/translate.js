function isCapitalized(string) {
  first = string[0];
  rest = string.slice(1);
  return first == first.toUpperCase() && rest == rest.toLowerCase();
}

function capitalize(string) {
  return string[0].toUpperCase() + string
    .slice(1)
    .toLowerCase();
}

function isLowerCase(string) {
  return string == string.toLowerCase();
}

function isUpperCase(string) {
  return string == string.toUpperCase();
}

// go through the DOM recursively
function getTextNodesIn(node, includeWhitespaceNodes) {
  var textNodes = [];
  var whitespace = /^\s*$/;

  function collectNodes(node) {
    if (includeWhitespaceNodes || (!whitespace.test(node.textContent))) { // nodeValue
      textNodes.push(node);
    }
  }

  function getTextNodes(node) {
    // it's just words
    if (node.nodeType == 3) {
      collectNodes({node: node, tag: null});
    } else if (node.nodeType === 1 && (node.nodeName.toLowerCase() === 'i' || node.nodeName.toLowerCase() === 'b' || node.nodeName.toLowerCase() === 'strong' || node.nodeName.toLowerCase() === 'em')) { // in case it's an element, but it's just style
      var newText = node.textContent.replace(/(<([^>]+)>)/ig, '');
      var newNode = document.createTextNode(newText);
      // collectNodes(newNode);
      collectNodes({node: node, tag: node.nodeName.toLowerCase()});
    } else if (node.nodeType === 1 && node.nodeName.toLowerCase() != "script" && node.nodeName.toLowerCase() != 'style') { // in case it's an element with other elements in it (possibly)
      for (var i = 0, len = node.childNodes.length; i < len; ++i) {
        getTextNodes(node.childNodes[i]);
      }
    }
  }

  getTextNodes(node);
  return textNodes;
}

function cleanupTextContent(textContent) {
  toReplace = [
    ':',
    '.',
    '?',
    '_',
    '@',
    '?',
    '"',
    "'",
    '”',
    '“',
    '‘',
    '’',
    ';',
    '(',
    ')',
    '«',
    '»',
    ',',
    '!'
  ];
  for (var x = 0; x < toReplace.length; x++) {
    // replace via regex
    re = new RegExp('\\' + toReplace[x], 'g');
    textContent = textContent.replace(re, ' ');
  }

  return $.trim(textContent);
}

function translate(createOverlay, removeOverlay) {

  createOverlay();

  var textNodes = getTextNodesIn(document.body, false);
  var eachTextContent;
  var tokens;
  var re;

  for (var i = 0; i < textNodes.length; i++) {
    eachNode = textNodes[i].node;
    eachTextContent = $.trim(eachNode.textContent);

    flag = false;
    if (eachTextContent.indexOf('Cole') >= 0) {
      flag = true;
    }

    eachTextContent = cleanupTextContent(eachTextContent);
    tokens = eachTextContent.split(/[\s,]+/);

    for (var j = 0; j < tokens.length; j++) {
      eachToken = tokens[j].replace(/(<([^>]+)>)/ig, '');
      replaceWord = mappings[eachToken.toLowerCase()];

      if (replaceWord) {
        if (isCapitalized(eachToken)) {
          eachNode.textContent = eachNode
            .textContent
            .replace(eachToken, capitalize(replaceWord));
        } else if (isUpperCase(eachToken)) {
          eachNode.textContent = eachNode
            .textContent
            .replace(eachToken, replaceWord.toUpperCase());
        } else {
          eachNode.textContent = eachNode
            .textContent
            .replace(eachToken, replaceWord);
        }
      }
    }
  }
  // callback for removing the overlay
  removeOverlay();
}

// clicking on the chrome extension icon
chrome
  .extension
  .onMessage
  .addListener(function (request, sender, sendResponse) {

    // start translation
    if (request.method == "start") {
      // ask the background script for the selected tab language
      chrome
        .extension
        .sendMessage({
          method: "getLanguage"
        }, function (response) {
          if (response) {
            language = response.data;
            if (language == "pt-PT" || language == "pt") {
              translate(injectOverlayElement, reverseOverlay);
            }
          }
        });
    };
  });
  