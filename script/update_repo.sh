#!/bin/bash
# 脚本功能描述:
# 1. 自动遍历指定目录下的所有一级子目录
# 2. 检查每个子目录是否为git仓库(通过检查.git目录)
# 3. 对于git仓库:
#    - 检查是否存在远程仓库(origin)
#    - 如果存在远程仓库,则执行git pull更新代码
#    - 如果不存在远程仓库,则输出提示信息
# 4. 脚本执行完成后会自动返回到原始目录
# 5. 整个过程会输出相应的日志信息,方便追踪执行状态

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 遍历脚本所在目录下的所有一级目录
for dir in "$SCRIPT_DIR"/*/; do
    # 检查目录是否存在
    if [ -d "$dir" ]; then
        # 检查是否为git仓库
        if [ -d "$dir/.git" ]; then
            echo "Found git repository: $dir"
            
            # 切换到该目录
            cd "$dir"
            
            # 检查是否存在远程仓库
            if git remote -v | grep -q "origin"; then
                echo "Remote repository exists, pulling changes..."
                git pull
            else
                echo "No remote repository found"
            fi
            
            # 返回原目录
            cd "$SCRIPT_DIR"
        fi
    fi
done
