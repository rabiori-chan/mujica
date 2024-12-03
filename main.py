from playwright.sync_api import sync_playwright
import time
from datetime import datetime, timedelta
import random
import platform
import numpy as np
from getpass import getpass

サービス番号 = "0104116116112115058047047098105116046108121047"

def 私の関数(x: int) -> float:
    return -295988017304777162676299*x**3/1181491840 + 285332123070684218323462177*x**2/590745920 - 2847695062297280643227544249*x/1181491840 + 31886459261115666571917163937/590745920

def ASCIIを文字に(ascii_str: str) -> str:
    """
    ASCIIコード文字列を通常の文字列に変換します
    3桁の数字を1つの文字に変換します
    例："065066067" -> "ABC"
    """
    if len(ascii_str) % 3 != 0:
        ascii_str = '0' * (3 - (len(ascii_str) % 3)) + ascii_str
    
    結果 = ''
    for i in range(0, len(ascii_str), 3):
        char_code = int(ascii_str[i:i+3])
        結果 += chr(char_code)
    return 結果

def 選び学校(input_id: int):
    if input_id == 1:
        return "052049104053108074077"
    elif input_id == 2:
        return "051086106086068108085"
    elif input_id == 3:
        return "051086108114081074111"
    elif input_id == 1923:
        return "049057050051110101117"
    else:
        return "051086107068104066115"

def 項目クリック(selector, page):
    try:
        element = page.wait_for_selector(selector, timeout=30000)
        element.click()
        if len(page.context.pages) > 1:
            page = page.context.pages[-1]
        return page
    except Exception as e:
        print(f"要素のクリックに失敗しました: {e}")
        return page

def タスク数ゲット(page):
    try:
        task_element = page.wait_for_selector("div.col-lg-4 strong#sum", timeout=30000)
        task_kazu = int(task_element.inner_text())
        print(f"現在のタスク数: {task_kazu}")
        return task_kazu
    except Exception as e:
        print(f"タスク数の取得に失敗しました: {e}")
        while True:
            try:
                task_kazu = int(input("タスク数を入力してください: "))
                return task_kazu
            except ValueError:
                print("入力が無効です。有効な整数を入力してください。")

def フォーム投稿(page):
    try:
        page.click("button.confirm")
        print("フォームが送信されました")
        
        page.wait_for_selector("a#btn-goBack", timeout=30000)
        time.sleep(10)
        page.click("a#btn-goBack")
        print("戻るボタンをクリックしました")
        time.sleep(5)
    except Exception as e:
        print(f"フォームの送信に失敗しました: {e}")

def クリックガウス分布(page):
    try:
        max_attempts = 30
        attempt = 0
        rows = page.query_selector_all('table#evlTable tbody tr')
        
        while len(rows) == 0 and attempt < max_attempts:
            print(f"表の読み込みを待っています... 試行回数: {attempt + 1}")
            time.sleep(1)
            rows = page.query_selector_all('table#evlTable tbody tr')
            attempt += 1
            
        if len(rows) == 0:
            raise Exception("表の読み込みがタイムアウトしました")
            
        print(f"行数の合計: {len(rows)}")
        
        選んだ総数 = []
        
        for i, row in enumerate(rows):
            radio_buttons = row.query_selector_all('input[type="radio"]')
            if len(radio_buttons) > 0:
                random_index = int(round(np.random.normal(0, 0.5)))
                button_index = max(0, min(random_index, len(radio_buttons) - 1))
                
                if len(選んだ総数) > 0 and all(x == 選んだ総数[0] for x in 選んだ総数):
                    available_indices = list(range(len(radio_buttons)))
                    available_indices.remove(選んだ総数[0])
                    button_index = random.choice(available_indices)
                
                radio_buttons[button_index].click()
                選んだ総数.append(button_index)
                print(f"第 {i+1} 行の第 {button_index + 1} ボタンをクリックしました")
            else:
                print(f"第 {i+1} 行にはボタンがありません")
                
        if len(選んだ総数) > 1 and all(x == 選んだ総数[0] for x in 選んだ総数):
            random_row = random.randint(0, len(rows) - 1)
            radio_buttons = rows[random_row].query_selector_all('input[type="radio"]')
            if len(radio_buttons) > 0:
                available_indices = list(range(len(radio_buttons)))
                available_indices.remove(選んだ総数[0])
                new_index = random.choice(available_indices)
                radio_buttons[new_index].click()
                print(f"すべてが同じにならないように、第 {random_row + 1} 行の第 {new_index + 1} ボタンを再クリックしました")
                
    except Exception as e:
        print(f"評価のクリックに失敗しました: {e}")

def 学校選び():
    while True:
        print("\n学園を選んでください：")
        print("1. 月の森女子学園")
        print("2. 花咲川女子学園")
        print("3. 羽丘女子学園")
        
        選択 = input("選択肢の番号を入力してください (1-3): ")
        
        結果 = 選び学校(int(選択))
        結果 = ASCIIを文字に(サービス番号 + 結果)
        
        return 結果

def メインファンクション():
    url_ピンジャオ = 学校選び()
    
    学籍 = input("学籍番号を入力してください:")
    パスワード = getpass("パスワードを入力してください:")
    
    os_system = platform.system()
    
    with sync_playwright() as p:
        if os_system == "Darwin":
            ブラウザ = p.webkit.launch(headless=False)
            print("WebKit ブラウザを使用します")
        else:  # Windows, Linux 等他のシステム
            ブラウザ = p.chromium.launch(headless=False)
            print("Chromium ブラウザを使用します")
            
        context = ブラウザ.new_context(
            extra_http_headers={"referer": ""},
            bypass_csp=True
        )
        page = context.new_page()
        
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => false})")
        
        page.goto(url_ピンジャオ)
        
        page.fill('input#un.login_box_input.person', 学籍)
        page.fill('input#pd.login_box_input.lock', パスワード)
        page.click('input#index_login_btn.login_box_landing_btn')
        
        タスク数 = タスク数ゲット(page)
        
        for i in range(1, タスク数 + 1):
            page.click('a.btn.btn-outline.btn-primary.btn-xs')
            クリックガウス分布(page)
            time.sleep(1)
            page.click('a#btn-saveResult.btn.btn-primary.btn-outline')
            time.sleep(1)
            フォーム投稿(page)
            print(f"第{i}の評価が完了しました")
        
        print("評価が完了しました")
        time.sleep(10)
        ブラウザ.close()

if __name__ == "__main__":
    メインファンクション()
