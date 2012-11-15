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
$(document).ready(function() {
  
  var mappings = new Object();
  mappings["projeto"] = "projecto";
  mappings["atividade"] = "actividade";
  
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
  console.log(textNodes);
  
  for (var textNode in textNodes) {
    
    console.log(textNode)
    
    // go through the mappings Object
    
  }
  
});





