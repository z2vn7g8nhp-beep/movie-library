// 离线缓存
//  - 网页本身：先走网络（拿到最新版），没网用缓存
//  - 片库索引：按版本号缓存，打开秒出、没网也能搜
//  - 海报、头像、照片：看过一次就存在手机里，下次直接显示（不用再从 IMDb / 豆瓣下载）
const SHELL = "yingku-shell-v5", IDX = "yingku-idx", IMG = "yingku-img-v1", IMG_MAX = 2500;
self.addEventListener("install", e => { self.skipWaiting(); e.waitUntil(caches.open(SHELL).then(c => c.addAll(["./", "manifest.json", "icon-180.png"]).catch(() => {}))); });
self.addEventListener("activate", e => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k.startsWith("yingku-shell-") && k !== SHELL) await caches.delete(k);
  await self.clients.claim();
})()));

const IMG_HOSTS = /(^|\.)m\.media-amazon\.com$|(^|\.)doubanio\.com$/;
let puts = 0;
async function trim(c){
  const ks = await c.keys();
  if (ks.length > IMG_MAX) for (const k of ks.slice(0, ks.length - IMG_MAX)) await c.delete(k);
}
self.addEventListener("fetch", e => {
  const req = e.request, u = new URL(req.url);
  if (req.method !== "GET") return;
  if (IMG_HOSTS.test(u.hostname)) {
    e.respondWith(caches.open(IMG).then(async c => {
      const hit = await c.match(req.url, {ignoreVary: true});
      if (hit) return hit;
      // IMDb 的图允许跨域，能看到是否成功；豆瓣的只能拿到"不透明"响应，坏图由页面发现后删掉
      const amazon = u.hostname.endsWith("media-amazon.com");
      const r = amazon ? await fetch(req.url, {mode: "cors", credentials: "omit"}) : await fetch(req);
      if (r.ok || (!amazon && r.type === "opaque")) { c.put(req.url, r.clone()).catch(() => {}); if (++puts % 50 === 0) trim(c); }
      return r;
    }).catch(() => fetch(req)));
    return;
  }
  if (u.origin !== location.origin) return;
  const isIdx = u.pathname.includes("/idx/") && !u.pathname.endsWith("info.json");
  if (isIdx) {
    e.respondWith(caches.open(IDX).then(async c => {
      const hit = await c.match(req);
      if (hit) return hit;
      const r = await fetch(req);
      if (r.ok) {
        c.put(req, r.clone());
        const base = u.pathname;   // 新版本的同名文件进来后，删掉旧版本
        c.keys().then(ks => ks.forEach(k => { const ku = new URL(k.url); if (ku.pathname === base && ku.search !== u.search) c.delete(k); }));
      }
      return r;
    }));
    return;
  }
  // 网页本身每次都向服务器确认有没有新版（GitHub 会让浏览器缓存 10 分钟，不这样会一直拿到旧版）
  e.respondWith(fetch(req, {cache: "no-cache"}).then(r => {
    if (r.ok) { const cp = r.clone(); caches.open(SHELL).then(c => c.put(req, cp)); }
    return r;
  }).catch(() => caches.match(req, {ignoreSearch: true}).then(r => r || caches.match("./"))));
});
