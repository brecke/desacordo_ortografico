var mappings = {
  'projeto': 'projecto',
  'pitecoide': 'pitecóide',
  'prelecionar': 'preleccionar',
  'osteoide': 'osteóide',
  'dactiliológico, datiliológico': 'dactiliológico',
  'seletividade': 'selectividade',
  'termoeletricidade': 'termoelectricidade',
  'pedra do ar': 'pedra-do-ar',
}

/*
 * Revert AO
 */
 
/*
 * Step 1
 * Checking whether the page is in Portuguese
 */
 
/* 
 * Google language detection API parameters
 * callback
 * key
 * prettyprint
 * q
 */
 
var key = "AIzaSyBYsks1R1ApmgQYkxswsbZi27aZtQqOAvU"
// var callback = "getLanguage"
var query = "Cavaco falou aos Portugueses no facebook"
// var prettyprint = "false"
var url = "https://www.googleapis.com/language/translate/v2/detect?key=" + key + "&q=" + query

// console.log("GET requesting...");
/*
$.get(url, { key: key, q: query, prettyprint: "false" }, function(data) {
  // $('.result').html(data);
  alert('Load was performed.');
});
*/
 
 
/* 
 * Step 2
 * Replace stuff to make it readable
 */

// $.getScript("mappings.js", function(){
// 
//   console.log("Mappings successfully imported...");
//    // alert("Script loaded and executed.");
//    // here you can use anything you defined in the loaded script
// 
// });
 
$(document).ready(function() {

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
              if (includeWhitespaceNodes || !whitespace.test(node.nodeValue)) {
                  textNodes.push(node);
              }
          } else {
              for (var i = 0, len = node.childNodes.length; i < len; ++i) {
                  getTextNodes(node.childNodes[i]);
              }
          }
      }
  
      getTextNodes(node);
      return textNodes;
  }
  
  var textNodes = getTextNodesIn(document.body);
  // console.log(textNodes);
  
  for(var i = 0; i < textNodes.length; i++) {
    word = textNodes[i].textContent;    
    replaceWord = mappings[ word.toLowerCase() ];
    
    if ( replaceWord ) {
        if ( isCapitalized(word) ) {
            word = capitalize( replaceWord );
        } else if ( isUpperCase(words) ) {
            word = replaceWord.toUpperCase();
        } else {
            word = replaceWord.toLowerCase();
        };
    };    
  }
  
});





