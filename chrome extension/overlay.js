function injectOverlayElement () {
    var overlay = document.createElement('div');
    overlay.setAttribute("class", "overlay");
    document.body.appendChild(overlay);

    $('.overlay').css({
        'opacity': '0.6',
        'background': '#000',
        'width': '100%',
        'height': '100%',
        'z-index': '10',
        'top': '0',
        'left': '0',
        'position': 'fixed'
    });
}

function reverseOverlay () {
    currentOpacity = $('.overlay').css('opacity');
    do {
        currentOpacity = currentOpacity - 0.1;
        $('.overlay').css('opacity', currentOpacity);
    } while (currentOpacity > 0.1);

    $('.overlay').remove();
}
