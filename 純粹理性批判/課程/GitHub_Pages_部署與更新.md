# 課程網站：GitHub Pages 部署與更新

## 已建好的網站檔案
- [網站首頁](../../../docs/index.html)：含 7 階段 / 36 堂課目錄，第一、二課可點擊
- [第一課互動網頁](../../../docs/lessons/01/index.html)：手機適配、目錄、答案揭曉、三題測驗與個人筆記
- [第二課互動網頁](../../../docs/lessons/02/index.html)：哥白尼式轉向、認識模型切換圖、四題測驗與個人筆記
- [停用 Jekyll 標記](../../../docs/.nojekyll)：使 GitHub Pages 原樣發布靜態 HTML

## 啟用（儲存庫管理者需操作一次）
1. 前往 [GitHub Pages 設定](https://github.com/wellwellxd/kant-works/settings/pages)。
2. 在 **Build and deployment → Source** 選擇 **Deploy from a branch**。
3. **Branch** 選擇 **main**，**Folder** 選擇 **/docs**。
4. 點擊 **Save**，再回來看 GitHub Pages 的部署狀態與實際網站連結。
5. 啟用成功後，預期網站網址是：
   - 首頁：https://wellwellxd.github.io/kant-works/
   - 第一課：https://wellwellxd.github.io/kant-works/lessons/01/
   - 第二課：https://wellwellxd.github.io/kant-works/lessons/02/

### 關於 Repository 與可見度
- 本專案目前為 **Public**（使用者確認符合期待），因此 GitHub 儲存庫內所有原典、課程檔案及提交紀錄都可被公開檢視。
- GitHub Pages 網站也應被視為公開；目前只從 `/docs` 發布網頁，但這不代表儲存庫內其他文件是私人內容。
- 本站頁面設有 noindex 宣告，這不是存取控制，也不能保證搜尋引擎永不收錄。

## 日後新增課程
1. 先在 `純粹理性批判/課程/第XX課/` 建立原著精讀計畫、完整中文教材和互動版 HTML。
2. 把 HTML 放到 `docs/lessons/XX/index.html`。
3. 更新 `docs/index.html`，把新課改成可點擊連結 `./lessons/XX/`。
4. 提交到 main 後，GitHub Pages 會按來源分支更新網站。
5. 重要：`docs/` 不是私人的筆記存放處，尤其不要公開學生個人提問紀錄、帳號、token、授權文件等。

## 教學使用
- 從德文 A/B 版原典查證，但學生閱讀材料一律先翻成**繁體中文**。
- 教材可以有互動、流程圖、音訊或影片，但應優先確保手機閱讀順暢。
- HTML 是純靜態檔，**課程筆記只儲存在裝置瀏覽器 localStorage**；不會同步 GitHub，也不跨裝置。
- 複製筆記後可以貼到 ChatGPT，請哲學家教一起討論。
- 若後續要跨裝置同步學習進度／個人筆記，需要另外設計登入、儲存與隱私措施，GitHub Pages 本身不提供資料庫後端。

## 狀態
- [x] 首頁靜態 HTML 提交至 main/docs
- [x] 第一課互動 HTML 提交至 main/docs
- [x] 第二課互動 HTML 提交至 main/docs，首頁與第一課新增對應連結
- [x] .nojekyll 已加入
- [ ] 再次確認 GitHub Settings → Pages 的目前部署來源及狀態（此處無設定存取權）
- [ ] 驗證公開網站網址已能成功讀取
