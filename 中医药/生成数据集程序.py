import json

def process_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    jsonl_data = []

    # 临时变量用于存储input的内容
    input_content = ""
    output_content = []

    for i in range(len(lines)):
        line = lines[i].strip()
        # 检查是否包含“病症”，该行作为input内容
        if "病症" in line:
            # 如果有前面的output内容，则保存
            if input_content:
                # 将当前的input和output内容生成一个JSON对象
                jsonl_entry = {
                    "instruction": "你是一个医生，熟悉中医药学，懂得中医知识，请你帮我分析病症，帮我给出治疗方案，帮我给出建议",
                    "input": input_content,
                    "output": "\n".join(output_content).strip()
                }
                jsonl_data.append(jsonl_entry)

            # 更新input内容
            input_content = line
            # 清空output内容
            output_content = []
        else:
            # 将其他内容加入到output内容
            output_content.append(line)

    # 如果处理完之后仍有剩余内容（防止最后一条数据遗漏）
    if input_content:
        jsonl_entry = {
            "instruction": "你是一个医生，熟悉中医药学，懂得中医知识，请你帮我分析病症，帮我给出治疗方案，帮我给出建议",
            "input": input_content,
            "output": "\n".join(output_content).strip()
        }
        jsonl_data.append(jsonl_entry)

    # 将结果保存为jsonl格式
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in jsonl_data:
            outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')

# 示例调用
input_file = 'input（清洗完成后的文件）.txt'  # 上一个程序输出的文件
output_file = 'output.jsonl'  # 最终生成的jsonl文件
process_to_jsonl(input_file, output_file)
