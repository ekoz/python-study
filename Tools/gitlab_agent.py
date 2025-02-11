# -*- coding: utf-8 -*-
# @author   :   eko.zhan
# @time     :   2024/12/31 10:31
# 获取 gitlab 工程下 docs 目录里得所有文件内容，并汇总成 docs.md 文件

import requests
import os

# 定义GitLab API的基本信息
GITLAB_URL = "https://gitlab.com"  # GitLab API的基础地址
PROJECT_ID = "9527"  # 替换为您项目的ID
ACCESS_TOKEN = "_733usW5iuyM4LDkHEqk"  # 替换为您的访问令牌
REF = "master"  # 分支名称，例如 'main' 或 'master'

# 组装请求头信息
headers = {"Private-Token": ACCESS_TOKEN}  # 使用令牌进行身份验证

content_list = []


# 获取项目中指定路径下的所有文件和目录
def get_files_and_dirs(project_id, path, ref, headers):
    url = f"{GITLAB_URL}/api/v4/projects/{project_id}/repository/tree"
    params = {"path": path, "ref": ref}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# 获取文件内容
def get_file_content(project_id, file_path, ref, headers):
    file_path = file_path.replace("/", "%2F")
    url = f"{GITLAB_URL}/api/v4/projects/{project_id}/repository/files/{file_path}/raw"
    params = {"ref": ref}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(f"{url} 无法访问")
        return ""


# 主函数
def main(dir_path):
    # 获取项目根目录下的文件和目录
    tree = get_files_and_dirs(PROJECT_ID, dir_path, REF, headers)
    print(dir_path, tree)
    for item in tree:
        if item["type"] == "blob":  # 文件
            file_path = item["path"]
            file_content = get_file_content(PROJECT_ID, file_path, REF, headers)
            # print(f"文件路径 - {file_path}:")
            # print(file_content)
            # print("\n")
            content_list.append(file_content)
        elif item["type"] == "tree":  # 目录
            directory_path = item["path"]
            # 递归获取目录下的所有文件
            main(directory_path)


if __name__ == "__main__":
    main("docs")
    # print(content_list)
    with open("docs.md", "w", encoding="utf-8") as file:
        file.write("\r\n".join(content_list))
