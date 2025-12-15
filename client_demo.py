from pathlib import Path
from paddleocr import PaddleOCRVL

input_file = "./files_in/《钢结构设计标准》（GB+50017+2017）.pdf"
output_path = Path("./output")

pipeline = PaddleOCRVL()
output = pipeline.predict(input=input_file)

markdown_list = []
markdown_images = []

input_path_obj = Path(input_file)
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
            new_name = f"imgs/page_{page_index}_img_{idx}{ext}"
            
            # Update markdown text
            if "markdown_texts" in md_info:
                md_info["markdown_texts"] = md_info["markdown_texts"].replace(img_name, new_name)
            
            new_images[new_name] = img_obj
        
        md_info["markdown_images"] = new_images

    markdown_list.append(md_info)
    markdown_images.append(md_info.get("markdown_images", {}))

markdown_texts = pipeline.concatenate_markdown_pages(markdown_list)

mkd_file_path = output_path / f"{Path(input_file).stem}.md"
mkd_file_path.parent.mkdir(parents=True, exist_ok=True)

with open(mkd_file_path, "w", encoding="utf-8") as f:
    f.write(markdown_texts)

for item in markdown_images:
    if item:
        for path, image in item.items():
            file_path = output_path / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(file_path)