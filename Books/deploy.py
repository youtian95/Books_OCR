import os
import subprocess
import sys

# --- 配置区域 ---
# SSH 密钥路径 (请确认路径是否正确，注意反斜杠转义或使用正斜杠)
SSH_KEY_PATH = "C:/Users/youti/.ssh/id_ed25519_1panel"
# 远程服务器信息
REMOTE_USER = "root"
REMOTE_HOST = "youtian95.cn"
# 远程网站根目录
REMOTE_DIR = "/opt/1panel/www/sites/standards.youtian95.cn/index/"
# ----------------

def run_command(command):
    """运行 Shell 命令并检查结果"""
    print(f"执行: {command}")
    # Windows 下运行 scp/ssh 可能需要 shell=True
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"错误: 命令执行失败 (代码 {result.returncode})")
        sys.exit(1)

def main():
    # 1. 构建 MkDocs
    print(">>> [1/3] 正在构建 MkDocs 静态文件...")
    run_command("mkdocs build")

    # 2. 清空远程目录
    print(">>> [2/3] 正在清空远程服务器目录...")
    # 使用 ssh 远程执行 rm 命令
    clean_cmd = f'ssh -i "{SSH_KEY_PATH}" {REMOTE_USER}@{REMOTE_HOST} "rm -rf {REMOTE_DIR}*"'
    run_command(clean_cmd)

    # 3. 上传新文件
    print(">>> [3/3] 正在上传新文件...")
    # 上传 site 文件夹下的所有内容
    # 注意：Windows 下通配符 * 在 subprocess 中可能不会被 shell 展开，
    # 所以这里我们上传 site/ 目录的内容到远程目录
    upload_cmd = f'scp -r -i "{SSH_KEY_PATH}" site/* {REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}'
    run_command(upload_cmd)

    print("\n>>> 部署成功！")

if __name__ == "__main__":
    # 切换到脚本所在目录，确保 mkdocs build 能找到 mkdocs.yml
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
