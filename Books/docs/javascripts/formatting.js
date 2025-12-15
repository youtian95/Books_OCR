document.addEventListener("DOMContentLoaded", function() {
    
    function formatParagraphs() {
        // 选择内容区域的所有段落
        var paragraphs = document.querySelectorAll('.md-typeset p');
        
        // 正则表达式匹配：
        // 1. 可选的大写字母加点 (如 L.)
        // 2. 数字
        // 3. 接着是 .数字 (至少出现一次，如 .1)
        // 示例匹配: 1.1.1, L.1.1, 5.2.3, A.1.2
        var regex = /^([A-Z]\.\d+(\.\d+)+|\d+(\.\d+){2,})/;

        paragraphs.forEach(function(p) {
            // 如果段落包含图片，跳过（CSS中已处理缩进，这里不需要加粗）
            if (p.querySelector('img')) {
                p.classList.add('no-indent');
                return;
            }

            var text = p.textContent.trim();
            var match = text.match(regex);
            
            if (match) {
                var matchText = match[0];
                
                // 避免重复处理
                if (p.innerHTML.includes('<strong>' + matchText + '</strong>')) {
                    p.classList.add('no-indent');
                    return;
                }

                // 将匹配到的序号加粗
                // 使用 replace 替换第一个匹配项
                // 注意：这里假设序号在段落开头
                p.innerHTML = p.innerHTML.replace(matchText, '<strong>' + matchText + '</strong>');
                
                // 添加 no-indent 类，取消缩进
                p.classList.add('no-indent');
            }
        });
    }

    formatParagraphs();
});
