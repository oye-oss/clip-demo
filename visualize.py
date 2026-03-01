import matplotlib.pyplot as plt
from PIL import Image
from clip_demo import search_by_text
import os
from glob import glob

def visualize_text_to_image(query, image_paths, top_k=4):
    results = search_by_text(query, image_paths, top_k=top_k)
    
    fig, axes = plt.subplots(1, top_k, figsize=(15, 4))
    fig.suptitle(f'Search: "{query}"', fontsize=16)
    
    for i, res in enumerate(results):
        img = Image.open(res['image_path'])
        axes[i].imshow(img)
        axes[i].set_title(f'Sim: {res["similarity"]:.3f}')   # 或直接 f'{res["similarity"]:.3f}'
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.savefig('retrieval_result.png')   # 保存图片
    print(f"可视化结果已保存为 retrieval_result.png")   # 仅提示，不影响
    # plt.show()   # 远程服务器上可以注释掉这行

if __name__ == "__main__":
    image_paths = glob("images/*.jpg") + glob("images/*.png") + glob("images/*.jpeg")
    query = "A man holding a fish"
    visualize_text_to_image(query, image_paths)