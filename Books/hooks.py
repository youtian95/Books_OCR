import re

def on_page_markdown(markdown, **kwargs):
    # 1. 标题处理 (Header Processing)
    # 逻辑与之前一致：将 1.1.1 或 A.1.1 转换为 #### 标题
    pattern = re.compile(r'^(?!#)((?:[A-Z]\.)?\d+(?:\.\d+)+)', re.MULTILINE)
    
    def replace_func(match):
        text = match.group(1)
        if text[0].isalpha():
            return f'#### {text}\n'
        else:
            if text.count('.') >= 2:
                return f'#### {text}\n'
            else:
                return text

    markdown = pattern.sub(replace_func, markdown)
    
    # 2. 公式自动编号 (Automatic Equation Numbering)
    lines = markdown.split('\n')
    new_lines = []
    
    current_section = ""
    formula_index = 0
    in_code_block = False
    
    # 匹配我们刚刚生成的标题格式 "#### 1.1.1"
    header_check = re.compile(r'^####\s+([A-Z0-9\.]+)')
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # 处理代码块 (Code Blocks) - 避免在代码块中修改公式
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            i += 1
            continue
            
        if in_code_block:
            new_lines.append(line)
            i += 1
            continue
            
        # 处理标题 (Headers) - 更新当前章节号，重置公式计数
        match = header_check.match(line)
        if match:
            current_section = match.group(1)
            formula_index = 0
            new_lines.append(line)
            i += 1
            continue
            
        # 处理数学公式 (Math Blocks)
        # 情况 A: 单行公式 $$ ... $$
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 2:
            if current_section:
                formula_index += 1
                content = stripped[2:-2]
                # 如果没有手动编号，则添加自动编号
                if '\\tag' not in content:
                    # 添加 \tag{章节号-序号}
                    new_line = f'$$ {content} \\tag{{{current_section}-{formula_index}}} $$'
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
            i += 1
            continue
            
        # 情况 B: 多行公式 $$ ...
        if stripped.startswith('$$'):
            block_lines = [line]
            j = i + 1
            found_end = False
            
            # 向下寻找结束符 $$
            while j < len(lines):
                l = lines[j]
                block_lines.append(l)
                l_stripped = l.strip()
                
                if l_stripped == '$$' or l_stripped.endswith('$$'):
                    found_end = True
                    # 找到结束符，添加编号
                    if current_section:
                        formula_index += 1
                        tag = f'\\tag{{{current_section}-{formula_index}}}'
                        
                        # 插入编号
                        if l_stripped == '$$':
                            # 结束符单独一行，编号插入到前一行
                            block_lines.insert(-1, tag)
                        else:
                            # 结束符在行尾，替换 $$ 为 \tag{...} $$
                            block_lines[-1] = block_lines[-1].replace('$$', f'{tag} $$')
                    
                    new_lines.extend(block_lines)
                    i = j + 1
                    break
                j += 1
            
            if not found_end:
                # 未找到结束符，原样保留
                new_lines.extend(block_lines)
                i = j
            continue

        new_lines.append(line)
        i += 1
        
    return '\n'.join(new_lines)
