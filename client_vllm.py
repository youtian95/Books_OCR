import argparse
from pathlib import Path
from paddleocr import PaddleOCRVL

'''
使用示例:
(1) 识别指定目录中的所有pdf文件，会为每个文件创建单独的输出子目录:
    python client_vllm.py --in_dir "./files_in" --out_dir "./output"
    # 使用 --skip_processed 跳过已存在结果的文件 (默认不跳过)
    python client_vllm.py --in_dir "./files_in" --out_dir "./output" --skip_processed
(2) 识别指定的pdf文件:
    python client_vllm.py --in_file "./files_in/前言.pdf" --out_dir "./output/前言"
'''

def parse_args():
    parser = argparse.ArgumentParser(description="PaddleOCR-VL Client Demo")
    parser.add_argument("--in_dir", dest="input_dir", type=str, help="Path to input directory")
    parser.add_argument("--in_file", dest="input_file", type=str, help="Path to input file")
    parser.add_argument("--out_dir", dest="output_path", type=str, default="./output", help="Path to output directory")
    parser.add_argument("--skip_processed", action="store_true", help="Skip files that have already been processed (default: False)")
    return parser.parse_args()

def process_one_file(pipeline, input_file, output_root, skip_processed=False):
    input_path_obj = Path(input_file)
    mkd_file_path = output_root / f"{input_path_obj.stem}.md"

    if skip_processed and mkd_file_path.exists():
        print(f"Skipping: {input_file} (Output exists)")
        return

    print(f"Processing: {input_file}")
    output = pipeline.predict(input=input_file)

    markdown_list = []
    markdown_images = []

    pdf_stem = input_path_obj.stem

    for res in output:
        md_info = res.markdown
        
        # Rename images to be meaningful
        original_images = md_info.get("markdown_images", {})
        new_images = {}
        if original_images:
            page_index = md_info.get("page_index", 0)
            for idx, (img_name, img_obj) in enumerate(original_images.items()):
                # Construct new name: imgs/{pdf_stem}_page_{page_index}_img_{idx}.jpg
                ext = Path(img_name).suffix or ".jpg"
                new_name = f"imgs/{pdf_stem}_page_{page_index}_img_{idx}{ext}"
                
                # Update markdown text
                if "markdown_texts" in md_info:
                    md_info["markdown_texts"] = md_info["markdown_texts"].replace(img_name, new_name)
                
                new_images[new_name] = img_obj
            
            md_info["markdown_images"] = new_images

        markdown_list.append(md_info)
        markdown_images.append(md_info.get("markdown_images", {}))

    markdown_texts = pipeline.concatenate_markdown_pages(markdown_list)

    # mkd_file_path is already calculated at the beginning of the function
    mkd_file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(mkd_file_path, "w", encoding="utf-8") as f:
        f.write(markdown_texts)

    for item in markdown_images:
        if item:
            for path, image in item.items():
                file_path = output_root / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                image.save(file_path)

def main():
    args = parse_args()
    
    if not args.input_dir and not args.input_file:
        print("Error: Please provide either --in_file or --in_dir.")
        return

    pipeline = PaddleOCRVL(vl_rec_backend="vllm-server", vl_rec_server_url="http://127.0.0.1:8118/v1")
    output_root = Path(args.output_path)

    if args.input_file:
        process_one_file(pipeline, args.input_file, output_root, args.skip_processed)
    elif args.input_dir:
        input_dir = Path(args.input_dir)
        if input_dir.exists():
            for pdf_file in input_dir.glob("*.pdf"):
                # Create a subfolder for each file in directory mode
                file_output_root = output_root / pdf_file.stem
                process_one_file(pipeline, str(pdf_file), file_output_root, args.skip_processed)
        else:
            print(f"Directory not found: {input_dir}")

if __name__ == "__main__":
    main()