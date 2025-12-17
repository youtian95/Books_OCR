import re

def process_headers(markdown):
    """
    1. 标题处理 (Header Processing)
    将 1.1.1 或 A.1.1 转换为 #### 标题
    同时为标题添加 ID，以便链接跳转
    返回: (处理后的markdown, 生成的章节ID集合)
    """
    pattern = re.compile(r'^(?!#)((?:[A-Z]\.)?\d+(?:\.\d+)+)', re.MULTILINE)
    section_ids = set()
    
    def replace_func(match):
        text = match.group(1)
        should_convert = False
        
        if text[0].isalpha():
            should_convert = True
        else:
            if text.count('.') >= 2:
                should_convert = True
        
        if should_convert:
            # 记录章节号，用于后续链接检查
            section_ids.add(text)
            # 添加自定义 ID，例如 #### 1.1.1 {: #sec-1.1.1 }
            return f'#### {text} {{: #sec-{text} }}\n'
        else:
            return text

    new_markdown = pattern.sub(replace_func, markdown)
    return new_markdown, section_ids

def process_equations(markdown):
    """
    2. 公式自动编号 (Automatic Equation Numbering)
    返回: (处理后的markdown, 生成的公式ID集合)
    """
    lines = markdown.split('\n')
    new_lines = []
    generated_ids = set()
    
    current_section = ""
    formula_index = 0
    in_code_block = False
    
    # 匹配我们刚刚生成的标题格式 "#### 1.1.1"
    # 注意：现在标题后面可能跟有属性列表 {: ... }，所以正则只需要匹配前面的数字部分
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
                tag_content = f"{current_section}-{formula_index}"
                
                # 获取缩进
                indent = line[:len(line) - len(line.lstrip())]
                
                # 如果没有手动编号，则添加自动编号
                # 例子： $$ E=mc^2 $$ -> $$ E=mc^2 \tag{章节号-序号} $$
                if '\\tag' not in content:
                    # 将锚点放在公式前面
                    # 使用 span.eq-anchor 配合 CSS 进行位置修正
                    anchor = f'{indent}<span id="eq-{tag_content}" class="eq-anchor"></span>'
                    new_line = f'{anchor}\n\n{indent}$$ {content} \\tag{{{tag_content}}} $$'
                    new_lines.append(new_line)
                    generated_ids.add(tag_content)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
            i += 1
            continue

        new_lines.append(line)
        i += 1
        
    return '\n'.join(new_lines), generated_ids

def process_references(markdown, generated_ids, section_ids):
    """
    3. 引用链接 (Reference Linking)
    替换 式（5.2.2-2） 为 [式（5.2.2-2）](#eq-5.2.2-2)
    替换 第 5.2.1 条 为 [第 5.2.1 条](#sec-5.2.1)
    仅当引用ID在当前页面生成过时才替换，避免死链。
    """
    # --- 公式引用 ---
    def ref_replace(match):
        full_text = match.group(0)
        ref_id = match.group(1)
        
        # 检查引用ID是否存在于当前页面
        if ref_id in generated_ids:
            return f'[{full_text}](#eq-{ref_id})'
        else:
            return full_text

    # 全角括号
    markdown = re.sub(r'式（([A-Z0-9\.]+-[\d]+)）', ref_replace, markdown)
    # 半角括号
    markdown = re.sub(r'式\(([A-Z0-9\.]+-[\d]+)\)', ref_replace, markdown)
    
    # --- 章节引用 ---
    def section_replace(match):
        full_text = match.group(0)
        sec_num = match.group(1)
        
        # 检查章节ID是否存在于当前页面
        if sec_num in section_ids:
            return f'[{full_text}](#sec-{sec_num})'
        else:
            return full_text
            
    # 匹配 "第 5.2.1 条" 或 "第5.2.1条"
    markdown = re.sub(r'第\s*([A-Z0-9\.]+)\s*条', section_replace, markdown)
    
    return markdown

def on_page_markdown(markdown, **kwargs):
    markdown, section_ids = process_headers(markdown)
    markdown, generated_ids = process_equations(markdown)
    markdown = process_references(markdown, generated_ids, section_ids)
    return markdown
