<script>
  var digimiamIsAnimated = false;
  var digimiamTimeout;
  var digimiamTL = anime.timeline({
      autoplay: false,
      direction: 'alternate',
      begin: function(anim) {
          digimiamIsAnimated = true;
      },
      complete: function(anim) {
          digimiamIsAnimated = false;
          digimiamTimeout = setTimeout(animateDigimiam, 6000);
      }
  }).add({
      targets: '.digimiam-door',
      scaleX: 0.85,
      duration: 900,
      easing: 'easeOutQuart'
  }, 100).add({
      targets: '.digimiam-head',
      translateX: 3,
      translateY: 2,
      duration: 900
  }, 100).add({
      targets: '.digimiam-arm',
      translateX: {value: -2},
      rotate: {value: -1},
      duration: 600
  }, 100).add({
      targets: '.digimiam-jaw',
      translateX: 3,
      translateY: 4,
      duration: 1000
  }, 0);

  document.querySelector('#digimiam-svg').onmouseenter = function() {
      if (!digimiamIsAnimated) {
          clearTimeout(digimiamTimeout);
          animateDigimiam();
      }
  };

  function animateDigimiam() {
      digimiamTL.play();
  }

  window.onload = function() {
        digimiamTimeout = setTimeout(animateDigimiam, 4000);
  }
</script>
