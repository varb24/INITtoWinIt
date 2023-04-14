
document.addEventListener('DOMContentLoaded', function () {
  const sphereContainer = document.getElementById('sphereContainer');
  const tags = [
    'TypeScript',
    'Python',
    'Java',
    'PyTorch',
    'HTML',
    'C++',
    'CSS',
    'React',
    'TensorFlow',
    'TypeScript',
    'Python',
    'Java',
    'PyTorch',
    'HTML',
    'C++',
    'CSS',
    'React',
    'TensorFlow',
    'TypeScript',
    'Python',
    'Java',
    'PyTorch',
    'HTML',
    'C++',
    'CSS',
    'React',
    'TensorFlow',
  ];

  const options = {
    radius:250,
    maxSpeed: 15.0,
    minSpeed: 2.0,
    direction: 135,
    keep: true,
  };

  TagCloud(sphereContainer, tags, options);

  let prevScrollpos = window.pageYOffset;
  window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
      document.querySelector('header').style.transform = 'translateY(0)';
    } else {
      document.querySelector('header').style.transform = 'translateY(-100%)';
    }
    prevScrollpos = currentScrollPos;
  };

});
