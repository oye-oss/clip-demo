# CLIP 多模态图文检索 Demo

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-orange.svg)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/🤗-Transformers-yellow.svg)](https://huggingface.co/)

## 📝 项目简介

本项目基于 OpenAI 的 **CLIP** 模型（Contrastive Language-Image Pre-training），实现了一个轻量级的**多模态图文检索系统**。CLIP 通过对比学习将图像和文本映射到同一个向量空间，使得跨模态相似度计算成为可能[citation:1][citation:8]。

**核心功能**：
- 🖼️ **以图搜文**：输入图片，返回最匹配的文本描述
- 📝 **以文搜图**：输入文本，返回最匹配的图片

本项目是我为学习多模态深度学习而准备的入门实践。通过这个项目，我深入理解了多模态模型的核心思想，并希望能在研究生阶段继续深入这一方向。

## 🚀 快速开始

### 环境配置

```bash
# 克隆仓库
git clone https://github.com/你的用户名/clip-multimodal-demo.git
cd clip-multimodal-demo

# 安装依赖
pip install torch torchvision transformers pillow matplotlib
