# Python Intro

- 語法簡潔、結構簡單，程式碼可讀性強，學習更加簡單
- 免費且開源，擁有豐富的開發者社群支援
- 完善的基礎程式庫
- 應用廣泛，能和大多數的程式語言共同使用

# Environment(Aanconda)

Anconda就像是 Python的懶人包，它內建了許多 Python的熱門套件，如此一來使用者就不用在安裝套件時面鄰種種錯誤訊息與漫長的 debug過程 (尤其是在 windows作業系統下)。換句話說，能讓 coder不用花費心力在處理系統環境端的問題，而是能直接捲起袖子開始寫程式，進行現實問題的分析。不僅如此，他還有內建 Spyder IDE與 Jupyter Notebook，這兩個編譯器對於新手而言相對友善。

## 1. 安裝環節

請先去anaconda官方網站 

[https://www.anaconda.com/download](https://www.anaconda.com/download)

**<u>必須用有效的email認證</u>**

![image](./image/anaconda_register_successful.png)

![image](./image/anaconda_email_download.png)


> **安裝時要注意以下這部分**
> 
> 注意安裝路徑稍後會用到
>  
> ![image](./image/anaconda_install_process_v1.png) 
>
> 勾選1,3項
> 
> ![image](./image/anaconda_install_process_v2.png)
>
> 然後照著安裝步驟next下去

## 2. 如何使用

Anaconda擁有精美強大的GUI介面，操作簡便直覺

這邊講解Terminal的用法

1. 先設定環境變數

![image](./image/anaconda_set_environment.png)

<span style="color:yellow">在編輯環境變數的地方輸入安裝anaconda的地方 + \condabin</span>
![image](./image/anaconda_set_environment_v2.png)

*在家目錄下面建立資料夾python_project並在該路徑開啟terminal*

``` powershell
conda env list
# 輸入該指令可看到只有一個環境叫做base這是anaconda預設的

conda create --name myenv python=3.11 # 這邊為環境命名為myenv並且版本為3.11
# 都照著系統提示走就對了(y/N)

# 啟動環境(左邊會出現目前環境名稱)
conda activate myenv

# 安裝我們需要的套件
pip install ipykernel jupyter

# 關閉環境
conda deactivate
```
# Lesson 1

開啟jupyter開發環境

``` powershell
jupyter notebook
# 通常會自動跳轉到網頁，如果沒有的話打開瀏覽器輸入localhost:8888
```
## demo a simple program

新增檔案

![image](./image/jupyter.png)

開發我們的第一支程式
```python
# First python program
demo = "Hello World!"
print(demo)
```
![image](./image/python_script_lesson1_helloWorld.png)

## 基礎觀念

- 型別
  - 字串(string)
  - 整數(int)
  - 浮點數(float)
  - 布林值(boolean) # python的布林值要首字要大寫
- 運算符號
  - 加減乘除(+,-,*,/)
  - 整數除法(//)
  - 餘數除法(%)
  - 次方(**)
- 比較運算子
  - <,>,<=,>=
  - 完全相同(==)
  - 不等於(!=)
- 邏輯運算子
  - 和(and, &)
  - 或(or, |)
  - 非(not)
  - 包含(in )
  - 判斷是否為同一物件(is )

```
x = 100
```