document.addEventListener('DOMContentLoaded', function(){
  // Theme toggle
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const current = localStorage.getItem('theme') || 'light';
  root.setAttribute('data-bs-theme', current);
  document.body.dataset.theme = current;
  if(toggle){ toggle.textContent = current === 'dark' ? '☀️' : '🌙'; }

  function setTheme(t){
    root.setAttribute('data-bs-theme', t);
    document.body.dataset.theme = t;
    localStorage.setItem('theme', t);
    if(toggle) toggle.textContent = t === 'dark' ? '☀️' : '🌙';
  }
  if(toggle){
    toggle.addEventListener('click', function(e){
      const next = root.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
      setTheme(next);
    });
  }

  // Review stars interactive widget: maps 1-5 stars to 2-10 value (star * 2)
  document.querySelectorAll('.star-rating').forEach(function(container){
    const stars = Array.from(container.querySelectorAll('.star'));
    const targetSelector = container.dataset.target;
    const input = targetSelector ? document.querySelector(targetSelector) : container.querySelector('input[type="hidden"]');

    function setVisual(count){
      stars.forEach((s, i)=>{
        if(i < count) s.classList.add('active'); else s.classList.remove('active');
      });
    }

    // initialize from input value
    if(input && input.value){
      const val = parseInt(input.value, 10) || 0;
      const starsCount = Math.round(val/2);
      setVisual(starsCount);
    }

    stars.forEach(function(s, idx){
      s.addEventListener('click', function(){
        const count = idx + 1;
        setVisual(count);
        if(input){ input.value = String(count * 2); }
      });
      s.addEventListener('mouseover', function(){
        setVisual(idx + 1);
      });
      s.addEventListener('mouseout', function(){
        if(input && input.value){
          setVisual(Math.round(parseInt(input.value,10)/2));
        } else {
          setVisual(0);
        }
      });
    });
  });

  // Review stars display: set filled width based on data-score (0-10)
  document.querySelectorAll('.review-stars').forEach(function(el){
    const score = parseFloat(el.dataset.score) || 0;
    const pct = Math.max(0, Math.min(100, (score / 10) * 100));
    const inner = el.querySelector('.stars-inner');
    if(inner){ inner.style.width = pct + '%'; }
  });

});
