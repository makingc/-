def process_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 新的文本内容
    new_lines = []
    
    # 遍历文件行
    for i in range(1, len(lines)):  # 从第二行开始
        # 如果当前行包含“病症”字样，检查上一行
        if '病症：' in lines[i]:
            # 如果上一行不为空，则删除上一行
            if lines[i-1].strip():  # 如果上一行不为空
                new_lines.pop()  # 删除上一行
        new_lines.append(lines[i])  # 添加当前行

    # 将处理后的文本写入输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(new_lines)

# 示例调用
input_file = '1（第一轮清洗文件）.txt'  # 输入文件名
output_file = 'input（清洗完成后的文件）.txt'  # 输出文件名
process_text(input_file, output_file)
