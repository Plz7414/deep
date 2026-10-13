import pandas as pd

df = pd.DataFrame({
    "姓名": ["Amy", "Ben", "Cindy", "David", "Emma"],
    "系級": ["資工一", "資工二", "企管一", "企管三", "外文二"],
    "成績": [88, 92, 76, 85, 95]
})

print(df)
print("平均分數:", df["成績"].mean())
print("最高分:", df["成績"].max())

# 進階:找出最高分的是誰
print(df.loc[df["成績"].idxmax()])