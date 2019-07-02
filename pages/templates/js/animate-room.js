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

  var puppetIsAnimated = false;
  var puppetTimeout;
  var puppetTL = anime.timeline({
      autoplay: false,
      direction: 'alternate',
      begin: function(anim) {
          puppetIsAnimated = true;
      },
      complete: function(anim) {
          puppetIsAnimated = false;
          puppetTimeout = setTimeout(animatePuppet, 6000);
      }
  }).add({
      targets: '.puppet-door',
      scaleX: 0.85,
      duration: 800,
      easing: 'easeOutQuart'
  }, 200).add({
      targets: '.puppet-eyes',
      translateY: -11,
      duration: 800,
      easing: 'easeOutQuart'
  }, 200).add({
      targets: '.puppet-knife',
      translateX: 4,
      translateY: 11,
      duration: 500,
      easing: 'linear'
  }, 0);

  document.querySelector('#puppet-svg').onmouseenter = function() {
      if (!puppetIsAnimated) {
          clearTimeout(puppetTimeout);
          animatePuppet();
      }
  };

  function animatePuppet() {
      puppetTL.play();
  }

  window.onload = function() {
        digimiamTimeout = setTimeout(animateDigimiam, 4000);
        puppetTimeout = setTimeout(animatePuppet, 8000);
  }
</script>
