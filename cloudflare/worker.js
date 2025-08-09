addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  const token = url.searchParams.get('token');
  if (token !== 'YOUR_SECURE_TOKEN') {
    return event.respondWith(new Response('Unauthorized', { status: 401 }));
  }
  return event.respondWith(fetch(`https://<YOUR_PAGES_URL>/proxy.pac`));
});
