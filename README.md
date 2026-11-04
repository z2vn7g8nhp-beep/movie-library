# 🎞 影库

自己的豆瓣电影：电影、剧集、老片、流媒体都能标记想看 / 在看 / 看过，打分、写短评、加标签；
片子按类型、导演、演员自动归类；评分来自豆瓣、IMDb、烂番茄三家，后台定期刷新。

全部跑在 GitHub 上，免费，不需要服务器。

## 它是怎么工作的

| 部分 | 做什么 | 频率 |
|---|---|---|
| 离线片库 | 用 IMDb 官方数据集生成约 12 万部电影和剧集的索引（带中文译名、海报、主创），存在手机里，搜索秒出、没网也能搜 | 每周日重建 |
| 补全详情 | 标记一部片子后，后台补齐中文名、豆瓣简介、演职员中文名和头像、三家评分、剧集每一季的豆瓣分 | 标记后 1～2 分钟 |
| 刷新评分 | 新片每天、两年内的片每周、老片每月刷新一次 | 每 6 小时一轮 |
| 在线搜索 | 离线片库里没有的冷门片，让后台去 IMDb 和豆瓣在线搜 | 约 1 分钟 |

你的标记、短评、标签都在**私有**仓库 `movie-library-data` 里，别人看不到。网页和抓取程序在公开仓库（这样 GitHub Actions 免费）。

## 第一次设置（大约 10 分钟）

1. **建两个仓库**：公开的 `movie-library`（放这些代码），私有的 `movie-library-data`（空的就行）。
2. **生成密钥**：GitHub 右上角头像 → Settings → Developer settings → Personal access tokens → **Fine-grained tokens** → Generate new token
   - Expiration 选长一点（比如 1 年）
   - Repository access 选 **Only select repositories**，勾选 `movie-library` 和 `movie-library-data`
   - Permissions → Repository permissions：**Contents** 选 Read and write，**Actions** 选 Read and write
3. **把密钥给后台**：`movie-library` 仓库 → Settings → Secrets and variables → Actions → New repository secret，名字 `DATA_TOKEN`，值是刚才的密钥。
4. **打开网页**：Settings → Pages → Build and deployment → Source 选 **GitHub Actions**。
5. **生成片库**：Actions → 片库索引和网页 → Run workflow。第一次大约 5～8 分钟。
6. **装到主屏幕**：Safari 打开 `https://你的用户名.github.io/movie-library/` → 分享 → 添加到主屏幕。
7. **连接**：从主屏幕打开 → 右上角设置 → 粘贴同一个密钥 → 连接。

数据仓库名字不是 `movie-library-data` 的话：在网站仓库 Settings → Secrets and variables → Actions → Variables 里加 `DATA_REPO`（例如 `你的用户名/别的名字`），网页设置里也填一下。

## 用法

- **搜索**：中文名、英文名、原名都行，加年份更准（`沙丘 2021`）。也可以粘贴 IMDb 或豆瓣链接。
- **快速标记**：首页 → 快速标记，点海报一下就标为看过，适合一开始批量补记。
- **剧集**：条目页的"分季"里点圆圈标记看完的季，全部看完会自动变成"看过"。
- **豆瓣对不上**：条目页最下面"豆瓣条目对不上？"，粘贴正确的豆瓣链接。
- **按类型、影人、标签浏览**：片库页上方的筛选；点任何演员、导演进入影人页，能看到你看过 TA 的哪些片、还有哪些没看。
- **备份**：设置 → 导出全部标记。

## 数据从哪来

- IMDb：官方非商业数据集（datasets.imdbws.com）+ 网页用的 GraphQL 接口（详情、海报）。
- 豆瓣：手机版 rexxar 接口（详情、评分、演职员），搜索建议接口和网页搜索（找条目）。
- 烂番茄：网页上的评分数据。
- Wikidata：IMDb ↔ 豆瓣 / 烂番茄 的编号对照。

这些除了 IMDb 数据集都不是公开给第三方的正式接口，改版后可能失效。网页设置里能看到每个数据源最近一次是否正常，哪个挂了把报错发给 Claude 修一下。

仅供个人使用，请不要公开传播或商用，也不要调高抓取频率。

## 文件说明

```
scraper/build_index.py      生成离线片库（每周）
scraper/sync.py             补全详情、刷新评分、在线搜索（每 6 小时 + 标记后）
scraper/sources.py          IMDb / 豆瓣 / 烂番茄 / Wikidata 的接口
docs/index.html             手机网页
.github/workflows/pages.yml 片库和网页的发布
.github/workflows/sync.yml  后台补全
```

离线片库存在 `index` 分支，每次覆盖，不会让仓库越来越大。
