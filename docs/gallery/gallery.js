const viewer = document.getElementById('viewer');
const filters = document.querySelectorAll('[data-filter]');
const sections = document.querySelectorAll('section[data-platform]');

filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(filter => filter.setAttribute('aria-pressed', String(filter === button)));
  sections.forEach(section => {
    section.hidden = button.dataset.filter !== 'all'
      && section.dataset.platform !== button.dataset.filter;
  });
}));

document.querySelectorAll('[data-file]').forEach(card => card.addEventListener('click', event => {
  // Preserve browser shortcuts for opening an original image in another tab.
  if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || !viewer.showModal) return;
  event.preventDefault();
  const image = document.getElementById('full-image');
  image.src = card.dataset.file;
  image.alt = card.dataset.title;
  document.getElementById('viewer-title').textContent = card.dataset.title;
  document.getElementById('original').href = card.dataset.file;
  document.getElementById('download').href = card.dataset.file;
  viewer.showModal();
}));

document.getElementById('close').addEventListener('click', () => viewer.close());
viewer.addEventListener('click', event => {
  if (event.target === viewer) viewer.close();
});
