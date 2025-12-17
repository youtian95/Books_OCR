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
        
        // paragraphs.forEach(function(p) {}
    }

    formatParagraphs();
});
