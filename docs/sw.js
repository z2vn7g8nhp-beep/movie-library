// 离线缓存：网页本身先走网络（拿到最新版），片库索引按版本号缓存，打开秒出、没网也能搜。
const SHELL = "yingku-shell-v2", IDX = "yingku-idx";
self.addEventListener("install", e => { self.skipWaiting(); e.waitUntil(caches.open(SHELL).then(c => c.addAll(["./", "manifest.json", "icon-180.png"]).catch(() => {}))); });
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;
  const isIdx = u.pathname.includes("/idx/") && !u.pathname.endsWith("info.json");
  if (isIdx) {
    e.respondWith(caches.open(IDX).then(async c => {
      const hit = await c.match(e.request);
      if (hit) return hit;
      const r = await fetch(e.request);
      if (r.ok) {
        c.put(e.request, r.clone());
        // 新版本的同名文件进来后，删掉旧版本
        const base = u.pathname;
        c.keys().then(ks => ks.forEach(k => { const ku = new URL(k.url); if (ku.pathname === base && ku.search !== u.search) c.delete(k); }));
      }
      return r;
    }));
    return;
  }
  e.respondWith(fetch(e.request).then(r => {
    if (r.ok) { const cp = r.clone(); caches.open(SHELL).then(c => c.put(e.request, cp)); }
    return r;
  }).catch(() => caches.match(e.request, {ignoreSearch: true}).then(r => r || caches.match("./"))));
});
