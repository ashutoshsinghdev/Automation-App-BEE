from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #launching the browers:-
    browser=playwright.chromium.launch(headless=False,slow_mo=5000)

    page=browser.new_page()

    page.goto("https://unsplash.com/")
    #locators:-
    #locate a link element with docs text (type):-
    # chekbox=page.get_by_role('checkbox',name="Default checkbox") #its kinda locator,name==lable

    # chekbox.highlight()
    # chekbox.check()

#locate using lables :-
    # get_email=page.get_by_label("Email address")
    # get_email.highlight()
    
#locate using placeholder :-

#     getemail=page.get_by_placeholder("Enter email")
#     getemail.highlight()
# #locate using simple text:-
#     getbutton=page.get_by_text("Success")
#     getbutton.click()

#locate using alt text image:-
    # getimg=page.get_by_alt_text("Sailboat on calm water with snow-capped mountain at sunset.")
    # getimg.click()
#locate using get by title locator:-
    getthing=page.get_by_title("nomricon")#fake just for example
    getthing.highlight()
    #get the url:-
    # print(f"chekbox url :{page.url}")

    browser.close()

    