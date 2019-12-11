import webbrowser

artists = ["아이유","박민영","박보영"]

for i in artists:
    webbrowser.open("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + i)