month = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# 2000/1/1 is Sat.

#一年のカレンダーを出力する
# ユーザーに調べたい年を入力してもらう
year = input("Enter year.\n>")
# 閏年かどうか調べて、monthを適宜29日に書き換える
if (year%4==0) and (year%100!=0) or (year%400==0):
    month['Feb'] = 29
# 元旦の曜日を算出して、以降の日付をそれに基づいて判断し、出力する
# calculate
# 2001 - 2000 = 1 (year) = 366 days



#一ヶ月のカレンダーを出力する
#一年バージョンからその月の最初の日付を算出
#出力する

#特定の日の曜日を答える