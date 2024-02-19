homework = input("请输入作业文件名（如assignment3.md）\n")
name = "夏天明"
college = "元培学院"
system_environment = "Windows 10 | 22H2"
python_environment = "Spyder IDE 5.4.3 | Python 3.11.4 64-bit"
c_environment = False  #若有C/C++环境请改为具体想要填充的字符串，不要改为True

context = ""
with open(homework, encoding="utf-8") as h:
    context = h.read()
output = context.replace("Hongfei Yan==（请改为同学的姓名、院系）==", f"{name} {college}") \
    .replace("==同学的姓名、院系==", f"{name} {college}") \
    .replace("macOS Ventura 13.4.1 (c)", system_environment) \
    .replace("Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)", python_environment) \
    .replace("【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==", f"【{name}，{college}，2023年秋】") \
    .replace("==（请改为同学的思路和代码）==", "") \
    .replace("# 请改为同学的代码\n", "") \
    .replace("```python\n# \n", "```python\n") \
    .replace("==（请替换为同学的AC代码截图，至少包含有\"Accepted\"的截图）==", "") \
    .replace("==（AC代码截图，至少包含有\"Accepted\"）==", "") \
    .replace("==（至少包含有\"Accepted\"）==", "") \
    .replace("==（请改为同学的操作系统、编程环境等）==\n", "") \
    .replace("\nC/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)", \
             f"\nC/C++编程环境：{c_environment}" if c_environment else "")
newfile = homework.replace(".md", "_filled.md")
with open(newfile, "x", encoding="utf-8") as f:
    f.write(output)
    print(f"文件已填充完成，请打开{newfile}查看")