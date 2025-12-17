/**
 * 格式化脚本 (formatting.js)
 * 包含客户端的交互增强和样式调整
 */

(function() {
    'use strict';

    /**
     * 初始化段落格式化
     * 目前主要逻辑已迁移至服务端 hooks.py，此处保留用于后续可能的客户端调整
     */
    function initParagraphFormatting() {
        // 选择内容区域的所有段落
        var paragraphs = document.querySelectorAll('.md-typeset p');
        
        // 正则表达式匹配：
        // 1. 可选的大写字母加点 (如 L.)
        // 2. 数字
        // 3. 接着是 .数字 (至少出现一次，如 .1)
        // 示例匹配: 1.1.1, L.1.1, 5.2.3, A.1.2
        var regex = /^([A-Z]\.\d+(\.\d+)+|\d+(\.\d+){2,})/;
        
        // paragraphs.forEach(function(p) {
        //     // 客户端格式化逻辑（如果需要）
        // });
    }

    /**
     * 初始化返回上一页的悬浮按钮
     */
    function initBackButton() {
        var backBtn = document.createElement('button');
        backBtn.innerHTML = '↩';
        backBtn.className = 'md-fab md-fab--bottom-left'; // 使用 Material 的样式类
        
        // 设置样式
        backBtn.style.cssText = `
            position: fixed; 
            bottom: 40px; 
            left: 20px; 
            z-index: 100; 
            font-size: 24px; 
            width: 40px; 
            height: 40px; 
            border-radius: 50%; 
            border: none; 
            background-color: var(--md-primary-fg-color); 
            color: var(--md-primary-bg-color); 
            cursor: pointer; 
            box-shadow: 0 2px 5px rgba(0,0,0,0.3); 
            display: none; 
            align-items: center; 
            justify-content: center;
        `;
        backBtn.title = "返回上一处 (Alt + ←)";
        
        document.body.appendChild(backBtn);

        // 监听点击事件
        backBtn.addEventListener('click', function() {
            history.back();
        });

        // 更新按钮可见性
        function updateVisibility() {
            if (window.history.length > 1) {
                backBtn.style.display = 'flex';
            } else {
                backBtn.style.display = 'none';
            }
        }
        
        // 初始化可见性
        updateVisibility();
        
        // 监听 hash 变化（可选，如果需要更精细的控制）
        window.addEventListener('hashchange', updateVisibility);
    }

    /**
     * 主入口
     */
    document.addEventListener("DOMContentLoaded", function() {
        initParagraphFormatting();
        initBackButton();
    });

})();
