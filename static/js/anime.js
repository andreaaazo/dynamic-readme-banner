const animation = anime({
    targets: '.logo path',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'cubicBezier(.5, .2, .3, 1, 1)',
    duration: 5000,
    delay: function(el, i) { return i * 50 },
    direction: 'alternate',
    loop: true
});

const animation_items = anime({
    targets: '.logo .item',
    fill: '#6A6A6A',
    duration: 5500,
    easing: 'cubicBezier(.5, .2, .3, 1)',
    loop: true,
    direction: 'alternate',
});

animation.play()