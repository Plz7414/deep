import pandas as pd

df = pd.DataFrame({
    "姓名": ["Amy", "Ben", "Cindy", "David", "Emma"],
    "系級": ["資工一", "資工二", "企管一", "企管三", "外文二"],
    "成績": [79, 92, None, 85, None]
})

print("【原始資料】")
print(df)
print("缺漏值數量:")
print(df.isna().sum())

df["成績"] = df["成績"].fillna(0)

print("\n【清理後資料】")
print(df)

print("\n平均分數:", df["成績"].mean())
print("最高分:", df["成績"].max())
print("最高分的人:")
print(df.loc[df["成績"].idxmax()])

filtered = df[df["成績"] >= 80]

print("\n【成績 >= 80 的資料】")
print(filtered)

filtered.to_csv("result.csv", index=False, encoding="utf-8-sig")
print("\n已輸出 result.csv")