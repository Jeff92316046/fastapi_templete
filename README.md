# FastAPI 專案結構

## 安裝步驟

1. 安裝依賴：

```bash
pip install fastapi uvicorn
```

2. 運行應用：

```bash
uvicorn src.main:app --reload
```

## 專案描述

- **api**: 包含 FastAPI 應用的路由定義。
- **controllers**: 包含處理請求的邏輯，例如 GET 和 POST 請求。
- **repositories**: 處理資料庫交互或數據管理邏輯。
- **data**: JSON 文件或其他數據文件，供應用使用。

---

## 啟動指南

1. 確保已安裝 Python 3.8 及以上版本。
2. 使用 `pip` 安裝必要的依賴。
3. 使用 `uvicorn src.main:app --reload` 啟動 FastAPI 伺服器。

伺服器啟動後，API 可通過 `http://127.0.0.1:8000` 訪問。  
可以使用`http://127.0.0.1:8000/docs`開啟swagger

