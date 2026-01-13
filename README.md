# Douyu-rank-crawler

## 项目介绍 / Project Introduction
A crawler that fetches daily, weekly and monthly ranking data of all categories from Douyu's web ranking lists, and exports the parsed data to Excel files for local storage.  
爬取斗鱼网页排行榜各分类的日榜、周榜、月榜数据，解析后将数据导出为Excel文件并本地保存。

If you have more refined and simplified code solutions, feel free to contact me for communication and discussion.  
若有更完善、更简便的代码方案，欢迎联系我沟通探讨。

## 功能特点 / Features
1. Support crawling daily, weekly and monthly ranking data of all categories on Douyu's ranking page  
   支持爬取斗鱼排行榜页面全分类的日榜、周榜、月榜数据
2. Automatically parse and format the crawled data, and export it to Excel files with clear structure  
   自动解析并格式化爬取的数据，导出结构清晰的Excel文件
3. The code logic is simple and easy to modify for custom crawling requirements  
   代码逻辑简洁，可轻松修改以适配自定义爬取需求

## 环境依赖 / Environment Dependencies
- Python 3.7 or higher  
- requests: For sending HTTP requests to obtain web data  
- pandas: For data processing and Excel export  
- openpyxl: For Excel file writing (pandas dependency)  

### 安装依赖 / Install Dependencies

 Open the command line and run the following command:  
 打开命令行，执行以下命令安装依赖：
 ```bash
 pip install requests pandas openpyxl
 ```
### 快速开始 / Quick Start

#### 1. 克隆仓库 / Clone the Repository

 git clone https://github.com/[你的GitHub用户名]/Douyu-rank-crawler.git
 cd Douyu-rank-crawler

#### 2. 运行爬虫 / Run the Crawler

 python Douyu-rank-crawler.py
 
#### 3. 查看结果 / Check Results

 After running, the Excel file containing the ranking data will be generated in the project directory.
 运行完成后，项目目录下会生成包含排行榜数据的Excel文件。
 
### 许可证 / License
 
This project is licensed under the MIT License - see the LICENSE file for details.
本项目基于MIT许可证开源 - 详见LICENSE文件。
 
### 联系作者 / Contact Author

 - GitHub: https://github.com/SunXun888
