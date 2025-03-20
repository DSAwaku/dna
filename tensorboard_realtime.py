import pandas as pd
from tensorboardX import SummaryWriter
import time
import argparse

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='Monitor training metrics with TensorBoard')
    parser.add_argument('--csv_file', type=str, required=True, help='Path to the CSV file')
    parser.add_argument('--log_dir', type=str, required=True, help='Path to the TensorBoard log directory')
    parser.add_argument('--interval', type=int, default=5, help='Interval in seconds to check for updates')
    args = parser.parse_args()

    # 创建TensorBoard日志写入对象
    writer = SummaryWriter(args.log_dir)
    last_step = -1  # 用于跟踪上一次写入的最大step值

    print(f"开始监控CSV文件: {args.csv_file}")
    print(f"TensorBoard日志目录: {args.log_dir}")

    # 无限循环，实时监控CSV文件
    while True:
        try:
            # 读取CSV文件
            df = pd.read_csv(args.csv_file)
            if 'step' not in df.columns:
                print("错误：CSV文件必须包含'step'列")
                break

            # 筛选出新的数据（step大于last_step）
            new_data = df[df['step'] > last_step]
            if not new_data.empty:
                for index, row in new_data.iterrows():
                    step = row['step']
                    # 将每个指标写入TensorBoard
                    for metric in ['train_accuracy', 'train_auroc', 'train_f1', 'train_loss', 'train_mcc']:
                        if metric in row and pd.notna(row[metric]):
                            writer.add_scalar(metric, row[metric], step)
                # 更新last_step为当前最大step值
                last_step = df['step'].max()
                print(f"已更新到step: {last_step}")

        except Exception as e:
            print(f"读取CSV文件时出错: {e}")

        # 每隔指定时间检查一次（默认5秒）
        time.sleep(args.interval)

    # 关闭TensorBoard写入对象
    writer.close()

if __name__ == '__main__':
    main()
